PREFIX = '/'

START_COMMAND = 'start'

HELLOW = '1'
ERROR_NAME  = ' Ошибка ввода. Введите полное имя!'
THANKS = '{}, {}'
REQUEST_PAY = {
    4: '3',
    2: '5',
    1: '9',
    0: '7'
}
PAY_KEY_TEXT = 'Оплатил'
PAY_OK = '4'

LIST_COMMAND = 'list'
UPDATE_COMMAND = 'edit'
SEND_COMMAND = 'send'
SEND_TEXT = 'Отправтье сообщение которое хотите разослать по всем пользователям.'
SEND_OK = 'Рассылка закончена!'
HELP = '/list - просмотра списка.\n/edit - для редакции.' 
ADMIN_TEXT = 'А кто же это??? - Это Админ.\n' + HELP
REG_TEXT = 'Пользователь {} зарегался. Дата следующего платежа - {}'
USER_KEY_TEXT = 'Пользователь'
USER_URL = 'tg://user?id={}'
UPDATE_DATE = 'Изменить дату'
UPDATE_KEY = 'update_'
UPDATE_TEXT = 'Текущая дата - {}. На какую хотите изменить?'
UPDATE_OK = 'Изменение сохранено.'
USER_UPDATE_TEXT = 'Ваша дата изменина на {}'
LIST_TEXT = 'Даты следующих платежей:'
CHOOSE_USER = 'Выберите пользователя:'
NO_USERS = 'Нет добавленных пользователей.'
EDIT_TEXT = 'Пользователь {}, дата следующего платежа - {}'
CHOOSE_KEY = 'choose_'
NEXT = 'Далее'
NEXT_CMD = 'next_'
BACK = 'Меню'
BACK_CMD = 'back_'
DELETE = 'Удалить'
DELETE_CMD = 'delete_'
DELETE_OK = 'Ползователь удален.'
ADMIN_PAY_OK = 'Проверьте оплату пользователя - {}'
ADMIN_PAY_NO = 'Пользователь {} не оплатил, отключай его нахер.'
ERROR = 'Ошибка'