from django import forms


# Login page
class LoginForm(forms.Form):
    email = forms.EmailField(label='E-Mail')
    password = forms.CharField(widget=forms.PasswordInput())


# Chatbot page
class ChatBotForm(forms.Form):
    messageLog = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'true', 'style': 'resize:none'}),
                                 required=False,
                                 label='Chat History')
    message = forms.CharField()
