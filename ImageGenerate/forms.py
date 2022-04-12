from django import forms


class TextUploadForm(forms.Form):
	description = forms.CharField()
	# mask = forms.ImageField()
