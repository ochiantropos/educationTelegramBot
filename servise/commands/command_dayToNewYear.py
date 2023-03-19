from base_abstruct_command import AbstructCommand

import sys, os
import datetime



commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class DayToNewYear(AbstructCommand):
    curent_sesion_lenght= 0
    def __init__(self):
        pass
    
    def reset(self):
        pass
    
    def days_until_new_year(self):
        today = datetime.date.today()
        new_year = datetime.date(today.year + 1, 1, 1)
        days_left = (new_year - today).days
        return days_left
    
    def run(self, args : list=[], local="en"):
        print(f"DebugLog: command >> DayToNewYear >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
        
        if local=="ua":
            ansver = f"До нового року {self.days_until_new_year()} днів"
        else:
            ansver = f"Until the new year {self.days_until_new_year()} days"
            
        print(f"DebugLog: command >> DayToNewYear >> run >> curent_sesion_lenght = 0 (next) (ansver = '{ansver}' )")
        return [ansver, False]