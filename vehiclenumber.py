def is_kerala_registered_vehicle(vehicle_number):
    temp = False
    if vehicle_number[:2] == 'KL':
        last_digits = vehicle_number[-4:]
        if last_digits.isdigit():
                temp = True
        print(last_digits)
    return temp

a = 'KL07BA9999'
print(is_kerala_registered_vehicle(a))