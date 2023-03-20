from base_abstruct_command import AbstructCommand
import sys, os

commands_dir = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(commands_dir)

class MostFrequentlyUsedLetter(AbstructCommand):
    command_sesion_lenght = 0
    curent_sesion_lenght = 0
    path_to_load = ""
    

    def find_most_common_letter(self, input_file_path, locate="en"):
        with open(input_file_path, 'r') as f:
            text = f.read().lower()
        letter_count = {}
        for letter in text:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        most_common_letter = max(letter_count, key=letter_count.get)
        count = letter_count[most_common_letter]
        if locate == "en":
            return f"Letter = {most_common_letter.upper()} count = {count} is the most used in this file"
        else:
            return f"Літера = {most_common_letter.upper()} кількість = {count} є найвживанішою у даному файлі"
    
    
    def reset(self):
        self.path_to_load = ""
        self.command_sesion_lenght = 0


    def run(self, args, local="en"):
        if self.curent_sesion_lenght == 0:
            print(f"DebugLog: command >> MostFrequentlyUsedLetter >> run >> args: {args}  self.curent_sesion_lenght = {self.curent_sesion_lenght}")
            
            if local == "ua":
                ansver = "Введіть шлях до файлу який потрібно змінити"
            else:
                ansver = "Enter the path to the file you want to change" 
                
            self.curent_sesion_lenght += 1
            print(f"DebugLog: command >> MostFrequentlyUsedLetter >> run >> curent_sesion_lenght = 0 (ansver = '{ansver}' )")
            
            return [ansver, True]
        
        elif self.curent_sesion_lenght == 1:
            
            if  os.path.isfile(rf"{args}"):
                
                self.path_to_load = rf"{args}"
                    
                ansver = self.find_most_common_letter(self.path_to_load, local)    
                    
                return [ansver, False]
                    
            else:                
                
                if local == "ua":
                    ansver = "щось пішло не так, введіть шлях до файлу ще раз"
                    
                else:
                    ansver = "something went wrong, enter the path to the file again"
                
                return [ansver, True]
            