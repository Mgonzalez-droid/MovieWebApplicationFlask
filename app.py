#FOR WEBPAGE SUPPORT
from flask import Flask, render_template, url_for

#FOR ORACLE CONNECTION
import cx_Oracle
import os
import sys

#FOR GENERATING HTML CODE ON THE FLY
import html

# These pertain to the active user of the website
username = ""
password = ""
isAdmin = False
isLoggedIn = False
#cur =
#conn

# ____ W E B P A G E S ____
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Reviews')
def reviews():
    query = "SELECT TITLE FROM MOVIE"

    #get cursor to render query
    cur, conn = connectOracle()

    cur.execute(query)

    result = cur.fetchall()

    #important close connection, after recieving data!
    cur.close()
    conn.close()

    return render_template('reviews.html', titles=result)

# this will allow for constant polling of reviews
@app.route('/update_review_page')
def updateReviewPage():
    pass

@app.route('/Reviews/Review')
def review():
    pass

@app.route('/Review-Statistics')
def reviewStats():
    return render_template('review-statistics.html')

@app.route('/login')
def login():
    return render_template('login-page.html')

@app.route('/login/create-user')
def createUser():
    return render_template('create-user-page.html')

@app.route('/query-one')
def queryOne():
    return render_template('query-one.html')

@app.route('/query-two')
def queryTwo():
    return render_template('query-two.html')

@app.route('/query-three')
def queryThree():
    return render_template('query-three.html')

@app.route('/query-four')
def queryFour():
    return render_template('query-four.html')

@app.route('/query-five')
def queryFive():
    return render_template('query-five.html')


def generateNewUser():
    pass

def loginProcedure():
    pass


#____ O R A C L E  C O N N E C T I O N _____
def connectOracle():
    
    #Pull user name and password from text files
    oracleUsername = ""
    oraclePassword = ""
    with open("Credentials/username.txt") as f:
        oracleUsername = f.readline()
    with open("Credentials/password.txt") as f:
        oraclePassword = f.readline()

    #Initialize the oracle client where you have it saved
    # it should be in the following to locations for UNIX and Windows
    if sys.platform.startswith("darwin"):
        cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/instantclient_19_8")
    elif sys.platform.startswith("win32"):
        cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_19_8")

    #Create a connection
    conn = cx_Oracle.connect(oracleUsername + "/" + oraclePassword + "@oracle.cise.ufl.edu:1521/orcl")

    #Create cursor
    cur = conn.cursor()

    #return cursor
    return cur, conn


# ____ Q U E R Y  G E N E R A T I O N ____

@app.route('/update_query_one')
def updateQueryOne():
    pass

def uniqueQueryOne():
    pass

@app.route('/update_query_two')
def updateQueryTwo():
    pass

def uniqueQueryTwo():
    pass 

@app.route('/update_query_three')
def updateQueryThree():
    pass

def uniqueQueryThree():
    pass

@app.route('/update_query_four')
def updateQueryFour():
    pass

def uniqueQueryFour():
    pass

@app.route('/update_query_five')
def updateQueryFive():
    pass

def uniqueQueryFive():
    pass


# Main entry point for application
if __name__ == "__main__":
    connectOracle()
    app.run(debug=True)