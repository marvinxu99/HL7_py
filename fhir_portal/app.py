from flask import Flask, jsonify, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
from config import Config
from datetime import timedelta
import asyncio
from fhir_portal.fhirpy_client.fetch_patient import fetch_patients
from fhir_portal.fhirpy_client.fetch_encounter import fetch_encounters


app = Flask(__name__)

# Load config from config.py
app.config.from_object(Config)

# Use the secret key for session management
app.secret_key = app.config['SECRET_KEY']

# Set session expiration to automatically clear the session after a certain time period
app.permanent_session_lifetime = timedelta(minutes=10)

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
    # If logged in, show the user's email and id
    session_d = dict(session)
    email = session_d.get('email', None)
    id = session_d.get('id', None)
    return f'Hello, email={email}, id={id}!'

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
    
    # Use the token to fetch user info
    resp = google.get('userinfo')  
    user_info = resp.json()
    print(user_info)

    # Store user email and id in session
    session['email'] = user_info['email']
    session['id'] = user_info['id']
    session.permanent = True
    
    return redirect('/')


@app.route('/patients')
def patients_page():
    # Render the patients.html template
    return render_template('patients.html')


# Route for the encounters page
@app.route('/encounters')
def encounters_page():
    return render_template('encounters.html')


# API endpoint to get patients as JSON
@app.route('/api/patients', methods=['GET'])
def get_patients():
    patients = asyncio.run(fetch_patients())
    return jsonify(patients)


# API endpoint to get encounters as JSON
@app.route('/api/encounters', methods=['GET'])
def get_encounters():
    encounters = asyncio.run(fetch_encounters())
    return jsonify(encounters)


# Logout route
@app.route('/logout')
def logout():
    session.pop('email', None)
    # session.clear()  # Clear all session data
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
