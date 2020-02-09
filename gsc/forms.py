class websiteForm(forms.Form):
    web_name = forms.CharField(max_length=80)
    website_url = forms.TextField()
