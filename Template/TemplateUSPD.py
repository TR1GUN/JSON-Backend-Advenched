# ////////////////////////////////////////////////////////////////////////////////////////////
#                               класс шаблон - Самый базовый
# ///////////////////////////////////////////////////////////////////////////////////////////

class TemplateUSPD:

    """
    Самый базовый класс функционала

    Содержит - кодировка/раскодировка JSON

    Логирование
    """
    # Код результата
    result = ''
    # Ответ что даем
    response = None

    def _HTTP_status_codes(self, code):
        """
        Внутренний метод для быстрого получения статуса ответа
        :param code:
        :return:
        """
        from service_data import status_codes
        status = status_codes.get(code)

        # Проверяем на пустоту
        if status is None:
            # Если ничего не получсили то отбрасываем что не приемлемо
            status = status_codes.get(406)
            # и логируем ошибку
            self._LOG(text_log='Error search status code', logger_level='CRITICAL')

        return str(status)

    # Необходимость такая, что в классах необходимо создать логгер , посмотрим что из этого выйдет
    def _LOG(self, text_log: str, text_name: str = '', logger_level: str = 'DEBUG'):

        # Импортируем модуль логирования
        from LoggerJournal.Logger import Logger

        # чтоб не выстрелить себе в ногу - Переводим в стрингу
        text_log = str(text_log)
        # получаем имя класса в котором произошла ошибка
        name_class = str(self.__class__.__name__)
        text_name = name_class + " : " + str(text_name)
        # Логируем

        # Logger(Name=text_name).DEBUG(text=text_log)
        Log = Logger(Name=text_name)

        logger_level_name = \
            {
                # Логеры дебага
                'DEBUG': Log.DEBUG,
                # Логеры Ошибки
                'ERROR': Log.ERROR,
                # Логеры инфо
                'INFO': Log.INFO,
                # Логеры опасность
                'WARNING': Log.WARNING,
                # Логеры Выстрелили в ногу
                'CRITICAL': Log.CRITICAL,
            }

        # Ставим в верхний регистр
        logger_level = logger_level.upper()
        # Чтоб не стрелять себе в ногу - проверяем что есть такой уровень логирования
        if logger_level not in list(logger_level_name.keys()):
            logger_level = 'DEBUG'

        # Вытаскиваем нужный нам уровень логирования, и спусаем наше значение
        logger_level_name.get(logger_level)(text=text_log)
