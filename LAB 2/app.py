from flask import Flask, request, render_template,make_response
app = Flask(__name__)

#@app.route('/')
#def index():
    #response = make_response('Hello World!')
    #response.headers['Content-Type'] = 'text/plain'
    #return response
@app.route('/')
def index():
    name = 'John'
    return render_template('index.html', name=name)
@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # validate the user's credentials and log them in
        if username == 'admin' and password == 'secret':
            return 'Login successful'
        else:
            return 'Invalid username or password'
    else:
        # show the login form
        return render_template('login.html')

