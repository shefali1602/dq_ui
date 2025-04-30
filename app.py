#import Libraries
import os
from flask import Flask, render_template, request, redirect, url_for
import oracledb
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

app= Flask(__name__)

#Oracle DB Connection Details
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORd')
db_dsn = os.getenv('DB_DSN')

#Connect to DB 
def get_db_connection():
    connection= oracledb.connect(user=db_username, password=db_password, dsn=db_dsn)
    return connection

@app.route('/',methods=['GET','POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    selected_id = None
    selected_data = None

    #Fetch all project ids from a drop down 
    cursor.execute("SELECT PROJID FROM DJFJFJ_DC.DC_CONFIG")
    ids = [row[0] for  row in cursor.fetchall()]

    if request.method =='POST' and 'selected_id' in request.form:
        selected_id= request.form[selected_id]
        cursor.execute("SELECT * FROM OWNER_gb.DC_CONFIG WHERE PROJID= :id",{'id':selected_id})
        row = cursor.fetchone()
        if row:
            masked_pwd = "*" * len(row[16])
            selected_data = (row[:16]+(masked_pwd,) +row[17:])
    cursor.close()
    conn.close()
    return render_template('index.html', id = ids, selected_id= selected_id, selected_data= selected_data)

@app.route('/add', methods=['POST'])
def add_record():
      conn = get_db_connection()
      cursor = conn.cursor()      

      projid = request.form['PROJID']
      ds_source = request.form['DS_SOURCE']
      sourcefile = request.form['SOURCEFILE']
      sourcedir = request.form['SOURCEDIR']
      souretable = request.form['SOURCETABLE']
      sourcecolumns = request.form['SOURCECOLUMNS']
      nulllogfile = request.form['NULLLOGFILE']
      duplicatelogfile = request.form['DUPLICATELOGFILE']
      outputpath = request.form['OUTPUTPATH']
      pkcol = request.form['PKCOL']
      dbschema = request.form['DBSCHEMA']
      targetlogfile = request.form['TARGETLOGFILE']
      db_host = request.form['DB_HOST']
      port = request.form['PORT']
      servicename = request.form['SERVICENAME']
      dbuser = request.form['DBUSER']
      dbenckey = request.form['DBENCKEY']
      chunksize = request.form['CHUNKSIZE']

     
      conn.commit()
      cursor.close()
      conn.close()
      return redirect(url_for('index'))

if __name__ == '__main__':
      app.run(debug= True)      