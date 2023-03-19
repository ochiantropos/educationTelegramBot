from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class CoordinatesOfTheCenterOfTheCircle(AbstructCommand):
    def __init__(self, *args):
        pass
    
    def reset(self):
        pass
    
    def run(self, args : list=[], local="en"):
        pass
        