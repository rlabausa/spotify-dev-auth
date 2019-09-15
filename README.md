# spotify-dev-auth
This Flask app helps streamline the tedious process of generating a Spotify access token through the **[Implicit Grant Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/#implicit-grant-flow)**. 

To get the app running:
1. Install the required dependencies:
    ```
    pip3 install -r requirements.txt
    ```
2. Configure your **.env** file with the following variables:
    - `SECRET_KEY`: This is required to use FlaskForms and can be generated with Python 3's `os` or `secrets` module.
        - In a Python shell, simply copy the output of either of the following commands into your **.env** file:
            ```Python
            # option 1 - generate key with os module
            import os
            os.urandom(32)

            # option 2 - generate key with secrets module
            import secrets
            secrets.token_hex(16)
            ```
    - `CLIENT_ID`: This is taken from an existing application in your Spotify developer [dashboard](https://developer.spotify.com/dashboard/) (you will need to create one if you don't already have one).
    - `RESPONSE_TYPE='token'`: The required parameter for obtaining authorization through the **Implicit Grant Flow**.
    - `REDIRECT_URI='http://localhost:5000/auth/callback/'`: This is the URL/route that is designed to work with this application. It must be white-listed in your application. 
        - To do this, visit: https://developer.spotify.com/dashboard/applications. Select your app. Go to **EDIT SETTINGS > Redirect URIs**, add in the URL and click **SAVE**.
3. (**Optional**) You can remove or configure the default scope by adding to or removing from the `scope` variable in the `auth` view function.
    - You can read about the various authorization scopes on: https://developer.spotify.com/documentation/general/guides/scopes/.
4. Once everything is configured to your liking, run the command:
    ```
    flask run
    ```
From there, you should be able to access the application via browser at http://localhost:5000/. Once you submit the form, it will redirect you to a login page asking to authorize the app to view your account. Once you've accepted, it will redirect you to the callback URL where you can copy the access token right off of the HTML page.