from google.oauth2.service_account import Credentials
from googleapiclient import discovery


CREDENTIALS_FILE = 'nice-particle-384808-4a149e37f38b.json'
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive']

def auth():
    """Функция авторизации."""
    credentials = Credentials.from_service_account_file(
                  filename=CREDENTIALS_FILE, scopes=SCOPES)
    # Создаём экземпляр класса Resource.
    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service, credentials


def create_spreadsheet(service):
    """Функция создания документа."""
    spreadsheet_body = {'properties': { # Свойства документа
                        'title': 'Бюджет путешествий',
                        'locale': 'ru_RU' },
                        # Свойства листов документа
                        'sheets': [{
                            'properties': {
                               'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Отпуск 2077',
                               'gridProperties': {
                                    'rowCount': 100,
                                    'columnCount': 100}
                                             }
                        }]} 
    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    spreadsheet_id = response['spreadsheetId'] 
    print('https://docs.google.com/spreadsheets/d/' + spreadsheet_id)
    return spreadsheet_id  


def set_user_permissions(spreadsheet_id, credentials):
    permissions_body={'type': 'user', # Тип учетных данных.
                      'role': 'writer', # Права доступа для учётной записи.
                      'emailAddress': 'margolokokill@gmail.com'} # Ваш личный гугл-аккаунт.
    
    # Создаётся экземпляр класса Resource для Google Drive API.
    drive_service = discovery.build('drive', 'v3', credentials=credentials)
    
    # Формируется и сразу выполняется запрос на выдачу прав вашему аккаунту.
    drive_service.permissions().create(
        fileId=spreadsheet_id,
        body=permissions_body,
        fields='id'
    ).execute() 

# Вызов функций
if __name__ == '__main__':
    service, credentials = auth()
    create_spreadsheet(service)   