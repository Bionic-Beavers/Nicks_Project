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
    
        return searchResults(results)

    return render_template("main.j2")

def searchResults(Organizations):
    return render_template("search-results.j2", Organizations=Organizations)

@app.route('/advanced-search', methods=('GET', 'POST'))
def advancedSearch():

    if request.method == 'POST':
        name = "%" + request.form['name'] + "%"
        

        # Remove the or None
        try:
            if request.form['category'] == '' or None:
                category = "%"
            else: 
                category = request.form['category']

            city = "%" + request.form['city'] + "%"

            if request.form['state'] == '' or None:
                state = "%"
            else: 
                state = request.form['state']


            query = "SELECT * FROM Organizations WHERE name LIKE %s AND category LIKE %s AND city LIKE %s AND state LIKE %s ORDER BY name" 
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,category,city,state))
            results = cursor.fetchall()
            cursor.close()

            return searchResults(results)
        
        except: 

            query = "SELECT * FROM Organizations WHERE name LIKE %s ORDER BY name" 
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,))
            results = cursor.fetchall()
            cursor.close()

            return searchResults(results)

    return render_template("advanced-search.j2")

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
    port = int(os.environ.get('PORT', 8540))
    app.run(port=port, debug=True) 


