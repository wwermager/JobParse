import sqlite3

class Job_Post(object):

    db = sqlite3.connect('test.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS job_postings (post_id INTEGER
              PRIMARY KEY, url text NOT NULL, app_url text, app_id
              integer, post_dt text, exp_dt text, email_sent INTEGER NOT NULL)''')
    db.commit()

    def __init__(self,post_id,url,app_url,app_id,post_dt,exp_dt,email_sent):
        """
        post_id: integer - edpost posting id
        url: text - edpost url
        app_url: text - Applitrack URL if available
        app_id: integer - Applitrack ID if available
        post_dt: text - Date posted on edpost
        exp_dt: text - Date expires on edpost
        email_sent: integer (0,1) : 0 if not yet sent, 1 if email sent
        """
        self.post_id = post_id
        self.url = url
        self.app_url = app_url
        self.app_id = app_id
        self.post_dt = post_dt
        self.exp_dt = exp_dt
        self.email_sent = email_sent

    def insert(self):
        self.cursor.execute("INSERT INTO job_postings \
                       (post_id,url,app_url,app_id,post_dt,exp_dt,email_sent) \
                       VALUES (?,?,?,?,?,?,?)" \
                       ,(self.post_id,self.url,self.app_url,self.app_id,self.post_dt,self.exp_dt,self.email_sent,))
        self.db.commit()
        self.db.close()
