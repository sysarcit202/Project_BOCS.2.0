from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.db import transaction, IntegrityError
from django.conf import settings
from .tokens import generate_token
from .models import User
from django.shortcuts import render     

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

def home(request):
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

    return render(request, 'authentication/login.html')

def home(request):
    return render(request, 'authentication/login.html')

def signup(request):
    context = {'title': 'Signup'}

    if request.method == 'POST':
        uemp_id = request.POST.get('UempId', None)
        
        fName = request.POST['Uname']
        email = request.POST['Uemail']
        jobRole = request.POST['UjRole']
        idNum = request.POST['UidNum']
        pass1 = request.POST['Upass']
        pass2 = request.POST['UrPass']

        # Check if email is already registered
        if User.objects.filter(Uemail=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('home')

        # Check if password is alphanumeric
        if not pass1.isalnum():
            messages.error(request, "Password must be Alpha-Numeric!")
            return redirect('home')

        try:
            with transaction.atomic():
                myuser = User(
                    UempId=uemp_id,
                    Uname=fName,
                    Uemail=email,
                    UjRole=jobRole,
                    UidNum=idNum,
                    Upass=pass1,
                    UrPass=pass2,
                )
                myuser.save()

                # Welcome Email
                subject = "Welcome to Project | BOCS - Login!!"
                message = f"Hello {myuser.Uname}!! \nWelcome to BOCS!! \nThank you for visiting our website. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nSystem Creator"
                from_email = settings.EMAIL_HOST_USER
                to_list = [myuser.Uemail]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                
                # Email Address Confirmation Email
                current_site = get_current_site(request)
                email_subject = "Confirm your Email @ Project BOCS - Login!!"
                message2 = render_to_string('authentication/email_confirmation.html', {
                    'name': myuser.Uname,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                    'token': generate_token.make_token(myuser)
                })
                email = EmailMessage(
                    email_subject,
                    message2,
                    settings.EMAIL_HOST_USER,
                    [myuser.Uemail],
                )
                email.fail_silently = True
                email.send()

                messages.success(request, "Your account has been successfully created. Please check your email to confirm your email address in order to activate your account.")
        except IntegrityError:
            messages.error(request, "An error occurred while creating the account. Please try again.")
            return redirect('home')

        return redirect('home')

    return render(request, 'authentication/signup.html', context)

def insertuser(request):
    if request.method == 'POST':
        vUempId = request.POST.get('UempId')
        vUname = request.POST.get('Uname')
        vUemail = request.POST.get('Uemail')
        vUjRole = request.POST.get('UjRole')
        vUidNum = request.POST.get('UidNum')
        vUpass = request.POST.get('Upass')
        vUrPass = request.POST.get('UrPass')

        # Check if any required field is missing
        if not all([vUempId, vUname, vUemail, vUjRole, vUidNum, vUpass, vUrPass]):
            return redirect('home')

        try:
            with transaction.atomic():
                us = User(
                    UempId=vUempId,
                    Uname=vUname,
                    Uemail=vUemail,
                    UjRole=vUjRole,
                    UidNum=vUidNum,
                    Upass=vUpass,
                    UrPass=vUrPass,
                )
                us.save()
                messages.success(request, "User successfully inserted!")
        except IntegrityError:
            messages.error(request, "An error occurred while inserting the user. Please try again.")
            return redirect('home')

    return render(request, 'authentication/login.html', {})

def reset(request):
    context = {'title': 'Forgot Password'}
    return render(request, 'authentication/reset_email.html', context)

    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        try:
            with transaction.atomic():
                myuser.is_active = True
                myuser.save()
                login(request, myuser)
                messages.success(request, "Your Account has been activated!!")
        except IntegrityError:
            messages.error(request, "An error occurred while activating the account. Please try again.")
            return redirect('home')
        return redirect('signin')
    else:
        return render(request, 'authentication/activation_failed.html')