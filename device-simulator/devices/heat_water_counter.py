heat_water_counter = {'name': "heatWater",
                      "volume": 871}


def heat_water():
    if heat_water_counter["volume"] < 9999:
        heat_water_counter["volume"] += 0.3
    else:
        heat_water_counter["volume"] = 0
    return heat_water_counter
