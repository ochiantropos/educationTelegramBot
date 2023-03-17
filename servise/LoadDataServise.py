from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod,abstractclass
import os
import pandas
import json

class AbstructLoadDataServise(ABC):
    @abstractclassmethod
    def GetCatalogPathByDischarge(self, Discharge):
        pass
    
    @abstractclassmethod
    def GetPandasTable(self, catalog_name):
        pass
    
    @abstractclassmethod
    def GetPrevPandasTable(self, catalog_name):
        pass
    
    @abstractclassmethod
    def GetNextPandasTable(self, catalog_name):
        pass
    
class LoadDataServise(AbstructLoadDataServise):
    
    
    def __init__(self):
        super().__init__()
    
    
    def GetCatalogPathByDischarge(self, Discharge):
        pass   
     
    def GetPandasTable(self, catalog_name):
        pass
    
    def GetPrevPandasTable(self, catalog_name):
        pass
    
    def GetNextPandasTable(self, catalog_name):
        pass