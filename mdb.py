import flask
import pymongo
from flask import Flask
from pymongo import MongoClient

#hst: history, hlst: help list,  hf_data: help form data, hc:helpcoin

mongo_url = "mongodb+srv://kskkoushik135:hmUGoaSjnHdTJXNW@cluster0.xgap26r.mongodb.net/"

user = MongoClient(mongo_url)

db = user['user_data']

user_name = db['user_name']


def create_user(username, email, password, location,fullname):
  un = user_name.find_one({'username': username})
  em = user_name.find_one({'email': email})
  if un is None and em is None:
    user_name.insert_one({
        'fullname': fullname,
        'username': username,
        'email': email,
        'password': password,
        'location': location,
        'hc_bal': 20,
        'hst': [],
        'hlst': []
    })
    return "user created"
  else:
    return "user already exists"


def login_retri(username):
  un = user_name.find_one({'username': username})
  if un is None:
    return "create an account"  # url to be inserted to go to main page
  else:
    return un['password']


def append_locdata(latitude, longitude):
      un=user_name.find_one({'username': 'default'})
      un['location_data'].append([latitude, longitude])

      return un['location_data']


def inchc_bal(username, hc_count):
  un = user_name.find_one({'username': username})
  if un is not None:
    un['hc_bal'] = hc_count + un['hc_bal']


def dechc_bal(username, hc_count):
  un = user_name.find_one({'username': username})
  if un is not None:
    un['hc_bal'] = un['hc_bal'] - hc_count


def get_usrdata(username):
  un = user_name.find_one({'username': username})
  if un is not None:
    return [un['hc_bal'], un['username'], un['email'], un['location'], un['fullname']]
  else:
    return []


def hf_data(username, title, description, location, hc_pay):    #extra functionality
  selected_users = user_name.find({'location': location})
  for user in selected_users:
    user['hlst'].append({
        'username': username,
        'title': title,
        'description': description,
        'location': location,
        'hc_pay': hc_pay
    })
  return []

def available_helps():
  un = user_name.find_one({'username': 'default'})
  return un['hlst']


def list_help(title,description,location,balance,username):
  filter= {'username': 'default'}
  update={'$push':{'hlst': [ title,description,location,balance,username]}}
  user_name.update_one(filter,update)


'''def hlp_accept(seeker,helper):
    seek = user_name.find_one({'username': seeker})
    seek['hst'].append()'''
