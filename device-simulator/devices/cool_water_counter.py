cool_water_counter = {"name": 'coolWater',
                      "volume": 4356}


def cool_water():
    if cool_water_counter["volume"] < 9999:
        cool_water_counter["volume"] += 0.5
    else:
        cool_water_counter["volume"] = 0
    return cool_water_counter
