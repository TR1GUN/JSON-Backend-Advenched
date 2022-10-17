# Класс работы с установленной таблицей
from Template.Template_WorkingWithModules import WorkingWithModules


class WorkWithTable(WorkingWithModules):
    """
    Класс для работы с Установленной
    """
    # Путь до API
    API = None

    # Таблица
    Table = None
    # Сам Запрос
    request = {}
    # Ответ на него
    response = ""
    body = None
    data_tag = None

    def __init__(self, method, uri, body, table_name, func_name, db_api_path, data_tag='settings'):

        # Переопределяем обязательные переменные

        # имя таблицы
        self.Table = table_name
        # Путь до Апи
        self.API = db_api_path

        self.data_tag = data_tag
        # Стандартный конструктор
        # делаем пустой ответ
        self.response = ""
        # Результат делаем что идет процесс
        self.result = '102 Processing'
        # сначала формируем таблицу запроса
        self.request = {"table": self.Table}
        # Читаем Сам запрос
        self.body = body
        # Отправляем запрос - Получаем ответ
        self.response = self.JSON_Method.get(method)(self)

    def _GET(self):
        """
        Выполнение метода GET
        :return:
        """

        # Формируем заголовочный JSON
        self.result = '102 Processing'
        method = 'get'
        # Формируем JSON что отправляем в API
        request = self.request
        request["method"] = method

        # ====== валидация JSON
        #
        # if body:
        #     # check in
        #     if not check_in(uri, __file__, body):
        #         return return_('400 Bad Request', 400, 'Bad JSON: ' + func_name + '(): body request')
        #     param = json.loads(body)
        #     request[tag_name] = param[tag_name]
        # indata = json.dumps(request)

        # ======
        # отправляем и получаем ответ
        response = self.Setup(json_dict=request)

        # ====== валидация JSON
        # # check out
        # if not check_out(uri, __file__, data.decode()):
        #     return return_('400 Bad Request', 400, 'Bad JSON answer: ' + func_name + '(): ' + db_api_path)
        # answer = json.loads(data.decode())
        # ======

        # if (answer["res"] != 0):
        #     return return_('500 Internal Server Error', answer["res"], db_api_path + " error res value")
        #
        # if answer[data_tag] is None:  # only for output "Settings":null if empty, not "Settings":[]
        #     outdata = '{"Settings":null}'
        #     return '200 OK', outdata
        #
        # response = {}
        # templates = []
        # records = answer[data_tag]
        # for record in records:
        #     templates.append(record)
        # response["Settings"] = templates
        # outdata = json.dumps(response, separators=(',', ':'))
        #
        # return '200 OK', outdata

        # Теперь разбираем ответ - Если он позитивный
        if self.result == '200 OK':
            # ЕСЛИ У НАС ПУСТОТА
            response = self.decode_from_json(response)
            if response.get(self.data_tag) is None:
                response = {"Settings": None}
                response = self.code_in_json(response)

            # иначе - формируем JSON ответа чтоб отразить
            else:
                settings = response.get(self.data_tag)
                templates = []
                for record in settings:
                    templates.append(record)
                response = {"Settings": templates}
                response = self.code_in_json(response)
        # outdata = json.dumps(response, separators=(',', ':'))

        return response

    def _POST(self):
        """
        Выполнение метода POST

        :return:
        """
        # Первоое что делаем - декодируем полученный JSON
        JSON = self.body
        JSON = self.decode_from_json(JSON)

        self.result = '102 Processing'

        method = 'post'

        # Формируем JSON что отправляем в API
        request = self.request
        request["method"] = method

        # Заполняем данными
        request[self.data_tag] = JSON.get("Settings")

        # отправляем и получаем ответ
        response = self.Setup(json_dict=request)

        return response

    def _PUT(self):
        """
        Выполнение метода PUT
        :return:
        """
        # Первоое что делаем - декодируем полученный JSON
        JSON = self.body
        JSON = self.decode_from_json(JSON)

        self.result = '102 Processing'

        method = 'put'

        # Формируем JSON что отправляем в API
        request = self.request
        request["method"] = method

        # Заполняем данными
        request[self.data_tag] = JSON.get("Settings")

        # отправляем и получаем ответ
        response = self.Setup(json_dict=request)

        return response

    def _DELETE(self):
        """
        Выполнение метода DELETE
        :return:
        """
        self.result = '102 Processing'

        method = 'delete'
        # Формируем JSON что отправляем в API
        request = self.request
        request["method"] = method

        # отправляем и получаем ответ
        response = self.Setup(json_dict=request)
        return response

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
    #                                        Классы Валидации
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
    #
    # def Validation_CheckIn(self):
    #     """
    #     Валидация на вход
    #     :return:
    #     """
    #     from return_error import return_
    #     from check_json_schema import check_in
    #
    #
    #     if body:
    #         # check in
    #         if not check_in(uri, __file__, body):
    #             return return_('400 Bad Request', 400, 'Bad JSON: ' + func_name + '(): body request')
    #         param = json.loads(body)
    #         request[tag_name] = param[tag_name]
    #     indata = json.dumps(request)
    #
    # def Validation_CheckOut(self):
    #     """
    #     Валидация на выход
    #     :return:
    #     """
    #     from return_error import return_
    #     from check_json_schema import check_out
    #
    #     # check out
    #     if not check_out(uri, __file__, data.decode()):
    #         return return_('400 Bad Request', 400, 'Bad JSON answer: ' + func_name + '(): ' + db_api_path)
    #     answer = json.loads(data.decode())

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
    JSON_Method = \
        {
            "GET": _GET,
            "POST": _POST,
            "PUT": _PUT,
            "DELETE": _DELETE,
        }
