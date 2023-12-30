from django.forms import ModelForm
from main.models import Contact, Comment

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']