from flask import Flask, jsonify, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from config import Config
import os


app = Flask(__name__)

# Load config from config.py
app.config.from_object(Config)

# Use the secret key for session management
app.secret_key = app.config['SECRET_KEY']

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],  # Get from config
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],  # Get from config
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',  # This includes the jwks_uri
    # access_token_url='https://accounts.google.com/o/oauth2/token',
    # access_token_params=None,
    # authorize_url='https://accounts.google.com/o/oauth2/auth',
    # authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    # userinfo_endpoint='https://www.googleapis.com/oauth2/v1/userinfo',  # This is Google API endpoint for user info
    client_kwargs={'scope': 'openid profile email'},
)

# Home route
@app.route('/')
def index():
    email = dict(session).get('email', None)
    return f'Hello, {email}!'

# Login route
@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

# Authorization route (callback)
@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()  # Get access token
    # you can save the token into database
    resp = google.get('userinfo')  # Use the token to fetch user info
    user_info = resp.json()
    print(user_info)
    session['email'] = user_info['email']  # Store user email in session
    return redirect('/')
# def authorize():
#     token = github.authorize_access_token()
#     # you can save the token into database
#     profile = github.get('/user', token=token)
#     return jsonify(profile)


# Logout route
@app.route('/logout')
def logout():
    session.pop('email', None)
    # session.clear()  # Clear all session data
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
