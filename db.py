#! /bin/python

import os
tmpFile = '123.txt'
sqlite3 = 'sqlite3'
dropTBL =  """drop table customer; 
"""
createTBL = """create table customer (
    id int NOT NULL,  
    LastName varchar(50) NOT NULL,
    FirstName varchar(50) NOT NULL,
    Address varchar(50) NOT NULL,
    City varchar(50) NOT NULL,
    PRIMARY KEY (id)
); 
"""
insertTBL = """insert into customer values (%s, '%s', '%s', '%s', '%s');
"""

selectTBL = """select * from customer;
"""
saveTBL = """.save py.db
"""
quitTBL = """.q
"""
# .save test.db
# .q

sqlSchema = dropTBL + createTBL
for line in open('customer.txt').readlines():
    line = line.replace('\n', '')
    data = line.split(':')
    sqlSchema += insertTBL % (data[0], data[1] ,data[2], data[3], data[4])

sqlSchema += selectTBL
sqlSchema += saveTBL
sqlSchema += quitTBL

f = open(tmpFile, 'w')
f.write(sqlSchema)
f.close()

shellTBL = 'cat %s | sqlite3' % tmpFile

print os.popen(shellTBL).read()
os.popen('rm %s' % tmpFile)

 #print db
