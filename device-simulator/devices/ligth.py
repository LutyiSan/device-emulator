from random import choice

my_light = {"name": "light",
            'mode': 3,
            "lamp-1": False,
            "lamp-1-dimm": 50,
            "lamp-2": False,
            "lamp-2-dimm": 50,
            "lamp-3": False,
            "lamp-3-dimm": 50,
            "lamp-4": False,
            "lamp-4-dimm": 50,
            "lamp-5": False,
            "lamp-5-dimm": 50,
            "lamp-6": False,
            "lamp-6-dimm": 50,
            "lamp-7": False,
            "lamp-7-dimm": 50,
            "lamp-8": False,
            "lamp-8-dimm": 50,
            "lamp-9": False,
            "lamp-9-dimm": 50,
            "lamp-10": False,
            "lamp-10-dimm": 50,
            "lamp-11": False,
            "lamp-11-dimm": 50,
            "lamp-12": False,
            "lamp-12-dimm": 50
            }


def light():
    if my_light['mode'] == 3:
        random_light()
        return random_light()
    elif my_light['mode'] == 1:
        return all_on()
    elif my_light['mode'] == 2:
        return all_off()


def random_light():
    my_light['mode'] = 3
    my_light["lamp-1"] = choice([True, False, False, True])
    my_light["lamp-2"] = choice([True, False, False, True])
    my_light["lamp-3"] = choice([True, False, False, True])
    my_light["lamp-4"] = choice([True, False, False, True])
    my_light["lamp-5"] = choice([True, False, False, True])
    my_light["lamp-6"] = choice([True, False, False, True])
    my_light["lamp-7"] = choice([True, False, False, True])
    my_light["lamp-8"] = choice([True, False, False, True])
    my_light["lamp-9"] = choice([True, False, False, True])
    my_light["lamp-10"] = choice([True, False, False, True])
    my_light["lamp-11"] = choice([True, False, False, True])
    my_light["lamp-12"] = choice([True, False, False, True])
    return my_light


def all_on():
    my_light['mode'] = 1
    my_light["lamp-1"] = True
    my_light["lamp-2"] = True
    my_light["lamp-3"] = True
    my_light["lamp-4"] = True
    my_light["lamp-5"] = True
    my_light["lamp-6"] = True
    my_light["lamp-7"] = True
    my_light["lamp-8"] = True
    my_light["lamp-9"] = True
    my_light["lamp-10"] = True
    my_light["lamp-11"] = True
    my_light["lamp-12"] = True
    return my_light


def all_off():
    my_light['mode'] = 2
    my_light["lamp-1"] = False
    my_light["lamp-2"] = False
    my_light["lamp-3"] = False
    my_light["lamp-4"] = False
    my_light["lamp-5"] = False
    my_light["lamp-6"] = False
    my_light["lamp-7"] = False
    my_light["lamp-8"] = False
    my_light["lamp-9"] = False
    my_light["lamp-10"] = False
    my_light["lamp-11"] = False
    my_light["lamp-12"] = False
    return my_light





