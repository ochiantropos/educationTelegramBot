from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class AreaOfTheTriangle(AbstructCommand):
    command_sesion_lenght = 2
    curent_sesion_lenght = 0
    
    a_value = 0
    b_value = 0
    s = 0
    
    def reset(self):
        self.curent_sesion_lenght = 0
        self.a_value = 0
        self.b_value = 0
        self.s = 0
        
        
    def __init__(self):
        pass
    
    def run(self, args, local="en"):        
        if self.curent_sesion_lenght == 0:
            ansver = ""
            print(f"DebugLog: command >> AreaOfTheTriangle >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "введіть довжину основи трикутника - b"
            else:
                ansver = "enter the length of the base of the triangle - b"
            
            print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 0 (next) (ansver = '{ansver}' )")
            
            self.curent_sesion_lenght += 1
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            print(f"DebugLog: command >> AreaOfTheTriangle >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if args.isdigit():
                try:
                    self.b_value = int(args)
                    if local == "ua":
                        ansver = "введіть вислоту опущену на основу - h"
                    else:
                        ansver = "enter the opening lowered to the base - h"
                    
                    print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 1 (next)  (ansver = '{ansver}' )")
                    self.curent_sesion_lenght += 1
                    return [ansver, True]
                    
                        
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть довжину основи трикутника ще раз - b"
                    else:
                        ansver = "something went wrong, enter the length of the base of the triangle again - b"
                    print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                    return [ansver, True]

            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                return [ansver, True]

                
        elif self.curent_sesion_lenght == 2:
            print(f"DebugLog: command >> AreaOfTheTriangle >> run >> args: {args} self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if args.isdigit():
                try:
                    self.a_value = int(args)
                    
                    self.s = 1/2 * self.a_value * self.b_value 
                    
                    if local == "ua":
                        ansver = f"S = {self.s}"
                    else:
                        ansver = f"S = {self.s}"
                        
                    print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                    self.curent_sesion_lenght  = 0
                    return [ansver, False]
 
                
                
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть вислоту опущену на основу ще раз - h"
                    else:
                        ansver = "something went wrong, enter the notch lowered to the base again - h"
                        
                    print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                    return [ansver, True]

            
            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                print(f"DebugLog: command >> AreaOfTheTriangle >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
