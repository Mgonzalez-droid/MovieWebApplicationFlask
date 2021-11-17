import cx_Oracle
import os
import sys

username = ""

with open("Credentials/username.txt") as f:
    username = f.readline()


password = ""

with open("Credentials/password.txt") as f:
    password = f.readline()

#Initialize the oracle client where you have it saved
if sys.platform.startswith("darwin"):
    cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/instantclient_19_8")
elif sys.platform.startswith("win32"):
    cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_19_8")

#Create a connection
conn = cx_Oracle.connect(username + "/" + password + "@oracle.cise.ufl.edu:1521/orcl")

print(conn.version)

#Create cursor
cur = conn.cursor()

query = """
SELECT * FROM CITY
"""

#Execute query
cur.execute(query)

result = cur.fetchall()

for index, tuple in enumerate(result):
    element_one = tuple[0]
    element_two = tuple[1]
    element_three = tuple[2]
    element_four = tuple[3]
    element_five = tuple[4]
    element_six = tuple[5]
    element_seven = tuple[6]
    print(element_one, element_two, element_three, element_four, element_five, element_six, element_seven)

#print(result)