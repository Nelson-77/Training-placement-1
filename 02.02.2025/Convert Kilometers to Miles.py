def km_to_miles(km):
    return km * 0.621371

kilometers = float(input("Enter distance in kilometers: "))
miles = km_to_miles(kilometers)
print("Distance in miles:", miles)
