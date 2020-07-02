from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your name"}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your email", "type":"email"}))
    phone_number = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your phone number"}))
    subject = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Subject"}))
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={"placeholder": "Your message"})
    )

    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'phone_number',
            'subject',
            'message'
        ]
