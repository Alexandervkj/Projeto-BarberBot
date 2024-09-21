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
