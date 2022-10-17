# Выход из авторизации
def method_json_backend(method, uri, body=None, level_user: [int] = None):
    """
    выход из авторизации

    :param method: Метод
    :param uri: URL
    :param body: JSON
    :param level_user:уровень доступа текущей сессии
    :return: Код результата, JSON / Код результата
    """
    # # Сначала Проверяем JSON
    # # -----> Логер
    # from LoggerJournal.Logger import Logger
    # Logger(Name='settings_Auth').DEBUG(text=str(''))
    # Logger(Name='Тип Запроса').DEBUG(text=str(method))
    # Logger(Name='URL').DEBUG(text=str(uri))
    # Logger(Name='body').DEBUG(text=str(body) + " , тип данных" + str(type(body)))
    # # ----->
    # Никаких проверок не надо
    # Сначала выясняем есть ли у нас такие права доступа
    # 0 - Доступ запрещен
    # 1 - Обычный Пользователь
    # 2 - Админ
    Access_level = {
        0: ["GET", "POST", "PUT", "DELETE"],
        1: ["GET", "POST", "PUT", "DELETE"],
        2: ["GET", "POST", "PUT", "DELETE"],
    }

    user_allowed = Access_level.get(level_user, ["GET", "POST", "PUT", "DELETE"])
    # Если наш метод разрешается - то пропускаем , нет , выбрасываем ошибку - недостаточно прав
    if method in user_allowed:

        return 200, "200 OK"

    # выбрасываем ошибку - недостаточно прав
    else:
        return 403, "403 Forbidden"
