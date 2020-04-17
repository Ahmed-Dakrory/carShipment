from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import cars
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect



# Create your views here.

def UserData(request):
    test_var = "hi, this is a variable from context processor"
    return {
        "var_for_template" : test_var,
          }

def logout_req(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])

def authUser(request):
    
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Ya welcome")
        else:
            # Return an 'invalid login' error message.
            print("invalid")
    except:
        pass
    
    return redirect(request.META['HTTP_REFERER'])

def answer_me(request):
    user = request.user
    print('The Current User is : '+user.username)
    field = request.GET.get('inputValue')
    u = None
    try:
        u = User.objects.get(username=field)
    except:
        pass
    answer = None
    if u == None:
        user = User.objects.create_user(field, field+'@gmail.com', 'password')
        user.save()
        answer = 'Your record '+field+' has been done'
    else:
        answer = 'Hi,'+field+' you are alreay exist'
    
    data = {
        'respond': answer
            }
    return JsonResponse(data)

def print_from_button(request,username):

    
    print('Button clicked')
    print(username)
        
    all_cars = cars.objects.all()

    context = {
        'allCars':all_cars
    }
    return render(request,'all_cars.html',context)

def getCarsView(request):
    all_cars = cars.objects.all()

    context = {
        'allCars':all_cars
    }
    return render(request,'all_cars.html',context)