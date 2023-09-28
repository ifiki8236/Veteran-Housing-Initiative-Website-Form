from flask import Flask, jsonify, request, render_template, url_for
from flask_cors import CORS
from methods_list import dictToList
from auth import LoginForm
# Create an instance of the Flask class
app = Flask
CORS(app)

app.config['SECRET KEY']='30e1de59b5e464dfb5a107e7e849447c'

# Define a route and a view function
@app.route('/', methods=['POST'])
def main():
    data = request.json
    
    dictToList(data)
    return jsonify({'message': 'Data received without error'})

@app.route('/login')
def login():
    form = LoginForm()
    # return render_template('login_page.html', title='Login', form=form)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

