# --------------------------------------------------------------------------------------------------------------
#                   Класс шаблон работы с различными API для внутреннего Пользования
#                     Работает точно так же как WorkingWithModules, но отдает не в JSON а в dict
#                      От него наследуемся когда нужен не прямой запуск API
# --------------------------------------------------------------------------------------------------------------


from Template.Template_WorkingWithModules import WorkingWithModules


class WorkingWithAPI(WorkingWithModules):
    """
    Здесь опишем класс который работает с различными API для внутреннего Пользования

    """

    def _POST(self):
        """
        Выполнение метода POST
        :param JSON:
        :return:
        """
        self.result = 501
        result = self._HTTP_status_codes(self.result)

        return result

    def _GET(self):
        """
        Выполнение метода GET
        :param JSON:
        :return:
        """

        self.result = 501
        result = self._HTTP_status_codes(self.result)

        return result

    def _PUT(self):
        """
        Выполнение метода PUT
        :param JSON:
        :return:
        """
        self.result = 501
        result = self._HTTP_status_codes(self.result)
        return result

    def _DELETE(self):
        """
        Выполнение метода DELETE
        :param JSON:
        :return:
        """
        self.result = 501
        result = self._HTTP_status_codes(self.result)
        return result

    # ======================================================>

    # А теперь переопределяем метод отдачи результата для того чтоб не отдавать в JSON
    def get_Result(self):
        """
        Метод для получения данных
        Возвращает : Результат запроса и ответ
        :return:
        """

        # Проверяем что отдаем - все должно отдаваться в str

        # Если используем int то расшифровываем код ошибки
        if type(self.result) is int:
            self.result = self._HTTP_status_codes(self.result)
        # Теперь проверяем
        if type(self.result) is not str:
            self.result = str(self.result)

        # сам ответ проверяем на словарь - и если нужно - кодируем
        # if type(self.response) is not dict:
        #     self.response = self.decode_from_json(JSON=self.response)

        return self.result, self.response

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
    JSON_Method = \
        {
            "GET": _GET,
            "POST": _POST,
            "PUT": _PUT,
            "DELETE": _DELETE,
        }