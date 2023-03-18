import sys, os


commands_dir = (os.path.abspath(os.path.dirname(__file__)) + '/commands/')
sys.path.append(commands_dir)

from command_time import TimeCommand



class CommandServise:
    
    last_ansver = ""
    status_of_command = False
    status_is_execute_command = False
    
    commands = {
        "time": TimeCommand()
    }
    
    def __init__(self):
        pass
    
    def FilterAnsver(self, ansver):
        
        if self.is_execute_command(ansver):
        
            self.status_is_execute_command = True
            data =  ansver.split(":")[1].split()
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> status_is_execute_command >> {self.status_is_execute_command}")
        
            return self.find_command_by_name(data[0], data[1])
        
        else:
            self.status_is_execute_command = False
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> status_is_execute_command >> {self.status_is_execute_command}")
            return None
    
    
    def is_execute_command(self, execute):
        data = execute.split(":")
        if len(data) >= 2 and data[0] == "__command":
            return True
        else:
            return False

    
    def find_command_by_name(self, _name, _local):
        if _name in list(self.commands.keys()):
            self.status_of_command = True
            
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> find_command_by_name >>  self.status_of_command >>  { self.status_of_command }")
            
            return [_name,_local]
            
        else:
            self.last_ansver = "NotFoundCommand"
            print(f"DebugLog: CommandServise >> FilterAnsver >> is_execute_command >> find_command_by_name >>  self.status_of_command >>  { self.status_of_command }")
            return [_name,_local]
            
            
    def run_command_by_name(self, _name, _local):
        request = self.commands[_name].run(local=_local)
        
        self.last_ansver, self.status_of_command = request[0], request[1]
        if self.status_of_command  == False:
            self.status_is_execute_command = False 

    def update_execute_to_command(self,_commnad_name,_local, NewExecuteCommand):
        request = self.commands[_commnad_name].run( [NewExecuteCommand], local=_local )
        
        self.last_ansver, self.status_of_command = request[0], request[1]
        if self.status_of_command  == False:
            self.status_is_execute_command = False 
