import sqlite3

db = sqlite3.connect('jobs.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS job_postings (post_id INTEGER
              PRIMARY KEY, url text NOT NULL, app_url text, app_id
              integer, desc text, post_dt text, exp_dt text, email_sent INTEGER NOT NULL)''')
db.commit()

def insert(post_id,url,app_url,app_id,desc,post_dt,exp_dt,email_sent):
    cursor.execute("INSERT OR IGNORE INTO job_postings \
                       (post_id,url,app_url,app_id,post_dt,exp_dt,email_sent) \
                       VALUES (?,?,?,?,?,?,?,?)" \
                       ,(post_id,url,app_url,app_id,desc,post_dt,exp_dt,email_sent,))
    db.commit()

def update_sent_status(post_id):
    cursor.execute("UPDATE job_postings SET email_sent = 1 \
                    WHERE post_id = ?",(post_id,))
    db.commit()

def get_records(is_sent=99):
    if is_sent == 0: # Select non-applitrack postings email NOT sent
        cursor.execute("SELECT * FROM job_postings \
                       WHERE app_id IS NULL \
                       AND email_sent = 0")
    elif is_sent == 1: # Select non-applitrack postings email sent
        cursor.execute("SELECT * FROM job_postings \
                       WHERE app_id IS NULL \
                       AND email_sent = 1")
    elif is_sent == 2: # Select unique applitrack postings
        cursor.execute("SELECT * FROM job_postings \
                       WHERE app_id NOT NULL \
                       GROUP BY app_id")
    elif is_sent == 3: # Select all applitrack postings
        cursor.execute("SELECT * FROM job_postings \
                       WHERE app_id NOT NULL")
    else: # Default get all post ids
        cursor.execute("SELECT post_id FROM job_postings")
    records = cursor.fetchall()
    return records

def close_db():
    db.close()

