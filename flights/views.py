from django.shortcuts import render
from .models import Flight, Passengers
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })

def flight(request, flight_id):
    try: 
        flight = Flight.objects.get(pk = flight_id)
    except Flight.DoesNotExist:
        return HttpResponse("Flight not found", status = 404)

    non_passengers = Passengers.objects.exclude(flights=flight).all()
    return render(request, "flights/flights.html",{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": non_passengers
    })

def book(request, flight_id):

    # For a post request, add a new flight
    if request.method == "POST":

        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passengers.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))