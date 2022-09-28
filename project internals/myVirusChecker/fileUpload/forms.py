from django import forms

class  FileUploadForm(forms.Form):
	"""docstring for  """
	file = forms.FileField()
	
