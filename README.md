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


 
Deployment instructions
===========================



Link to live demo on Heroku
===========================

[Live Demo on Heroku](https://i2x-challenge-demo.herokuapp.com/)