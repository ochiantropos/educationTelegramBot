from base_abstruct_command import AbstructCommand

import sys, os, math

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class ScalarProductOfVectors(AbstructCommand):
    curent_sesion_lenght = 0
    value_a = 0
    value_b = 0
    value_fi = 0
    
    def reset(self):
        self.value_a = 0
        self.value_b = 0
        self.value_fi = 0
        self.curent_sesion_lenght = 0

    def scalar_product_of_vectors(self, v1, v2, angle_degrees, local):
        angle_radians = math.radians(angle_degrees)
        scalar_product = v1 * v2 * math.cos(angle_radians)
        if local == "ua":
            return f"Скалярним добутком векторів із величинами {v1} і {v2} та кутом {angle_degrees} градусів є {scalar_product:.2f}."
        else:
            return f"The scalar product of vectors with magnitudes {v1} and {v2}, and angle {angle_degrees} degrees is {scalar_product:.2f}."


    def __init__(self, *args):
        pass
    
    def run(self, args, local="en"):
        
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "Введіть заначення довжини вектора А"
            else:
                ansver = "Enter the assignment of the length of the vector A" 
            self.curent_sesion_lenght += 1
            
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            return [ansver, True]
            
        elif self.curent_sesion_lenght == 1:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            if args.isdigit():
                try:
                    self.value_a = int(args)
                    
                    if local == "ua":
                        ansver = "Введіть заначення довжини вектора B"
                    else:
                        ansver = "Enter the assignment of the length of the vector B" 
                    self.curent_sesion_lenght += 1
            
                    print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 1 (next) (ansver = '{ansver}' )")
                    return [ansver, True]
                    
                    
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть заначення довжини вектора A ще раз"
                    else:
                        ansver = "something went wrong, enter the assignment of the length of the vector A again" 
                
                    print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                    return [ansver, True]
                
                
            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                    
                print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                return [ansver, True]
        elif self.curent_sesion_lenght == 2:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            if args.isdigit():
                try:
                    self.value_b = int(args)
                    
                    if local == "ua":
                        ansver = "Введіть заначення кута між ними "
                    else:
                        ansver = "Enter the angle between them" 
                    self.curent_sesion_lenght += 1
            
                    print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 2 (next) (ansver = '{ansver}' )")
                    return [ansver, True]
                    
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть заначення довжини вектора B ще раз"
                    else:
                        ansver = "something went wrong, enter the assignment of the length of the vector B again" 
                
                    print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                    return [ansver, True]
                
                
            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
                    
                print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
            
        elif self.curent_sesion_lenght == 3:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            try:
                self.value_c = int(args)
                ansver = self.scalar_product_of_vectors(self.value_a, self.value_b, self.value_c, local)
                return [ansver, False]          
                
            except:
                if local == "ua":
                    ansver = "The " + args  + " is not a valid angle"
                else:
                    ansver =  args + " не є допустимим кутом"
                    
                print(f"DebugLog: command >> ScalarProductOfVectors >> run >> curent_sesion_lenght = 3 (ansver = '{ansver}' )")
                return [ansver, True]
                