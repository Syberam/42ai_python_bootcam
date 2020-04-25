#!/usr/bin/env python
import time
import getpass
from random import randint


def log(function):
    def wrapper(*args, **kwargs):
        t_in = time.time()
        ret = function(*args, **kwargs)
        t_out = time.time()
        exec_time = t_out - t_in
        if exec_time > 0.001:
            exec_time_str = "{:.3f} s ".format(exec_time)
        else:
            exec_time_str = "{:.3f} ms".format(exec_time * 1000)
        with open('machine.log', 'a+') as f:
            f.write("({})Running: {:<20} [ exec-time = {} ]\n".format(
                getpass.getuser(),
                ' '.join(w.capitalize() for w in function.__name__.split('_')),
                exec_time_str
            ))
        return ret
    return wrapper


class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
