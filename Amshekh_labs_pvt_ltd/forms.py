from multiprocessing.sharedctypes import Value
from django import forms

class usersForm(forms.Form):  # You can give any name to class, i have given usersForm. In bracket forms is what we import just now and Form is the class name.
    num1 = forms.CharField(label="Value 1")  # character field that means there will be textbox
    num2 = forms.CharField(label="Value 2")
    num3 = forms.CharField(label="Value 3", required=False)
