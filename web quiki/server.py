from flask import Flask
from flask import render_template, request, session, redirect
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/joining')
def joining():
    return render_template('join_now.html')

@app.route('/join')
def join():
    username = request.form.get('username')
    mail = request.form.get('email')
    password = request.form.get('password')
    opp_username = f'{username}.json'
    user_directory = os.listdir(path='users')
    if opp_username in user_directory:
        print(f'[red]<!>Username already used | user:{username}')
        return redirect('/loginpage')

    if opp_username not in user_directory:
        filename = f'users\{username}.json'
        data = {
            "username": username,
            "Email": mail,
            "password": password
            }
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f'[purple]<+> New Account created | [blue]user:{username} | Email:{mail} | [blue]passw:{password}')
        #try:
        #    email_sender.send_mail(email=mail)
        #    print(f'[green]<?> Email sendt to Email: {mail}')
        #except:
        #    print(f'[red]<?> Email not sendt to Email: {mail}')
        #    pass
        return redirect('/dashboard')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8989)