from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class BotName(AbstructCommand):
    curent_sesion_lenght = 0
    
    def reset(self):
        pass
    
    def __init__(self):
        pass
    
    def run(self, args , local="en"):
        print(f"DebugLog: command >> BotName >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
        
        if local=="ua":
            ansver = f"Мене звуть educationBot"
        else:
            ansver = f"My name is educationBot"
            
        print(f"DebugLog: command >> BotName >> run >> curent_sesion_lenght = 0 (next) (ansver = '{ansver}' )")
        return [ansver, False]