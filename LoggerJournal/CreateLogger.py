# # Здесь расположим сам скрипт логгера
# # UPD : Необходим для того чтоб логи не дублировались
#
#
# _name = "JSON-Backend "
#
# import logging
# from logging import StreamHandler, Formatter
#
#
# # Делаем логирование - Уровень - Инфо
# logging.basicConfig(level=logging.DEBUG)
# # Задаем ему имя - По имени файла
# logger = logging.getLogger(_name)
# # Не распрстраняем на родителей
# logger.propagate = False
#
# # Делаем формат
# # formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter = Formatter(fmt='[ %(levelname)s ] - %(message)s')
# # Делаем обработчики - Пихаем в системный журнал все это
# journald_handler = journal.JournalHandler(SYSLOG_IDENTIFIER=logger.name)
# journald_handler.setFormatter(formatter)
# journald_handler.setLevel(logging.DEBUG)
# logger.addHandler(journald_handler)