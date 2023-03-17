from typing import List
from pprint import pprint
import os.path
from pandas import DataFrame, read_json

class Category:
    name: str
    en: str
    ua: str

    def __init__(self, path: str):
        df = read_json(path + "request_router.json")
        pprint(df)
        
        
Category("D:\GitHub\educationTelegramBot\data\request_router.json")