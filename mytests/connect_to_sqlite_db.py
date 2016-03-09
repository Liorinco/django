# -*- coding: utf8 -*-

import os.path
import sqlite3


project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
db_path = os.path.abspath(os.path.join(project_path, "mysite", "db.sqlite3"))
conn = sqlite3.connect(db_path)
curs = conn.cursor()
curs.execute("PRAGMA database_list;")
for result in curs:
    print result
curs.execute("SELECT name FROM main.sqlite_master WHERE type='table';")
for result in curs:
    print result
conn.close()
