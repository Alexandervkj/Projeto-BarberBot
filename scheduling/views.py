from django.shortcuts import render
from .models import BarberShop, Appointment

def appointment_view(request):
    barber_shops = BarberShop.objects.all()

    if request.method == 'POST':
        client_name = request.POST['client_name']
        date = request.POST['date']
        time = request.POST['time']
        barber_shop = BarberShop.objects.get(id=request.POST['barber_shop'])

        # Criar agendamento
        appointment = Appointment.objects.create(
            client_name=client_name,
            date=date,
            time=time,
            barber_shop=barber_shop
        )

        return render(request, 'success.html', {'appointment': appointment})

    return render(request, 'appointment_form.html', {'barber_shops': barber_shops})

SERVICOS = ['Corte de cabelo', 'Barba', 'Corte e barba']
PROFISSIONAIS = ['João', 'Maria', 'Pedro']

def chatbot_view(request):
    if request.method == 'POST':
        # Lógica do chatbot
        if 'nome' not in request.POST:
            return render(request, 'chatbot.html', {'message': 'Qual é o seu nome?'})
        
        nome = request.POST['nome']
        
        if 'servico' not in request.POST:
            return render(request, 'chatbot.html', {
                'message': f'Olá, {nome}! Qual serviço você deseja?',
                'servicos': SERVICOS
            })
        
        servico = request.POST['servico']
        
        if 'profissional' not in request.POST:
            return render(request, 'chatbot.html', {
                'message': f'Você escolheu {servico}. Quem você gostaria que fizesse o serviço?',
                'profissionais': PROFISSIONAIS
            })
        
        profissional = request.POST['profissional']
        
        if 'data' not in request.POST:
            return render(request, 'chatbot.html', {
                'message': f'O profissional escolhido foi {profissional}. Qual a data desejada?',
            })
        
        data = request.POST['data']
        
        if 'telefone' not in request.POST:
            return render(request, 'chatbot.html', {
                'message': f'A data escolhida é {data}. Qual seu número de telefone?',
            })
        
        telefone = request.POST['telefone']
        
        if 'confirmacao' not in request.POST:
            return render(request, 'chatbot.html', {
                'message': f'Você deseja agendar {servico} com {profissional} no dia {data} e seu telefone é {telefone}? (sim/não)',
            })
        
        # Aqui você pode salvar o agendamento ou fazer o que precisar
        confirmacao = request.POST['confirmacao']
        if confirmacao.lower() == 'sim':
            return render(request, 'chatbot.html', {'message': 'Agendamento confirmado!'})
        else:
            return render(request, 'chatbot.html', {'message': 'Agendamento cancelado.'})

    return render(request, 'chatbot.html', {'message': 'Qual é o seu nome?'})