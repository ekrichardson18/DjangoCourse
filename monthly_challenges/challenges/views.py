from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# function accepts a request
def january(request):
    # function will return a response
    # as an argument to the HttpResponse, we can pass response data
    return HttpResponse("This is the request for January!")

def february(request):
    return HttpResponse("This is the request for February!")

# dynamically decides which response to send without hardcoding 
def monthly_challenge(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = 'Eat no meat for the entire month!'
    elif month == 'february':
        challenge_text = 'Walk for 20 minutes every day!'
    elif month == 'march': 
        challenge_text = 'Learn Django for at least 20 minutes a day!'
    else:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(challenge_text)