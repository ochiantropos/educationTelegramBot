import os

class SaveManager:
    save_direvtory = ""
    tamplate = [
        "<div style=\"width:100%; height: auto; display: inline-block; box-sizing: border-box;\">",
        "<h3 style=\"width:50%; height: auto;margin-left: auto; margin-right: auto; box-sizing: border-box; font-size: 220%;text-align:left;\">",
        "",
        "</h3>"
        "<p style=\"font-size: 150%; width: 60%;height: auto;margin-left: auto;margin-right: auto;box-sizing: border-box; text-align:center;\">",
        "",
        "</p>",
        "</div>"
    ]
    
    def __init__(self, path_to_save):
        self.save_direvtory = path_to_save
        
        
    def SaveToHtml(self, user_massage, bot_massage, file_name ):
        file_name = file_name + ".html"
        real_file_path_name = os.path.join(self.save_direvtory, file_name)
        self.tamplate[2] = "user"
        self.tamplate[5] = user_massage
        with open(rf"{real_file_path_name}", "a") as save_file:
            save_file.write(  " ".join(self.tamplate)  )
            
        self.tamplate[2] = "bot"
        self.tamplate[5] = bot_massage
        with open(rf"{real_file_path_name}", "a") as save_file:
            save_file.write(  " ".join(self.tamplate)  )
            
# s = SaveManager(r"C:\Users\bhj01\OneDrive\Рабочий стол")

# s.SaveToHtml("/start", "asfdsgfdhgjgkjhkhjghdfgsdfas\nadfsgdhjgkhljhgf\nasfddghjgkjh\nasdsgdfhgj\ndsfgs", "my_save_file")

# s.SaveToHtml("/dfdsgsd", "asfdsgfdhgjgkasfafsaasjhkhjghdfgsdfas\nadfsgdhjgkhljhgf\nasfddghjgkjh\nasdsgdfhgj\ndsfgsasfdsgfdhgjgkasfafsaasjhkhjghdfgsdfas\nadfsgdhjgkhljhgf\nasfddghjgkjh\nasdsgdfhgj\ndsfgs", "my_save_file")

