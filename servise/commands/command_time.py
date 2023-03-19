from base_abstruct_command import AbstructCommand
import datetime

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class TimeCommand(AbstructCommand):
    command_sesion_lenght = 0
    curent_sesion_lenght = 0
    
    def reset(self):
        pass
    
    def run(self, args : list=[], local="en"):
        
        if self.curent_sesion_lenght == 0: # last proces
            print(f"DebugLog: command >> TimeCommand >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            today = datetime.date.today()
            self.curent_sesion_lenght = 0
            print(f"DebugLog: command >> TimeCommand >> run >> curent_sesion_lenght = 0 (next) (ansver = '{today}' )")

            return [today,False]
        
        else:
            return ['',False]
            