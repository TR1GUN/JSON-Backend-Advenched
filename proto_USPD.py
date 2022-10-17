# ///////////////////////////////////////////////////////////////////////////////////////////
# Здесь расположим очень важную вещь - определяем по какому протоколу будем общаться,
# По маркеру определяем что за протокол и вытаскиваем необходимый handlers по нужному протоколу
#                                   Это важно
# ///////////////////////////////////////////////////////////////////////////////////////////

from USPD_Protocol_UM_31_SMART import handlers_UM31
from USPD_Protocol_UM_40_SMART import handlers_UM40
from service_config import USPD_protocol_default, USPD_protocol_UM_40, USPD_protocol_UM_31

# ///////////////////////////////////////////////////////////////////////////////////////////

# Соответствие методов протокола по их маркеру
protocol_handlers = {
    # ------ Значения в int ---------
    USPD_protocol_UM_40: handlers_UM40,
    USPD_protocol_UM_31: handlers_UM31,

    # ------ Значения в str ---------
    str(USPD_protocol_UM_40): handlers_UM40,
    str(USPD_protocol_UM_31): handlers_UM31,
}


# очень важная функция - нормализация значений
def normalize_value_protocol(protocol_USPD):
    """
    Это очень важная вспомогательная функция
    :param protocol_USPD:
    :return:
    """
    # ЕСЛИ ВООБЩЕ ЕСТЬ указание о протоколе :
    if protocol_USPD is not None:
        # Пытаемся перевести в int значение
        try:
            protocol_USPD = int(protocol_USPD)
        except Exception as error:

            from LoggerJournal.Logger import Logger
            text = "Not correct value USPD protocol.\n " \
                   + " Received value : " + str(protocol_USPD) + \
                   "\n" + "Exception : " + str(error)
            Logger().DEBUG(text)

            protocol_USPD = None

    return protocol_USPD


# Основная Функция определения протокола
def define_protocol(protocol_USPD):
    """
    Механизм Выбора протокола
    :param protocol_USPD:
    :return:
    """
    # Первое - Проверяем есть ли полученный протокол в списке поддерживаемых
    support_protocol_list = list(protocol_handlers.keys())

    # если не поддерживает - то используем значение по умолчанию
    if protocol_USPD not in support_protocol_list:
        from LoggerJournal.Logger import Logger
        text = "Not support USPD protocol.\n " + " Received value : " + str(protocol_USPD)
        Logger().DEBUG(text)

        protocol_USPD = USPD_protocol_default

    # Теперь пробуем вытащить нужный протокол
    headers = protocol_handlers.get(protocol_USPD)
    # Возвращаем что нашли
    return headers


# Основная функция выдачи нужного метода по IRI
def get_function(URI, protocol_USPD):
    headers = define_protocol(protocol_USPD=protocol_USPD)

    header = headers.get(URI)

    return header
