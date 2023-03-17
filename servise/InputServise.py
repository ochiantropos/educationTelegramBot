from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod,abstractclass
import os
import pandas
import json

class AbstructInputServise(ABC):
    @abstractclassmethod
    def Massage(self, massage):
        pass

    @abstractclassmethod
    def FindJsonPath(self, path):
        pass
    
    
    
class InputServise(AbstructInputServise):
    data_folder = os.path.join(os.path.dirname(__file__), "../data/")
    discharge = ""
    
    def __init__(self):
        super().__init__()
        
        
    def Massage(self massage):
        