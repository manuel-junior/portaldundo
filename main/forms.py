from django import forms
 #	our	new	form 

class  ContactForm(forms.Form):
	contact_name = forms.CharField()
	contact_email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)

	#	the	new	bit	we're	adding
	def	__init__(self,	*args,	**kwargs):
		super(ContactForm,	self).__init__(*args,	**kwargs)
		self.fields['contact_name'].label =	""
		self.fields['contact_email'].label = ""
		self.fields['content'].label = ""
