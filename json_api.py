# from Template.Template_USPD_Linux import TemplateUSPD

#
# class MakeResponse(TemplateUSPD):
#     """
#     Это класс который позволяет сформировать ответ на наш запрос
#
#     Он является наследником от базового класса, чтоб было НОРМАЛЬНОЕ логирование
#     """
#     # Это сам Ответ
#     Response = None
#     # Это статус операции
#     Status_Code = None
#
#     # наш URI
#     URI = None
#     # наш Метод
#     METHOD = None
#     # наш протокол
#     PROTOCOL_USPD = None
#     # Версия нашего протокола
#     PROTOCOL_VERSION = None
#     # Контент
#     BODY = None
#     # Уровень ДОСТУПА
#     USER = None
#
#     def __init__(self, URI, METHOD, BODY, PROTOCOL_USPD, USER):
#         """
#         Класс который обрабатывает все запросы
#         """
#         # Обнуляем
#         # Ответ
#         self.Response = None
#         # Это статус операции
#         self.Status_Code = None
#         # наш URI
#         self.URI = None
#         # наш Метод
#         self.METHOD = None
#         # наш протокол
#         self.PROTOCOL_USPD = None
#         # Версия нашего протокола
#         self.PROTOCOL_VERSION = None
#         # Контент
#         self.BODY = None
#         # Уровень ДОСТУПА
#         self.USER = None
#
#         # Отлаживаемся
#         Debug_string = "Received :" + \
#                        "\nURI: " + str(URI) + \
#                        "\nMETHOD: " + str(METHOD) + \
#                        "\nPROTOCOL_USPD: " + str(PROTOCOL_USPD) + \
#                        "\nJSON: " + str(BODY) + \
#                        "\nUSER: " + str(USER)
#
#         self._LOG(text_log=Debug_string, logger_level="DEBUG")
#
#         # итак - Первое что делаем - ПОЛУЧАЕМ НУЖНЫЕ ПЕРЕМЕННЫЕ :
#         # URI запроса по которому будем определять наш функционал
#         self.URI = URI
#         # Метод запроса - необходим для корректной работы функционала
#         self.METHOD = METHOD
#         # наш JSON что отправляли
#         self.BODY = BODY
#
#         # Протокол УСПД по которому производиться вся работа
#         self.PROTOCOL_USPD = PROTOCOL_USPD
#         # Версия используемого протокола
#         # self.PROTOCOL_VERSION = PROTOCOL_VERSION
#
#         # Определяем права доступа
#         self.USER = USER
#         # Первое - Определяем протокол - Получаем
#         handlers = self._Definition_protocol()
#         # Второе - Вытаскиваем функцию функционала что нужна
#         handler = handlers.get(URI)
#         if handler:
#             # Запускаем наше приложение
#             self.Status_Code, self.Response = self._Setup_JSON_API(handler)
#         else:
#             self.Status_Code = "405 Method Not Allowed"
#             self.Response = "405 Method Not Allowed"
#
#     def _Definition_protocol(self):
#         """
#         Определяем протокол, по которому работаем
#         :return: Возвращаем список URL по которым работаем
#         """
#         from proto_USPD import define_protocol
#         handlers = define_protocol(protocol_USPD=self.PROTOCOL_USPD)
#         return handlers
#
#     def _Setup_JSON_API(self, handler):
#
#         """
#         Здесь запускаем функцию что отвечает за
#         :return:
#         """
#
#         try:
#             code, result = handler(method=self.METHOD, uri=self.URI, body=self.BODY, level_user=self.USER)
#         except Exception as e:
#             # Выбрасываем ошибку
#             error_string = "Error to setup JSON API. Exception :" + str(e)
#
#             self._LOG(text_log=error_string, logger_level="ERROR")
#             code = "500 Internal Server Error"
#             result = "500 Internal Server Error"
#
#         return code, result
#
#     def Result(self):
#         """
#         Отдаем статус операции
#         :return: код результата , Ответ
#         """
#         return self.Status_Code, self.Response


# ===================================================================================================================
#
# ===================================================================================================================
from LoggerJournal.Logger import Logger


def application_JSON(URI, METHOD, BODY, PROTOCOL_USPD, USER):
    """
    Приложение JSON
    :param URI:
    :param METHOD:
    :param BODY:
    :param PROTOCOL_USPD:
    :param USER:
    :return:
    """
    # Первое - Определяем протокол - Получаем
    from proto_USPD import define_protocol
    handlers = define_protocol(protocol_USPD=PROTOCOL_USPD)

    # Второе - Вытаскиваем функцию функционала что нужна
    handler = handlers.get(URI)
    if handler:
        # Запускаем функцию отвечающую за этот URL
        try:
            code, result = handler(method=METHOD, uri=URI, body=BODY, level_user=USER)
        except Exception as e:
            # Выбрасываем ошибку
            error_string = "Error to setup JSON API. Exception :" + str(e)

            Logger(Name=str(__name__)).ERROR(error_string)

            code = "500 Internal Server Error"
            result = "500 Internal Server Error"
    else:
        error_string = "Request url not allowed :" + "\nURI : " + str(URI) + "\nPROTOCOL_USPD : " + str(PROTOCOL_USPD)

        Logger(Name=str(__name__)).ERROR(error_string)

        code = "405 Method Not Allowed"
        result = "405 Method Not Allowed"

    return code, result
