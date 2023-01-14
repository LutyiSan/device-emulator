import json
from random import choice


class Lamp:
    state = False
    min_bright = 0
    max_bright = 100
    bright = 0

    def __init__(self, name=''):
        self.name = name

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def set_bright(self, value):
        if isinstance(value, int):
            if self.max_bright <= value <= self.max_bright:
                self.bright = value


class LightRoom:

    def __init__(self, name, quantity):
        self.name = name
        self.light_quantity = quantity
        self.lighters = []

    def create_lighters(self):
        for num in range(1, self.light_quantity + 1):
            self.lighters.append(Lamp(f'td{num}'))

    def all_off(self):
        for lighter in self.lighters:
            lighter.off()
        return self.ret_json()

    def all_on(self):
        for lighter in self.lighters:
            lighter.on()
        return self.ret_json()

    def all_random(self):
        for lighter in self.lighters:
            action = choice([1, 0])
            if action:
                lighter.on()
            else:
                lighter.off()
        return self.ret_json()

    def ret_json(self):
        ret_json = {'name': self.name}
        for lighter in self.lighters:
            ret_json[lighter.name] = lighter.state
        return json.dumps(ret_json)

# Usage
# room = LightRoom('light',10)
# room.create_lighters()
# room.all_random()
