def zero_fuel(distance_to_pump, mpg, fuel_left):
    if float(distance_to_pump) > 0:
        if (distance_to_pump / mpg) <= fuel_left:
            return True
        else: return False
    return False