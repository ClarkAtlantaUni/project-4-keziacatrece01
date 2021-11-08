#TODO Add the missing routes or complete the logic of the existing routes

import json
import os
import uuid
from datetime import datetime
from hashlib import md5
from pathlib import Path

from cis301.project4.phonecall import PhoneCall
from cis301.project4.server.PhoneBillServer import PhoneBillServer
from flask import Flask, request, redirect, render_template, g, session
from flask_bootstrap import Bootstrap

from cis301.project4.util import Util

app = PhoneBillServer( __name__ )


def run(port=8000, file="database.txt"):
    app.set_port(port)
    app.set_file(file)
    Bootstrap( app )
    app.start(True)


@app.route('/home')
@app.route( '/' )
def home():
    message = dict()
    message["date"] =datetime.now().strftime( '%Y' )
    message["file"]= app.get_file()
    message["text"] = "Welcome to Phone Bill Application!"
    if session.get('user'):
        message["username"] = session['user']
    return render_template( "index.html",message=message );

@app.route('/auth', methods=["POST", "GET"])
def authenticate():
    if request.method=="GET":
        message = dict()
        message["date"] = datetime.now().strftime('%Y')
        message["text"] = "Enter your credentials"
        return render_template( "template_login.html", message=message )
    else:
        # TODO: authenticate the user
        data = request.json
        user = dict()
        if data is None:
            return '{"res":"400", "text":"invalid username or password."}'

        if len(data)==0 or not data['password'] or not data['email']:
            return '{"res":"400", "text":"Please enter username and password."}'
        user['password'] = str(md5(data['password'].encode()).digest())
        user['email'] = data['email']
        if app.get_userdb().authenticate_user(user):
            message = dict()
            message["date"] = datetime.now().strftime('%Y')
            user = app.get_userdb().get_user_by_email(user)
            message["user"] = user[0]
            message["text"] = "Welcome " + user[0]
            session['user'] = user[0]
            session['uid']= user[1]
            if data.get( 'client' ):
                return '{"res":"200", "text":"authenticated user."}'
            else:
                return redirect('/user/home')
        else:
            return '{"res":"400", "text":"invalid username or password."}'


@app.route('/register', methods=["POST", "GET"])
def register():
    #TODO: register the user

    if request.method == "GET":
        message = dict()
        message["date"] = datetime.now().strftime('%Y')
        message["text"] = "Register as a new user"
        return render_template( "template_register.html", message=message )
    elif request.method == "POST":
        data = request.json
        user = dict()
        user['id'] = str(uuid.uuid4())
        user['name'] = data['name']
        user['password'] = str(md5(data['password'].encode()).digest())
        user['email'] = data['email']
        message =""
        if app.get_userdb().insert_user(user):
            message = '{"res":"200", "text":"Your account is active now"}'
        else:
            message = '{"res":"400", "text":"user name already exist"}'
        return message
    else:
        return render_template( "invalid_page.html", message="" )

@app.route('/logout', methods=["GET"])
def logout():
    session.clear()
    message = dict()
    message['user'] = "Test User"
    message["date"] = datetime.now().strftime( '%Y' )
    message["text"] = "Welcome"
    if request.method == "GET":
        # TODO: authenticate the user
        return redirect("/home")

@app.route('/user/home')
def user_home():
    if session['user'] and session['uid']:
        message = dict()
        message["date"] = datetime.now().strftime( '%Y' )
        message["username"] = session['user']
        message["text"] = "Welcome " + session['user']
        return render_template('user.html', message=message)
    else:
        redirect('/auth')

@app.route('/user/search')
def user_search():
    if session.get('user') and session.get('uid'):
        message = dict()
        message["date"] = datetime.now().strftime( '%Y' )
        message["username"] = session['user']
        message["text"] = "Welcome " + session['user']+ ". The seach function will be available soon!"
        return render_template('index.html', message=message)
    else:
        redirect('/auth')

@app.route('/user/add', methods=["GET","POST"])
def add_phonecall():
        if request.method=='GET':
            #TODO: load the form from the template
            if session.get( 'user' ) and session.get( 'uid' ):
                return  '{"res":"401", "text":"Not implemented"}'
            else:
                redirect( '/auth' )
        #gather phone call info.
        elif request.method == 'POST':
            if session.get( 'user' ) and session.get( 'uid' ):
                #contains phonecall info
                data = request.json
                caller = data['caller']
                callee = data['callee']
                startdate = data['startdate']
                enddate= data['enddate']
                # check and validate user data
                message=""
                if Util.isValidPhoneNumber(caller) and Util.isValidPhoneNumber(callee):
                    phonecall = PhoneCall( callee, caller, startdate, enddate )
                    phonecall.set_uid(session.get('uid'))
                    app.get_userdb().insert_phonecall(phonecall)

                    #add the new phone call to the database
                    print(phonecall)
                    #if insertion is a success
                    message = '{"res":"200", "text":"added a new phone call"}'

                else:
                    message = '{"res":"400", "text":"invalid phone call attributes"}'

                return message
            else:
                return '{"res":"401", "text":"Auth failed"}'
        else:
            return '{"res":"401", "text":"Method not supported"}'

if __name__ == "__main__":
    run()