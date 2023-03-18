from abc import ABC, abstractmethod

class AbstructCommand(ABC):
    @abstractmethod
    def run(self, args : list=[]) -> list:
        pass
