from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from django.core import serializers
from django.http.response import JsonResponse


from .forms import AddForm
from .models import Todo, Person

def person(request):
    if request.method == "POST":
        # f = AddForm()
        p = Person.objects.create(idPerson = request.POST.get("id"))
        return HttpResponse("<h2>add User , id = {0}</h2>".format(request.POST.get("id")))
        
    if request.method == "GET":
        return render(request,"person.html",{"people":Person.objects.all()})

def todo(request):
    if request.method == "POST":
        t = Todo.objects.create(text = request.POST.get("text"),person_id = request.POST.get("person_id"),ittodo = request.POST.get("ittodo"))
        return HttpResponse("<h2>Add todo,\n{0}\nidperson_id = {1}</h2>".format(request.POST.get("text"),request.POST.get("person_id")))
    if request.method == "GET":
        return render(request,"todo.html",{"todos":Todo.objects.all()})

def tododel(request, person_id, idtodo):
    if request.method == "DELETE":
        t = Todo.objects.filter(person_id = person_id,ittodo = idtodo)
        t.delete()
        return HttpResponse("Deleted")

def todoperson(request,id ):
    if request.method == "GET":
        #return render(request,"todo.html",{"todos":Todo.objects.filter(person_id=id)})
        #data1 = serializers.serialize('json',{'data':Todo.objects.filter(person_id=id)})
        return HttpResponse(Todo.objects.filter(person_id=id).values("person_id","ittodo","text"))
    else:
        return("Bad method")
