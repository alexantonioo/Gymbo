from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_client:
                return redirect('client_dashboard')
            elif user.is_trainer:
                return redirect('trainer_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

@login_required
@user_passes_test(lambda u: u.is_client)
def client_dashboard(request):
    return render(request, 'client_view/client_layout.html')

@login_required
@user_passes_test(lambda u: u.is_trainer)
def trainer_dashboard(request):
    return render(request, 'trainer_view/trainer_view.html')


def home_view(request):
    return redirect('login')
