from flask import Flask, render_template, json, request, redirect

import database.db_connector as db

import os

# Configuration

app = Flask(__name__)

db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/search-results')
def searchResults():
    return render_template("search-results.j2")

@app.route('/advanced-search')
def advancedSearch():
    return render_template("advanced-search.j2")

@app.route('/browse')
def browse():
    return render_template("browse.j2")

@app.route('/organization')
def organizationPage():
    name = request.args.get('name')
    summary = request.args.get('summary')
    imgPath = request.args.get('imgPath')
    return render_template("organization-page.j2", name=name, summary=summary, imgPath=imgPath)




# Listener 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8542))
    app.run(port=port, debug=True) 


