from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from pprint import pprint
import sys,locale,os,pandas,json


# Встановлюємо кодування на utf-8
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Встановлюємо локаль на uk_UA.UTF-8
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

extra = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/extra_class/')
models = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/models/')

sys.path.append(extra)
sys.path.append(models)


from LinksManager import LinkManager
from catalog import Category



class AbstructInputServise(ABC):
    @abstractclassmethod
    def Massage(self, massage):
        pass
    
    @abstractclassmethod
    def BackTopPrev(self, local):
        pass
    
    @abstractclassmethod
    def IsMassageInPath(self, massage):
        pass
    
    
class InputServise(AbstructInputServise):
    discharge = ""
    linkManager = None
    
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.linkManager = LinkManager(path)
        
    def IsMassageInPath(self, massage):
        for way in self.linkManager.get_all_path_way():
            if massage == way:
                return True
            else:
                continue
            
        return False
        
    def BackTopPrev(self, local = "en"):
        dir_now, leaved_dir = self.linkManager.back_to_prev_catalog()
        if local == "en":
            ansver = f"You come Back to {dir_now} menu"
        else:
            ansver = f"Ви повернулись до {dir_now} меню"
            
        print(f"DebugLog: linkManager come back to {dir_now} and get ansver {ansver}")
        return ansver
        
        
    def Massage(self, massage) -> str:
        ansver = ""
        if self.IsMassageInPath(massage):
            prev_path = self.linkManager.get_curent_path()
            if  self.linkManager.is_the_category_folder(massage):
                ansver = self.linkManager.get_ansver_is_not_command_by_key(massage)
                print(f"DebugLog: linkManager find {massage} and get ansver {ansver}")
                lang = self.linkManager.go_to_next_catalog(massage)
                if lang == "ua":
                    ad_ansver = self.linkManager.get_all_ukranian_path_way()
                else:
                    ad_ansver = self.linkManager.get_all_english_path_way()
                    
                ansver += ad_ansver
                
                print(f"DebugLog: linkManager ansver += ad_ansver and get (ansver = {ansver})")
                print(f"DebugLog: linkManager go from ( {prev_path} ) >> to >> ( {self.linkManager.get_curent_path()} ) ")
                return ansver
                
            else:
                ansver = self.linkManager.get_ansver_is_not_command_by_key(massage)
                print(f"DebugLog: linkManager find {massage} and get ansver {ansver}")
                print(f"DebugLog: run command with name [{massage}]")
                return ansver
        
        else:
            print(f"DebugLog: cant find {massage} in linkManager with curent direct in ( { self.linkManager.get_curent_path() } )")
            return "NotFoundCommand"
    
