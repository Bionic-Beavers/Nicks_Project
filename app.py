from flask import Flask, render_template, json, request, redirect

import requests

import database.db_connector as db

import os

import MySQLdb

# Configuration

app = Flask(__name__)

db_connection = db.connect_to_database()

# Routes 

@app.route('/', methods=('GET', 'POST'))
def root():
    
    if request.method == 'POST':
        name = "%" + request.form['name'] + "%"
        query = "SELECT * FROM Organizations WHERE name LIKE %s ORDER BY name" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,))
        results = cursor.fetchall()
        cursor.close()
    
        return render_template("search-results.j2", Organizations=results)

    return render_template("main.j2")

@app.route('/search-results', methods=('GET', 'POST'))
def searchResults(Organizations):

    if request.method == 'POST':
        name = "%" + request.form['name'] + "%"
        query = "SELECT * FROM Organizations WHERE name LIKE %s ORDER BY name" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,))
        results = cursor.fetchall()
        cursor.close()
        
        return render_template("search-results.j2", Organizations=results)

    return render_template("search-results.j2",)

@app.route('/advanced-search', methods=('GET', 'POST'))
def advancedSearch():

    query = "SELECT * FROM Organizations ORDER BY name;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    cursor.close()

    if request.method == 'POST':
        name = "%" + request.form['name'] + "%"
        
        if request.form['category'] == '':
            category = "%"
        else: 
            category = request.form['category']

        if request.form['country'] == '':
            country = "%"
        else: 
            country = request.form['country']

        query = "SELECT * FROM Organizations WHERE name LIKE %s AND category LIKE %s AND country LIKE %s ORDER BY name" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,category,country))
        results = cursor.fetchall()
        cursor.close()
        
        return render_template("search-results.j2", Organizations=results)

    return render_template("advanced-search.j2", Organizations=results)

@app.route('/browse')
def browse():
    query = "SELECT * FROM Organizations ORDER BY name;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    cursor.close()

    return render_template("browse.j2", Organizations=results)

def get_organization(id):
    query = "SELECT * FROM Organizations WHERE organization_id =" + str(id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    organization = cursor.fetchone()
    cursor.close()

    return organization

@app.route('/<int:id>/organization', methods=('GET', 'POST'))
def organizationPage(id):
    organization = get_organization(id)


    wikiName = organization['name']
    payload = {"article": wikiName}

    output = requests.get('https://hidden-basin-72940.herokuapp.com/', params=payload)

    summary = output.text

    return render_template("organization-page.j2", organization=organization, summary=summary)




# Listener 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8542))
    app.run(port=port, debug=True) 


