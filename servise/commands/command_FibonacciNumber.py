from base_abstruct_command import AbstructCommand

import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class FibonacciNumber(AbstructCommand):
    curent_sesion_lenght = 0
    number = 0
    
    def reset(self):
        self.curent_sesion_lenght = 0
        self.number = 0
    
    def __init__(self, *args):
        pass
    
    def fibonacci(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
    
    def run(self, args, local="en"):
        
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> FibonacciNumber >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "введіть номер числа в ряді"
            else:
                ansver = "enter the number number in the row"
            self.curent_sesion_lenght += 1
            print(f"DebugLog: command >> FibonacciNumber >> run >> curent_sesion_lenght = 0 (next) (ansver = '{ansver}' )")
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            print(f"DebugLog: command >> FibonacciNumber >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            if args.isdigit():
                try:
                    self.number = int(args)
                    f = self.fibonacci( self.number)
                    if local == "ua":
                        ansver = f"Число з номером { self.number} у ряді фібоначчі = {f}"
                    else:
                        ansver = f"A number with a number { self.number} in the Fibonacci sequence = {f}"
                    
                    print(f"DebugLog: command >> FibonacciNumber >> run >> curent_sesion_lenght = 1 (next) (ansver = '{ansver}' )")
                    return [ansver, False]
                    
                    
                except:
                    if local == "ua":
                        ansver = "щось пішло не так введіть чило ще раз"
                    else:
                        ansver = "something went wrong, enter the number number in the row again "
                    print(f"DebugLog: command >> FibonacciNumber >> run >> curent_sesion_lenght = 1 (ansver = '{ansver}' )")
                    return [ansver, True]
            
            
            else:
                if local == "ua":
                    ansver = "The " + args  + " not the integer number"
                else:
                    ansver =  args + " не ціле число"
            
                print(f"DebugLog: command >> FibonacciNumber >> run >> curent_sesion_lenght = 2 (ansver = '{ansver}' )")
                return [ansver, True]
        
        