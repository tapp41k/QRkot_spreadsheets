from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings


FORMAT = "%Y/%m/%d %H:%M:%S"

DEFAULT_GRID_PROPERTIES = {
    'rowCount': 100,
    'columnCount': 11
}

DEFAULT_SPREADSHEET_BODY = {
    'properties': {
        'title': '',
        'locale': 'ru_RU'
    },
    'sheets': [{
        'properties': {
            'sheetType': 'GRID',
            'sheetId': 0,
            'title': 'Лист1',
            'gridProperties': DEFAULT_GRID_PROPERTIES
        }
    }]
}

TABLE_HEADER = [
    ['Отчет от', 'Топ проектов по скорости закрытия'],
    ['id проекта', 'Название проекта', 'Время сбора', 'Описание']
]


async def spreadsheets_create(wrapper_services: Aiogoogle, title_date: str = None) -> str:
    """Создание гугл таблицы."""
    now_date_time = title_date or datetime.now().strftime(FORMAT)
    spreadsheet_body = DEFAULT_SPREADSHEET_BODY.copy()
    spreadsheet_body['properties']['title'] = f'Отчет на {now_date_time}'

    service = await wrapper_services.discover('sheets', 'v4')

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    """Предоставление прав."""
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    """Запись данных в таблицу."""
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        ['Отчет от', now_date_time],
    ]
    table_values.extend(TABLE_HEADER)
    table_values.extend([
        list(map(str, [
            project[0],
            project[1],
            f'{(project[4] - project[3]).days} day(s)',
            project[2]
        ])) for project in projects
    ])

    num_rows = len(table_values)
    num_cols = len(table_values[0])

    update_range = f'A1:{chr(64 + num_cols)}{num_rows}'

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=update_range,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
