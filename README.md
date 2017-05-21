#README for i2x Challenge

API doc
===========================

```
/admin

/users
/users/
/users/~redirect
/users/(?P<username>[\w.@+-]+)/$
/users/~update/
/users/~assign-team/
/users/~send-invitation/

/accounts
/accounts/signup/
/accounts/login/
/accounts/logout/
/accounts/password/change/
/accounts/password/set/
/accounts/email/
/accounts/confirm-email/
/accounts/confirm-email/(?P<key>[-:\w]+)/$
/accounts/password/reset/
/accounts/password/reset/done/
/accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$
/accounts/password/reset/key/done/$

/invitations
/invitations/send-invitations/
/invitations/send-json-invite/
/invitations/accept-invite/(?P<key>\w+)/
```

Instructions on Running locally
===========================
##Prerequisites
```
Python3
PostgreSQL>=9.4
Mac/Linux
```

##Use virtualenv
```
python -m venv ENV
source ENV/bin/activate
```
##Clone this repository
```
git clone https://github.com/vrootic/i2x_challenge.git
```
##Install packages
```
cd i2x_challenge
pip install -r requirements
```
##Initialize DB
```
createdb i2x_challenge
python manage.py migrate
```
##Create Superuser
```
python manage.py createsuperuser
```
##Start Dev Server
```
python manage.py runserver
```

Deployment instructions
===========================
##Install Heroku Toolbelt
First, [sign up to Heroku](https://signup.heroku.com/)
Then, install [Heroku toolbelt](https://toolbelt.heroku.com/)

```
heroku login
```
##Create Heroku app
```
heroku create [your_app_name]
```
##Set environment variables
```
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DJANGO_SECRET_KEY='[your secret key]'
heroku config:set DJANGO_SETTINGS_MODULE='config.settings.production'
heroku config:set DJANGO_ALLOWED_HOSTS='.herokuapp.com'
```
##Push to deploy
```
git push heroku master
```
##Migrate the DB
```
heroku run python manage.py migrate
```

Finish!



Link to live demo on Heroku
===========================

[Live Demo on Heroku](https://i2x-challenge-demo.herokuapp.com/)