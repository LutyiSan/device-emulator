from random import uniform

el_counter = {'name': "esCounter",
              'volt-a': 221,
              "volt-b": 219,
              'volt-c': 223,
              "curr-a": 34,
              "curr-b": 32,
              "curr-c": 29,
              "act-en": 2430,
              "react-en": 270,
              "full-en": 2700,
              "act-pow": 6.00,
              "react-pow": 4.00,
              "full-pow": 9.00,
              }


def electro_counter():
    el_counter['name'] = "esCounter"
    el_counter['volt-a'] = uniform(221, 223)
    el_counter["volt-b"] = uniform(219, 220)
    el_counter['volt-c'] = uniform(220, 223)
    el_counter["curr-a"] = uniform(34, 35)
    el_counter["curr-b"] = uniform(32, 34)
    el_counter["curr-c"] = uniform(29, 31)

    if el_counter["act-en"] < 8999:
      #  print(el_counter["act-en"])
        el_counter["act-en"] = el_counter["act-en"] + 1
    #    print(el_counter["act-en"])
    else:
        el_counter["act-en"] = 0

    if el_counter["react-en"] < 999:
        el_counter["react-en"] += 0.1
    else:
        el_counter["react-en"] = 0

    if el_counter["full-en"] < 9999:
        el_counter["full-en"] += 1
    else:
        el_counter["full-en"] = 0
    el_counter["act-pow"] = uniform(6.0, 6.5)
    el_counter["react-pow"] = uniform(4.0, 4.4)
    el_counter["full-pow"] = uniform(9.0, 9.9)
    return el_counter
