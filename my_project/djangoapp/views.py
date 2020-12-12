from django.shortcuts import render,redirect
from django.http import HttpResponse
from djangoapp.models import user
from djangoapp.form import userForm

# Create your views here.
def index(request):
	return render(request,'index.html')
def avengers(request):
	return render(request,'avengers.html')
	
def avengers2(request):
	return render(request,'avengers2.html')
def avengers3(request):
	return render(request,'avengers3.html')
def avengers4(request):
	return render(request,'avengers4.html')
def batman1(request):
	return render(request,'batman1.html')
def batman2(request):
	return render(request,'batman2.html')
def batman3(request):
	return render(request,'batman3.html')
def joker(request):
	return render(request,'joker.html')
def blackwidow(request):
	return render(request,'black widow.html')
def morbius(request):
	return render(request,'morbius.html')
def wonderwoman(request):
	return render(request,'wonderwoman.html')
def birdsofprey(request):
	return render(request,'birdsofprey.html')
def movies(request):
	return render(request,'movies.html')
def manofsteel(request):
	return render(request,'manofsteel.html')
def spiderman(request):
	return render(request,'spiderman.html')
def book(request):
	if request.method=="POST":
		form=userForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/success")
	else:
		form=userForm()
		return render(request,"book.html",{'sform':form})

def about(request):
	return render(request,'aboutus.html')
def contact(request):
	return render(request,'contact.html')
def success(request):
	return render(request,'submit.html')