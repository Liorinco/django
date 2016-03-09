# -*- coding: utf8 -*-

"""
    !!! FAIL: Never run !!!
"""

import os.path
import sqlite3


project_path = os.path.abspath(os.pardir)
conn = sqlite3.connect(
    os.path.abspath(os.path.join(project_path, "mysite", "db.sqlite3")))
curs = conn.cursor()
curs.execute("PRAGMA database_list;")
conn.close()
