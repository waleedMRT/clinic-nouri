from django.shortcuts import render , redirect
import urllib.parse


def home(request):
    return render(request , 'core/home.html')


def about(request):
    return render(request , 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        text = f"""
            رسالة جديدة من الموقع:
            الاسم: {name}
            الإيميل: {email}
            الرسالة: {message}
        """

        encoded_text = urllib.parse.quote(text)
        whatsapp_number = "213558184717"
        url = f"https://wa.me/{whatsapp_number}?text={encoded_text}"
        return redirect(url)

    return render(request , 'core/contact.html')

# Create your views here.
