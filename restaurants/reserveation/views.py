from django.shortcuts import render
from .forms import reservationForm

# Create your views here.

def reserve(request):
    reservation_form = reservationForm()
    if request.method == "POST" :
        print("here 1")
        reservation_form = reservationForm(request.POST)
        if reservation_form.is_valid():
            print("here 2")
            context1 = {"name":reservation_form.cleaned_data['name']}
            reservation_form.save()
            return render(request, "reservation/success.html", context1)
    else:
        reservation_form = reservationForm()
                
    context = {
        "form":reservation_form, 
    }
    
    
    return render(request, "reservation/reservation.html", context)