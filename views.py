from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Company
from .forms import NewForm
# Create your views here.
def home(request):
	orglist=Company.objects.all()
	return render(request,'MyApp/home.html',{ 'orglist':orglist })

def org_create(request):
	form = NewForm(request.POST or None ,request.FILES or None )
	if form.is_valid():
		instance= form.save()
		instance.save()
		return HttpResponseRedirect('/')
	context={'form': form}
	return  render (request,"MyApp/create.html", context)
def org_retrive(request,id=None):
	instance = get_object_or_404(Company,id=id)
	context ={'instance' : instance}
	return  render (request,"MyApp/retrive.html",context)
def org_update(request,id=None):
	instance = get_object_or_404(Company,id=id)
	form = NewForm(request.POST or None,request.FILES or None ,instance=instance)
	if form.is_valid():
		instance = form.save()
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context ={'instance':instance,'form':form}
	return  render (request,"MyApp/update.html" , context)
def org_delete(request,id=None):
	instance =get_object_or_404(Company,id=id)
	instance.delete()
	return render(request,"MyApp/delete.html")