from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_components import SelectMultipleField

class AuthorizationTokenForm(FlaskForm):
    client_id = StringField(validators=[DataRequired()])
    response_type = StringField(validators=[DataRequired()])
    redirect_uri = StringField(validators=[DataRequired()])
    scope = SelectMultipleField(validators=[DataRequired()],
        choices=(
            (
                ('Spotify Connect', (
                    ('user-modify-playback-state', 'user-modify-playback-state'),
                    ('user-read-playback-state', 'user-read-playback-state'),
                    ('user-read-currently-playing', 'user-read-currently-playing')
                )),
                ('Listening History ', (
                    ('user-top-read', 'user-top-read'),
                    ('user-read-recently-played', 'user-read-recently-played')
                )),
                ('Library', (
                    ('user-library-modify', 'user-library-modify'),
                    ('user-library-read', 'user-library-read')
                )),
                ('Follow', (
                    ('user-follow-modify', 'user-follow-modify'),
                    ('user-follow-read', 'user-follow-read')
                )),
                ('Playlists', (
                    ('playlist-read-private', 'playlist-read-private'),
                    ('playlist-modify-public', 'playlist-modify-public'),
                    ('playlist-modify-private', 'playlist-modify-private'),
                    ('playlist-read-collaborative', 'playlist-read-collaborative')
                )),
                ('Users', (
                    ('user-read-private', 'user-read-private'),
                    ('user-read-email', 'user-read-email')
                )),
                ('Playback', (
                    ('app-remote-control', 'app-remote-control'),
                    ('streaming', 'streaming')
                ))
            )
        )
    )
    form_submit = SubmitField('Submit')
