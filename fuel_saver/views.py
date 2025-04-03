#I'm going to call on these methods in urls.py


#if you want to import httpresponse use this:
#from django.http import HttpResponse


#if you want to import render use this:
#from django.shortcuts import render

#request means if a link references something:
# def homepage(request):
#     #return HttpResponse("Check out my homepage")
#     return render(request, 'home.html')

# def about(request):
#     #return HttpResponse("All about the site")
#     return render(request, 'about.html')

# def index(request):
#     #return HttpResponse("This is my app")
#     return render(request, 'index.html')

from django.shortcuts import render

def fuel_cost(fuel_type, economy, fuel_prices, annual_mileage):
    """Calculate annual or monthly fuel cost based on user selection."""
    if fuel_type == "unleaded":
        fuel_price = fuel_prices["unleaded"]
    elif fuel_type == "diesel":
        fuel_price = fuel_prices["diesel"]
    else:
        return None  # Invalid fuel type

    return (annual_mileage / economy) * fuel_price

from django.shortcuts import render

def calculate_fuel_cost(fuel_type, economy, unleaded_price, diesel_price, mileage):
    """Calculate fuel cost based on fuel type, economy, and mileage."""
    fuel_price = unleaded_price if fuel_type == "unleaded" else diesel_price
    return (mileage / economy) * fuel_price

def calculate_fuel(request):
    if request.method == "POST":
        # Get form inputs
        unleaded_price = float(request.POST.get("unleaded_cost"))
        diesel_price = float(request.POST.get("diesel_cost"))
        interval = request.POST.get("interval")
        car1_fuel_type = request.POST.get("fuel_type1")
        car2_fuel_type = request.POST.get("fuel_type2")
        car1_economy = float(request.POST.get("fuel_economy1"))
        car2_economy = float(request.POST.get("fuel_economy2"))
        annual_mileage = float(request.POST.get("annual_mileage"))

        # Calculate annual fuel costs
        fc1 = calculate_fuel_cost(car1_fuel_type, car1_economy, unleaded_price, diesel_price, annual_mileage)
        fc2 = calculate_fuel_cost(car2_fuel_type, car2_economy, unleaded_price, diesel_price, annual_mileage)

        # Convert to monthly if needed
        if interval == "monthly":
            fc1 /= 12
            fc2 /= 12

        # Pass form values and results back to the template
        return render(request, "index.html", {
            "fc1": round(fc1, 2), "fc2": round(fc2, 2),
            "unleaded_price": unleaded_price, "diesel_price": diesel_price,
            "interval": interval,
            "fuel_economy1": car1_economy, "fuel_economy2": car2_economy,
            "fuel_type1": car1_fuel_type, "fuel_type2": car2_fuel_type,
            "annual_mileage": annual_mileage
        })

    return render(request, "index.html")


