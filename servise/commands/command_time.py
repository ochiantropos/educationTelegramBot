from base_abstruct_command import AbstructCommand
import datetime

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class TimeCommand(AbstructCommand):
    command_sesion_lenght = 0
    curent_sesion_lenght = 0
    
    def run(self, args : list=[], local="en"):
        
        if self.curent_sesion_lenght == 0: # last proces
            today = datetime.date.today()
            print(f"DebugLog: command >> time >> run >> get set today date {today}")
            self.curent_sesion_lenght = 0
            
            return [today,False]
        
        else:
            return ['',False]
            