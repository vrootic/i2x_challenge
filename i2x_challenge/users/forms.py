# -*- coding: utf-8 -*-
from django import forms


class InvitationForm(forms.Form):
    email = forms.EmailField(required=False, max_length=255)
    message = forms.CharField(
    	required=False,
    	initial="I would like to invite you to my team.",
    	widget=forms.Textarea
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print("team_name")
        pass