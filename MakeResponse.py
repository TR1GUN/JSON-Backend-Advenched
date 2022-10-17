from Template.Template_USPD_Linux import TemplateUSPD


# Класс который содерд

class SessionsUSPD(TemplateUSPD):
    """
    Класс который определяет Сессии к УСПД
    Каждое соединение к УСПД = Сессия

    ОЧЕНЬ ВАЖНЫЙ КЛАСС - так как реализует механизм авторизации
    """

    # Создаем тут бланк куков
    Session_Cookies_dict = {}

    # Поддержанные методы
    support_method = ["GET", "POST", "PUT", "DELETE"]
    # Контент что отдаем

    # Код состояния

    # Ответ сервера

    Content_type = {
        "HTTP_HTML": "text/html",
        "HTTP_JAVASCRIPT": "application/javascript",
        "HTTP_JSON": "application/json",
        "HTTP_CSS": "text/css",
        "HTTP_ICO": "image/x-icon",
        "HTTP_SVG": "image/svg+xml"}

    def __init__(self):
        """
        В этом классе представлен контроль сессий к УСПД
        Все сессии сделаны за счет Cookies
        """

    # Здесь делаем новые куки для того чтоб просто были
    def _CreateCookie(self):
        """
        Здесь делаем новые куки
        """
        from http import cookies
        from datetime import datetime
        from random import randint

        Cookie_Value = cookies.SimpleCookie()
        # Cookie_Value = cookiejar.CookieJar()

        # айди сессии - Unixtime + рандомно сгенерированное число int32
        sessionid = str(int(datetime.now().timestamp())) + str(int(randint(1000000000, 9999999999)))

        # Делаем нашу куку
        Cookie_Value["sessionid"] = sessionid
        # Убираем хедлер
        Cookie_Value = Cookie_Value.output(header="")
        # Убираем все пробелы
        Cookie_Value = Cookie_Value.replace(" ", '')
        return Cookie_Value

    # Здесь нормализуем куки
    def _Define_Cookie(self, cookie: str) -> list:
        """
        Здесь нормализуем Cookies
        :param cookie:
        :return:
        """
        # Удаляем все пробелы
        if type(cookie) is str:
            cookie = cookie.replace(" ", '')
            from re import findall
            # Паттерн парсинга
            patern_cookie = '(sessionid=\\d{20})'
            # Получаем значение нашей скорости
            cookie_list = findall(patern_cookie, cookie)
        else:
            cookie_list = []
        return cookie_list

    # Протухание кукис
    def _CookieCheck(self, Cookies):
        """
        ОЧИЩАЕМ ВСЕ ПРОТУХШИЕ КУКИ
        :param Cookies:
        :return:
        """
        # ОЧИЩАЕМ ВСЕ ПРОТУХШИЕ КУКИ

        if Cookies and (Cookies in self.Session_Cookies_dict):
            try:
                Cookies_UNIXTIME = int(Cookies[10:-10])
                from datetime import datetime
                UNIXTIME = int(datetime.now().timestamp())
                if UNIXTIME - Cookies_UNIXTIME > 30 * 60:
                    self.Session_Cookies_dict.pop(Cookies)
                    return False
                else:
                    return True
            except Exception as e:
                error = "BAD COOKIES " + str(Cookies) + "to UNIXTIME" + str(Cookies[10:-10]) + ", exception :" + str(e)
                self._LOG(text_log=error, logger_level="ERROR")
                self.Session_Cookies_dict.pop(Cookies)
                return False
        else:
            return False

    def _Get_Cookies_Request(self, COOKIE) -> list:
        """
        Определяем лист КОРЕКТНЫХ КУКИС
        :param COOKIE:
        :return:
        """
        # Лист с ХОРОШИМИ КУКАМИ
        Cookies_normal = []
        # 1. ОНИ ДОЛЖНЫ БЫТЬ НЕ ПРОХУЩИМИ
        # 2. ОНИ ДОЛЖНЫ БЫТЬ КОРЕКТНЫМИ
        # Удаляем протухшие куки
        self._Delete_Invalid_Cookies()
        # Нормализуем наши куки
        Cookies_list = self._Define_Cookie(COOKIE)

        # Теперь перебираем все куки на валидность

        for cookie in Cookies_list:
            # Если они валидны - добавляем в наш список
            if self._CookieCheck(cookie):
                Cookies_normal.append(cookie)
        # Если у нас вообще остались куки

        return Cookies_normal

    def _Delete_Invalid_Cookies(self):
        """
        Здесь удаляем протухшие куки
        :return:
        """
        for cookie in self.Session_Cookies_dict:
            self._CookieCheck(cookie)

    def Make_Response(self, URI, METHOD, BODY, PROTOCOL_USPD, COOKIE):
        """
        ОСНОВНОЙ МЕТОД ДЛЯ ТОГО ЧТОБ СДЕЛАТЬ ОТВЕТ
        :param COOKIE: Куки запроса
        :param URI: Получаемый URI сессии
        :param METHOD: НАШ метод запроса
        :param BODY: Тело запроса
        :param PROTOCOL_USPD: Протокол взаимодействия УСПД
        :return:
        """
        # Определяем что метод у нас - подходит - Если да - то отправляем дальше
        if METHOD in self.support_method:

            code, data, Content = self._define_type_session(URI=URI, METHOD=METHOD, BODY=BODY,
                                                            PROTOCOL_USPD=PROTOCOL_USPD, COOKIE=COOKIE)
        # Если нет - то так и говорим - метод не поддерживаетья
        else:

            error = "Method Not Allowed. Request method : " + str(METHOD) + " . URI : " + str(URI)
            self._LOG(text_log=error, logger_level="ERROR")
            # Возвращаем ошибку
            code = self._HTTP_status_codes(405)
            data = self._HTTP_status_codes(405)
            Content = [('Content-Type', self.Content_type.get("HTTP_HTML"))]

        return code, data, Content

    def _define_type_session(self, URI, METHOD, BODY, PROTOCOL_USPD, COOKIE):
        """
        Здесь происходит определение типа сессии - ЭТО ВАЖНО
        :param URI:
        :param METHOD:
        :param BODY:
        :param PROTOCOL_USPD:
        :param COOKIE:
        :return:
        """
        # Здесь все просто нам необходимо достать куки и определить -
        # ЭТО ПРОДОЛЖЕНИЕ КАКОЙ ТО СЕССИИ или это создание новой сессии
        # Если у нас авторизация - ТО неважно что у нас в куках - мы просто создаем новую сессию
        if URI == "/auth":
            code, data, Content = self._Create_sessions(URI=URI, METHOD=METHOD, BODY=BODY, PROTOCOL_USPD=PROTOCOL_USPD)
        elif URI == "/main_index":
            # Здесь формируем запрос - Если нет валидных кук - выбрасываем страницу логина , если они есть отдаем мэйн
            code, data, Content = self._Define_main(URI=URI, METHOD=METHOD, BODY=BODY, COOKIE=COOKIE)

        # КУКИ есть
        else:
            code, data, Content = self._Continue_sessions(URI=URI, METHOD=METHOD, BODY=BODY,
                                                          PROTOCOL_USPD=PROTOCOL_USPD, COOKIE=COOKIE)

        return code, data, Content

    def _Define_main(self, URI, METHOD, BODY, COOKIE):
        """

        :param URI:
        :param METHOD:
        :param BODY:
        :param COOKIE:
        :return:
        """
        # Итак - шо делаем - проверяем наличие кук в запросе
        Cookies_normal = self._Get_Cookies_Request(COOKIE=COOKIE)

        # если у нас есть валидные куки - то отправляем мэйн
        if Cookies_normal:
            code = self._HTTP_status_codes(200)
            data = self._HTTP_status_codes(200)
            Content = [('Content-Type', self.Content_type.get("HTTP_HTML"))]
        # Иначе выбрасываем страницу логином
        else:
            code = self._HTTP_status_codes(401)
            data = self._HTTP_status_codes(401)
            Content = [('Content-Type', self.Content_type.get("HTTP_HTML"))]

        return code, data, Content

    def _Create_sessions(self, URI, METHOD, BODY, PROTOCOL_USPD):
        """
        Создание НОВОЙ сессии
        :param URI:
        :param METHOD:
        :param BODY:
        :param PROTOCOL_USPD:
        :param PROTOCOL_USPD:
        :return:
        """
        # Здесь запускаем нашу исполняемую функцию
        code, user = self._Setup_JSON_API(URI=URI, METHOD=METHOD, BODY=BODY, PROTOCOL_USPD=PROTOCOL_USPD, USER=0)
        # ЕСЛИ УСПЕШНО - создаем куки
        # debug_string = "state : " + str(code) + "user : " + str(user)
        # self._LOG(text_log=debug_string)
        if code == "200 OK":
            # Создаем куку
            Cookie_Value = self._CreateCookie()
            # Формируем ответ
            Content = [('Content-Type', self.Content_type.get("HTTP_HTML")), ("Set-Cookie", str(Cookie_Value))]
            # И добавляем куки в наш лист кук
            self.Session_Cookies_dict[Cookie_Value] = user
            data = "200 OK"
        else:

            data = code
            Content = [('Content-Type', self.Content_type.get("HTTP_HTML"))]
        return code, data, Content

    def _Continue_sessions(self, URI, METHOD, BODY, PROTOCOL_USPD, COOKIE):
        """
        Продолжение уже существующей сессии
        :param URI:
        :param METHOD:
        :param BODY:
        :param PROTOCOL_USPD:
        :param COOKIE:
        :return:
        """
        # 1. ОНИ ДОЛЖНЫ БЫТЬ НЕ ПРОХУЩИМИ
        # 2. ОНИ ДОЛЖНЫ БЫТЬ КОРЕКТНЫМИ
        # Удаляем протухшие куки
        self._Delete_Invalid_Cookies()
        # Нормализуем наши куки
        Cookies_list = self._Define_Cookie(COOKIE)

        # Теперь перебираем все куки на валидность
        Cookies_normal = []
        for cookie in Cookies_list:
            # Если они валидны - добавляем в наш список
            if self._CookieCheck(cookie):
                Cookies_normal.append(cookie)
        # Если у нас вообще остались куки
        if Cookies_normal:
            # ТЕПЕРЬ - БЕРЕМ ПОСЛЕДНИЕ корректные куки
            Cookie = Cookies_normal.pop()
            USER = self.Session_Cookies_dict.get(Cookie, 0)
            # если у нас разлогирование - очищаем его
            if URI == "/logoff":

                code, data, Content = self._Sessions_Response(URI=URI,
                                                              METHOD=METHOD,
                                                              BODY=BODY,
                                                              PROTOCOL_USPD=PROTOCOL_USPD,
                                                              USER=USER)
                # И удаляем из нашего листа кук куки если они есть
                self.Session_Cookies_dict.pop(Cookie)
                # И заодно все протухшие куки
                self._Delete_Invalid_Cookies()

                Content = [('Content-Type', self.Content_type.get("HTTP_HTML"))]

            # Если у нас не авторизация - то переиспользуем старые
            else:
                code, data, Content = self._Sessions_Response(URI=URI,
                                                              METHOD=METHOD,
                                                              BODY=BODY,
                                                              PROTOCOL_USPD=PROTOCOL_USPD,
                                                              USER=USER)

        # ЕСли нет кук - то говорим что надо авторизоваться
        else:
            code = "401 Unauthorized"
            data = "401 Unauthorized"
            Content = [('Content-Type', self.Content_type.get("HTTP_HTML"))]

        return code, data, Content

    def _Sessions_Response(self, URI, METHOD, BODY, PROTOCOL_USPD, USER):
        """
        Продолжение сессии - получение ответа JSON
        :param URI:
        :param METHOD:
        :param BODY:
        :param PROTOCOL_USPD:
        :param USER:
        :return:
        """
        try:
            # Здесь запускаем нашу исполняемую функцию
            code, data = self._Setup_JSON_API(URI=URI, METHOD=METHOD, BODY=BODY, PROTOCOL_USPD=PROTOCOL_USPD, USER=USER)

            # Переводим в строку наше состояние - Это важно
            Content = [('Content-Type', self.Content_type.get("HTTP_JSON"))]

        except Exception as e:
            code = "500 Internal Server Error"
            data = "500 Internal Server Error"
            error = "Error Server .Exception :" + str(e)
            self._LOG(text_log=error, logger_level="ERROR")

            Content = [('Content-Type', self.Content_type.get("HTTP_JSON"))]

        return code, data, Content

    def _Setup_JSON_API(self, URI, METHOD, BODY, PROTOCOL_USPD, USER):
        """
        Здесь получаем основной ответ от бэка
        :param URI:
        :param METHOD:
        :param BODY:
        :param PROTOCOL_USPD:
        :param USER:
        :return:
        """

        # Здесь запускаем нашу исполняемую функцию

        try:
            from json_api import application_JSON
            state, data = application_JSON(URI=URI, METHOD=METHOD, BODY=BODY, PROTOCOL_USPD=PROTOCOL_USPD,
                                           USER=USER)
        except Exception as e:
            state = "500 Internal Server Error"
            data = "500 Internal Server Error"
            error = "Error setup JSON API. Exception: " + str(e)
            self._LOG(logger_level="ERROR", text_log=error)
        return state, data
