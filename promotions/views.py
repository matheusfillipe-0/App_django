 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

promotions = [
   {
        'id': 1,
        'title': 'Mono',
        'description': 'Figurinhas exclusivas em preto e branco, com design minimalista que transmite simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/lovu',
        'preco' : '250.00'
    },
    {
        'id': 2,
        'title': 'Noir',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/x347',
        'preco' : '220.00'
    },
    {
        'id': 3,
        'title': 'Éden',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/4ak',
        'preco' : '240.00'
    }, 
    {
        'id': 4,
        'title': 'Sombra',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/8uk8',
        'preco' : '299.99'
    },
    {
        'id': 5,
        'title': 'Zen',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/c05',
        'preco' : '199.99'
    },
    {
        'id': 6,
        'title': 'Minimal',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/v21q',
        'preco' : '170.00'
        
    }
    
]
  
users = [
    {'username': 'user1', 'password': 'senha1'},
    {'username': 'user2', 'password': 'senha2'},
    {'username': 'user3', 'password': 'senha3'},
]


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)

        if user:
            return redirect('/')  
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'promotions/login.html')



def detail_promotion(request, promotion_id):
    context = {
        'promotion': promotions[int(promotion_id) - 1],
        'promotion_id' : promotion_id
    }

    return render(request, 'promotions/detalhe.html',
                   context)
 