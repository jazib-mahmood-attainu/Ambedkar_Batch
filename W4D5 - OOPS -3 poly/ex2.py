"""
Whichever file you are running 
"""

from ex import Parent
class child(Parent):
    def __init__(self):
        print("child")

obj = child()

obj.eat()

print(__name__)