from django.shortcuts import render
from django.http import HttpResponse
from Name_Fairy_APP.models import Name
import random

# Create your views here.
def index(request):
    return render(request, "index.html",)



def search(request):
    counter = random.randint(1,6)
    query_list = Name.objects.filter(nameId=counter)


    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            query_list = query_list.filter(gender__iexact=gender)

    if 'genre' in request.GET:
        genre = request.GET['genre']
        if genre:
            query_list = query_list.filter(genre__iexact=genre)

    context = {
        'items': query_list,
    }
    return render(request, "index.html", context)
