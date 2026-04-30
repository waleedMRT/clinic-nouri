from django.shortcuts import render , redirect
from .models import Apointement
from django.contrib import messages

from datetime import date


def add_apointement(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        date_selected = request.POST.get('date')

        if date_selected < str(date.today()):
            messages.error(request , 'لا يمكنك الحجز في الماضي')
            return redirect('add_apointement')
        
        count = Apointement.objects.filter(date=date_selected).count()

        if count >= 30:
            messages.error(request , 'تم الوصول للحد الأقصى لهذا اليوم , جرب يوم آخر')
            return redirect('add_apointement')
        
        exists = Apointement.objects.filter(phone=phone , date=date_selected).exists()
        if exists:
            messages.error(request , 'هذا الرقم لديه حجز مسبق في هذا اليوم')
            return redirect('add_apointement')
        

        Apointement.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            age=age,
            date=date_selected
        )
        messages.success(request , 'تم الحجز بنجاح')
        return redirect('add_apointement')
    
    return render(request , 'apointement/apointement.html')

            
# Create your views here.
