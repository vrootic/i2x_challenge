# -*- coding: utf-8 -*-
from django import forms

from ..invitations.models import Invitation


class InvitationForm(forms.Form):
    email = forms.EmailField(required=False, max_length=255)
    message = forms.CharField(
    	required=False,
    	initial="I would like to invite you to my team.",
    	widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(InvitationForm, self).__init__(*args, **kwargs)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        email = self.cleaned_data["email"]
        invite = Invitation.create(email, inviter=self.request.user)
        invite.send_invitation(self.request)
        