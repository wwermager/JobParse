import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS job_postings (post_id INTEGER
              PRIMARY KEY, url text NOT NULL, app_url text, app_id
              integer, post_dt text, exp_dt text, email_sent INTEGER NOT NULL)''')
db.commit()

def insert(post_id,url,app_url,app_id,post_dt,exp_dt,email_sent):
    cursor.execute("INSERT INTO job_postings \
                       (post_id,url,app_url,app_id,post_dt,exp_dt,email_sent) \
                       VALUES (?,?,?,?,?,?,?)" \
                       ,(post_id,url,app_url,app_id,post_dt,exp_dt,email_sent,))
    db.commit()

def close():
    db.close()
