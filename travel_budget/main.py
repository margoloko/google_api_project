import argparse

from services import DRIVE_SERVICE, EMAIL_USER, SHEETS_SERVICE


if __name__ == '__main__':
    # Экземпляра класса ArgumentParser
    parser = argparse.ArgumentParser(description='Бюджет путешествий')
    parser.add_argument('-c', '--create',
                        help='Создать файл - введите "имя, бюджет"')
    parser.add_argument('-i', '--id',
                        help='Указать id spreadsheet')
    parser.add_argument('-cl', '--clear_all',
                        action='store_true',
                        help='Удалить все spreadsheets')
    parser.add_argument('-ls', '--list',
                        action='store_true',
                        help='Вывести все spreadsheets')
    parser.add_argument('-u', '--update',
                        help='Обновить данные табилицы')
    # Парсинг аргументов командной строки
    args = parser.parse_args()
