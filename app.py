from flask import Flask, render_template, json, request, redirect

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
        query = "SELECT * FROM Organizations WHERE name LIKE %s" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,))
        results = cursor.fetchall()
        cursor.close()
    
        print(results)

        return render_template("search-results.j2", Organizations=results)

    return render_template("main.j2")

@app.route('/search-results', methods=('GET', 'POST'))
def searchResults(Organizations):

    if request.method == 'POST':
        name = "%" + request.form['name'] + "%"
        query = "SELECT * FROM Organizations WHERE name LIKE %s" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,))
        results = cursor.fetchall()
        cursor.close()
        
        return render_template("search-results.j2", Organizations=results)

    return render_template("search-results.j2",)

@app.route('/advanced-search', methods=('GET', 'POST'))
def advancedSearch():

    if request.method == 'POST':
        name = "%" + request.form['name'] + "%"
        query = "SELECT * FROM Organizations WHERE name LIKE %s" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name,))
        results = cursor.fetchall()
        cursor.close()
        
        return render_template("search-results.j2", Organizations=results)

    return render_template("advanced-search.j2")

@app.route('/browse')
def browse():
    query = "SELECT * FROM Organizations;"
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

    name = request.args.get('name')
    summary = request.args.get('summary')
    imgPath = request.args.get('imgPath')

    return render_template("organization-page.j2", organization=organization)




# Listener 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8542))
    app.run(port=port, debug=True) 


