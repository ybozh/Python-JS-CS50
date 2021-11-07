from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

# def flight(request, flight_id):
#     flight = Flight.objects.get(id=flight_id)
#     passengers = flight.passengers.all()
#     return render(request, "flights/flight.html", {
#         "flight": flight,
#         "passengers": passengers
#     })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })

def book(request, flight_id):

    # Якщо запит post - додаємо новий рейс
    if request.method == "POST":

        # Отримуємо доступ до рейсів
        flight = Flight.objects.get(pk=flight_id)

        # Знаходимо id пасажира через дані з надісланої форми
        passenger_id = int(request.POST["passenger"])

        # Знаходимо пасажира за id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Додаємо пасажира на рейс
        passenger.flights.add(flight)

        # Перенаправляємо користувача на сторінку рейсів
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))