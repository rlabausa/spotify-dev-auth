#!/path/to/python3/virtual/environment
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect

from forms import AuthorizationTokenForm

# load environment variables
proj_dir = os.path.dirname(__file__)
env_path = os.path.join(proj_dir, '.env')
load_dotenv(env_path)

# instantiate flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# default authorization landing screen
@app.route('/', methods=['GET', 'POST'])
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    form = AuthorizationTokenForm(client_id = os.environ.get('CLIENT_ID'),
                                  response_type = os.environ.get('RESPONSE_TYPE'), 
                                  redirect_uri = os.environ.get('REDIRECT_URI'),
                                  scope = ['user-read-private', 'playlist-read-private', 'playlist-modify-private', 'playlist-modify-public'] )

    if form.validate_on_submit():
        CLIENT_ID = form.client_id.data
        RESPONSE_TYPE = form.response_type.data
        REDIRECT_URI = form.redirect_uri.data
        SCOPE = form.scope.data

        url = f'https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type={RESPONSE_TYPE}&redirect_uri={REDIRECT_URI}&scope={"%20".join(SCOPE)}'

        return redirect(url)

    return render_template('form_auth.html', form=form)

# authorization redirect uri
@app.route('/auth/callback/', methods=['GET'])
def auth_callback():
    return render_template('table_res.html')
