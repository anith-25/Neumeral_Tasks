from ast import And, Or


def is_kerala_registered_vehicle(vehicle_number):
    temp = False
    if vehicle_number[:2] == 'KL':
        if len(vehicle_number) == 10:
            if (vehicle_number[2:4].isdigit()) and (vehicle_number[4:6].isalpha()) and (vehicle_number[6:].isdigit()):
                mid_number = vehicle_number[2:4]
                print(mid_number)
                if int(mid_number) <= 72:
                    temp = True
        elif len(vehicle_number) == 9:
            if (vehicle_number[2:4].isdigit()) and (vehicle_number[4].isalpha()) and (vehicle_number[5:].isdigit()):       
                mid_number = vehicle_number[2:4]
                if int(mid_number) <= 72:
                    temp = True
            elif (vehicle_number[2].isdigit()) and (vehicle_number[3:5].isalpha()) and (vehicle_number[5:].isdigit()):
                temp = True
        elif len(vehicle_number) == 8:
            if(vehicle_number[2].isdigit()) and (vehicle_number[3].isalpha()) and (vehicle_number[4:].isdigit()):
                temp = True
    return temp

a = 'KL7A9999'
print(is_kerala_registered_vehicle(a))