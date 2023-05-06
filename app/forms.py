from django import forms
from app.models import *
class Topicforms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class Webpageforms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','email']
        
class Accessrecordforms(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields=['author','date']
