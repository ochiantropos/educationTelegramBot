from typing import List
from pprint import pprint
import os.path as path
from pandas import DataFrame, read_json

class Category:
    json_hash: str
    catalog_path: str
    data: DataFrame
    

    def __init__(self, path: str):
        self.catalog_path = path
        self.read_json_catalog();
        
    
    def read_json_catalog(self):
        self.data = read_json( path.join(self.catalog_path , "request_router.json") ,encoding='utf-8', orient="records ")
