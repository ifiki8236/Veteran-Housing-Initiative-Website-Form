from flask import Flask, jsonify, request, render_template, session, redirect,g, url_for, flash
import os
from flask_cors import CORS
from methods_list import dictToList
# from auth import LoginForm
# Create an instance of the Flask class
app = Flask(__name__, static_url_path='/static')
CORS(app)

# app.config['SECRET_KEY']='30e1de59b5e464dfb5a107e7e849447c'
app.secret_key=os.urandom(24)

# Define a route and a view function
@app.route('/', methods=['POST'])
def main():
    data = request.json
    
    dictToList(data)
    return jsonify({'message': 'Data received without error'})

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        session.pop('user', None)
        if request.form['password']=='password':
            session['user']=request.form['username']
            return redirect(url_for('protected'))
    return render_template('login_page.html')

@app.route('/admin', methods=['GET','POST'])
def protected():
    if g.user:
        return render_template('admin.html',user=session['user'])
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user=None

    if 'user' in session:
        g.user=session['user']

@app.route('/dropsession', methods=['GET', 'POST'])
def dropsession():
    session.pop('user', '')
    return redirect(url_for('login'))
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

