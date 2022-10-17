# # В этом файле расположим функцию для логирования в журнал событий линуха
# # для маленьких - команда
# # sudo journalctl -f
# from systemd import journal
#
#
# def Log(text: str):
#     """
#     Метод для того чтоб логировать journalctl все что нам надо
#     :param text:
#     :return:
#     """
#     api = "JSON-Backend "
#     err = api + ': ' + str(text)
#
#     # for LOG_ERR -> PRIORITY = 3
#     journal.send(err, PRIORITY=3)
#
#
# # =================================================================================================================
# #                               Класс Логгера
# # =================================================================================================================
# class Logger:
#     import os
#
#     _name = "JSON-Backend "
#     # os.path.basename(__file__).split('.')[0]
#     # _Error = None
#     # _Debug = None
#     # _Info = None
#     _log = None
#
#     # Логгер
#     def __init__(self, Name: str = ''):
#         """
#         Текущий файл
#         os.path.basename(__file__).split('.')[0]
#         :param Name:
#         """
#
#         # Сначала Делаем правильное имя
#         self._name = self._name + str(Name)
#         # И делаем в итоге логи
#         # # Ошибок
#         # self._Error = self._logger_error()
#         # # Дебажный
#         # self._Debug = self._logger_debug()
#         # # Инфо
#         # self._Info = self._logger_info()
#
#         # self._log = self._logger_create()
#
#         self._log = self._logger_create()
#
#     # def _logger_info(self):
#     #     import logging
#     #
#     #     # Делаем логирование - Уровень - Инфо
#     #     logging.basicConfig(level=logging.INFO)
#     #     # Задаем ему имя - По имени файла
#     #     logger = logging.getLogger(self._name)
#     #     # Не распрстраняем на родителей
#     #     logger.propagate = False
#     #     # Делаем обработчики - Пихаем в системный журнал все это
#     #     journald_handler = journal.JournalHandler(SYSLOG_IDENTIFIER=logger.name)
#     #     journald_handler.setLevel(logging.INFO)
#     #     logger.addHandler(journald_handler)
#     #
#     #     return logger
#     #
#     # def _logger_error(self):
#     #     import logging
#     #
#     #     # Делаем логирование - Уровень - Инфо
#     #     logging.basicConfig(level=logging.INFO)
#     #     # Задаем ему имя - По имени файла
#     #     logger = logging.getLogger(self._name)
#     #     # Не распрстраняем на родителей
#     #     logger.propagate = False
#     #     # Делаем обработчики - Пихаем в системный журнал все это
#     #     journald_handler = journal.JournalHandler(SYSLOG_IDENTIFIER=logger.name)
#     #     journald_handler.setLevel(logging.ERROR)
#     #     logger.addHandler(journald_handler)
#     #
#     #     return logger
#     #
#     # def _logger_debug(self):
#     #     import logging
#     #
#     #     # Делаем логирование - Уровень - Инфо
#     #     logging.basicConfig(level=logging.INFO)
#     #     # Задаем ему имя - По имени файла
#     #     logger = logging.getLogger(self._name)
#     #     # Не распрстраняем на родителей
#     #     logger.propagate = False
#     #     # Делаем обработчики - Пихаем в системный журнал все это
#     #     journald_handler = journal.JournalHandler(SYSLOG_IDENTIFIER=logger.name)
#     #     journald_handler.setLevel(logging.DEBUG)
#     #     logger.addHandler(journald_handler)
#     #
#     #     return logger
#     def _logger_create(self):
#
#         Loger = CreateLoger(self._name)
#         return Loger.get_logger()
#
#     # def _logger_create(self):
#     #     import logging
#     #     from logging import StreamHandler, Formatter
#     #     import sys
#     #
#     #     # Делаем логирование - Уровень - Инфо
#     #     logging.basicConfig(level=logging.DEBUG)
#     #     # Задаем ему имя - По имени файла
#     #     logger = logging.getLogger(self._name)
#     #     # Не распрстраняем на родителей
#     #     logger.propagate = False
#     #
#     #     # Делаем формат
#     #     # formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     #     formatter = Formatter(fmt='[ %(levelname)s ] - %(message)s')
#     #     # Делаем обработчики - Пихаем в системный журнал все это
#     #     journald_handler = journal.JournalHandler(SYSLOG_IDENTIFIER=logger.name)
#     #     journald_handler.setFormatter(formatter)
#     #     journald_handler.setLevel(logging.DEBUG)
#     #     logger.addHandler(journald_handler)
#     #
#     #
#     #     return logger
#
#     # Итак - Что теперь - Пробрасываем наверх методы для логирования
#
#     def INFO(self, text=''):
#         """Метод для логирования в лог Info """
#         from logging import INFO
#
#         # self._log = logger
#
#
#         self._log.setLevel(level=INFO)
#         Log(text="Уровень :  " + str('INFO'))
#
#         self._log.info(str(text))
#
#     def ERROR(self, text=''):
#         """Метод для логирования в лог Error """
#
#         from logging import ERROR
#
#         # self._log = logger
#
#         self._log.setLevel(level=ERROR)
#
#         Log(text="Уровень :  " + str('ERROR'))
#
#         self._log.error(str(text))
#
#     def DEBUG(self, text=''):
#         """Метод для логирования в лог Debug """
#         from logging import DEBUG
#
#         # self._log = logger
#
#         self._log.setLevel(level=DEBUG)
#
#         Log(text="Уровень :  " + str('DEBUG'))
#
#         self._log.debug(str(text))
#
#     def WARNING(self, text=''):
#         """Метод для логирования в лог Warning """
#
#         from logging import WARNING
#         # self._log = logger
#
#         self._log.setLevel(level=WARNING)
#
#         Log(text="Уровень :  " + str('WARNING'))
#         self._log.warning(str(text))
#
#     def CRITICAL(self, text=''):
#         """Метод для логирования в лог Critical """
#
#         from logging import CRITICAL
#         # self._log = logger
#
#         self._log.setLevel(level=CRITICAL)
#         Log(text="Уровень :  " + str('CRITICAL'))
#         self._log.critical(str(text))
#
#
#
#
# #
# #
# # Log_test = LoggerJournal(Name="LOL")
# # Log_test.ERROR('------------Это ЛОГ Ошибок 1--------------------')
# # Log_test.INFO('------------Это ЛОГ Инфо 1--------------------')
# # LoggerJournal(Name="LOL").DEBUG('------------Это ЛОГ ДЕБАГ 1--------------------')
# # Log_test.WARNING('------------Это ЛОГ WARNING 1--------------------')
# # Log_test.CRITICAL('------------Это ЛОГ CRITICAL 1--------------------')
# #
# #
# # Log(text="Запустили :  " + str(__file__)+" , Что у нас есть " + str(id(Log_test))  )
# #
# # Log_test.ERROR('------------Это ЛОГ Ошибок 2--------------------')
# # Log_test.INFO('------------Это ЛОГ Инфо 2--------------------')
# # LoggerJournal(Name="LOL").DEBUG('------------Это ЛОГ ДЕБАГ 2--------------------')
# # Log_test.WARNING('------------Это ЛОГ WARNING 2--------------------')
# # Log_test.CRITICAL('------------Это ЛОГ CRITICAL 2--------------------')
# #
# #
# # Log(text="Запустили :  " + str(__file__)+" , Что у нас есть " + str(id(Log_test))  )
# #
# # LoggerJournal(Name="LOL").ERROR('------------Это ЛОГ Ошибок 3--------------------')
# # Log(text="Запустили :  " + str(__file__)+" , Что у нас есть " + str(id(Log_test))  )
# #
# # LoggerJournal(Name="LOL").INFO('------------Это ЛОГ Инфо 3--------------------')
# # LoggerJournal(Name="LOL").DEBUG('------------Это ЛОГ ДЕБАГ 3 --------------------')
# # LoggerJournal(Name="LOL").WARNING('------------Это ЛОГ WARNING 3--------------------')
# # LoggerJournal(Name="LOL").CRITICAL('------------Это ЛОГ CRITICAL 3--------------------')
# #
