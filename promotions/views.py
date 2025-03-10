from django.shortcuts import render


promotions = [
   {
        'id': 1,
        'title': 'Figurinha 1',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/lovu'
    },
    {
        'id': 2,
        'title': 'Figurinha 2',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/x347'
    },
    {
        'id': 3,
        'title': 'Figurinha 3',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/4ak'
    }, 
    {
        'id': 4,
        'title': 'Figurinha 4',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/lovu'
    },
    {
        'id': 5,
        'title': 'Figurinha 5',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/x347'
    },
    {
        'id': 6,
        'title': 'Figurinha 6',
        'description': 'Uma ilustração minimalista em preto e branco, capturando a essência de simplicidade e elegância.',
        'imagem_url': 'https://www.pic.surf/4ak'
    },
    
]

def detail_promotion(request, promotion_id):
    context = {
        'promotion': promotions[int(promotion_id) - 1],
        'promotion_id' : promotion_id
    }

    return render(request, 'promotions/detalhe.html',
                   context)
