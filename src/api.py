from src.abstract_api import AbsAPI
import requests

class ConnectHHapi(AbsAPI):
    """Класс для подключения к API и получения вакансий"""

    def __init__(self, url_get='https://api.hh.ru/vacancies'):
        self.url_get = url_get

    def get_vacancies(self, keyword):
        """Получение списка вакансий в формате json"""

        response = requests.get(self.url_get, params={'text': keyword, 'area': '113', 'per_page': 100})
        vacancies = response.json()['items']
        return vacancies
