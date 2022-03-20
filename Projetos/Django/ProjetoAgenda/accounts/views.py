from email import message
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)
    if not user:
        messages.error(request, "User or password is incorrect")
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, "Logado com sucesso.")
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Invalid')
        return render(request, 'accounts/register.html')

    if password != password2:
        messages.error(request, 'Senhas são diferentes.')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'Senha precisa ter 6 ou mais caracteres.')
        return render(request, 'accounts/register.html')

    if len(username) < 6:
        messages.error(request, 'Usuário precisa ter 6 ou mais caracteres.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/register.html')

    if not name or not lastname or not email or not username or not password or not password2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/register.html')

    user = User.objects.create_user(
        username=username, email=email, password=password, first_name=name, last_name=lastname)
    user.save()
    messages.success(request, 'Registro com sucesso')
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, "Erro ao enviar o formulário")
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(
        request, f"{request.POST.get('nome')}, contato salvo com sucesso")
    return redirect('dashboard')
