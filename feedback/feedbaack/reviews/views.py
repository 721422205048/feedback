from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
from .forms import ReviewsForm
from .models import Reviews
def review(request):

    if request.method=="POST":     #checking if post is used
        form=ReviewsForm(request.POST)  #checks if form has data
        if form.is_valid():             #form validaTION
            print(form.cleaned_data)       # used to print the form data in the terminal 
            review=Reviews(user_name=form.cleaned_data
            ['user_name'],
            review_text=form.cleaned_data['review_text'],
            rating=form.cleaned_data['rating'])
            review.save()                   #save in database
            return HttpResponseRedirect("/thankyou")   #redirect to thankyou.html
    else:
            form=ReviewsForm()
            return render(request,"review.html",{"form":form 
            })

def thankyou(request):
    return render(request,"thankyou.html",{"has_error":False
    })