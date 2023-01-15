from random import uniform

cool_center = {"name": "coolCenter", 'mode': 0, "te-1": 13.4, "pe-1": 6.2, "te-2": 11.1, "pe-2": 2.7, "te-3": 10.3,
               "pe-3": 2.9,
               "pe-4": 6.9, "pe-9": 2.9,
               "pe-5": 4.4, "pe-10": 5.3, "pe-6": 4.5, "pe-7": 2.9, "te-4": 11.2, "pe-8": 6.0, "pe-11": 0.1,
               "pe-12": 0.1,
               "pe-13": 0.1, "pe-14": 11.1, "te-5": 8.9, "y1": False, "y5": True, "y2": True, "y3": False, "y4": False,
               "y6": False, "y7": False, "y8": True, "y9": True, "uao1": False, 'uao2': True, "uoo": False,
               "dps1": True,
               "dps2": False, "nc1": True, "nc2": False, "nc3": True, "nc4": False, 'start-nc1': True,
               'start-nc2': False, 'start-nc3': True, 'start-nc4': False}


def cooling_center():
    set_te()
    cool_center["y1"] = False
    cool_center["y5"] = True
    cool_center["y2"] = True
    cool_center["y3"] = False
    cool_center["y4"] = False
    cool_center["y6"] = False
    cool_center["y7"] = False
    cool_center["y8"] = True
    cool_center["y9"] = True
    cool_center["uao1"] = False
    cool_center['uao2'] = True
    cool_center["uoo"] = False
    set_pump()
    return cool_center


def set_te():
    cool_center["te-1"] = uniform(13.3, 13.5)
    cool_center["te-2"] = uniform(10.9, 11.2)
    cool_center["te-3"] = uniform(10.2, 10.5)
    cool_center["te-4"] = uniform(11.0, 11.2)
    cool_center["te-5"] = uniform(8.8, 9.0)


def set_pe():
    cool_center["pe-1"] = uniform(6.1, 6.3)
    cool_center["pe-2"] = uniform(2.7, 2.9)
    cool_center["pe-3"] = uniform(2.8, 3.0)
    cool_center["pe-4"] = uniform(6.8, 7.0)
    cool_center["pe-9"] = uniform(2.9, 3.1)
    cool_center["pe-5"] = uniform(4.4, 4.5)
    cool_center["pe-10"] = uniform(5.1, 5.3)
    cool_center["pe-6"] = uniform(4.4, 4.6)
    cool_center["pe-7"] = uniform(2.9, 3.1)
    cool_center["pe-8"] = uniform(5.9, 6.1)
    cool_center["pe-11"] = uniform(0.1, 1)
    cool_center["pe-12"] = uniform(0.1, 1)
    cool_center["pe-13"] = uniform(0.1, 1)
    cool_center["pe-14"] = uniform(11.0, 11.2)


def set_pump():
    if cool_center['start-nc1']:
        cool_center["nc1"] = True
        cool_center["dps1"] = True
    else:
        cool_center["nc1"] = False
        cool_center["dps1"] = False
    if cool_center['start-nc2']:
        cool_center["nc2"] = True
        cool_center["dps1"] = True
    else:
        cool_center["nc2"] = False
        cool_center["dps1"] = False
    if cool_center['start-nc3']:
        cool_center["nc3"] = True
        cool_center["dps2"] = True
    else:
        cool_center["nc3"] = False
        cool_center["dps2"] = False
    if cool_center['start-nc4']:
        cool_center["nc4"] = True
        cool_center["dps2"] = True
    else:
        cool_center["nc4"] = False
        cool_center["dps2"] = False


def pump_ch_control(pump, state):
    cool_center['mode'] = 1
    if state:
        cool_center[pump] = True
    else:
        cool_center[pump] = False

    return cool_center
