#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:01:14 2020

@author: jarhaiti
"""

from django import forms


class ContactForms(forms.Form):
    message_name = forms.CharField(label="Nom", max_length=100)
    message_email = forms.EmailField(label = "Email")
    message = forms.CharField(widget=forms.Textarea)
    pass

    