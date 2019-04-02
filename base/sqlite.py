import sqlite3
import sys

script, filename = sys.argv

try:
    conn = sqlite3.connect('c:/temp/main.db')
    recordset = conn.cursor()
    sqlcmd = 'select max(id) from bats_users'
    recordset.execute(sqlcmd)

except Exception:
    print('database error. quitting (-1).')
    sys.exit(-1)

fields = recordset.fetchone()
max_id = int(fields[0])

try:
    f = open(filename,'r')

except Exception:
    print('cannot open file for reading. quitting (-2).')
    sys.exit(-2)

for line in f:
    fields = line.split('\t')
    user = fields[1]
    login = fields[2]
    logout = fields[3]
    max_id += 1
    sqlcmd = 'insert into bats_users values(%d,'%s','%s','%s')' % (max_id, user, login, logout)
    recordset.execute(sqlcmd)

f.close()

conn.commit()
conn.close()
conn.close()