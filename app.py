from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World"

@app.route('/home')
def home():
    return "This is home page"

from controller import *