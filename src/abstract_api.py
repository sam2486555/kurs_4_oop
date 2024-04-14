from abc import ABC, abstractmethod

class AbsAPI(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass