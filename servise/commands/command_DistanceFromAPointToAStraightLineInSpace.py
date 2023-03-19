from base_abstruct_command import AbstructCommand

import sys, os,math

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class DistanceFromAPointToAStraightLineInSpace(AbstructCommand):
        
    curent_sesion_lenght = 0
    a_value = [None,None]
    b_value = [None,None]
    c_value = [None,None]
    
    def __init__(self, *args):
            pass

    
    def reset(self):
        self.curent_sesion_lenght = 0
        self.a_value = [None,None]
        self.b_value = [None,None]
        self.c_value = [None,None]
        
    def distance_to_line(self,point, line_start, line_end):
        """
    Обчислює відстань від точки до прямої в просторі.

    :param point: Список з координатами точки у вигляді [x, y].
    :param line_start: Список з координатами початкової точки прямої у вигляді [x, y].
    :param line_end: Список з координатами кінцевої точки прямої у вигляді [x, y].
    :return: Відстань від точки до прямої.
    """
        x1, y1 = line_start
        x2, y2 = line_end
        x, y = point

        numerator = abs((x - x1) * (y2 - y1) - (y - y1) * (x2 - x1))
        denominator = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        return float(numerator) / float(denominator)
    

    
    def run(self, args : list=[], local="en"):
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "введіть значення координат x,y для P точки"
            else:
                ansver = "enter the coordinate value x,y of P point" 
                
            self.curent_sesion_lenght += 1
            
            print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            
            print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            try:            
                l  = args.split()
                    
                self.a_value[0] = int(l[0])
                self.a_value[1] = int(l[1])
                
                if local == "ua":
                    ansver = "введіть значення координат x,y для A точки на прямій"
                else:
                    ansver = "enter the coordinate value of x,y for A point by direct"
                
                self.curent_sesion_lenght += 1
                print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> curent_sesion_lenght = 1 (next)  (ansver = '{ansver}' )")
                
                return [ansver, True]
                
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для P точки знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for P point again"
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                    
                return [ansver, True]
    
    
        elif self.curent_sesion_lenght == 2:
            print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            try:            
                l  = args.split()
                    
                self.b_value[0] = int(l[0])
                self.b_value[1] = int(l[1])
                
                if local == "ua":
                    ansver = "введіть значення координат x,y для B точки на прямій"
                else:
                    ansver = "enter the coordinate value of x,y for B point by direct"
                
                self.curent_sesion_lenght += 1
                print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> curent_sesion_lenght = 2 (next)  (ansver = '{ansver}' )")
                
                return [ansver, True]
                
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для A точки знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for A point again"
                    
                print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                    
                return [ansver, True]
        
        elif self.curent_sesion_lenght == 3:
            print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            try:            
                l  = args.split()
                    
                self.c_value[0] = int(l[0])
                self.c_value[1] = int(l[1])
                
                d = self.distance_to_line(self.a_value, self.b_value, self.c_value)
                
                if local == "ua":
                    ansver = f"Відстань = {d}"
                else:
                    ansver = f"Distanse = {d}"
                    
                self.curent_sesion_lenght += 1
                print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> curent_sesion_lenght = 3 (next)  (ansver = '{ansver}' )")
                
                return [ansver, False]
                
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для B точки знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for B point again"
                    
                print(f"DebugLog: command >> DistanceFromAPointToAStraightLineInSpace >> run >> curent_sesion_lenght = 3 (ansver = '{ansver}' )")
                    
                return [ansver, True]