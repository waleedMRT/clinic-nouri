from django.shortcuts import render , redirect
from apointement.models import Apointement
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.utils import timezone

@login_required
def dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden('غير مسموح')

    today = timezone.now().date()
    tab = request.GET.get('tab' , 'all')
    
    total_appointements = Apointement.objects.all().order_by('-date')
    today_appointements = Apointement.objects.filter(date=today).order_by('created_at')

    

    if tab == 'today':
        appointements = today_appointements
    else:
        appointements = total_appointements    
    
    # filtering
    selected_date = request.GET.get('date')
    if selected_date:
        appointements = appointements.filter(date=selected_date)

    

    # pagination
    paginator = Paginator(appointements, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "total_appointements_count": total_appointements.count(),
        "today_appointements_count" : today_appointements.count(),
        "selected_date": selected_date,
        "tab" : tab
    }

    return render(request, 'dashboard/dashboard.html', context)


# Create your views here.
