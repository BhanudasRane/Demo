from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    # dest1 = Destination()
    # dest1.name= 'Mumbai'
    # dest1.img ="destination_1.jpg"
    # dest1.desc='Mumbai is great'
    # dest1.price = 7000
    # dest1.offer = False
    
    # dest2 =Destination()
    # dest2.name = 'Pune'
    # dest2.img ="destination_2.jpg"
    # dest2.desc = 'The birth place of Chatrapati Shivaji maharaj'
    # dest2.price = 7001
    # dest2.offer = True

    # dest3 =Destination()
    # dest3.name = 'Nashik'
    # dest3.desc = 'The Most Beautiful smart city'
    # dest3.img ="destination_3.jpg"
    # dest3.price = 7002
    # dest3.offer = False
    
    # dests =[dest1,dest2,dest3]
    dests = Destination.objects.all()
    return render(request,"index.html",{'dests':dests})