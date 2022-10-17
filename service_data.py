# ---------------------------------------------------------------------------------------------------------------------
# Добавим сюда Коды состояний - Необходимы для сбрасывания правильных ошибок
# ---------------------------------------------------------------------------------------------------------------------
status_codes = \
    {
        # •	ВСЕ хорошо
        200: "200 OK",
        # • Плохой запрос
        400: "400 Bad Request",
        # Не авторизован
        401: "401 Unauthorized",
        # •  Запрещено
        403: "403 Forbidden",
        # •	Не найдено
        404: "404 Not Found",
        # • Метод не поддерживается  +
        405: "405 Method Not Allowed",
        # •	Превышен интервал запроса
        408: "408 Request Timeout",
        # Много отправили
        413: "413 Payload Too Large",
        # • ВАШ УРЛ СЛИШКОМ ДЛИННЫЙ
        414: "414 URI Too Long",
        # • Не обрабатываемый экземпляр
        422: "422 Unprocessable Entity",
        # •	- внутренияя ошибка сервера
        500: "500 Internal Server Error",
        # •	Не реализовано – Заглушка для методов что не реализованы (в шаблоне класса)
        501: "501 Not Implemented",
        # сервис недоступен
        503: "503 Service Unavailable",
        # •	Отвал по таймауту
        522: "522 Connection Timed Out",

        # ==== Я добавил новые==>
        # •	В Процессе
        102: "102 Processing",
        # •	В Заблокировано
        423: "423 Locked",
        # •	Конфликт
        409: "409 Conflict",
        # •	Не приемлемо
        406: '406 Not Acceptable',

    }

# ---------------------------------------------------------------------------------------------------------------------
#                           Список всех поддерживаемых Measures в формате "measures_name":"расшифровка"
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#                                                Протокол 40 СМАРТ
# ---------------------------------------------------------------------------------------------------------------------
measures_UM40_dict = \
    {
        'ElConfig': 'конфигурация электросчетчика',
        'DigConfig': 'конфигурация модуля дискретных вводов/выводов',
        'PlsConfig': 'конфигурация концентратора импульсных счетчиков',
        'ElMomentEnergy': 'мгновенные показания энергии электросчетчика',
        'ElMomentQuality': 'мгновенные ПКЭ',
        'ElDayEnergy': 'показания электросчетчика на начало суток',
        'ElDayConsEnergy': 'потребление электросчетчика за сутки',
        'ElMonthEnergy': 'показания электросчетчика на начало месяца',
        'ElMonthConsEnergy': 'потребление электросчетчика за месяц',
        'ElArr1ConsPower': 'профили мощности первого массива профилей мощности электросчетчика',
        'DigMomentState': 'мгновенные показания модуля дискретных вводов/выводов',
        'DigJournalState': 'архив изменения состояний модуля дискретных вводов/выводов',
        'PlsMomentPulse': 'мгновенные показания энергии концентратора импульсных счетчиков',
        'PlsDayPulse': 'показания концентратора импульсных счетчиков на начало суток',
        'PlsMonthPulse': 'показания концентратора импульсных счетчиков на начало месяца',
        'PlsHourPulse': 'показания на начало часа концентратора импульсных счетчиков',
        'ElJrnlPwr': 'управление питанием',
        'ElJrnlTimeCorr': 'коррекция времени электросчетчика',
        'PlsJrnlTimeCorr': 'коррекция времени концентратора импульсных счетчиков',
        'ElJrnlReset': 'сброс показаний',
        'ElJrnlC1Init': 'инициализация первого массива профилей',
        'ElJrnlC2Init': 'инициализация второго массива профилей',
        'ElJrnlTrfCorr': 'коррекция тарификатора',
        'ElJrnlOpen': 'открытие крышки',
        'ElJrnlUnAyth': 'неавторизованный доступ',
        'ElJrnlPwrA': 'управление фазой А',
        'ElJrnlPwrB': 'управление фазой В',
        'ElJrnlPwrC': 'управление фазой С',
        'ElJrnlProg': 'программирование',
        'ElJrnlRelay': 'управление реле',
        'ElJrnlLimESumm': 'лимит суммарной энергии',
        'ElJrnlLimETrf': 'потарифиный лимит энергии',
        'ElJrnlLimETrf1': 'лимит энергии тарифа 1',
        'ElJrnlLimETrf2': 'лимит энергии тарифа 2',
        'ElJrnlLimETrf3': 'лимит энергии тарифа 3',
        'ElJrnlLimETrf4': 'лимит энергии тарифа 4',
        'ElJrnlLimUAMax': 'ограничение максимального напряжения фазы А',
        'ElJrnlLimUAMin': 'ограничение минимального напряжения фазы А',
        'ElJrnlLimUBMax': 'ограничение максимального напряжения фазы В',
        'ElJrnlLimUBMin': 'ограничение минимального напряжения фазы В',
        'ElJrnlLimUCMax': 'ограничение максимального напряжения фазы С',
        'ElJrnlLimUCMin': 'ограничение минимального напряжения фазы С',
        'ElJrnlLimUABMax': 'ограничение максимального расхождения напряжения фаз А и В',
        'ElJrnlLimUABMin': 'ограничение минимального расхождения напряжения фаз А и В',
        'ElJrnlLimUBCMax': 'ограничение максимального расхождения напряжения фаз В и С',
        'ElJrnlLimUBCMin': 'ограничение минимального расхождения напряжения фаз В и С',
        'ElJrnlLimUCAMax': 'ограничение максимального расхождения напряжения фаз С и А',
        'ElJrnlLimUCAMin': 'ограничение минимального расхождения напряжения фаз С и А',
        'ElJrnlLimIAMax': 'ограничение максимального тока фазы А',
        'ElJrnlLimIBMax': 'ограничение максимального тока фазы В',
        'ElJrnlLimICMax': 'ограничение максимального тока фазы С',
        'ElJrnlLimFreqMax': 'ограничение максимальной частоты сети',
        'ElJrnlLimFreqMin': 'ограничение минимальной частоты сети',
        'ElJrnlLimPwr': 'ограничение мощности',
        'ElJrnlLimPwrPP': 'ограничение прямой активной мощности',
        'ElJrnlLimPwrPM': 'ограничение прямой реактивной мощности',
        'ElJrnlLimPwrQP': 'ограничение обратной реактивной мощности',
        'ElJrnlReverce': 'реверс'
    }

measures_UM40_list = list(measures_UM40_dict.keys())

# ---------------------------------------------------------------------------------------------------------------------
#                                                Протокол 40 СМАРТ
#                        Список Job которые у нас используются для общения со счетчиками
# ---------------------------------------------------------------------------------------------------------------------

job_UM40_dict = \
    {
        "GetTime": "Текущее показание времени прибора учета	Любое время. Одно значение",
        "PlsGetTime": "Текущее показание времени импульсного концентратора . Любое время. Одно значение",
        "ElGetTime": "Текущее показание времени Электросчетчика	Любое время. Одно значение",
        "DigGetTime": "Текущее показание времени Дискретного прибора учета.	Любое время. Одно значение",
        "SetTime": "Установка времени прибора учета",
        "PlsSetTime": "Установка времени импульсного концентратора",
        "ElSetTime": "Установка времени Электросчетчика",
        'DigSetTime': "Установка времени Дискретного прибора учета",
        "SyncTime": "Синхронизация времени прибора учета	Требует запроса текущего времени.",
        "PlsSyncTime": "Синхронизация времени импульсного концентратора.	Требует запроса текущего времени.",
        "ElSyncTime": "Синхронизация времени Электросчетчика. Требует запроса текущего времени.",
        "DigSyncTime": "Синхронизация времени Дискретного прибора учета.	Требует запроса текущего времени.",
        "GetRelay": "Запрос состояний реле прибора учета",
        "PlsGetRelay": "Запрос состояний реле импульсного концентратора",
        "ElGetRelay": "Запрос состояний реле Электросчетчика",
        "DigGetRelay": "Запрос состояний реле Дискретного прибора учета",
        "SetRelay": "Установка состояний реле прибора учета",
        "PlsSetRelay": "Установка состояний реле импульсного концентратора",
        "ElSetRelay": "Установка состояний реле Электросчетчика",
        "DigSetRelay": "Установка состояний реле Дискретного прибора учета",
        "GetSerial": "Запрос серийного номера",
        "PlsSerial": "Запрос серийного номера импульсного концентратора",
        "ElSerial": "Запрос серийного номера Электросчетчика",
        "DigSerial": "Запрос серийного номера Дискретного прибора учета",

    }

# Текущее показание времени прибора учета

GetTime_list = \
    [
        'GetTime',
        'PlsGetTime',
        'ElGetTime',
        'DigGetTime'
    ]

# Установка времени прибора учета

SetTime_list = \
    [
        'SetTime',
        'PlsSetTime',
        'ElSetTime',
        'DigSetTime'
    ]

# Синхрв онизация времени прибора учета

SyncTime_list = \
    [
        'SyncTime',
        'PlsSyncTime',
        'ElSyncTime',
        'DigSyncTime'
    ]

# Запрос состояний реле прибора учета

GetRelay_list = \
    [
        'GetRelay',
        'PlsGetRelay',
        'ElGetRelay',
        'DigGetRelay',
    ]

# Установка состояний реле прибора учета

SetRelay_list = \
    [
        'SetRelay',
        'PlsSetRelay',
        'ElSetRelay',
        'DigSetRelay'
    ]

# Запрос серийного номера

GetSerial_list = \
    [
        'GetSerial',
        'PlsSerial',
        'ElSerial',
        'DigSerial'
    ]

# ---------------------------------------------------------------------------------------------------------------------
#                                 Тарифное расписание - для счетчиков СПОДЭС
# ---------------------------------------------------------------------------------------------------------------------
job_Calendar_dict = \
    {
        #
        # Имя календаря тарифного расписания
        "ElCalendarNameActive": "Запрос - Имя календаря тарифного расписания - Активный",
        "ElCalendarNamePassive": "Запрос - Имя календаря тарифного расписания - Пассивный",
        "ElSetCalendarNameActive": "Установка - Имя календаря тарифного расписания - Активный",
        "ElSetCalendarNamePassive": "Установка - Имя календаря тарифного расписания - Пассивный",

        # Сезонный профиль тарифного расписания
        # Активный\Пассивный календарь
        # Чтение\Запись
        "ElCalendarSeasonActive": "Запрос -  Сезонный профиль тарифного расписания -  Активный",
        "ElCalendarSeasonPassive": "Запрос - Сезонный профиль тарифного расписания -  Пассивный",
        "ElSetCalendarSeasonActive": "Установка -  Сезонный профиль тарифного расписания - Активный",
        "ElSetCalendarSeasonPassive": "Установка -  Сезонный профиль тарифного расписания - Пассивный",

        # Недельный профиль тарифного расписания
        # Активный\Пассивный календарь
        # Чтение\Запись
        "ElCalendarWeekActive": "Запрос - Недельный профиль тарифного расписания - Активный",
        "ElCalendarWeekPassive": "Запрос - Недельный профиль тарифного расписания - Пассивный",
        "ElSetCalendarWeekActive": "Установка - Недельный профиль тарифного расписания - Активный",
        "ElSetCalendarWeekPassive": "Установка - Недельный профиль тарифного расписания - Пассивный",

        # Суточный профиль тарифного расписания
        # Активный\Пассивный календарь
        # Чтение\Запись
        "ElCalendarDayActive": "Запрос - Суточный профиль тарифного расписания - Активный",
        "ElCalendarDayPassive": "Запрос - Суточный профиль тарифного расписания - Пассивный",
        "ElSetCalendarDayActive": "Установка - Суточный профиль тарифного расписания - Активный",
        "ElSetCalendarDayPassive": "Установка - Суточный профиль тарифного расписания - Пассивный",

        # Дата активации тарифного расписания
        # Активный\Пассивный календарь
        # Чтение\Запись
        "ElCalendarActivateTime": "Запрос - Дата активации тарифного расписания",
        "ElSetCalendarActivateTime": "Установка - Дата активации тарифного расписания",

        # Активация тарифного расписания
        # Чтение\Запись
        "ElSetCalendarActivatePassive": "Установка - Активация тарифного расписания",
    }
# ---------------------------------------------------------------------------------------------------------------------
job_UM40_list = measures_UM40_list + list(job_UM40_dict.keys()) + list(job_Calendar_dict.keys())

# ---------------------------------------------------------------------------------------------------------------------
#                                                Протокол 31 СМАРТ
# ---------------------------------------------------------------------------------------------------------------------
measures_UM31_dict = \
    {
        'mRelay': 'текущие состояния реле',
        "mTime": "Время прибора учета",
        'mQual': 'текущие ПКЭ',
        'mEng': 'текущие показания энергии',
        'aCfg': 'конфигурация',
        'aEng': 'срезы показаний энергии',
        'aQual': 'срезы ПКЭ',
        'aDay': 'показания на начало суток',
        'aDayCons': 'потребление за сутки',
        'aMonth': 'показания на начало месяца',
        'aMonthCons': 'потребление за месяц',
        'aCons': 'профили мощности',
        'aHour': 'Показания на начало часа',
        'jrnlPwr': 'журнал управление питанием',
        'jrnlTimeCorr': 'журнал коррекция времени',
        'jrnlReset': 'журнал сброс показаний',
        'jrnlC1Init': 'журнал инициализация первого массива профилей',
        'jrnlC2Init': 'журнал инициализация второго массива профилей',
        'jrnlTrfCorr': 'журнал коррекция тарификатора',
        'jrnlOpen': 'журнал открытие крышки',
        'jrnlUnAyth': 'журнал неавторизованный доступ',
        'jrnlPwrA': 'журнал управление фазой А',
        'jrnlPwrB': 'журнал управление фазой В',
        'jrnlPwrC': 'журнал управление фазой С',
        'jrnlProg': 'журнал программирование',
        'jrnlRelay': 'журнал управление реле',
        'jrnlLimESumm': 'журнал лимит суммарной энергии',
        'jrnlLimETrf': 'журнал потарифный лимит энергии',
        'jrnlLimETrf1': 'журнал лимит энергии тарифа 1',
        'jrnlLimETrf2': 'журнал лимит энергии тарифа 2',
        'jrnlLimETrf3': 'журнал лимит энергии тарифа 3',
        'jrnlLimETrf4': 'журнал лимит энергии тарифа 4',
        'jrnlLimUAMax': 'журнал ограничение максимального напряжения фазы А',
        'jrnlLimUAMin': 'журнал ограничение минимального напряжения фазы А',
        'jrnlLimUBMax': 'журнал ограничение максимального напряжения фазы В',
        'jrnlLimUBMin': 'журнал ограничение минимального напряжения фазы В',
        'jrnlLimUCMax': 'журнал ограничение максимального напряжения фазы С',
        'jrnlLimUCMin': 'журнал ограничение минимального напряжения фазы С',
        'jrnlLimUABMax': 'журнал ограничение максимального расхождения напряжения фаз А и В',
        'jrnlLimUABMin': 'журнал ограничение минимального расхождения напряжения фаз А и В',
        'jrnlLimUBCMax': 'журнал ограничение максимального расхождения напряжения фаз В и С',
        'jrnlLimUBCMin': 'журнал ограничение минимального расхождения напряжения фаз В и С',
        'jrnlLimUCAMax': 'журнал ограничение максимального расхождения напряжения фаз С и А',
        'jrnlLimUCAMin': 'журнал ограничение минимального расхождения напряжения фаз С и А',
        'jrnlLimIAMax': 'журнал ограничение максимального тока фазы А',
        'jrnlLimIBMax': 'журнал ограничение максимального тока фазы В',
        'jrnlLimICMax': 'журнал ограничение максимального тока фазы С',
        'jrnlLimFreqMax': 'журнал ограничение максимальной частоты сети',
        'jrnlLimFreqMin': 'журнал ограничение минимальной частоты сети',
        'jrnlLimPwr': 'ограничение мощности',
        'jrnlLimPwrPP': 'журнал ограничение прямой активной мощности',
        'jrnlLimPwrPM': 'журнал ограничение прямой реактивной мощности',
        'jrnlLimPwrQP': 'журнал ограничение обратной активной мощности',
        'jrnlRvr': 'журнал реверс',
    }

measures_UM31_list = list(measures_UM31_dict.keys()) + list(job_Calendar_dict.keys())

# ---------------------------------------------------------------------------------------------------------------------
#                                           Тэги конкретных данных
# ---------------------------------------------------------------------------------------------------------------------

# А теперь пропишем нужные тэги значений этим замечательным людям
ElectricConfig_tag = ['serial', 'model', 'cArrays', 'isDst', 'isClock', 'isTrf', 'isAm', 'isRm', 'isRp', 'kI', 'kU',
                      'const']

# ВЫРЕЗАНО 'isClock'
PulseConfig_tag = ['serial', 'model', 'chnl', 'isDst']

# ВЫРЕЗАНО 'isClock'
DigitalConfig_tag = ['serial', 'model', 'chnlIn', 'chnlOut', 'isDst']

ElecticEnergyValues_tag = ['A+0', 'A+1', 'A+2', 'A+3', 'A+4', 'A-0', 'A-1', 'A-2', 'A-3', 'A-4',
                           'R+0', 'R+1', 'R+2', 'R+3', 'R+4', 'R-0', 'R-1', 'R-2', 'R-3', 'R-4']

ElectricQualityValues_tag = ['UA', 'UB', 'UC', 'IA', 'IB', 'IC', 'PS', 'PA', 'PB', 'PC', 'QS', 'QA',
                             'QB', 'QC', 'SS', 'SA', 'SB', 'SC', 'AngAB', 'AngBC', 'AngAC', 'kPS', 'kPA', 'kPB', 'kPC',
                             'Freq']

ElectricPowerValues_tag = ['cTime', 'P+', 'Q+', 'P-', 'Q-', 'isPart', 'isOvfl', 'isSummer']

PulseValues_tag = ['Pls1', 'Pls2', 'Pls3', 'Pls4', 'Pls5', 'Pls6', 'Pls7', 'Pls8', 'Pls9', 'Pls10', 'Pls11', 'Pls12',
                   'Pls13', 'Pls14', 'Pls15', 'Pls16', 'Pls17', 'Pls18', 'Pls19', 'Pls20', 'Pls21', 'Pls22', 'Pls23',
                   'Pls24', 'Pls25', 'Pls26', 'Pls27', 'Pls28', 'Pls29', 'Pls30', 'Pls31', 'Pls32']

DigitalValues_tag = ['Chnl1', 'Chnl2', 'Chnl3', 'Chnl4', 'Chnl5', 'Chnl6', 'Chnl7', 'Chnl8', 'Chnl9', 'Chnl10',
                     'Chnl11', 'Chnl12', 'Chnl13', 'Chnl14', 'Chnl15', 'Chnl16', 'Chnl17', 'Chnl18', 'Chnl19', 'Chnl20',
                     'Chnl21', 'Chnl22', 'Chnl23', 'Chnl24', 'Chnl25', 'Chnl26', 'Chnl27', 'Chnl28', 'Chnl29', 'Chnl30',
                     'Chnl31', 'Chnl32']

JournalValues_tag = ['event', 'eventId']

measures_tag_UM40_list = ElectricConfig_tag + PulseConfig_tag + DigitalConfig_tag + ElecticEnergyValues_tag + \
                         ElectricQualityValues_tag + ElectricPowerValues_tag + PulseValues_tag + DigitalValues_tag + \
                         JournalValues_tag
# ---------------------------------------------------------------------------------------------------------------------
#                               Часовые пояса - Необходимы для установки времени
# ---------------------------------------------------------------------------------------------------------------------

Time_Zone_dict = {
    "Africa/Abidjan": "+00:00",
    "Africa/Accra": "+00:00",
    "Africa/Addis_Ababa": "+03:00",
    "Africa/Algiers": "+01:00",
    "Africa/Asmara": "+03:00",
    "Africa/Asmera": "+03:00",
    "Africa/Bamako": "+00:00",
    "Africa/Bangui": "+01:00",
    "Africa/Banjul": "+00:00",
    "Africa/Blantyre": "+02:00",
    "Africa/Brazzaville": "+01:00",
    "Africa/Bujumbura": "+02:00",
    "Africa/Cairo": "+02:00",
    "Africa/Casablanca": "+00:00",
    "Africa/Ceuta": "+01:00",
    "Africa/Conakry": "+00:00",
    "Africa/Dakar": "+00:00",
    "Africa/Dar_es_Salaam": "+03:00",
    "Africa/Djibouti": "+03:00",
    "Africa/Douala": "+01:00",
    "Africa/El_Aaiun": "+00:00",
    "Africa/Freetown": "+00:00",
    "Africa/Gaborone": "+02:00",
    "Africa/Harare": "+02:00",
    "Africa/Johannesburg": "+02:00",
    "Africa/Juba": "+03:00",
    "Africa/Kampala": "+03:00",
    "Africa/Khartoum": "+03:00",
    "Africa/Kigali": "+02:00",
    "Africa/Kinshasa": "+01:00",
    "Africa/Lagos": "+01:00",
    "Africa/Libreville": "+01:00",
    "Africa/Lome": "+00:00",
    "Africa/Luanda": "+01:00",
    "Africa/Lubumbashi": "+02:00",
    "Africa/Lusaka": "+02:00",
    "Africa/Malabo": "+01:00",
    "Africa/Maputo": "+02:00",
    "Africa/Maseru": "+02:00",
    "Africa/Mbabane": "+02:00",
    "Africa/Mogadishu": "+03:00",
    "Africa/Monrovia": "+00:00",
    "Africa/Nairobi": "+03:00",
    "Africa/Ndjamena": "+01:00",
    "Africa/Niamey": "+01:00",
    "Africa/Nouakchott": "+00:00",
    "Africa/Ouagadougou": "+00:00",
    "Africa/Porto-Novo": "+01:00",
    "Africa/Sao_Tome": "+00:00",
    "Africa/Timbuktu": "+00:00",
    "Africa/Tripoli": "+02:00",
    "Africa/Tunis": "+01:00",
    "Africa/Windhoek": "+01:00",
    "America/Adak": "-10:00",
    "America/Anchorage": "-09:00",
    "America/Anguilla": "-04:00",
    "America/Antigua": "-04:00",
    "America/Araguaina": "-03:00",
    "America/Argentina/Buenos_Aires": "-03:00",
    "America/Argentina/Catamarca": "-03:00",
    "America/Argentina/ComodRivadavia": "-03:00",
    "America/Argentina/Cordoba": "-03:00",
    "America/Argentina/Jujuy": "-03:00",
    "America/Argentina/La_Rioja": "-03:00",
    "America/Argentina/Mendoza": "-03:00",
    "America/Argentina/Rio_Gallegos": "-03:00",
    "America/Argentina/Salta": "-03:00",
    "America/Argentina/San_Juan": "-03:00",
    "America/Argentina/San_Luis": "-03:00",
    "America/Argentina/Tucuman": "-03:00",
    "America/Argentina/Ushuaia": "-03:00",
    "America/Aruba": "-04:00",
    "America/Asuncion": "-04:00",
    "America/Atikokan": "-05:00",
    "America/Atka": "-10:00",
    "America/Bahia": "-03:00",
    "America/Bahia_Banderas": "-06:00",
    "America/Barbados": "-04:00",
    "America/Belem": "-03:00",
    "America/Belize": "-06:00",
    "America/Blanc-Sablon": "-04:00",
    "America/Boa_Vista": "-04:00",
    "America/Bogota": "-05:00",
    "America/Boise": "-07:00",
    "America/Buenos_Aires": "-03:00",
    "America/Cambridge_Bay": "-07:00",
    "America/Campo_Grande": "-04:00",
    "America/Cancun": "-06:00",
    "America/Caracas": "-04:30",
    "America/Catamarca": "-03:00",
    "America/Cayenne": "-03:00",
    "America/Cayman": "-05:00",
    "America/Chicago": "-06:00",
    "America/Chihuahua": "-07:00",
    "America/Coral_Harbour": "-05:00",
    "America/Cordoba": "-03:00",
    "America/Costa_Rica": "-06:00",
    "America/Creston": "-07:00",
    "America/Cuiaba": "-04:00",
    "America/Curacao": "-04:00",
    "America/Danmarkshavn": "+00:00",
    "America/Dawson": "-08:00",
    "America/Dawson_Creek": "-07:00",
    "America/Denver": "-07:00",
    "America/Detroit": "-05:00",
    "America/Dominica": "-04:00",
    "America/Edmonton": "-07:00",
    "America/Eirunepe": "-05:00",
    "America/El_Salvador": "-06:00",
    "America/Ensenada": "-08:00",
    "America/Fort_Wayne": "-05:00",
    "America/Fortaleza": "-03:00",
    "America/Glace_Bay": "-04:00",
    "America/Godthab": "-03:00",
    "America/Goose_Bay": "-04:00",
    "America/Grand_Turk": "-05:00",
    "America/Grenada": "-04:00",
    "America/Guadeloupe": "-04:00",
    "America/Guatemala": "-06:00",
    "America/Guayaquil": "-05:00",
    "America/Guyana": "-04:00",
    "America/Halifax": "-04:00",
    "America/Havana": "-05:00",
    "America/Hermosillo": "-07:00",
    "America/Indiana/Indianapolis": "-05:00",
    "America/Indiana/Knox": "-06:00",
    "America/Indiana/Marengo": "-05:00",
    "America/Indiana/Petersburg": "-05:00",
    "America/Indiana/Tell_City": "-06:00",
    "America/Indiana/Valparaiso": "-06:00",
    "America/Indiana/Vevay": "-05:00",
    "America/Indiana/Vincennes": "-05:00",
    "America/Indiana/Winamac": "-05:00",
    "America/Indianapolis": "-05:00",
    "America/Inuvik": "-07:00",
    "America/Iqaluit": "-05:00",
    "America/Jamaica": "-05:00",
    "America/Jujuy": "-03:00",
    "America/Juneau": "-09:00",
    "America/Kentucky/Louisville": "-05:00",
    "America/Kentucky/Monticello": "-05:00",
    "America/Knox_IN": "-06:00",
    "America/Kralendijk": "-04:00",
    "America/La_Paz": "-04:00",
    "America/Lima": "-05:00",
    "America/Los_Angeles": "-08:00",
    "America/Louisville": "-05:00",
    "America/Lower_Princes": "-04:00",
    "America/Maceio": "-03:00",
    "America/Managua": "-06:00",
    "America/Manaus": "-04:00",
    "America/Marigot": "-04:00",
    "America/Martinique": "-04:00",
    "America/Matamoros": "-06:00",
    "America/Mazatlan": "-07:00",
    "America/Mendoza": "-03:00",
    "America/Menominee": "-06:00",
    "America/Merida": "-06:00",
    "America/Metlakatla": "-08:00",
    "America/Mexico_City": "-06:00",
    "America/Miquelon": "-03:00",
    "America/Moncton": "-04:00",
    "America/Monterrey": "-06:00",
    "America/Montevideo": "-03:00",
    "America/Montreal": "-05:00",
    "America/Montserrat": "-04:00",
    "America/Nassau": "-05:00",
    "America/New_York": "-05:00",
    "America/Nipigon": "-05:00",
    "America/Nome": "-09:00",
    "America/Noronha": "-02:00",
    "America/North_Dakota/Beulah": "-06:00",
    "America/North_Dakota/Center": "-06:00",
    "America/North_Dakota/New_Salem": "-06:00",
    "America/Ojinaga": "-07:00",
    "America/Panama": "-05:00",
    "America/Pangnirtung": "-05:00",
    "America/Paramaribo": "-03:00",
    "America/Phoenix": "-07:00",
    "America/Port_of_Spain": "-04:00",
    "America/Port-au-Prince": "-05:00",
    "America/Porto_Acre": "-05:00",
    "America/Porto_Velho": "-04:00",
    "America/Puerto_Rico": "-04:00",
    "America/Rainy_River": "-06:00",
    "America/Rankin_Inlet": "-06:00",
    "America/Recife": "-03:00",
    "America/Regina": "-06:00",
    "America/Resolute": "-06:00",
    "America/Rio_Branco": "-05:00",
    "America/Rosario": "-03:00",
    "America/Santa_Isabel": "-08:00",
    "America/Santarem": "-03:00",
    "America/Santiago": "-03:00",
    "America/Santo_Domingo": "-04:00",
    "America/Sao_Paulo": "-03:00",
    "America/Scoresbysund": "-01:00",
    "America/Shiprock": "-07:00",
    "America/Sitka": "-09:00",
    "America/St_Barthelemy": "-04:00",
    "America/St_Johns": "-03:30",
    "America/St_Kitts": "-04:00",
    "America/St_Lucia": "-04:00",
    "America/St_Thomas": "-04:00",
    "America/St_Vincent": "-04:00",
    "America/Swift_Current": "-06:00",
    "America/Tegucigalpa": "-06:00",
    "America/Thule": "-04:00",
    "America/Thunder_Bay": "-05:00",
    "America/Tijuana": "-08:00",
    "America/Toronto": "-05:00",
    "America/Tortola": "-04:00",
    "America/Vancouver": "-08:00",
    "America/Virgin": "-04:00",
    "America/Whitehorse": "-08:00",
    "America/Winnipeg": "-06:00",
    "America/Yakutat": "-09:00",
    "America/Yellowknife": "-07:00",
    "Antarctica/Casey": "+11:00",
    "Antarctica/Davis": "+05:00",
    "Antarctica/DumontDUrville": "+10:00",
    "Antarctica/Macquarie": "+11:00",
    "Antarctica/Mawson": "+05:00",
    "Antarctica/McMurdo": "+12:00",
    "Antarctica/Palmer": "-04:00",
    "Antarctica/Rothera": "-03:00",
    "Antarctica/South_Pole": "+12:00",
    "Antarctica/Syowa": "+03:00",
    "Antarctica/Troll": "+00:00",
    "Antarctica/Vostok": "+06:00",
    "Arctic/Longyearbyen": "+01:00",
    "Asia/Aden": "+03:00",
    "Asia/Almaty": "+06:00",
    "Asia/Amman": "+02:00",
    "Asia/Anadyr": "+12:00",
    "Asia/Aqtau": "+05:00",
    "Asia/Aqtobe": "+05:00",
    "Asia/Ashgabat": "+05:00",
    "Asia/Ashkhabad": "+05:00",
    "Asia/Baghdad": "+03:00",
    "Asia/Bahrain": "+03:00",
    "Asia/Baku": "+04:00",
    "Asia/Bangkok": "+07:00",
    "Asia/Beirut": "+02:00",
    "Asia/Bishkek": "+06:00",
    "Asia/Brunei": "+08:00",
    "Asia/Calcutta": "+05:30",
    "Asia/Choibalsan": "+08:00",
    "Asia/Chongqing": "+08:00",
    "Asia/Chungking": "+08:00",
    "Asia/Colombo": "+05:30",
    "Asia/Dacca": "+06:00",
    "Asia/Damascus": "+02:00",
    "Asia/Dhaka": "+06:00",
    "Asia/Dili": "+09:00",
    "Asia/Dubai": "+04:00",
    "Asia/Dushanbe": "+05:00",
    "Asia/Gaza": "+02:00",
    "Asia/Harbin": "+08:00",
    "Asia/Hebron": "+02:00",
    "Asia/Ho_Chi_Minh": "+07:00",
    "Asia/Hong_Kong": "+08:00",
    "Asia/Hovd": "+07:00",
    "Asia/Irkutsk": "+08:00",
    "Asia/Istanbul": "+02:00",
    "Asia/Jakarta": "+07:00",
    "Asia/Jayapura": "+09:00",
    "Asia/Jerusalem": "+02:00",
    "Asia/Kabul": "+04:30",
    "Asia/Kamchatka": "+12:00",
    "Asia/Karachi": "+05:00",
    "Asia/Kashgar": "+08:00",
    "Asia/Kathmandu": "+05:45",
    "Asia/Katmandu": "+05:45",
    "Asia/Khandyga": "+09:00",
    "Asia/Kolkata": "+05:30",
    "Asia/Krasnoyarsk": "+07:00",
    "Asia/Kuala_Lumpur": "+08:00",
    "Asia/Kuching": "+08:00",
    "Asia/Kuwait": "+03:00",
    "Asia/Macao": "+08:00",
    "Asia/Macau": "+08:00",
    "Asia/Magadan": "+10:00",
    "Asia/Makassar": "+08:00",
    "Asia/Manila": "+08:00",
    "Asia/Muscat": "+04:00",
    "Asia/Nicosia": "+02:00",
    "Asia/Novokuznetsk": "+07:00",
    "Asia/Novosibirsk": "+06:00",
    "Asia/Omsk": "+06:00",
    "Asia/Oral": "+05:00",
    "Asia/Phnom_Penh": "+07:00",
    "Asia/Pontianak": "+07:00",
    "Asia/Pyongyang": "+09:00",
    "Asia/Qatar": "+03:00",
    "Asia/Qyzylorda": "+06:00",
    "Asia/Rangoon": "+06:30",
    "Asia/Riyadh": "+03:00",
    "Asia/Saigon": "+07:00",
    "Asia/Sakhalin": "+11:00",
    "Asia/Samarkand": "+05:00",
    "Asia/Seoul": "+09:00",
    "Asia/Shanghai": "+08:00",
    "Asia/Singapore": "+08:00",
    "Asia/Taipei": "+08:00",
    "Asia/Tashkent": "+05:00",
    "Asia/Tbilisi": "+04:00",
    "Asia/Tehran": "+03:30",
    "Asia/Tel_Aviv": "+02:00",
    "Asia/Thimbu": "+06:00",
    "Asia/Thimphu": "+06:00",
    "Asia/Tokyo": "+09:00",
    "Asia/Ujung_Pandang": "+08:00",
    "Asia/Ulaanbaatar": "+08:00",
    "Asia/Ulan_Bator": "+08:00",
    "Asia/Urumqi": "+08:00",
    "Asia/Ust-Nera": "+10:00",
    "Asia/Vientiane": "+07:00",
    "Asia/Vladivostok": "+10:00",
    "Asia/Yakutsk": "+09:00",
    "Asia/Yekaterinburg": "+05:00",
    "Asia/Yerevan": "+04:00",
    "Atlantic/Azores": "-01:00",
    "Atlantic/Bermuda": "-04:00",
    "Atlantic/Canary": "+00:00",
    "Atlantic/Cape_Verde": "-01:00",
    "Atlantic/Faeroe": "+00:00",
    "Atlantic/Faroe": "+00:00",
    "Atlantic/Jan_Mayen": "+01:00",
    "Atlantic/Madeira": "+00:00",
    "Atlantic/Reykjavik": "+00:00",
    "Atlantic/South_Georgia": "-02:00",
    "Atlantic/St_Helena": "+00:00",
    "Atlantic/Stanley": "-03:00",
    "Australia/ACT": "+10:00",
    "Australia/Adelaide": "+09:30",
    "Australia/Brisbane": "+10:00",
    "Australia/Broken_Hill": "+09:30",
    "Australia/Canberra": "+10:00",
    "Australia/Currie": "+10:00",
    "Australia/Darwin": "+09:30",
    "Australia/Eucla": "+08:45",
    "Australia/Hobart": "+10:00",
    "Australia/LHI": "+10:30",
    "Australia/Lindeman": "+10:00",
    "Australia/Lord_Howe": "+10:30",
    "Australia/Melbourne": "+10:00",
    "Australia/North": "+09:30",
    "Australia/NSW": "+10:00",
    "Australia/Perth": "+08:00",
    "Australia/Queensland": "+10:00",
    "Australia/South": "+09:30",
    "Australia/Sydney": "+10:00",
    "Australia/Tasmania": "+10:00",
    "Australia/Victoria": "+10:00",
    "Australia/West": "+08:00",
    "Australia/Yancowinna": "+09:30",
    "Brazil/Acre": "-05:00",
    "Brazil/DeNoronha": "-02:00",
    "Brazil/East": "-03:00",
    "Brazil/West": "-04:00",
    "Canada/Atlantic": "-04:00",
    "Canada/Central": "-06:00",
    "Canada/Eastern": "-05:00",
    "Canada/East-Saskatchewan": "-06:00",
    "Canada/Mountain": "-07:00",
    "Canada/Newfoundland": "-03:30",
    "Canada/Pacific": "-08:00",
    "Canada/Saskatchewan": "-06:00",
    "Canada/Yukon": "-08:00",
    "Chile/Continental": "-03:00",
    "Chile/EasterIsland": "-05:00",
    "Cuba": "-05:00",
    "Egypt": "+02:00",
    "Eire": "+00:00",
    "Etc/GMT": "+00:00",
    "Etc/GMT+0": "+00:00",
    "Etc/UCT": "+00:00",
    "Etc/Universal": "+00:00",
    "Etc/UTC": "+00:00",
    "Etc/Zulu": "+00:00",
    "Europe/Amsterdam": "+01:00",
    "Europe/Andorra": "+01:00",
    "Europe/Athens": "+02:00",
    "Europe/Belfast": "+00:00",
    "Europe/Belgrade": "+01:00",
    "Europe/Berlin": "+01:00",
    "Europe/Bratislava": "+01:00",
    "Europe/Brussels": "+01:00",
    "Europe/Bucharest": "+02:00",
    "Europe/Budapest": "+01:00",
    "Europe/Busingen": "+01:00",
    "Europe/Chisinau": "+02:00",
    "Europe/Copenhagen": "+01:00",
    "Europe/Dublin": "+00:00",
    "Europe/Gibraltar": "+01:00",
    "Europe/Guernsey": "+00:00",
    "Europe/Helsinki": "+02:00",
    "Europe/Isle_of_Man": "+00:00",
    "Europe/Istanbul": "+02:00",
    "Europe/Jersey": "+00:00",
    "Europe/Kaliningrad": "+02:00",
    "Europe/Kiev": "+02:00",
    "Europe/Lisbon": "+00:00",
    "Europe/Ljubljana": "+01:00",
    "Europe/London": "+00:00",
    "Europe/Luxembourg": "+01:00",
    "Europe/Madrid": "+01:00",
    "Europe/Malta": "+01:00",
    "Europe/Mariehamn": "+02:00",
    "Europe/Minsk": "+03:00",
    "Europe/Monaco": "+01:00",
    "Europe/Moscow": "+03:00",
    "Europe/Nicosia": "+02:00",
    "Europe/Oslo": "+01:00",
    "Europe/Paris": "+01:00",
    "Europe/Podgorica": "+01:00",
    "Europe/Prague": "+01:00",
    "Europe/Riga": "+02:00",
    "Europe/Rome": "+01:00",
    "Europe/Samara": "+04:00",
    "Europe/San_Marino": "+01:00",
    "Europe/Sarajevo": "+01:00",
    "Europe/Simferopol": "+03:00",
    "Europe/Skopje": "+01:00",
    "Europe/Sofia": "+02:00",
    "Europe/Stockholm": "+01:00",
    "Europe/Tallinn": "+02:00",
    "Europe/Tirane": "+01:00",
    "Europe/Tiraspol": "+02:00",
    "Europe/Uzhgorod": "+02:00",
    "Europe/Vaduz": "+01:00",
    "Europe/Vatican": "+01:00",
    "Europe/Vienna": "+01:00",
    "Europe/Vilnius": "+02:00",
    "Europe/Volgograd": "+03:00",
    "Europe/Warsaw": "+01:00",
    "Europe/Zagreb": "+01:00",
    "Europe/Zaporozhye": "+02:00",
    "Europe/Zurich": "+01:00",
    "GB": "+00:00",
    "GB-Eire": "+00:00",
    "GMT": "+00:00",
    "GMT+0": "+00:00",
    "GMT0": "+00:00",
    "GMT-0": "+00:00",
    "Greenwich": "+00:00",
    "Hongkong": "+08:00",
    "Iceland": "+00:00",
    "Indian/Antananarivo": "+03:00",
    "Indian/Chagos": "+06:00",
    "Indian/Christmas": "+07:00",
    "Indian/Cocos": "+06:30",
    "Indian/Comoro": "+03:00",
    "Indian/Kerguelen": "+05:00",
    "Indian/Mahe": "+04:00",
    "Indian/Maldives": "+05:00",
    "Indian/Mauritius": "+04:00",
    "Indian/Mayotte": "+03:00",
    "Indian/Reunion": "+04:00",
    "Iran": "+03:30",
    "Israel": "+02:00",
    "Jamaica": "-05:00",
    "Japan": "+09:00",
    "Kwajalein": "+12:00",
    "Libya": "+02:00",
    "Mexico/BajaNorte": "-08:00",
    "Mexico/BajaSur": "-07:00",
    "Mexico/General": "-06:00",
    "Navajo": "-07:00",
    "NZ": "+12:00",
    "NZ-CHAT": "+12:45",
    "Pacific/Apia": "+13:00",
    "Pacific/Auckland": "+12:00",
    "Pacific/Chatham": "+12:45",
    "Pacific/Chuuk": "+10:00",
    "Pacific/Easter": "-06:00",
    "Pacific/Efate": "+11:00",
    "Pacific/Enderbury": "+13:00",
    "Pacific/Fakaofo": "+13:00",
    "Pacific/Fiji": "+12:00",
    "Pacific/Funafuti": "+12:00",
    "Pacific/Galapagos": "-06:00",
    "Pacific/Gambier": "-09:00",
    "Pacific/Guadalcanal": "+11:00",
    "Pacific/Guam": "+10:00",
    "Pacific/Honolulu": "-10:00",
    "Pacific/Johnston": "-10:00",
    "Pacific/Kiritimati": "+14:00",
    "Pacific/Kosrae": "+11:00",
    "Pacific/Kwajalein": "+12:00",
    "Pacific/Majuro": "+12:00",
    "Pacific/Marquesas": "-09:30",
    "Pacific/Midway": "-11:00",
    "Pacific/Nauru": "+12:00",
    "Pacific/Niue": "-11:00",
    "Pacific/Norfolk": "+11:30",
    "Pacific/Noumea": "+11:00",
    "Pacific/Pago_Pago": "-11:00",
    "Pacific/Palau": "+09:00",
    "Pacific/Pitcairn": "-08:00",
    "Pacific/Pohnpei": "+11:00",
    "Pacific/Ponape": "+11:00",
    "Pacific/Port_Moresby": "+10:00",
    "Pacific/Rarotonga": "-10:00",
    "Pacific/Saipan": "+10:00",
    "Pacific/Samoa": "-11:00",
    "Pacific/Tahiti": "-10:00",
    "Pacific/Tarawa": "+12:00",
    "Pacific/Tongatapu": "+13:00",
    "Pacific/Truk": "+10:00",
    "Pacific/Wake": "+12:00",
    "Pacific/Wallis": "+12:00",
    "Pacific/Yap": "+10:00",
    "Poland": "+01:00",
    "Portugal": "+00:00",
    "PRC": "+08:00",
    "ROC": "+08:00",
    "ROK": "+09:00",
    "Singapore": "+08:00",
    "Turkey": "+02:00",
    "UCT": "+00:00",
    "Universal": "+00:00",
    "US/Alaska": "-09:00",
    "US/Aleutian": "-10:00",
    "US/Arizona": "-07:00",
    "US/Central": "-06:00",
    "US/Eastern": "-05:00",
    "US/East-Indiana": "-05:00",
    "US/Hawaii": "-10:00",
    "US/Indiana-Starke": "-06:00",
    "US/Michigan": "-05:00",
    "US/Mountain": "-07:00",
    "US/Pacific": "-08:00",
    "US/Samoa": "-11:00",
    "UTC": "+00:00",
    "W-SU": "+03:00",
    "Zulu": "+00:00",
}
