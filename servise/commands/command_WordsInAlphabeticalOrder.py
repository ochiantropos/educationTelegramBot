from base_abstruct_command import AbstructCommand
import sys, os, string

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class WordsInAlphabeticalOrder(AbstructCommand):
    command_sesion_lenght = 0
    curent_sesion_lenght = 0
    path_to_load = ""
    path_to_upload = ""
    
    def sort_words(self,input_file_path, output_file_path):
        # Відкриваємо вхідний файл та зчитуємо всі дані в змінну data
        with open(input_file_path, 'r') as f:
            data = f.read()

        # Видаляємо всі знаки пунктуації та перетворюємо текст в список слів
        words = data.translate(str.maketrans('', '', string.punctuation)).split()

        # Сортуємо список слів за алфавітом
        sorted_words = sorted(words)

        # Записуємо відсортовані слова в вихідний файл
        with open(output_file_path, 'w') as f:
            f.write('\n'.join(sorted_words))
    
    
    def reset(self):
        self.path_to_upload = ""
        self.path_to_load = ""
        self.command_sesion_lenght = 0


    def run(self, args, local="en"):
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> WordsInAlphabeticalOrder >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "Введіть шлях до файлу який потрібно змінити"
            else:
                ansver = "Enter the path to the file you want to change" 
                
            self.curent_sesion_lenght += 1
            print(f"DebugLog: command >> WordsInAlphabeticalOrder >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            
            if  os.path.isfile(rf"{args}"):
                
                self.path_to_load = rf"{args}"
                
                if local == "ua":
                    ansver = "Введіть шлях до файлу в який записати результат"
                else:
                    ansver = "Enter the path to the file to save the result" 
                    
                self.curent_sesion_lenght += 1
                    
                return [ansver, True]
                    
                
            else:                
                
                if local == "ua":
                    ansver = "щось пішло не так, введіть шлях до файлу який потрібно змінити ще раз"
                    
                else:
                    ansver = "something went wrong, enter the path to the file you want to change again"
                
                return [ansver, True]
            
        elif self.curent_sesion_lenght == 2:
                
            if  os.path.isfile(rf"{args}"):
                
                self.path_to_upload = rf"{args}"
                    
                self.sort_words(self.path_to_load,self.path_to_upload)    
                if local == "ua":
    
                    ansver = "Операцію виконано"
                    
                else: 
                    ansver = "The operation is completed"
                    
                return [ansver, False]
                    
                
            else:                
                
                if local == "ua":
                    ansver = "щось пішло не так, введіть шлях до файлу в який записати результат ще раз"
                    
                else:
                    ansver = "something went wrong, enter the path to the file to save the result again"
                
                return [ansver, True]       