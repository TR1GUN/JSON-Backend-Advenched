# from LoggerJournal.CreateLogger import logger , _name

from service_config import debug_mode
# =================================================================================================================
#                               Класс Логгера
# =================================================================================================================
class Logger:
    import os

    _name = "JSON-Backend "
    # os.path.basename(__file__).split('.')[0]
    # _Error = None
    # _Debug = None
    # _Info = None
    _log = None

    # Логгер
    def __init__(self, Name: str = ''):
        """
        Текущий файл
        os.path.basename(__file__).split('.')[0]
        :param Name:
        """

        # Сначала Делаем правильное имя
        self._name = self._name + str(Name)

        self._name = str(Name)
    # Итак - Что теперь - Пробрасываем наверх методы для логирования

    def INFO(self, text=''):
        """Метод для логирования в лог Info """
        if debug_mode :
            # from logging import INFO
            #
            # self._log = logger
            #
            # self._log.setLevel(level = INFO)
            # Log(text="Уровень :  " + str('INFO'))
            text = "["+ self._name + "] : " + text


            print(str(text))

    def ERROR(self, text=''):
        """Метод для логирования в лог Error """

        # from logging import ERROR
        #
        # self._log = logger
        #
        # self._log.setLevel(level=ERROR)

        # Log(text="Уровень :  " + str('ERROR'))
        text = "[" + self._name + "] : " + text
        print(str(text))

    def DEBUG(self, text=''):
        """Метод для логирования в лог Debug """
        if debug_mode:
            from logging import DEBUG

            # self._log = logger
            # self._log.setLevel(level=DEBUG)

            # Log(text="Уровень :  " + str('DEBUG'))
            text = "[" + self._name + "] : " + text
            # self._log.debug(str(text))
            print(str(text))

    def WARNING(self, text=''):
        """Метод для логирования в лог Warning """

        # from logging import WARNING
        # self._log = logger
        #
        # self._log.setLevel(level=WARNING)

        # Log(text="Уровень :  " + str('WARNING'))
        text = "[" + self._name + "] : " + text
        # self._log.warning(str(text))
        print(str(text))


    def CRITICAL(self, text=''):
        """Метод для логирования в лог Critical """

        # from logging import CRITICAL
        # self._log = logger
        #
        # self._log.setLevel(level=CRITICAL)
        # Log(text="Уровень :  " + str('CRITICAL'))
        text = "[" + self._name + "] : " + text

        # self._log.critical(str(text))
        print(str(text))