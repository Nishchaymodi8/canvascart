from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.hashers import check_password
import re
from   .models import UserProfile
from django.contrib.auth.hashers import make_password

# Create your views here.
def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        errors = {}

        # 🔹 EMAIL VALIDATION
        if not email:
            errors['email'] = "Email is required"
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            errors['email'] = "Invalid email format"
        elif UserProfile.objects.filter(email=email).exists():
            errors['email'] = "Email already exists"

        # 🔹 PASSWORD VALIDATION
        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif not re.search(r'[A-Z]', password):
            errors['password'] = "Must contain uppercase letter"
        elif not re.search(r'[a-z]', password):
            errors['password'] = "Must contain lowercase letter"
        elif not re.search(r'[0-9]', password):
            errors['password'] = "Must contain a number"
        elif not re.search(r'[!@#$%^&*]', password):
            errors['password'] = "Must contain special character"

        # 🔹 IF ERROR → SHOW AGAIN
        if errors:
            return render(request, 'signup.html', {'errors': errors})

        # Save to DB
        user = UserProfile(
            full_name=full_name,
            email=email,
            password=make_password(password)
        )
        user.save()

        return redirect('/login/')  # after signup

    return render(request, 'signup.html')


def show_home(request):
    user_name = request.session.get('user_name')  # optional

    return render(request, 'home.html', {
        'user_name': user_name
    })
   
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("Entered Email:", email)
        print("Entered Password:", password)

        try:
            user = UserProfile.objects.get(email=email)
            print("User found in DB:", user.email)
            print("Stored Password:", user.password)
        except UserProfile.DoesNotExist:
            print("User NOT found")
            return render(request, 'login.html', {'error': 'Invalid email'})

        result = check_password(password, user.password)
        print("Password Match:", result)

        if result:
            request.session['user_id'] = user.pk
            request.session['user_name'] = user.full_name
            print("LOGIN SUCCESS")

            return redirect('home')
        else:
            print("LOGIN FAILED")
            return render(request, 'login.html', {'error': 'Invalid password'})

    return render(request, 'login.html')

def logout_view(request):
    request.session.pop('user_id', None)
    request.session.pop('user_name', None)

    return redirect('home')