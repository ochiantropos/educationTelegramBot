import os
from datetime import datetime
class SaveManager:
    save_direvtory = ""

    def __init__(self, path_to_save):
        self.save_direvtory = path_to_save

    @staticmethod
    def get_file_name_by_data(self):
        nav_data_to_day = datetime.now()
        date_time = nav_data_to_day.strftime("%m_%d_%Y_%Hh")
        return date_time
        
    def SaveToHtml(self, user_massage, bot_massage):
        file_name = "data-" + self.get_file_name_by_data(self) + ".txt"
        real_file_path_name = os.path.join(self.save_direvtory, file_name)
        ansver = "\n\tuser :\n\n"
        ansver += user_massage
        ansver += "\n\tbot :\n\n"
        ansver += bot_massage
        with open(real_file_path_name, "a+", encoding="UTF-8") as save_file:
            save_file.write(ansver)
