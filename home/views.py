from django.shortcuts import render


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


def home_view(request):
    context = {
        'promotions': promotions
    }
    return render(request, 'home/home.html', context)


