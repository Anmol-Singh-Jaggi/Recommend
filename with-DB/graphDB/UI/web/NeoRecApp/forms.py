from django import forms

class UserIDForm(forms.Form):
    userid = forms.IntegerField(label='User ID')

class UpdateRatingForm(forms.Form):
    userid = forms.IntegerField(label='User ID')
    movieid = forms.IntegerField(label='Movie ID')
    rating = forms.IntegerField(label="New Rating")

