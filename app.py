from flask import Flask, render_template, request, redirect, url_for
from mdb import create_user, login_retri, get_usrdata, hf_data, append_locdata,available_helps,list_help


app = Flask(__name__)


@app.route('/')
def fun1():
  return render_template('index.html')

@app.route("/geo_data" , methods = ['POST'])
def index():
    lat = request.form['latitude']
    lon = request.form['longitude']
    all_locations = append_locdata(lat,lon)
    return render_template("index.html", lati = lat , longi = lon, all_locations = all_locations)

@app.route('/account_create', methods=['POST'])
def create2_user():
  fullname = str(request.form['fullname'])
  username = str(request.form['username'])
  email = str(request.form['email'])
  password = str(request.form['password'])
  location = str(request.form['location'])
  status = create_user(username, email, password, location, fullname)
  li=get_usrdata(username)
  if status == 'user created':
      return render_template('profile.html', username=username, balance=li[0],email=li[2],location=li[3],fullname=li[4])

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/login')
def login():
   return render_template('login.html')


@app.route('/account_login', methods=['POST'])
def login1():
  username = str(request.form['username'])
  password_g = str(request.form['password'])    #password_g is given password
  status= login_retri(username)
  li=get_usrdata(username)
  if status != 'create an account':
      password_db = status
      if password_g == password_db:
          return render_template('profile.html', username=username, balance=li[0],email=li[2],location=li[3],fullname=li[4])
      else:
          return render_template('index.html')
            
@app.route('/help/<username>')
def help(username):
   return render_template('request.html' , username=username)

@app.route('/avhelps')
def avhelps():
   li=available_helps()
   return render_template('map.html',li=li)

@app.route('/get_data', methods=['POST'])
def get_usrdata1():
  username = str(request.form['username'])
  return get_usrdata(username)

@app.route('/view_help')
def view_help():
   return render_template('helpview.html')

@app.route('/store_helps', methods=['POST'])   
def store_helps():
  username = str(request.form['username'])
  title = str(request.form['title'])
  description = str(request.form['description'])
  location = str(request.form['location'])
  hc_pay = str(request.form['hc_pay'])
  list_help( title, description, location, hc_pay,username)
  li=available_helps()
  return render_template('map.html', username=username,li=li)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
