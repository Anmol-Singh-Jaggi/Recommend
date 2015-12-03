from django import forms

class UserIDForm(forms.Form):
    userID = forms.IntegerField(label='User ID')

class UpdateRatingForm(forms.Form):
    userID = forms.IntegerField(label='User ID')
    movieID = forms.IntegerField(label='Movie ID')
    rating = forms.IntegerField(label="Movie Rating")

class RecommendForm(forms.Form):
    userID = forms.IntegerField(label='User ID')
    recoID = forms.IntegerField(label='Reco ID')
