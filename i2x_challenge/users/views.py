# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import InvitationForm
from ..invitations.models import Invitation


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['first_name', 'last_name', 'team_name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


def assign_team(request):
    if request.method == "POST":
        invited_user = User.objects.get(id=request.user.id)
        if invited_user.team_name == "":
            try:
                invitation = Invitation.objects.get(email=request.user.email)
                invited_user.team_name = invitation.inviter.team_name
                invited_user.save()
            except ObjectDoesNotExist:
                print("invitation not exist")

        return JsonResponse({"response": "successful"})

class InvitationView(FormView):
    template_name = 'users/invitation.html'
    form_class = InvitationForm
    
    def get_form_kwargs(self):
        kwargs = super(InvitationView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(InvitationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})
