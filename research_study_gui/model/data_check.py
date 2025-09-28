from abc import ABC, abstractmethod

class DataCheck(ABC):
    @abstractmethod
    def summary(self):
        pass
    @abstractmethod
    def is_valid(self):
        pass