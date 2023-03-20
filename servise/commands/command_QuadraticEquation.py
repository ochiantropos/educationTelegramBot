from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class QuadraticEquation(AbstructCommand):
    command_sesion_lenght = 2
    curent_sesion_lenght = 0
    
    a_value = 0
    b_value = 0
    c_value = 0
    
    def solve_quadratic_equation(self, a, b, c, lang):
        # Обчислюємо дискримінант
        discriminant = b**2 - 4*a*c

        # Перевіряємо, чи є розв'язки
        if discriminant < 0:
            if lang == "ua":
                return "Рівняння не має розв'язків"
            else:
                return "The equation has no solutions"            

        elif discriminant == 0:
            x = -b / (2*a)
            if lang == "ua":
                return f"Рівняння має один розв'язок: x = {x}"
                
            else:
                return f"The equation has one solution: x = {x}"
                
                
        else:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            if lang == "ua":
                return f"Рівняння має два розв'язки: x1 = {x1}, x2 = {x2}"
                
            else:
                return f"The equation has two solutions: x1 = {x1}, x2 = {x2}"
    
    
    def reset(self):
        self.curent_sesion_lenght = 0
        self.a_value = 0
        self.b_value = 0
        self.c_value = 0
        
    
    def __init__(self, *args):
        pass
    
    def run(self, args , local="en"):
        
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> QuadraticEquation >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "введіть значення A квадратного рівняння"
            else:
                ansver = "enter the value of A for the quadratic equation" 
                
            self.curent_sesion_lenght += 1
            print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            print(f"DebugLog: command >> QuadraticEquation >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            if args.isdigit():
                try:
                    self.a_value = int(args)
                    if local == "ua":
                        ansver = "введіть значення B квадратного рівняння"
                    else:
                        ansver = "enter the value of B for the quadratic equation" 
                    
                    self.curent_sesion_lenght += 1
                    print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 1 (next)  (ansver = '{ansver}' )")
                    return [ansver, True]
                    
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть A ще раз"
                    else:
                        ansver = "something went wrong, enter the A again" 
                
                    print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                    return [ansver, True]
                
            else:
                if local == "ua":
                   ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                    
                print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                return [ansver, True]
        elif self.curent_sesion_lenght == 2:
            print(f"DebugLog: command >> QuadraticEquation >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            if args.isdigit():
                try:
                    self.b_value = int(args)
                    if local == "ua":
                        ansver = "введіть значення C квадратного рівняння"
                    else:
                        ansver = "enter the value of C for the quadratic equation" 
                    
                    self.curent_sesion_lenght += 1
                    print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 2 (next)  (ansver = '{ansver}' )")
                    return [ansver, True]
                    
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть B ще раз"
                    else:
                        ansver = "something went wrong, enter the B again" 
                
                    print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                    return [ansver, True]
                
            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                    
                print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
            
        elif self.curent_sesion_lenght == 3:
            print(f"DebugLog: command >> QuadraticEquation >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            if args.isdigit():
                try:
                    self.b_value = int(args)
                    ansver = self.solve_quadratic_equation(self.a_value, self.b_value, self.c_value, local)
                    self.curent_sesion_lenght += 1
                    print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 3 (next)  (ansver = '{ansver}' )")
                    return [ansver, False]
                    
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть C ще раз"
                    else:
                        ansver = "something went wrong, enter the C again" 
                
                    print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 3 (ansver = '{ansver}' )")
                    return [ansver, True]
                
            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                    
                print(f"DebugLog: command >> QuadraticEquation >> run >> curent_sesion_lenght = 3 (ansver = '{ansver}' )")
                return [ansver, True]
                
                
            
            
            
