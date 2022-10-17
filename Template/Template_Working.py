# --------------------------------------------------------------------------------------------------------------
# класс- шаблон работы всех остальных классов работы backend
# --------------------------------------------------------------------------------------------------------------
from Template.TemplateUSPD import TemplateUSPD


class TemplateWorking(TemplateUSPD):
    """
    класс- шаблон работы всех остальных классов работы backend

    Выдача результата
    """

    # поле пути до нашей API что запускаем
    API = ''

    # Код результата
    result = ''
    # Ответ что даем
    response = None
    method = None

    def _POST(self):
        """
        Выполнение метода POST
        :param JSON:
        :return:
        """

        # Ставим ответ - BRUH , Не реализованно
        self.result = 501
        result = self._HTTP_status_codes(self.result)

        return result

    def _GET(self):
        """
        Выполнение метода GET
        :param JSON:
        :return:
        """
        # Ставим ответ - BRUH , Не реализованно
        self.result = 501
        result = self._HTTP_status_codes(self.result)

        return result

    def _PUT(self):
        """
        Выполнение метода PUT
        :param JSON:
        :return:
        """
        # Ставим ответ - BRUH , Не реализованно
        self.result = 501
        result = self._HTTP_status_codes(self.result)
        return result

    def _DELETE(self):
        """
        Выполнение метода DELETE
        :param JSON:
        :return:
        """
        # Ставим ответ - BRUH , Не реализованно
        self.result = 501
        result = self._HTTP_status_codes(self.result)
        return result

    # def get_Result(self):
    #     """
    #     Метод для получения данных
    #     Возвращает : Результат запроса и ответ
    #     :return:
    #     """
    #
    #     return self.result, self.response

    def code_in_json(self, JSON):
        """
        Метод для конвертации нашего словаря в JSON

        :param JSON:
        :return:
        """
        import json
        # UPD : сделаем проверку - кодируем только в том случае если получаем словарь
        if type(JSON) is dict:
            outdata = json.dumps(JSON)
        else:
            try:
                outdata = JSON

            except  Exception as e:
                # Логируем ошибку
                self._LOG(text_log="code error , Exception :" + str(e), logger_level="ERROR")
                outdata = {}

        return outdata

    def decode_from_json(self, JSON):
        """
        Метод для обвертки нашего JSON в словарь

        :param JSON:
        :return:
        """
        import json
        # UPD : сделаем проверку - если объекта не существует (None , b'' ) то возвращаем пустой словарь

        if JSON:
            if type(JSON) is dict:
                outdata = JSON
            else:
                try:
                    outdata = json.loads(JSON)
                except Exception as e:
                    # Логируем ошибку
                    self._LOG(text_log="decode error , Exception :" + str(e), logger_level="ERROR")
                    outdata = {}
        else:
            outdata = {}

        return outdata

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
        if type(self.response) is dict:
            self.response = self.code_in_json(JSON=self.response)

        if type(self.response) is not str:
            self.response = str(self.response)

        return self.result, self.response
