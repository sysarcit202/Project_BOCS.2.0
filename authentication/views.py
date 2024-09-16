from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from main import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializer import UserSerializer
# @api_view(['GET','POST'])

# Create your views here.
def home(request):
    context = {
        'title': 'Project_BOCS'
    }

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            name = user.name
            return render(request, 'dashboard/dashboard.html', {'name': name})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, 'authentication/login.html', context)

def signup(request):
    context = {
        'title': 'Project_BOCS | Signup'
    }

    if request.method == 'POST':
        empId = request.POST['UempId']
        fName = request.POST['Uname']
        email = request.POST['Uemail']
        jobRole = request.POST['UjRole']
        idNum = request.POST['UidNum']
        pass1 = request.POST['Upass']
        pass2 = request.POST['UrPass']

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")

        if not pass1.isalnum():
            messages.error(request, "Password must be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(empId, fName, pass1)
        myuser.name = fName
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account has been successfully created. Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome to Project | BOCS - Login!!"
        message = "Hello " + myuser.name + "!! \n" + "Welcome to BOCS!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nSystem Creator"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Project BOCS - Login!!"
        message2 = render_to_string('authentication/email_confirmation.html',{
            
            'name': myuser.name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('home')

    return render(request, 'authentication/signup.html', context)

def reset(request):
    context = {
        'title': 'Project_BOCS | Forgot Password'
    }
    return render(request, 'authentication/reset_email.html', context)

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Succesfully!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'authentication/activation_failed.html')
