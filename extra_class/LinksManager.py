import os.path as path
import os, sys
from pprint import pprint

models_directory = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/models/')
sys.path.append(models_directory)


from catalog import Category
from pandas import DataFrame
from random import randint

import locale

# Встановлюємо кодування на utf-8
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Встановлюємо локаль на uk_UA.UTF-8
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')




class LinkManager:
    __path : str
    DataCategory : Category
    is_catalog = True
    
    def __init__(self, _path: str):
        self.__path = _path
        self.DataCategory = Category(_path)
        
    def get_curent_path(self):
        return self.__path

    def go_to_next_catalog(self, next_directive):
        next_dir_real_name = ""
        type_lang = "en"
        
        for index, row in self.DataCategory.data.iterrows():
            if row["en"] == next_directive:
                next_dir_real_name = row["name"]
                type_lang = "en"
                
            elif row["ua"] == next_directive:
                next_dir_real_name = row["name"]
                type_lang = "ua"
            
            else:
                pass
            
        self.DataCategory.catalog_path = path.join(self.DataCategory.catalog_path,next_dir_real_name)
        self.__path = self.DataCategory.catalog_path
        self.DataCategory.read_json_catalog()
        return type_lang
        
    
    def back_to_prev_catalog(self):
        dir_list = self.DataCategory.catalog_path.split("\\")
        self.DataCategory = Category("\\".join(  [ dir_list[dir_index_item]  for dir_index_item in range( 0, len( dir_list ) - 1 )  ] ))
        self.__path =  self.DataCategory.catalog_path
        return dir_list[-2], dir_list[-1]
        
    
    
    def get_all_subdirectory(self):
        subdirectives = []
        for index, row in self.DataCategory.data.iterrows():
            if "is_catalog" in self.DataCategory.data.columns: 
                if row["is_catalog"] == True:
                    if "en" in self.DataCategory.data.columns and "ua" in self.DataCategory.data.columns: 
                        subdirectives.append(row["en"])
                        subdirectives.append(row["ua"])
                        
        return subdirectives
        
    def get_all_commands(self):
        commands = []
        for index, row in self.DataCategory.data.iterrows():
            if "is_catalog" in self.DataCategory.data.columns: 
                if row["is_catalog"] == False:
                    if "en" in self.DataCategory.data.columns and "ua" in self.DataCategory.data.columns: 
                        commands.append(row["en"])
                        commands.append(row["ua"])

        return commands
    '''
        func return all command and directory tags
    
    '''
    def get_all_path_way(self):
        way = []
        for index, row in self.DataCategory.data.iterrows():
            if "en" in self.DataCategory.data.columns and "ua" in self.DataCategory.data.columns: 
                way.append(row["en"])
                way.append(row["ua"])
                
        
        
        #pprint(way)
        return way
    
    def get_all_ukranian_path_way(self):
        way = []
        for index, row in self.DataCategory.data.iterrows():
            if "ua" in self.DataCategory.data.columns: 
                way.append(row["ua"])
                
        #pprint(way)
        ansver = "\n"
        for item in way:
            ansver += "\n" + item
        
        return ansver
    
    def get_all_english_path_way(self):
        way = []
        for index, row in self.DataCategory.data.iterrows():
            if "en" in self.DataCategory.data.columns: 
                way.append(row["en"])
        ansver = "\n"
        for item in way:
            ansver += "\n" + item
        
        return ansver
    
    
    def is_the_category_folder(self, key):
        for index, row in self.DataCategory.data.iterrows():
            if row["en"] == key or row["ua"] == key :
                #print( row["name"] + " and " + str(row["is_catalog"]))
                return row["is_catalog"]

            else:
                continue
        return False
    
    
    def get_ansver_is_not_command_by_key(self, key):
        # if in english
        for index, row in self.DataCategory.data.iterrows():
            if row["en"] == key:
                return self.if_english_command(row)
            
            elif row["ua"] == key:
                return self.if_ukranian_command(row)
            
            else:
                continue
        return "Sory something do wrong :("
                
                
    def if_english_command(self, row):
        d = row["is_comand"]
        if row["is_comand"] != True:
            if row["is_many_answer"] != True:
                s = row["en_answer"]
                print(f"DebugLog: row[\"en_answer\"]: {s}")
                return row["en_answer"]
            else:
                many_answers = row["en_answer"].split("[]")
                return many_answers[randint(0, len(many_answers)-1)]
        else:
           return self.command_run(row["command_name"], local="en")
            
        
    def if_ukranian_command(self, row):
        if row["is_comand"] != True:
            if row["is_many_answer"] != True:
                s = row["ua_answer"]
                print(f"DebugLog: row[\"ua_answer\"]: {s}")
                return row["ua_answer"]
            else:
                many_answers = row["ua_answer"].split("[]")
                return many_answers[randint(0, len(many_answers)-1)]
        else:
            return self.command_run(row["command_name"], local="ua")
        

    def command_run(self, tag, local="en"):
        return f"__command:{tag} {local}"
    
    
    
    
# l = LinkManager("D:\\GitHub\\educationTelegramBot\\data\\")
# print("----------------------------------------")
# l.go_to_next_catalog("start")
# print("----------------------------------------")
# l.go_to_next_catalog("physics")
# print("----------------------------------------")
# l.back_to_prev_catalog()
# print("----------------------------------------")
# print(l.get_curent_path())
# print("----------------------------------------")
# print(l.DataCategory.data)
# print("----------------------------------------")
