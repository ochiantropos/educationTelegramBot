import sys, os


commands_dir = (os.path.abspath(os.path.dirname(__file__)) + '/commands/')
sys.path.append(commands_dir)

from command_AreaOfTheTriangle import AreaOfTheTriangle
from command_botName import BotName
from command_CoordinatesOfTheCenterOfTheCircle import CoordinatesOfTheCenterOfTheCircle
from command_dayToNewYear import DayToNewYear
from command_DistanceFromAPointToAStraightLineInSpace import DistanceFromAPointToAStraightLineInSpace
from command_FibonacciNumber import FibonacciNumber
from command_FindTheCoordinatesOfAPoint import FindTheCoordinatesOfAPoint
from command_QuadraticEquation import QuadraticEquation
from command_ScalarProductOfVectors import ScalarProductOfVectors
from command_StefanBoltzmannLaw import StefanBoltzmannLaw
from command_time import TimeCommand

class CommandServise:
    curent_running_command = ""
    last_ansver = ""
    status_of_command = False
    status_is_execute_command = False
    
    commands = {
        "time": TimeCommand(),
        "AreaOfTheTriangle" : AreaOfTheTriangle(),
        "botName" : BotName(),
        "CoordinatesOfTheCenterOfTheCircle" : CoordinatesOfTheCenterOfTheCircle(),
        "dayToNewYear" : DayToNewYear(),
        "DistanceFromAPointToAStraightLineInSpace" : DistanceFromAPointToAStraightLineInSpace(),
        "FibonacciNumber" : FibonacciNumber(),
        "FindTheCoordinatesOfAPoint" : FindTheCoordinatesOfAPoint(),
        "QuadraticEquation" : QuadraticEquation(),
        "ScalarProductOfVectors" : ScalarProductOfVectors(),
        "StefanBoltzmannLaw" : StefanBoltzmannLaw()
    }
    
    def __init__(self):
        pass
    
    def FilterAnsver(self, ansver):
        
        if self.is_execute_command(ansver):
        
            self.status_is_execute_command = True
            data =  ansver.split(":")[1].split()
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> status_is_execute_command >> {self.status_is_execute_command}")
        
            return self.find_command_by_name(data[0], data[1])
        
        else:
            self.status_is_execute_command = False
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> status_is_execute_command >> {self.status_is_execute_command}")
            return None
    
    
    def is_execute_command(self, execute):
        data = execute.split(":")
        if len(data) >= 2 and data[0] == "__command":
            return True
        else:
            return False

    
    def find_command_by_name(self, _name, _local):
        if _name in list(self.commands.keys()):
            self.status_of_command = True
            
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> find_command_by_name >>  self.status_of_command >>  { self.status_of_command }")
            
            return [_name,_local]
            
        else:
            self.last_ansver = "NotFoundCommand"
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> find_command_by_name >>  self.status_of_command >>  { self.status_of_command }")
            return [_name,_local]
            
            
    def run_command_by_name(self, _name, _local):
        try:
            self.commands[_name].reset()
        except:
            print(f"DebugLog: exept ?!!! CommandServise >> run_command_by_name >> for command with name [{_name}] dont exist Reset Method")
        try:
            request = self.commands[_name].run("",local=_local)
            self.last_ansver, self.status_of_command = request[0], request[1]        
            self.curent_running_command = _name
        
        except:
            print(f"DebugLog: exept ?!!! CommandServise >> run_command_by_name >> for command with name [{_name}] dont exist Run Method")


    def update_execute_to_command(self, NewExecuteCommand,_commnad_name,_local):
        request = self.commands[_commnad_name].run( NewExecuteCommand, local=_local )
        self.last_ansver, self.status_of_command = request[0], request[1]
