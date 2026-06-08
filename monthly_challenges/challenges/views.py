from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes a day!',
    'march': 'Learn Django for at least 20 minutes a day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes a day!',
    'june': 'Learn Django for at least 20 minutes a day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes a day!',
    'september': 'Learn Django for at least 20 minutes a day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Walk for at least 20 minutes a day!',
    'december': None,
}
# Create your views here.

def monthly_challenges_home_page(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     # iterate over the keys to create the list items
    #     list_items += f'<li><a href="{reverse("month-challenge", args=[month])}">{month.capitalize()}</a></li>'

    # response_data = f"""
    #     <ul>
    #         {list_items}
    #     </ul>
    # """
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {"months": months})

# function accepts a request
def january(request):
    # function will return a response
    # as an argument to the HttpResponse, we can pass response data
    return HttpResponse("This is the request for January!")

def february(request):
    return HttpResponse("This is the request for February!")

def monthly_challenge_by_number(request, month):
    # will return a list of keys, first key in the dictionary will be first item in list
    months = list(monthly_challenges.keys())
    # check to see if month is a valid index
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    # forward the user to the specific month that was selected
    redirect_month = months[month - 1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    # want to redirect, not send a response
    return HttpResponseRedirect(redirect_url)

# dynamically decides which response to send without hardcoding 
def monthly_challenge(request, month):
    try:
        # access using key in monthly challenges dictionary
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month": month})
    except:
        # return HttpResponseNotFound('<h1>This month is not supported.</h1>')
        raise Http404()

