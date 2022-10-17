# from json_api import application_JSON
from LoggerJournal.Logger import Logger
from MakeResponse import SessionsUSPD


# Создадим лист кук
# Cookies_dict = {}

#
# # Проверка - Поддерживается ли метод или нет
# def check_method(method):
#     """
#     Здесь смотрим - Поддерживается ли вообще этот метод
#     :param method:
#     :return:
#     """
#
#     support_method = ["GET", "POST", "PUT", "DELETE"]
#
#     if method in support_method:
#         return True
#     else:
#         return False
#

# Определение длины контента
def define_content_length(CONTENT_LENGTH):
    """
    Определение длины контента - Если нет ничего - ставим 0
    :param CONTENT_LENGTH:
    :return:
    """
    # Очень важный момент - если у нас пустая строка или None ставим 0
    if CONTENT_LENGTH == '':
        CONTENT_LENGTH = 0

    # Теперь надо быть аккуратнее - переводим в int
    try:
        # Пытаемся преобразовать в int
        body_size = int(CONTENT_LENGTH)
        # ---->> Отладка ---->>
        # Logger(Name='Читаем контент CONTENT_LENGTH : ').INFO(str(CONTENT_LENGTH))
        # Logger(Name='type  CONTENT_LENGTH : ').INFO(str(type(CONTENT_LENGTH)))
        # ---->># ---->> ---->>

    except Exception as e:
        body_size = 0
        # Логируем ошибку ---->
        Logger(Name=str(__name__)).ERROR("Exception " + str(e) + ", body_size = 0")

    return body_size


#
# # Здесь делаем новые куки для того чтоб просто были
# def CreateCookie():
#     """
#     Здесь делаем новые куки для того чтоб просто были
#     """
#     from http import cookies
#     from datetime import datetime
#     from random import randint
#
#     Cookie_Value = cookies.SimpleCookie()
#
#     # айди сессии - Unixtime + рандомно сгенерированное число int32
#     sessionid = str(int(datetime.now().timestamp())) + str(int(randint(1000000000, 9999999999)))
#
#     # Делаем нашу куку
#     Cookie_Value["sessionid"] = sessionid
#
#     # Убираем хедлер
#     Cookie_Value = Cookie_Value.output(header="")
#     # Убираем все пробелы
#     Cookie_Value = Cookie_Value.replace(" ", '')
#     return Cookie_Value
#
#
# # Протухание кукис
# def CookieCheck(Cookies):
#     # ОЧИЩАЕМ ВСЕ ПРОТУХШИЕ КУКИ
#
#     if Cookies and (Cookies in Cookies_dict):
#         try:
#             Cookies_UNIXTIME = int(Cookies[10:-10])
#             from datetime import datetime
#             UNIXTIME = int(datetime.now().timestamp())
#             if UNIXTIME - Cookies_UNIXTIME > 30 * 60:
#                 Cookies_dict.pop(Cookies)
#                 return False
#             else:
#                 return True
#         except Exception as e:
#             error = "BAD COOKIES " + str(Cookies) + "to UNIXTIME" + str(Cookies[10:-10]) + ", exception :" + str(e)
#             Logger(Name=str(__name__)).ERROR(str(error))
#             Cookies_dict.pop(Cookies)
#             return False
#     else:
#         return False
#
#

Sessions = SessionsUSPD()


# ТОЧКА ВХОДА В BACKEND
def application(env, start_response):
    # ---->> Отладка ---->>

    Logger().DEBUG("Cookies :" + str(Sessions.Session_Cookies_dict))
    # Logger().DEBUG("Cookies :"+str(Cookies_dict))
    Logger().DEBUG("Запустили :\n   "
                   "env " + str(env) +
                   " \nstart_response : " + str(start_response))
    # -------------------------------------------------------
    # итак - Первое что делаем - ПОЛУЧАЕМ НУЖНЫЕ ПЕРЕМЕННЫЕ :
    # URI запроса по которому будем определять наш функционал
    uri = env.get('PATH_INFO')
    # Метод запроса - необходим для корректной работы функционала
    method = env.get('REQUEST_METHOD')
    # Протокол УСПД по которому производиться вся работа
    protocol_USPD = env.get('HTTP_X_PROTOCOL_USPD')
    # Версия используемого протокола
    # protocol_versions = env.get('HTTP_X_PROTOCOL_VERSION')
    # Куки - Это важно
    Cookies = env.get('HTTP_COOKIE', "")
    # Высчитываем длину контента
    content_length = env.get('CONTENT_LENGTH', 0)

    # --------->
    # Читаем размер буфера
    body_size = define_content_length(CONTENT_LENGTH=content_length)
    # Читаем прилетающий JSON :
    body = env['wsgi.input'].read(body_size)
    # Обрабатываем пустой  body
    if body == b'':
        body = None
    state, data, Content = Sessions.Make_Response(URI=uri, METHOD=method, BODY=body, PROTOCOL_USPD=protocol_USPD,
                                                  COOKIE=Cookies)

    # ----------->
    # # Первое - Определяем протокол - Получаем
    # handlers = proto_USPD.define_protocol(protocol_USPD=protocol_USPD)
    # # Второе - Вытаскиваем функцию функционала что нужна
    # handler = handlers.get(uri)

    # # Прежде чем вычитывать надо определиться - Поддерживается ли этот метод
    # if not check_method(method):
    #     Logger().ERROR("405 : Method Not Allowed")
    #     # Возвращаем ошибку
    #     state = "405 Method Not Allowed"
    #     data = "405 Method Not Allowed"
    #     Content = [('Content-Type', '"text/html"')]
    # else:
    #     # Читаем размер буфера
    #     body_size = define_content_length(CONTENT_LENGTH=content_length)
    #     # Читаем прилетающий JSON :
    #     body = env['wsgi.input'].read(body_size)
    #     # Обрабатываем пустой  body
    #     if body == b'':
    #         body = None
    #
    #     # ---->> Отладка ---->>
    #     Logger().DEBUG("Полученные Данные : " +
    #                    '\nPATH_INFO : ' + str(uri) +
    #                    '\nREQUEST_METHOD : ' + str(method) +
    #                    '\nCONTENT_LENGTH : ' + str(body_size) +
    #                    '\nBody : ' + str(body) +
    #                    '\nCookies : ' + str(Cookies))
    #     # ---->># ---->> ---->>
    #     # Если у нас авторизация - То выдаем новые куки
    #     if uri == "/auth":
    #         # Сначала проводим авторизацию
    #         try:
    #             # Здесь запускаем нашу исполняемую функцию
    #             state, user = application_JSON(URI=uri, METHOD=method, BODY=body, PROTOCOL_USPD=protocol_USPD, USER=0)
    #             # ЕСЛИ УСПЕШНО - создаем куки
    #             debug_string = "state : " + str(state) + "user" + str(user)
    #             Logger().DEBUG(debug_string)
    #             if state == "200 OK":
    #                 # Создаем куку
    #                 Cookie_Value = CreateCookie()
    #                 # Формируем ответ
    #                 Content = [('Content-Type', 'text/html'), ("Set-Cookie", str(Cookie_Value))]
    #                 # И добавляем куки в наш лист кук
    #                 Cookies_dict[Cookie_Value] = user
    #                 data = "200 OK"
    #             else:
    #                 # state = "403 Forbidden"
    #                 data = state
    #                 Content = [('Content-Type', 'text/html')]
    #
    #         except Exception as e:
    #
    #             # Логируем ошибку ---->
    #             Logger(Name=str(__name__)).ERROR("except Error" + str(e) + "\nreturn  ")
    #             state = "400 Bad Request"
    #             data = "400 Bad Request"
    #             Content = [('Content-Type', 'text/html')]
    #
    #     # Иначе - Проверяем наличие кук
    #     else:
    #         # Если у нас  куки есть проверяем на протухание их
    #         # КУКИ есть
    #         if CookieCheck(Cookies):
    #             user = Cookies_dict.get(Cookies, 0)
    #             # если у нас разлогирование - очищаем его
    #             if uri == "/logoff":
    #
    #                 # Здесь запускаем нашу исполняемую функцию
    #                 state, data = application_JSON(URI=uri, METHOD=method, BODY=body, PROTOCOL_USPD=protocol_USPD, USER=user)
    #
    #                 # И удаляем из нашего листа кук куки если они есть
    #                 Cookies_dict.pop(Cookies)
    #                 # И заодно все протухшие куки
    #                 for cookie in Cookies_dict:
    #                     CookieCheck(cookie)
    #                 data = "200 OK"
    #                 Content = [('Content-Type', 'text/html')]
    #
    #             # Если у нас не авторизация - то переиспользуем старые
    #             else:
    #                 try:
    #                     # Здесь запускаем нашу исполняемую функцию
    #                     state, data = application_JSON(URI=uri, METHOD=method, BODY=body, PROTOCOL_USPD=protocol_USPD, USER=user)
    #                     # Переводим в строку наше состояние - Это важно
    #                     state = str(state)
    #                     Content = [('Content-Type', 'application/json'), ("Set-Cookie", str(Cookies))]
    #
    #                 except Exception as e:
    #                     state = "500 Internal Server Error"
    #                     data = "500 Internal Server Error"
    #                     error = "Error Server .Exception :" + str(e)
    #                     Logger(Name=str(__name__)).ERROR(str(error))
    #
    #                 Content = [('Content-Type', 'application/json'), ("Set-Cookie", str(Cookies))]
    #
    #         # ЕСли нет кук - то говорим что надо авторизоваться
    #         else:
    #             state = "401 Unauthorized"
    #             data = "401 Unauthorized"
    #             Content = [('Content-Type', 'text/html')]

    # Теперь пытаемся отправить ответ
    try:

        # Делаем ответ
        # Теперь проверяем корректность типов
        from service_data import status_codes
        if type(state) is not str:
            state = status_codes.get(state, str(state))

        start_response(state, Content)

        # ---->> Отладка ---->>
        Logger().DEBUG(
            "Информация что отдаем : \n" +
            '\nstate : ' + str(state) +
            '\ndata : ' + str(data) +
            '\nContent : ' + str(Content)
        )
        # ---->># ---->> ---->>

        return [str.encode(str(data))]
    # except UnboundLocalError:
    except Exception as e:
        start_response('404 Not Found', [('Content-Type', 'text/html')])

        # Логируем ошибку ---->
        Logger(Name=str(__name__)).ERROR("except Error" + str(e) + "\nreturn  ")

        return [b'ERROR']
# ------------------------------------------------------------------------------------------------------------------
#                                  ПРИМЕР ЗАПРОСА в дебаг режиме
# ------------------------------------------------------------------------------------------------------------------
# start_response  = '<built-in function uwsgi_spit>' env = {'QUERY_STRING': '', 'REQUEST_METHOD': 'GET',
# 'CONTENT_TYPE': '', 'CONTENT_LENGTH': '', 'REQUEST_URI': '/settings/meter/table', 'PATH_INFO':
# '/settings/meter/table', 'DOCUMENT_ROOT': '/usr/share/nginx/html', 'SERVER_PROTOCOL': 'HTTP/1.1', 'REQUEST_SCHEME':
# 'http', 'REMOTE_ADDR': '192.168.202.146', 'REMOTE_PORT': '52668', 'SERVER_PORT': '80', 'SERVER_NAME': '',
# 'HTTP_HOST': '192.168.202.143', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0;
# Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#
# 'HTTP_ACCEPT': '*/*', 'HTTP_REFERER': 'http://192.168.202.143/meter_table.html?',
# 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_ACCEPT_LANGUAGE': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# 'wsgi.input': '<uwsgi._Input object at 0xb5e8bc90>',
# 'wsgi.file_wrapper': '<built-in function uwsgi_sendfile>', 'wsgi.version': (1, 0),
# 'wsgi.errors': '<_io.TextIOWrapper name=2 mode=\'w\' encoding=\'UTF-8\'>', 'wsgi.run_once': False,
# 'wsgi.multithread': False, 'wsgi.multiprocess': True, 'wsgi.url_scheme': 'http',
# 'uwsgi.version': b'2.0.19.1', 'uwsgi.node': b'NanoPi-NEO-Core'}
#
# application(env = env, start_response =start_response )
