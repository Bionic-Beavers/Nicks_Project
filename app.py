from flask import Flask, render_template, json

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
    return render_template("organization-page.j2")




# Listener 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8541))
    app.run(port=port, debug=True) 


