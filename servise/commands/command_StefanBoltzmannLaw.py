from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class StefanBoltzmannLaw(AbstructCommand):
    curent_sesion_lenght = 0
    
    a_value = 0
    b_value = 0
    c_value = 0
    
    
    def reset(self):
        self.curent_sesion_lenght = 0
        self.a_value = 0
        self.b_value = 0
        self.c_value = 0
    
    def __init__(self, *args):
        pass
    
    def stefan_boltzmann_law(self, T, sigma, A):
        """
        T: температура поверхні в Кельвінах
        sigma: стала Стефана-Больцмана
        A: площа поверхні в квадратних метрах
        """
        return sigma * T**4 * A
    
    
    
    def run(self, args , local="en"):
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "введіть значення A - площа поверхні тіла"
            else:
                ansver = "enter the value ofі A - body surface area" 
                
            self.curent_sesion_lenght += 1
            print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            
            return [ansver, True]
        
        elif  self.curent_sesion_lenght == 1:
            print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            try:
                self.a_value = int(args)
                
                if local == "ua":
                    ansver = "введіть значення T - абсолютна температура тіла"
                else:
                    ansver = "enter the value of T - absolute body temperature" 
                self.curent_sesion_lenght += 1
                
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 1 (next) (ansver = '{ansver}' )")
                return [ansver, True]
                    
                
            except:
                if local == "ua":
                    ansver = "The " + args  + " is not a valid number"
                else:
                    ansver =  args + " не є допустимим значенням"
                self.curent_sesion_lenght += 1
                    
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                return [ansver, True]
            
        elif  self.curent_sesion_lenght == 2:
            print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            try:
                self.b_value = int(args)

                self.curent_sesion_lenght += 1
                sigma = 0.00000005670374419
                res = self.stefan_boltzmann_law(self.a_value, sigma , self.b_value)
                
                if local == "ua":
                    ansver = f"Потужність = {res}"
                else:
                    ansver = f"Power = {res}"
                
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 2 (next) (ansver = '{ansver}' )")
                return [ansver, False]
                    
                
            except:
                if local == "ua":
                    ansver = "The " + args  + " is not a valid number"
                else:
                    ansver =  args + " не є допустимим значенням"
                    
                self.curent_sesion_lenght += 1
                    
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
        
