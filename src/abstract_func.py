from abc import ABC, abstractmethod


class Functions(ABC):

    """Абстрактный класс"""

    @abstractmethod
    def add_vacancy(self, *args):
        pass

    @abstractmethod
    def get_data(self, *args):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass