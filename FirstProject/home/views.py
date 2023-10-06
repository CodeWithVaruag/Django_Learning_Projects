from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers

from home.models import Contact
# Create your views here.
def home(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")
    
def about(request):
    return render(request,'about.html') 

def services(request):
    return render(request,'services.html') 
 

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Contact saved successfully")

    return render(request,'contact.html')  

def api(request):
    # Query all contacts
    contacts = Contact.objects.all()

    # Serialize the queryset to JSON
    data = serializers.serialize('json', contacts)

    # Create a JsonResponse and return it
    return JsonResponse({'contacts': data}, safe=False)
    
              
    