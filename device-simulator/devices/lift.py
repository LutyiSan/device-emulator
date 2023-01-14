from random import choice


def lift():
    device = {"name": "lift", "stage11": False, "stage12": False, "stage13": False, "stage14": False, "stage15": False,
              "stage16": False, "stage17": False, "door": False, "stage21": False, "stage22": False, "stage23": False,
              "stage24": False, "stage25": False, "stage26": False, "stage27": False, "door2": False, "door3": False,
              "stage31": False, "stage32": False, "stage33": False, "stage34": False, "stage35": False,
              "stage36": False, "stage37": False}
    lift1 = choice([11, 12, 13, 14, 15, 16, 17])
    door1 = choice([True, False, False, True, True, False])
    lift2 = choice([21, 22, 23, 24, 25, 26, 27])
    door2 = choice([True, False, False, True, True, False])
    lift3 = choice([31, 32, 33, 34, 35, 36, 37])
    door3 = choice([True, False, False, True, True, False])
    for i in device.keys():
        if str(lift1) in i:
            device[i] = True
            device["door"] = door1
            break
    for i in device.keys():
        if str(lift2) in i:
            device[i] = True
            device["door2"] = door2
            break
    for i in device.keys():
        if str(lift3) in i:
            device[i] = True
            device["door3"] = door3
            break
    return device



