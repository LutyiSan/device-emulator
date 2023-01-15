from random import uniform, randrange

my_itp = {"name": "itp",
          'mode': 0,
          "te-1": 69,
          "te-2": 62,
          "te-3": 60,
          "te-4": 51,
          "te-5": 56,
          "te-6": 57,
          "pe-1": 4.5,
          "pe-2": 3.6,
          "pe-3": 4.4,
          "pe-4": 4.1,
          "valve-1": 12,
          "valve-2": 62,
          "pump-1": True,
          "pump-2": False,
          "pump-3": False,
          "pump-4": True,
          "dps-1": True,
          "dps-2": False,
          "dps-3": False,
          "dps-4": True,
          'start-pump-1': True,
          'start-pump-2': False,
          'start-pump-3': False,
          'start-pump-4': True,
          "set-gvs-temp": 50,
          "set-ot-temp": 65,
          'case': 1
          }


def itp():
    te_set()
    pe_set()
    valve_set()
    if my_itp['mode'] == 0:
        pump_set()
    return my_itp


def te_set():
    my_itp["te-1"] = uniform(68, 69)
    my_itp["te-2"] = uniform(62, 63)
    my_itp["te-3"] = uniform(60, 61)
    my_itp["te-4"] = uniform(51, 52)
    my_itp["te-5"] = uniform(65, 67)
    my_itp["te-6"] = uniform(57, 58)
    my_itp["set-gvs-temp"] = 50
    my_itp["set-ot-temp"] = 65


def pe_set():
    my_itp["pe-1"] = uniform(4.5, 4.7)
    my_itp["pe-2"] = uniform(3.6, 3.8)
    my_itp["pe-3"] = uniform(4.4, 4.6)
    my_itp["pe-4"] = uniform(4.1, 4.3)


def valve_set():
    if my_itp["case"] == 1:
        my_itp["valve-1"] += 1
    elif my_itp["case"] == 2:
        my_itp["valve-1"] -= 1
    if my_itp["valve-1"] == 80:
        my_itp["case"] = 2
    if my_itp["valve-1"] == 0:
        my_itp["case"] = 1
    if my_itp["case"] == 1:
        my_itp["valve-2"] += 1
    elif my_itp["case"] == 2:
        my_itp["valve-2"] -= 1
    if my_itp["valve-2"] == 80:
        my_itp["case"] = 2
    if my_itp["valve-2"] == 0:
        my_itp["case"] = 1


def pump_set():
    if my_itp['start-pump-1']:
        my_itp["pump-1"] = True
        my_itp["dps-1"] = True
    else:
        my_itp["pump-1"] = False
        my_itp["dps-1"] = False
    if my_itp['start-pump-2']:
        my_itp["pump-2"] = True
        my_itp["dps-2"] = True
    else:
        my_itp["pump-2"] = False
        my_itp["dps-2"] = False
    if my_itp['start-pump-3']:
        my_itp["pump-3"] = True
        my_itp["dps-3"] = True
    else:
        my_itp["pump-3"] = False
        my_itp["dps-3"] = False
    if my_itp['start-pump-4']:
        my_itp["pump-4"] = True
        my_itp["dps-4"] = True
    else:
        my_itp["pump-4"] = False
        my_itp["dps-4"] = False


def pump_control(pump, state):
    my_itp['mode'] = 1
    if state:
        my_itp[pump] = True
    else:
        my_itp[pump] = False
    pump_set()
