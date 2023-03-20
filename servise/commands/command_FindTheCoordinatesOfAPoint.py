from base_abstruct_command import AbstructCommand

import sys, os, math

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class FindTheCoordinatesOfAPoint(AbstructCommand):   
    curent_sesion_lenght = 0
    
    pointA = [None, None]
    d = 0
    azimuth = 0
    def reset(self):
        self.pointA = [None, None]
        self.d = 0
        self.curent_sesion_lenght = 0
        self.azimuth = 0
    
    def __init__(self, *args):
        pass
    
    
    def find_point_b(self,point_a, distance, azimuth):
        x1, y1 = point_a
        x2 = x1 + distance * math.cos(math.radians(azimuth))
        y2 = y1 + distance * math.sin(math.radians(azimuth))
        return [x2, y2]
    
    def run(self, args : list=[], local="en"):
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "Введіть відомі координати точки А"
            else:
                ansver = "Enter the known coordinates of point A" 
                
            self.curent_sesion_lenght += 1
            print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            try:
                
                l = args.split()
                self.pointA[0] = int(l[0])
                self.pointA[1] = int(l[1])
                
                
                if local == "ua":
                    ansver = "Введіть відому відстань d"
                else:
                    ansver = "Enter the known distanse d" 
                    
                self.curent_sesion_lenght += 1
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                
                return [ansver, True]
                    
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для точки A знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for point A again"
                    
                print(f"DebugLog: command >> FindTheCoordinatesOfAPoint >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")     
                return [ansver, True]
                   
                
        elif self.curent_sesion_lenght == 2:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            try:
                self.d = int (args)
                
                if local == "ua":
                    ansver = "Введіть відомий кут азимута"
                else:
                    ansver = "Enter the known azimuth angle" 
                    
                self.curent_sesion_lenght += 1
                
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                
                return [ansver, True]
                    
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення d знову"
                else:
                    ansver = "something went wrong, enter the coordinate value d again"
                    
                print(f"DebugLog: command >> FindTheCoordinatesOfAPoint >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
                
                
        elif self.curent_sesion_lenght == 3:
            print(f"DebugLog: command >> ScalarProductOfVectors >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            try:
                self.azimuth = int(args)
                
                x = self.find_point_b(self.pointA, self.d, self.azimuth)
                
                if local == "ua":
                    ansver = f"Точка B \n( {x[0]},{x[1]} ) "
                else:
                    ansver = f"Point B \n( {x[0]},{x[1]} ) "

                self.curent_sesion_lenght += 1
                
                print(f"DebugLog: command >> StefanBoltzmannLaw >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                
                return [ansver, False]
                    
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення азимуту знову"
                else:
                    ansver = "something went wrong, enter the azimuth again"
                    
                print(f"DebugLog: command >> FindTheCoordinatesOfAPoint >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
