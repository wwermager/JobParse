import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS job_postings (post_id INTEGER
              PRIMARY KEY, url text NOT NULL, app_url text, app_id
              integer, post_dt text, exp_dt text, email_sent INTEGER NOT NULL)''')
db.commit()

def insert(post_id,url,app_url,app_id,post_dt,exp_dt,email_sent):
    cursor.execute("INSERT OR IGNORE INTO job_postings \
                       (post_id,url,app_url,app_id,post_dt,exp_dt,email_sent) \
                       VALUES (?,?,?,?,?,?,?)" \
                       ,(post_id,url,app_url,app_id,post_dt,exp_dt,email_sent,))
    db.commit()
def update_sent_status(post_id):
    cursor.execute("UPDATE job_postings SET email_sent = 1 \
                    WHERE post_id = ?",(post_id))
    db.commit()
def get_records(is_sent=2):
    if is_sent == 0:
        cursor.execute("SELECT * FROM job_postings WHERE email_sent = 0")
    elif is_sent == 1:
        cursor.execute("SELECT * FROM job_postings WHERE email_sent = 1")
    else:
        cursor.execute("SELECT * FROM job_postings")
    records = cursor.fetchall()
    return records

def close_db():
    db.close()
