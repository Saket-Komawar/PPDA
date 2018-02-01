from django import forms

class dataForm(forms.Form):
	docFile = forms.FileField(
		label = 'Upload a CSV file in Encrypted Format',
		help_text = 'Maximum 10Mb'
	)	

	epsilon = forms.FloatField() #(max, min)
	sensitivity = forms.FloatField() 
