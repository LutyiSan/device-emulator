from random import choice

device = {"name": "scud",
          "td1": False,
          "td1alarm": False,
          "td2": False,
          "td2alarm": False,
          "td3": False,
          "td3alarm": False,
          "td4": False,
          "td4alarm": False}


def scud():
    entry_point = choice(["td1", "td2", "td3", "td4"])
    device[entry_point] = True
    al_entry_point = choice(["td3alarm", "td3alarm", "td3alarm", "td3alarm"])
    device[al_entry_point] = choice([False, False, False, False, True, False, False, False, False, True])
    return device
