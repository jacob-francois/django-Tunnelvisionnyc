from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def portraits(request):
    return render(request,'app/portraits.html')

def contact(request):
    return render(request,'app/contact.html')
