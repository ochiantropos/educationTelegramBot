import os.path as path
import os, sys

models_directory = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/models/')
sys.path.append(models_directory)

from catalog import Category
from pandas import DataFrame

class LinkManager:
    __path : str
    DataCategory : Category
    
    def __init__(self, _path: str):
        self.__path = _path
        self.DataCategory = Category(_path)
        

    def go_to_next_catalog(self, next_directive):
        self.DataCategory.catalog_path = path.join(self.DataCategory.catalog_path,next_directive)
        self.DataCategory.read_json_catalog()
        
    def back_to_prev_catalog(self):
        dir_list = self.DataCategory.catalog_path.split("\\")
        self.DataCategory.catalog_path =  "\\".join(  [ dir_list[dir_index_item]  for dir_index_item in range( 0, len( dir_list ) - 1 )  ] )
    
    def get_all_subdirectory(self):
        subdirectives = []
        for index, row in self.DataCategory.data.iterrows():
            if "is_catalog" in self.DataCategory.data.columns: 
                if row["is_catalog"] == True:
                    if "name" in self.DataCategory.data.columns: 
                        subdirectives.append(row["name"])
        print(subdirectives)
        
        
                            
linkmanager =LinkManager("D:\\GitHub\\educationTelegramBot\\data");
linkmanager.get_all_subdirectory()
linkmanager.go_to_next_catalog("start")
linkmanager.get_all_subdirectory()
