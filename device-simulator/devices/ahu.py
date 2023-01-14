from random import uniform
from loguru import logger

ahu = {'name': "ahu",
       'mode': 1,
       "te-oat": 25.8,
       "te-sf": 23.1,
       "te-rf": 24.5,
       "te-heat": 38.3,
       "heat-valve": 10.0,
       "cool-valve": 76.2,
       "rec-valve": 10.6,
       "sf-state": True,
       "rf-state": False,
       "heat-pump-state": False,
       "cool-pump-state": True,
       "rec-pump-state": False,
       "sf-dumper": True,
       "rf-dumper": False,
       "rec-dumper": True,
       "thermostat": False,
       "filter-1": True,
       "filter-2": True,
       "filter-3": False,
       "start-ahu": True,
       "temp-set": 22,
       "season": 1,
       "start-heat-pump": 2,
       "start-cool-pump": 2,
       "start-rec-pump": 2,
       "start-sf-dumper": True,
       "start-rf-dumper": False,
       "start-rec-dumper": True,
       "h-case": 1,
       "c-case": 1
       }


def ahu_logic():
    if ahu['mode'] == 2:
        ahu_stop()
    else:
        te_set()
        if ahu['season'] == 1:
            winter_mode()
        elif ahu['season'] == 2:
            summer_mode()
        ahu["rec-valve"] = 0
        ahu["sf-state"] = True
        ahu["rf-state"] = True
        ahu["rec-pump-state"] = False
        ahu["sf-dumper"] = True
        ahu["rf-dumper"] = True
        ahu["rec-dumper"] = False
        ahu["thermostat"] = False
        ahu["filter-1"] = True
        ahu["filter-2"] = True
        ahu["filter-3"] = True
        ahu["start-ahu"] = True
        ahu["temp-set"] = 22
        ahu["start-heat-pump"] = True
        ahu["start-cool-pump"] = False
        ahu["start-rec-pump"] = False
        ahu["start-sf-dumper"] = True
        ahu["start-rf-dumper"] = True
        ahu["start-rec-dumper"] = False
    return ahu


def te_set():
    ahu["te-oat"] = uniform(14, 15)
    ahu["te-sf"] = uniform(19, 20)
    ahu["te-rf"] = uniform(21, 22)
    ahu["te-heat"] = uniform(38, 42)


def winter_mode():
    ahu["cool-valve"] = 0
    ahu["cool-pump-state"] = False
    ahu["heat-pump-state"] = True
    if ahu["h-case"] == 1:
        ahu["heat-valve"] += 1
    elif ahu["h-case"] == 2:
        ahu["heat-valve"] -= 1
    if ahu["heat-valve"] == 80:
        ahu["h-case"] = 2
    if ahu["heat-valve"] <= 0:
        ahu["h-case"] = 1


def summer_mode():
    ahu["heat-valve"] = 0
    ahu["cool-pump-state"] = True
    ahu["heat-pump-state"] = False
    if ahu["c-case"] == 1:
        ahu["cool-valve"] += 1
    elif ahu["c-case"] == 2:
        ahu["cool-valve"] -= 1
    if ahu["cool-valve"] == 80:
        ahu["c-case"] = 2
    if ahu["cool-valve"] <= 0:
        ahu["c-case"] = 1


def ahu_stop():
    ahu['mode'] = 2
    te_set()
    ahu["heat-valve"] = 0
    ahu["cool-valve"] = 0
    ahu["case"] = 1
    ahu["rec-valve"] = 0
    ahu["sf-state"] = False
    ahu["rf-state"] = False
    ahu["heat-pump-state"] = False
    ahu["heat-pump-state"] = False
    ahu["heat-pump-state"] = False
    ahu["sf-dumper"] = False
    ahu["rf-dumper"] = False
    ahu["rec-dumper"] = False
    ahu["thermostat"] = False
    ahu["filter-1"] = False
    ahu["filter-2"] = False
    ahu["filter-3"] = False
    ahu["start-ahu"] = False
    ahu["temp-set"] = 22
    ahu["start-heat-pump"] = False
    ahu["start-cool-pump"] = False
    ahu["start-rec-pump"] = False
    ahu["start-sf-dumper"] = False
    ahu["start-rf-dumper"] = False
    ahu["start-rec-dumper"] = False
    return ahu


def start_ahu():
    ahu['mode'] = 1
    return ahu_logic()


def ahu_set_season(season):
    ahu['season'] = season
    return ahu_logic()
