import flask 
import pymongo
from flask import Flask
from pymongo import MongoClient

#hst: history, hlst: help list,hf_data: help form data,hc:helpcoin


mongo_url = "mongodb+srv://kskkoushik135:hmUGoaSjnHdTJXNW@cluster0.xgap26r.mongodb.net/"

user=MongoClient(mongo_url)

db= user['user_data']

user_name= db['user_name']

def create_user(username, email, password, location):
    un = user_name.find_one({'username': username})
    em = user_name.find_one({'email': email})
    if un is None and em is None:
        user_name.insert_one({'username': username, 'email': email, 'password': password, 'location': location, 'hc_bal':20, 'hst':[], 'hlst':[]})
        return "user created"
    else:
        return "user already exists"


def login(username, password):
    un = user_name.find_one({'username': username})
    if un is None:
        return "create an account"   # url to be inserted to go to main page
    else:
        if un['password'] == password:
            return "dive into help coin"    # url to be inserted
        else:
            return "incorrect password"   
        

def inchc_bal(username, hc_count):
    un = user_name.find_one({'username': username})
    un['hc_bal']=hc_count+un['hc_bal']

def dechc_bal(username, hc_count):
    un = user_name.find_one({'username': username})
    un['hc_bal']=un['hc_bal']-hc_count


def get_usrdata(username):
    un = user_name.find_one({'username': username})
    return [un['hc_bal'], un['username'],un['email'],un['location']]


def hf_data(username, title, description, location, hc_pay):
    selected_users = user_name.find({'location': location})
    for user in selected_users:
        user['hlst'].append({'username': username,'title': title, 'description': description, 'location': location, 'hc_pay': hc_pay})


'''def hlp_accept(seeker,helper):
    seek = user_name.find_one({'username': seeker})
    seek['hst'].append()'''



