from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/Reviews/Review')
def review():
    return render_template('review.html')

@app.route('/Review-Statistics')
def reviewStats():
    return render_template('review-statistics.html')

@app.route('/login')
def login():
    return render_template('login-page.html')

@app.route('/login/create-user')
def createUser():
    return render_template('create-user-page.html')

def generateReviewsPage():
    pass

def generateReviewPage():
    pass

def generateNewUser():
    pass

def loginProcedure():
    pass

def uniqueQueryOne():
    pass

def uniqueQueryTwo():
    pass 

def uniqueQueryThree():
    pass

def uniqueQueryFour():
    pass

if __name__ == "__main__":
    app.run(debug=True)