from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class CoordinatesOfTheCenterOfTheCircle(AbstructCommand):
    curent_sesion_lenght = 0
    a_value = [None,None]
    b_value = [None,None]
    c_value = [None,None]
    
    def reset(self):
        self.curent_sesion_lenght = 0
        self.a_value = [None,None]
        self.b_value = [None,None]
        self.c_value = [None,None]
    
    def __init__(self, *args):
        pass
    
    def find_circle_center(self, point1, point2, point3, local):
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        div = (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        x = ((x1**2 + y1**2)*(y2-y3) + (x2**2 + y2**2)*(y3-y1) + (x3**2 + y3**2)*(y1-y2))/(2*div)
        y = ((x1**2 + y1**2)*(x3-x2) + (x2**2 + y2**2)*(x1-x3) + (x3**2 + y3**2)*(x2-x1))/(2*div)
        if local == "ua":
            return f"Центр кола знаходиться в ({round(x,2)}, {round(y,2)})"

        else:
            return f"The center of the circle is at ({round(x,2)}, {round(y,2)})"
    
    
    def run(self, args, local="en"):
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "введіть значення координат x,y для 1 точки"
            else:
                ansver = "enter the coordinate value of 1 point" 
                
            self.curent_sesion_lenght += 1
            
            print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            
            return [ansver, True]
                    
        elif self.curent_sesion_lenght == 1:
            l = args.split()
            
            print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            try:            
                    
                self.a_value[0] = int(l[0])
                self.a_value[1] = int(l[1])
                
                if local == "ua":
                    ansver = "введіть значення координат x,y для 2 точки"
                else:
                    ansver = "enter the coordinate value of x,y for 2 point"
                
                self.curent_sesion_lenght += 1
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 1 (next)  (ansver = '{ansver}' )")
                
                return [ansver, True]
                
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для 1 точки знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for 1 point again"
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                    
                return [ansver, True]
            
        elif self.curent_sesion_lenght == 2:
            l = args.split()
            
            print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            try:            
                    
                self.b_value[0] = int(l[0])
                self.b_value[1] = int(l[1])
                
                if local == "ua":
                    ansver = "введіть значення координат x,y для 3 точки"
                else:
                    ansver = "enter the coordinate value of x,y for 3 point"
                
                self.curent_sesion_lenght += 1
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 2 (next)  (ansver = '{ansver}' )")
                
                return [ansver, True]
                
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для 2 точки знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for 2 point again"
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                    
                return [ansver, True]
            
        elif self.curent_sesion_lenght == 3:
            l = args.split()
            
            print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            try:            
                self.c_value[0] = int(l[0])
                self.c_value[1] = int(l[1])
                
                ansver = self.find_circle_center(self.a_value, self.b_value,self.c_value,local)
                
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 3 (next)  (ansver = '{ansver}' )")
                
                return [ansver, False]
                
            except:
                if local == "ua":
                    ansver = "щось пішло не так, введіть значення координат x,y для 3 точки знову"
                else:
                    ansver = "something went wrong, enter the coordinate value of x,y for 3 point again"
                
                print(f"DebugLog: command >> CoordinatesOfTheCenterOfTheCircle >> run >> curent_sesion_lenght = 3 (ansver = '{ansver}' )")
                    
                return [ansver, True]   