from db import Job_Post
record = Job_Post(9999999991,"test","test",111111111111,"test","test",1)
print record.app_id
record.insert()
