from flask import Flask, request
from mdb import create_user, inchc_bal, dechc_bal, login, get_usrdata, hf_data

app = Flask(__name__)
@app.route('/')
def fun1():
    return "working"
    
@app.route('/account_create' , methods=['POST'])
def create_user():
    username=str(request.form['username'])
    email=str(request.form['email'])
    password=str(request.form['password'])
    location=str(request.form['location'])
    return create_user(username, email, password, location)


@app.route('/account_login' , methods=['POST'])
def login():
    username=str(request.form['username'])
    password=str(request.form['password'])
    return login(username, password)

@app.route('/get_data' , methods=['POST'])
def get_usrdata():
    username=str(request.form['username'])
    return get_usrdata(username)

@app.route('/helpform_data' , methods=['POST'])
def hf_data():
    username=str(request.form['username']) 
    title=str(request.form['title'])
    description=str(request.form['description'])
    location=str(request.form['location'])
    hc_pay=str(request.form['hc_pay'])
    return hf_data(username,title,description,location,hc_pay)


if __name__ == "__main__":
      app.run(host= '0.0.0.0',debug =True)

