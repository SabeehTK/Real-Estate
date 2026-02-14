from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View
from accounts.forms import UserForm,LoginForm,ProfileForm
from django.contrib import messages

from accounts.forms import OtpLoginForm
from accounts.models import EmailOTP
from django.core.mail import send_mail


# Create your views here.
class Registerview(View):
    def get(self, request):
        user_form = UserForm()
        profile_form = ProfileForm()
        context = {'registerform': user_form, 'profileform': profile_form}
        return render(request,'register.html',context)
    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print(user)
            profile = user.profile
            profile.phone = profile_form.cleaned_data['phone']
            profile.address = profile_form.cleaned_data['address']
            profile.profile_picture = profile_form.cleaned_data['profile_picture']
            profile.save()
            print(profile)
            return redirect('accounts:login')

class Loginview(View):
    def get(self, request):
        form_instance = LoginForm()
        context = {'loginform': form_instance}
        return render(request,'login.html',context)
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data #fetches data after validation
            u=data['username']#retrieves username from cleaned data
            p=data['password']#retrieves username from cleaned data
            user=authenticate(username=u,password=p)#calls authenticate to verify if user exists
                                                    #if user exists then it returns to the user object
                                                    #else none
            if user:#if user exists
                login(request,user)  #add the user into current session
                return redirect('index')
            else: #if not exists
                messages.error(request, "Invalid Username or Password!")
                return redirect('accounts:login')

class LoginViaOtp(View):
    def get(self, request):
        form_instance = OtpLoginForm()
        context = {'otpform': form_instance}
        return render(request,'loginviaotp.html',context)
    def post(self, request):
        form_instance = OtpLoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.generate_otp()
            send_mail(
                subject="Landonhand-OTP",
                message=f"Dear {u.user.username},\n\n"
                        f"Your OTP for LandOnHand Login is {u.code}.\n\n\n"
                        f"Do Not share the OTP with anyone including Landonhand personal.",
                from_email=None,
                recipient_list=[u.user.email],
                fail_silently=False,
            )
            u.save()
            return redirect('accounts:otpverification')

class OtpVerificationView(View):
    def get(self, request):
        return render(request,'otpverification.html')
    def post(self, request):
        o = request.POST['o']  # retrieve the otp send by the user
        try:
            u = EmailOTP.objects.get(code=o)  # check whether record matching with the entered otp exists
        except EmailOTP.DoesNotExist:
            messages.error(request, "Invalid or expired OTP!")
            return redirect('accounts:otpverification')
        #checks expiry of otp:
        if not u.is_valid():
            u.delete()  # remove expired OTP
            messages.error(request, "OTP has expired. Please request a new one.")
            return redirect('accounts:loginviaotp')

        # if exists then:
        # u.code = None  # clear the otp from table
        user=u.user
        u.delete() #clear the entire emailotp field
        login(request,user)  # add the user into current session
        return redirect('index')



class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')