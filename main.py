from src.api import ConnectHHapi
from src.func import ListVacancies
from src.sorting import sorting


def interface():
    """Функция для взаимодействия с пользователем"""

    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = ConnectHHapi()
    vacancies = hh.get_vacancies(user_vacancy)

    fv = ListVacancies()
    fv1 = fv.save_vacancies(vacancies)

    name_vac = input('Введите название вакансии: \n')
    fv3 = fv.add_vacancy(name_vac)

    name_criterion = input('Опишите свои сильные качества: \n')
    fv4 = fv.get_data(name_criterion)

    n = input('Введите количество вакансий для просмотра: \n')
    top_vacancies = sorting(int(n))

    name_exit = input('Нажмите ENTER чтобы выйти из программы : \nЕсли программа выдала не те вакансии повторите поиск вводя все те же данные\n')
    if name_exit == '':
        fv4 = fv.delete_vacancy()

if __name__ == "__main__":
    interface()
