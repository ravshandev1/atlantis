from django.shortcuts import render, redirect
from django.conf import settings
from requests import post
from pytz import timezone
from .models import About, Application, BotMessage, Contact, Partner, Carousel, OurSolve, Step
from django.contrib import messages


def index(request):
    about = About.objects.first()
    contact = Contact.objects.first()
    carousels = Carousel.objects.all()
    partners = Partner.objects.all()
    our_solves = OurSolve.objects.all()
    steps = Step.objects.all()
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        obj = Application.objects.create(name=name, email=email, phone=phone, message=message)
        text = f"Ism: {obj.name}\n"
        text += f"Telefon: {obj.phone}\n"
        text += f"Email: {obj.email}\n"
        text += f"Javob berildi: ❌\n"
        text += f"Habar: {obj.message}\n"
        text += f"Yuborilgan vaqt: {obj.created_at.astimezone(tz=timezone('Asia/Tashkent')).strftime('%d.%m.%Y %H:%M')}"
        payload = {
            "chat_id": settings.GROUP_ID,
            "text": text,
            "parse_mode": "HTML"
        }
        res = post(f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage", json=payload)
        BotMessage.objects.create(application_id=obj.id, message_id=res.json()['result']['message_id'])
        messages.success(request, "Success")
        return redirect('.')
    return render(request, 'index.html',
                  {'steps': steps, 'our_solves': our_solves, 'contact': contact, 'partners': partners,
                   'carousels': carousels, 'about': about})