from typing import Iterable

flag: bool = True

def greet(name:str) -> None:
    """Say hello to everyone"""
    print("Hi" + name)

def greetAll(names: Iterable[str]) -> None:
  for name in names:
    greet(name)

greetAll(["Bob", "Billy", "Burt"])

some_data : tuple[int, bool, str] = (42, True, "Manchester")

x: dict[str, float] = {"field1": 2.0, "field2": 3.0}

def myDiv(x : float, y : float) -> (float | None):
    if y!= 0: return x/y
    else:     return None

myDict : dict[str, float | str] = {"temp" : 273.0, "units": "Kelvin"}

class Complex: 
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

h : Complex = Complex(3.0, -4.5)

reveal_type(abs)