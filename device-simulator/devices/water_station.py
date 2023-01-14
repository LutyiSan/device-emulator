from random import uniform

water_station = {"name": "waterStation",
                 "pe-1": 1.4,
                 "pe-2": 3.2,
                 "pe-3": 3.1,
                 "pe-4": 3.4,
                 "pe-5": 3.4,
                 "pump-1": True,
                 "pump-2": True,
                 "pump-3": True,
                 "pump-1-start": True,
                 "pump-2-start": True,
                 "pump-3-start": True,
                 "start": True,
                 'case': 0
                 }


def pump_station():
    if water_station['case'] == 6:
        water_station['case'] = 0
    if water_station['case'] == 0:
        case_0()
    elif water_station['case'] == 1 or water_station['case'] == 5:
        case_1_5()
    elif water_station['case'] == 2 or water_station['case'] == 4:
        case_2_4()
    elif water_station['case'] == 3:
        case_3()
    return water_station


def case_0():
    water_station['pe-1'] = uniform(1.4, 1.6)
    water_station['pe-2'] = water_station['pe-1']
    water_station['pe-3'] = water_station['pe-1']
    water_station['pe-4'] = water_station['pe-1']
    water_station['pe-5'] = uniform(1.4, 1.6)
    water_station['pump-1'] = False
    water_station['pump-2'] = False
    water_station['pump-3'] = False
    water_station['case'] += 1


def case_1_5():
    water_station['pe-1'] = uniform(1.4, 1.6)
    water_station['pe-2'] = uniform(3.1, 3.4)
    water_station['pe-3'] = water_station['pe-1']
    water_station['pe-4'] = water_station['pe-1']
    water_station['pe-5'] = water_station['pe-2']
    water_station['pump-1'] = True
    water_station['pump-2'] = False
    water_station['pump-3'] = False
    water_station['case'] += 1


def case_2_4():
    water_station['pe-1'] = uniform(1.4, 1.6)
    water_station['pe-2'] = uniform(3.1, 3.4)
    water_station['pe-3'] = uniform(3.2, 3.5)
    water_station['pe-4'] = water_station['pe-1']
    water_station['pe-5'] = (water_station['pe-2'] + water_station['pe-3']) / 2
    water_station['pump-1'] = True
    water_station['pump-2'] = True
    water_station['pump-3'] = False
    water_station['case'] += 1


def case_3():
    water_station['pe-1'] = uniform(1.4, 1.6)
    water_station['pe-2'] = uniform(3.1, 3.4)
    water_station['pe-3'] = uniform(3.2, 3.5)
    water_station['pe-4'] = uniform(3.3, 3.5)
    water_station['pe-5'] = (water_station['pe-2'] + water_station['pe-3'] + water_station['pe-4']) / 3
    water_station['pump-1'] = True
    water_station['pump-2'] = True
    water_station['pump-3'] = True
    water_station['case'] += 1
