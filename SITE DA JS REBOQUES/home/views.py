from django.http import Http404
from django.shortcuts import render
from urllib.parse import quote_plus

PRODUCTS = [
    {
        'slug': 'reboque-padrao',
        'title': 'Reboque padrão',
        'category': 'Reboque Padrão',
        'image': 'catalogo/padrão-1Eixo.jpeg',
        'trucado_image': 'catalogo/padrão-Trucado.jpeg',
        'short_description': 'Escolha o tamanho ideal para o seu transporte, com acessórios disponíveis para deixar o reboque completo.',
        'details': ['Estrutura em aço com pintura resistente', 'Projeto homologado para uso em estrada', 'Disponível em vários tamanhos para sua necessidade'],
        'sizes': [
            {'label': 'C 1,50m x L 1,20m x A 0,50m', 'price': 'R$ 6.990'},
            {'label': 'C 1,80m x L 1,20m x A 0,50m', 'price': 'R$ 7.399'},
            {'label': 'C 2,00m x L 1,20m x A 0,50m', 'price': 'R$ 7.599'},
            {'label': 'C 2,00m x L 1,30m x A 0,50m', 'price': 'R$ 8.490'},
            {'label': 'C 2,00m x L 1,30m x A 1,00m', 'price': 'R$ 8.490'},
            {'label': 'C 2,00m x L 1,40m x A 0,50m', 'price': 'R$ 9.290'},
            {'label': 'C 2,00m x L 1,40m x A 1,00m', 'price': 'R$ 10.119'},
            {'label': 'C 2,00m x L 1,50m x A 0,50m', 'price': 'R$ 10.890'},
            {'label': 'C 2,00m x L 1,50m x A 1,00m', 'price': 'R$ 10.890'},
        ],
    },
    {
        'slug': 'reb-jetski-berco-madeira',
        'title': 'Reboque Jetski berço madeira',
        'category': 'Reboque Especial',
        'price': 'R$ 9.490',
        'image': 'catalogo/jestki-Roldanas.jpeg',
        'short_description': 'Berço em madeira para transportar seu jetski com segurança.',
        'details': ['Berço em madeira reforçada', 'Fixação segura para jetski', 'Acabamento resistente a intempéries'],
    },
    {
        'slug': 'reb-jetski-berco-roldanas',
        'title': 'Reboque Jetski berço roldanas',
        'category': 'Reboque Especial',
        'price': 'R$ 9.990',
        'image': 'catalogo/jestki-Roldanas.jpeg',
        'short_description': 'Versão com roldanas para facilitar o carregamento do jetski.',
        'details': ['Rolamentos resistentes', 'Entrada mais rápida para o jetski', 'Piso reforçado e acabamento durável'],
    },
    {
        'slug': 'reb-quadri-jet-berco-madeira',
        'title': 'Reboque Quadri-jet berço em madeira',
        'category': 'Reboque Especial',
        'price': 'R$ 9.990',
        'image': 'catalogo/quadri-Jet-Madeira.jpeg',
        'short_description': 'Berço em madeira para quadri-jets, resistente e prático.',
        'details': ['Berço de madeira para quadri-jets', 'Suporte anti-vibração', 'Acabamento pensado para manuseio fácil'],
    },
    {
        'slug': 'reb-quadri-jet-berco-roldanas',
        'title': 'Reboque Quadri-jet berço roldanas',
        'category': 'Reboque Especial',
        'price': 'R$ 10.490',
        'image': 'catalogo/quadri-Jet-Roldanas.jpeg',
        'short_description': 'Roldanas que facilitam a subida e descida do quadri-jet.',
        'details': ['Roldanas resistentes ao peso', 'Carregamento mais suave', 'Piso reforçado e acabamento premium'],
    },
    {
        'slug': 'reb-quadriciclo-piso-madeira',
        'title': 'Reboque Quadriciclo piso em madeira',
        'category': 'Reboque Especial',
        'price': 'R$ 8.490',
        'image': 'catalogo/quadriciclo-Entrada.jpeg',
        'short_description': 'Piso em madeira para transporte seguro de quadriciclos.',
        'details': ['Piso em madeira reforçada', 'Fixação de segurança para quadriciclo', 'Perfil resistente para uso contínuo'],
    },
    {
        'slug': 'reb-quadriciclo-piso-chapa-14-s-bau',
        'title': 'Reboque Quadriciclo piso em chapa 14 (S/ baú)',
        'category': 'Reboque Especial',
        'price': 'R$ 9.490',
        'image': 'catalogo/quadriciclo-Chapa.jpeg',
        'short_description': 'Piso em chapa para quadriciclo, sem baú, resistente e eficiente.',
        'details': ['Piso em chapa 14', 'Sem baú para carga limpa', 'Ideal para quadriciclos pesados'],
    },
    {
        'slug': 'reb-quadriciclo-piso-chapa-14-c-bau',
        'title': 'Reboque Quadriciclo piso em chapa 14 (C/ baú)',
        'category': 'Reboque Especial',
        'price': 'R$ 10.290',
        'image': 'catalogo/quadriciclo-Chapa.jpeg',
        'short_description': 'Piso em chapa 14 com baú para transporte protegido.',
        'details': ['Piso em chapa 14', 'Baú integrado para proteção extra', 'Construção robusta para uso intenso'],
    },
    {
        'slug': 'reb-quadri-moto-piso-chapa-14-c-bau',
        'title': 'Reboque Quadri-Moto piso em chapa 14 (C/ baú)',
        'category': 'Reboque Especial',
        'price': 'R$ 11.090',
        'image': 'catalogo/quadri-Moto.jpeg',
        'short_description': 'Piso em chapa 14 com baú, ideal para motos e quadriciclos.',
        'details': ['Piso em chapa 14', 'Baú incluso para transporte seguro', 'Equipamento robusto para estrada'],
    },
    {
        'slug': 'reb-quadri-cargo-piso-bloco-naval-s-bau',
        'title': 'Reboque Quadri-Cargo piso em bloco naval (S/ baú)',
        'category': 'Reboque Especial',
        'price': 'R$ 9.990',
        'image': 'catalogo/quadri-Cargo.jpeg',
        'short_description': 'Piso de bloco naval para cargas resistentes, sem baú.',
        'details': ['Piso em bloco naval', 'Sem baú para flexibilidade de carga', 'Boa resistência à água e impacto'],
    },
    {
        'slug': 'reb-para-03-motos-s-bau',
        'title': 'Reboque para 03 motos (S/ baú)',
        'category': 'Reboque Especial',
        'price': 'R$ 9.490',
        'image': 'catalogo/reb-3Motos.jpeg',
        'short_description': 'Capacidade para até 3 motos com segurança e estabilidade.',
        'details': ['Espaço para 3 motos', 'Sem baú para carregamento rápido', 'Suporte reforçado para transporte seguro'],
    },
    {
        'slug': 'reb-transp-fibra-otica',
        'title': 'Reboque Transporte Bobinas de Fibra Ótica',
        'category': 'Reboque Especial',
        'price': 'R$ 9.990',
        'image': 'catalogo/transp-Fibra-Ótica.jpeg',
        'short_description': 'Especial para transporte de bobinas de fibra ótica com cuidado.',
        'details': ['Suporte específico para bobinas', 'Transporte seguro e firme', 'Estrutura reforçada para cargas delicadas'],
    },
    {
        'slug': 'reb-utv-motors-02-eixos',
        'title': 'Reboque UTV/MOTORS 02 eixos C 3,30m x L 2,00m',
        'category': 'Reboque Especial',
        'price': 'R$ 16.990',
        'image': 'catalogo/UTV-MOTORS.jpeg',
        'short_description': 'Reboque UTV com 2 eixos para carga mais pesada e estável.',
        'details': ['Dimensões: C 3,30m x L 2,00m', '2 eixos para maior estabilidade', 'Ideal para UTVs e cargas pesadas'],
    },
    {
        'slug': 'reb-utv-motors-04-eixos',
        'title': 'Reboque UTV/MOTORS 04 eixos C 4,50m x L 2,00m',
        'category': 'Reboque Especial',
        'price': 'R$ 19.490',
        'image': 'catalogo/UTV-MOTORS.jpeg',
        'short_description': 'Configuração 4 eixos para máximo suporte e segurança.',
        'details': ['Dimensões: C 4,50m x L 2,00m', '4 eixos para carga máxima', 'Construção robusta para uso ininterrupto'],
    },
    {
        'slug': 'reb-carga-viva-2-cavalos',
        'title': 'Reboque Carga viva para 02 cavalos',
        'category': 'Reboque Especial',
        'price': 'R$ 17.490',
        'image': 'catalogo/carga-Viva-2Cavalos.jpeg',
        'short_description': 'Projetado para transporte vivo de até 2 cavalos com segurança.',
        'details': ['Dimensões: C 2,30m x L 1,50m x A 1,50m', 'Estrutura segura para animais', 'Ventilação adequada e acabamento reforçado'],
    },
]

ACCESSORIES = [
    {'name': 'Estepe aro 13', 'price': 'R$ 499', 'description': 'Roda sobressalente para uso emergencial.'},
    {'name': 'Estepe aro 14', 'price': 'R$ 849', 'description': 'Roda sobressalente para rodas aro 14.'},
    {'name': 'Baú pequeno', 'price': 'R$ 800', 'description': 'Baú compacto para guardar ferramentas e itens leves.'},
    {'name': 'Baú médio', 'price': 'R$ 1.500', 'description': 'Baú de tamanho médio com boa capacidade de carga.'},
    {'name': 'Baú grande', 'price': 'R$ 1.500', 'description': 'Baú espaçoso para itens maiores e transporte seguro.'},
    {'name': 'Descanso lateral simples', 'price': 'R$ 390', 'description': 'Apoio lateral simples para reboques.'},
    {'name': 'Eixo adicional', 'price': 'R$ 3.200', 'description': 'Melhora a capacidade de carga e estabilidade do reboque.'},
    {'name': 'Teto de aço 2,00x1,20', 'price': 'R$ 1.400', 'description': 'Cobertura de aço resistente para proteção adicional.'},
    {'name': 'Capota marítima 2,00x1,20', 'price': 'R$ 950', 'description': 'Proteção resistente à água para cargas expostas.'},
    {'name': 'Teto + lona para reboque', 'price': 'R$ 4.790', 'description': 'Teto com lona para cobrir e proteger a carga.'},
    {'name': 'Sistema de freio inercial', 'price': 'R$ 4.290', 'description': 'Freio inercial para maior segurança em descidas.'},
]


def home(request):
    return render(request, 'home/home.html', {
        'all_products': PRODUCTS,
    })


def product_detail(request, slug):
    product = next((p for p in PRODUCTS if p['slug'] == slug), None)
    if not product:
        raise Http404('Produto não encontrado')
    contact_text = f"Olá, tenho interesse no produto {product['title']}."
    contact_url = f"https://wa.me/558199460014?text={quote_plus(contact_text)}"
    return render(request, 'home/product_detail.html', {
        'product': product,
        'contact_url': contact_url,
        'accessories': ACCESSORIES,
    })
