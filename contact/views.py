# -*- coding: utf-8 -*-
"""
@author: dan.wlodarski
"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm
from django.views import generic
from . import models


class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            'name',
            'email',
            'base_zipcode',
            'plus4_zipcode',
            'comment'
        ]

        @property
        def helper(self):
            helper = FormHelper()
            # Need to do some prettier things in this layout.
            helper.layout = Layout(
                Field('name'),
                Field('email'),
                Field('base_zipcode'),
                Field('plus4_zipcode'),
                Field('comment'),
                Submit(
                    'submit',
                    'Submit your request for contact from a SPARC representative',
                    css_class='btn-success'
                )
            )
            return helper


class IndexView(SuccessMessageMixin, generic.CreateView):
    template_name = 'contact/index.html'
    success_message = 'Your request for contact has been recieved. A SPARC representative will be in touch within ' \
        '48 hours. Thank you!'
    form_class = ContactForm
