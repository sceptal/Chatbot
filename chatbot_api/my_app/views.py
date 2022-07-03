from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import boto3
from .forms import ChatBotForm, LoginForm


# Create your views here.

# View for the login page
def home_page(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            user_password = form.cleaned_data['password']

            # Check email and password, currently non-functional
            if user_email is not None and user_password is not None:
                return redirect('/chat_bot')

    template = loader.get_template('main.html')
    context = {'form': form}

    return HttpResponse(template.render(context, request))

# View for the chatbot page
def chat_bot_view(request):
    form = ChatBotForm()

    if request.method == 'POST':
        form = ChatBotForm(request.POST)
        form_initial = {'messageLog': [], 'message': ''}
        if form.is_valid():
            # Add the received message and chat bot reply to the log
            if form.cleaned_data['messageLog'] != '':
                form_initial['messageLog'] = form.cleaned_data['messageLog'].split('\n')
            form_initial['messageLog'].append(form.cleaned_data['message'])
            form_initial['messageLog'].append(send_message(form.cleaned_data['message']))

        form_initial['messageLog'] = '\n'.join(form_initial['messageLog'])
        form = ChatBotForm(initial=form_initial)

    template = loader.get_template('chat_bot.html')
    context = {'form': form}

    return HttpResponse(template.render(context, request))


# Return a reply from the chatbot, currently non-functional
def send_message(user_message):
    bot_reply = 'chat bot reply to: ' + user_message

    return bot_reply
