import string
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Incorrect User or Password')
            return redirect('login')

    else:
        return render(request, 'login.html')


# Create your views here.
def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if first_name == "" or last_name == "" or username == "" or password1 == "" or password2 == "" or email == "":
            messages.info(request, 'Please Fill the empty form')

            return redirect('registration')

        elif len(first_name) < 4:
            messages.info(request, 'Length of the First Name must be greater than 3 character')
            return redirect('registration')
        elif len(first_name) > 20:
            messages.info(request, 'Length of the First Name must be Smaller than 20 character')
            return redirect('registration')
        elif len(last_name) < 4:
            messages.info(request, 'Length of the Last Name must be greater than 3 character')
            return redirect('registration')
        elif len(last_name) > 20:
            messages.info(request, 'Length of the Last Name must be Smaller than 20 character')
            return redirect('registration')
        elif len(username) < 4:
            messages.info(request, 'Length of the Username must be greater than 3 character')
            return redirect('registration')
        elif len(first_name) > 20:
            messages.info(request, 'Length of the Username must be Smaller than 20 character')
            return redirect('registration')
        elif first_name in string.digits:
            messages.info(request, 'Numbers and special Character is not allowed in First Name')
            return redirect('registration')
        elif last_name in string.digits:
            messages.info(request, 'Numbers and special Character is not allowed in Last Name')
            return redirect('registration')
        elif username in string.digits:
            messages.info(request, 'Numbers and special Character is not allowed in Username')
            return redirect('registration')
        elif len(password1) < 8:
            messages.info(request, 'Password must be greater or equal to 8')
            return redirect('registration')
        elif len(password1) > 50:
            messages.info(request, 'Password must be greater or equal to 8 and up to 50 ')
            return redirect('registration')
        elif not re.search('[!@#$%^&*()_+=-]', password1):
            messages.info(request, 'Password must contain at least 1 character and 1 special character')
            return redirect('registration')
        elif not re.search('[1234567890]', password1):
            messages.info(request, 'Password must contain at least 1 character and 1 special character')
            return redirect('registration')
        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name Taken')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('registration')
    else:
        return render(request, 'registration.html')
