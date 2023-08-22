from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm
# Create your views here.

#forms.py를 이용한 회원가입 로직
def signup(request):
    register_form = RegisterForm()
    context = {'forms':register_form}

    if request.method =='GET':
        return render(request, 'account/signup.html', context)
    
    elif request.method =='POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_email = register_form.user_email,
                user_phone = register_form.user_phone,
                user_gender = register_form.user_gender
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'account/signup.html', context)
    

#로그인 
def login(request):
    loginform = LoginForm()
    context ={'forms':loginform}

    if request.method =='GET':
        return render(request, 'account/login.html', context)
    
    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session']= loginform.login_session
            request.session.set_expiry(0)
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'account/login.html',context)
    
#로그아웃
def logout(request):
    request.session.flush()
    return redirect('/')