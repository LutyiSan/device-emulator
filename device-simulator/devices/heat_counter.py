from random import uniform

heat_counter = {'name': "heatCounter",
                'TE-1': 56,
                "TE-2": 34,
                'TE-3': 70,
                "TE-4": 60,
                "PE-1": 3.5,
                "PE-2": 2.8,
                "PE-3": 4.2,
                "PE-4": 3.5,
                "massa-in": 2321,
                "massa-out": 923,
                "volume-in": 628,
                "volume-out": 23,
                "heat-power": 2456,
                "heat-energy": 786}


def heat_en_counter():
    heat_counter['TE-1'] = uniform(58, 61)
    heat_counter["TE-2"] = uniform(45, 50)
    heat_counter['TE-3'] = uniform(58, 61)
    heat_counter["TE-4"] = uniform(54, 56)
    heat_counter["PE-1"] = uniform(3.3, 3.5)
    heat_counter["PE-2"] = uniform(2.6, 2.9)
    heat_counter["PE-3"] = uniform(3.2, 3.4)
    heat_counter["PE-4"] = uniform(3.2, 3.4)
    heat_counter["massa-in"] = 1000
    heat_counter["massa-out"] = 250
    heat_counter["volume-in"] = 400
    heat_counter["volume-out"] = 10
    heat_counter["heat-power"] = 1450 * uniform(0.1, 0.2)
    heat_counter["heat-energy"] = 450 * uniform(0.1, 0.2)
    if heat_counter['massa-in'] < 2500:
        heat_counter['massa-in'] = heat_counter['massa-in'] + 1
    else:
        heat_counter['massa-in'] = 1000
    if heat_counter['massa-out'] < 1750:
        heat_counter['massa-out'] = heat_counter['massa-out'] + 1
    else:
        heat_counter['massa-out'] = 250
    if heat_counter['volume-in'] < 1150:
        heat_counter['volume-in'] = heat_counter['volume-in'] + 0.5
    else:
        heat_counter['volume-in'] = 400
    if heat_counter['volume-out'] < 310:
        heat_counter['volume-out'] = heat_counter['volume-out'] + 0.2
    else:
        heat_counter['volume-out'] = 10
    return heat_counter
