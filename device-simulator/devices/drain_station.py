dn_station = {'name': "dnStation",
              "pump1-work": False,
              "pump1-alarm": False,
              "pump2-work": False,
              "pump2-alarm": False,
              "ls-1": False,
              "ls-2": False,
              "ls-3": False,
              'case': 0}


def drain_station():
    if dn_station['case'] == 10:
        dn_station['case'] = 0
    if dn_station['case'] == 0:
        dn_station['ls-2'] = False
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = False
        dn_station['pump2-work'] = False
        dn_station['ls-1'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 1:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = False
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = False
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 2:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = True
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = False
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 3:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = True
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = True
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 4:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = True
        dn_station['ls-3'] = True
        dn_station['pump1-work'] = True
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 5:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = True
        dn_station['ls-3'] = True
        dn_station['pump1-work'] = True
        dn_station['pump2-work'] = True
        dn_station['case'] += 1
    elif dn_station['case'] == 6:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = True
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = True
        dn_station['pump2-work'] = True
        dn_station['case'] += 1
    elif dn_station['case'] == 7:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = True
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = True
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 8:
        dn_station['ls-1'] = True
        dn_station['ls-2'] = False
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = True
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    elif dn_station['case'] == 9:
        dn_station['ls-1'] = False
        dn_station['ls-2'] = False
        dn_station['ls-3'] = False
        dn_station['pump1-work'] = False
        dn_station['pump2-work'] = False
        dn_station['case'] += 1
    return dn_station
