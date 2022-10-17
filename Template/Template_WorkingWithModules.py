# --------------------------------------------------------------------------------------------------------------
# Класс шаблон работы с различными API
# --------------------------------------------------------------------------------------------------------------
from Template.Template_Working import TemplateWorking


class WorkingWithModules(TemplateWorking):
    """
    Основной класс-шаблон для работы JSON Backend c МОДУЛЯМИ Проекта - Это важно

    """

    # поле пути до нашей API что запускаем
    API = ''
    result = '102 Processing'
    response = None
    Table = None
    method = None

    def Setup_subprocess(self, JSON):
        """
        Данный метод запускает нужную API на железке и читает ответ на нее - Это важно
        :return: Возвращает результат запуска
        """

        # data = SetupSSH(JSON=JSON, API=self.API).answer_JSON
        # print('data', data)
        import subprocess
        #
        # Запускаем процесс
        # Очень важно - делаем это через TRY - возможно приложения и нет (например зарядные станции )
        try:
            process = subprocess.Popen(self.API, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process.stdin.write(str.encode(JSON))
            data, error = process.communicate()
        except Exception as e:
            # Если у нас произошла ошибка -  Логируем ее
            data_exception = {
                "exception": str(e),
                "error": "application is not found",
                "res": 1,
            }

            # Кодируем в дата чтоб вызвать нужную ошибку в валидации
            data = self.code_in_json(data_exception)
            # Логируем ошибку
            self._LOG(text_log=str(data_exception), logger_level='CRITICAL')

        # запускаем
        return data

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

    def Setup(self, json_dict: dict):
        """
        Метод запуска и валидации ошибок

        :param json_dict:
        :return:
        """
        # Логирование
        # ------------------------>
        text_log = str("JSON request for API :\nAPI :" + str(self.API) + "\nJSON:" + str(json_dict))
        self._LOG(text_log=text_log, logger_level="DEBUG")
        # ------------------------>

        if type(json_dict) is dict:
            # Проверяем На валидацию
            validation_in = self._Validation_JSON(JSON=json_dict, postfix="in")
            # Если все ок - отправляем
            if validation_in:
                # Упаковываем
                json = self.code_in_json(JSON=json_dict)
                # отправляем
                result = self.Setup_subprocess(JSON=json)
                # Декодируем
                result = self.decode_from_json(result)

        # Логирование
        # ------------------------>
                text_log = str("JSON answer from API :\nAPI :" + str(self.API) + "\nJSON:" + str(result))
                self._LOG(text_log=text_log, logger_level="DEBUG")
        # ------------------------>

                validation_out = self._Validation_JSON(JSON=result, postfix="out")
                if validation_out:
                    # Выполняем проверку
                    # если все хорошо

                    # Так - очень важный момент - если у нас флоат - то переводим в инт
                    if type(result.get("res")) is float:
                        result["res"] = int(result.get("res"))

                    if result.get("res") == 0:

                        self.result = '200 OK'
                        outdata = result

                    # Если произошла ошибка в самой АПИ
                    else:
                        self.result = '500 Internal Server Error'
                        outdata = self.result

                        # Логируем результат
                        error = 'Response in Error at work API, Check working API.' + "\n" + \
                                "====================RESPONSE====================" + "\n" + \
                                str(result) + '\n' + \
                                "==============================================="
                        self._LOG(text_log=error, logger_level="CRITICAL")

                # Валидация на выход - НЕУСПЕШНО
                else:
                    self.result = '423 Locked'
                    outdata = self.result

                    # Логируем результат
                    error = 'Response from API is not format API, Check format Response.' + "\n" + \
                            "====================RESPONSE====================" + "\n" + \
                            str(result) + '\n' + \
                            "==============================================="
                    self._LOG(text_log=error, logger_level="ERROR")

            # ВАЛИДАЦИЯ НА ВХОД - НЕУСПЕШНА
            else:
                self.result = '409 Conflict'
                outdata = self.result

                # Логируем результат
                error = 'Request JSON-Backend is not format API, Check format request.' + "\n" + \
                        "====================REQUEST====================" + "\n" + \
                        str(json_dict) + '\n' + \
                        "==============================================="
                self._LOG(text_log=error, logger_level="ERROR")

        # Если мы спустили не словарь
        else:

            # Выбрасываем ошибку взад  -400  Bad Request
            self.result = '400 Bad Request'
            outdata = self.result

            # Логируем результат
            error = 'Request is not dict, Check format request.' + "\n" + \
                    "====================REQUEST====================" + "\n" + \
                    str(json_dict) + '\n' + \
                    "==============================================="
            self._LOG(text_log=error, logger_level="ERROR")

        # # Теперь запоковываем это все в JSON
        # outdata = self.code_in_json(JSON=outdata)
        return outdata

    def _Validation_JSON(self, JSON, postfix):
        """
        Здесь проводим валидацию нашего JSON
        """

        # Поставим заглушку - что валидация точно успешна
        result = True
        # Здесь проводим валидацию нашего JSON
        # from check_json_schema import check
        #
        # result = check(JSON=JSON, request_type=self.method, postfix=postfix, API=self.API, table_name=self.Table)

        return result

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
    JSON_Method = \
        {
            "GET": _GET,
            "POST": _POST,
            "PUT": _PUT,
            "DELETE": _DELETE,
        }

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
