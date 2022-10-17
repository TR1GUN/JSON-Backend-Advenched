# ////////////////////////////////////////////////////////////////////////////////////////////
#                 Здесь работаем с Протоколом УМ-31 SMART
# ///////////////////////////////////////////////////////////////////////////////////////////

from USPD_UM31 import Functionality_of_Device

#     По УРЛ определяем наш запрос - Это важно

handlers_UM31 = {
    # //////-----------------------------------------------------------------///////
    #                            Авторизация
    # //////-----------------------------------------------------------------///////
    # Авторизация - стоит заглушка
    '/auth': Functionality_of_Device.method_json_backend,
    # Отключение - хз - запрос не робит на УМ-31
    '/logoff': Functionality_of_Device.method_json_backend,
    # //////-----------------------------------------------------------------///////
    #                             Настройки
    # //////-----------------------------------------------------------------///////
    # //////////////////////   Настройки Авторизации /////////////////////////////////

    # // Авторизация по протоколу JSON - Стоит заглушка
    '/settings/proto/json/auth': Functionality_of_Device.method_json_backend,

    # ////////////////////// Настройки устройства /////////////////////////////////
    # # Настройки ethernet
    # '/settings/ip': Functionality_of_Device.settings_Ethernet,
    #
    # # Настройки Настройки цифровых интерфейсов
    # '/settings/uart': Functionality_of_Device.settings_Uart,
    #
    # # // Настройки линий питания
    # '/settings/dout': Functionality_of_Device.settings_PowerLine,
    #
    # # // Настройки локального времени
    # '/settings/time/local': Functionality_of_Device.settings_TimeLocal,

    # //////////////////////   Настройки модема /////////////////////////////////
    #
    # # // Настройки СИМ Карты
    # '/settings/modem/sim': Functionality_of_Device.settings_SIM,



    # //////////////////////   Клиенты и серверы /////////////////////////////////
    # # // - Настройки HTTP сервера
    # '/settings/servers/tcp': Functionality_of_Device.settings_TCP_Server,
    #
    # # // Сервера синхронизации времени
    # '/settings/servers/sntp': Functionality_of_Device.settings_NTP_Server,
    #
    # # // - Таблица аккаунтов SMTP - Изначально было  - /settings/smtp
    # '/settings/servers/smtp': Functionality_of_Device.settings_Account_SMTP,
    #
    # # // Настройки MQTT брокера
    # '/settings/servers/mqtt': Functionality_of_Device.settings_Broker_MQTT,
    #

    # //////////////////////   Приборы учета /////////////////////////////////
    # // Переписал - Таблица Счетчиков
    '/settings/meter/table': Functionality_of_Device.method_json_backend,

    # //////////////////////   Система событий /////////////////////////////////
    #
    # # // - таблица Calendar в БД системы событий
    # '/settings/events/calendar': Functionality_of_Device.settings_Calendar,
    #
    # # // Настройки расписаний
    # '/settings/events/schdl': Functionality_of_Device.settings_Scheduler,
    #
    # # // - Настройки - Настройка системы событий
    # '/settings/events/manager': Functionality_of_Device.settings_Event_Manager,
    #
    # # // Шаблоны приборов учета
    # '/settings/templates/meter': Functionality_of_Device.settings_Meter_Templates,
    #
    # # //Шаблоны данных приборов учета
    # '/settings/templates/arch': Functionality_of_Device.settings_Meter_Data_Templates,
    #
    # # // - таблица MeterMessages в БД системы событий
    # '/settings/templates/messages': Functionality_of_Device.settings_Meter_Messages,
    #
    # # //  таблица Email в БД системы событий
    # '/settings/templates/email': Functionality_of_Device.settings_Email,
    #
    # # // Опрос приборов учета по событиям
    # '/settings/actions/meter': Functionality_of_Device.settings_Poller,

    # // Условия синхронизации времени
    # // ПОКА НЕТ ПОДДЕРЖКИ ВО ФРОНТЕНДЕ + НЕТ JSON протокола
    # '/settings/actions/sntp': Functionality_of_Device.settings_Time_Synchronization_Conditions,

    # # // -  таблица SMTPMeterMessages в БД системы событий
    # '/settings/actions/smtp': Functionality_of_Device.settings_SMTP_Meter_Messages,
    #
    # # // - таблица MQTTMeterMessages в БД системы событий
    # '/settings/actions/mqtt': Functionality_of_Device.settings_MQTT_Meter_Messages,
    # //////-----------------------------------------------------------------///////
    #                         Опрос приборов учета
    # //////-----------------------------------------------------------------///////

    # // Считывание - Архивные показатели/ Текущие показатели
    '/meter/data': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                      Управление приборами учета
    # //////-----------------------------------------------------------------///////
    # // Задание времени
    '/meter/settings/time': Functionality_of_Device.method_json_backend,

    # // Задание положения реле
    '/meter/settings/relay': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                          Тарифное расписание
    # //////-----------------------------------------------------------------///////

    # // Активация тарифного расписания
    '/meter/settings/calendar/activate': Functionality_of_Device.method_json_backend,

    # // Имя календаря тарифного расписания
    '/meter/settings/calendar/name': Functionality_of_Device.method_json_backend,

    # // Сезонный профиль тарифного расписания
    '/meter/settings/calendar/season': Functionality_of_Device.method_json_backend,

    # // Недельный профиль тарифного расписания
    '/meter/settings/calendar/week': Functionality_of_Device.method_json_backend,

    # // Суточный профиль тарифного расписания
    '/meter/settings/calendar/day': Functionality_of_Device.method_json_backend,

    # // Дата активации тарифного расписания
    '/meter/settings/calendar/time': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                               Действия
    # //////-----------------------------------------------------------------///////
    #
    # // - Перезагрузка устройства
    '/action/restart': Functionality_of_Device.method_json_backend,
    #
    # # //  информации о времени - перезапись
    '/action/time/set': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                            Журналы изделия
    # //////-----------------------------------------------------------------///////

    # // Журнал изменения времени +
    '/jrnl/time': Functionality_of_Device.method_json_backend,
    # //Журнал ответов приборов учета
    '/jrnl/meter/answ': Functionality_of_Device.method_json_backend,
    # Журнал перезагрузок +
    '/jrnl/reset': Functionality_of_Device.method_json_backend,
    # Журнал Системы событий
    '/jrnl/action': Functionality_of_Device.method_json_backend,
    # Не существующие журналы

    # Журнал сетевых подключений +
    '/jrnl/srvconn': Functionality_of_Device.method_json_backend,
    # Журнал подключений PPP клиента (GPRS) +
    '/jrnl/ppp/clconn': Functionality_of_Device.method_json_backend,
    # Журнал поднятия PPP-сервера (CSD) +
    '/jrnl/ppp/srvconn': Functionality_of_Device.method_json_backend,
    # Журнал входящих вызовов (CSD) +
    '/jrnl/call': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов +
    '/jrnl/din/sens': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/pwrline': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/power': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/charge': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/open': Functionality_of_Device.method_json_backend,
    # Журнал авторизации (HTTP-сервер) +
    '/jrnl/auth/json': Functionality_of_Device.method_json_backend,

    # Журнал хранилища почтовых сообщений +
    '/jrnl/mail/msg': Functionality_of_Device.method_json_backend,
    # Журнал отправки почтовых сообщений +
    '/jrnl/mail/send': Functionality_of_Device.method_json_backend,

    # Журнал изменения версии ВПО изделия +
    '/jrnl/update/version': Functionality_of_Device.method_json_backend,
    # Журнал обновления ВПО загрузчика изделия +
    '/jrnl/update/loader': Functionality_of_Device.method_json_backend,

    # Журнал хранилища исходящих SMS сообщений +
    '/jrnl/sms/msg': Functionality_of_Device.method_json_backend,
    # Журнал отправки SMS сообщений +
    '/jrnl/sms/send': Functionality_of_Device.method_json_backend,
    # Журнал приема SMS сообщений +
    '/jrnl/sms/get': Functionality_of_Device.method_json_backend,

    # Журнал установки связи с MQTT брокером +
    '/jrnl/mqtt/connect': Functionality_of_Device.method_json_backend,
    # Журнал обмена сообщениями с MQTT брокером +
    '/jrnl/mqtt/message': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                      Информация о состоянии изделия
    # //////-----------------------------------------------------------------///////
    # # // Состояние линий питания
    # '/state/dout': Functionality_of_Device.settings_PowerLine_Status,

    # информации о времени - ОБЬЕДЕНИЛ В ОДИН КЛАСС
    # // Настройки информации о времени - получение
    '/state/time': Functionality_of_Device.method_json_backend,

    # // Информация о конфигурации системы
    '/state/system': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                   Зарядные станции - Не поддерживается в 31 СМАРТ
    # //////-----------------------------------------------------------------///////
    # # -Таблица зарядных станций - Переписал
    # '/settings/charge/table': Functionality_of_Device.settings_Charge_Station_Table,
    #
    # # # - Состояние зарядных станций - Переписал
    # '/charge/data/arch': Functionality_of_Device.settings_Charge_Station_Arch_Data,

    # ///////////////////////////////////////////////////////

    # /////////////////////ДОБАВИЛ///////////////////////////


    # //////-----------------------------------------------------------------///////
    #                   НЕ ЗАВЕЗЕНО ВО ФРОНТЕНД , НЕ ОТОБРАЖЕННО БЫЛО В ДОКЕ
    # //////-----------------------------------------------------------------///////

    # ВАЖНО
    # # // - Таблица аккаунтов SMTP - изменил на /settings/servers/smtp
    # '/settings/smtp': settings_Account_SMTP,

    # //////-----------------------------------------------------------------///////
    # ///////////////////// iec60870 ///////////////////////////
    #                      ПРОТОКОЛ МЭК - Не поддерживается в 31 СМАРТ
    # //////-----------------------------------------------------------------///////
    # # // - iec60870 - Работа с таблицей MapIOA - Переписал
    # '/settings/iec60870_5_104/mapioa': Functionality_of_Device.settings_Map_IOA,
    #
    # # // - iec60870 - работа с таблицей ValueDescription - переписал
    # '/settings/iec60870_5_104/value_description': Functionality_of_Device.settings_Value_Description,
    # # // - iec60870 - работа с таблицей TemplateName - переписал
    # '/settings/iec60870_5_104/template_name': Functionality_of_Device.settings_Template_Name,
    # # // - iec60870 - работа с таблицей COTTypes - переписал
    # '/settings/iec60870_5_104/cot_types': Functionality_of_Device.settings_COT_Types,
    # # // - iec60870 - работа с таблицей TypeIDTypes - переписал
    # '/settings/iec60870_5_104/type_id_types': Functionality_of_Device.settings_Type_ID_Types,
    #
    # # // - iec60870 - работа с таблицей Settings - Переписал
    # '/settings/iec60870_5_104/iec60870_settings': Functionality_of_Device.settings_IEC60870_Settings,
    #
    # # // - iec60870 - работа с таблицей IEC60870Template - Переписал
    # '/settings/iec60870_5_104/iec60870_template': Functionality_of_Device.settings_IEC60870_Template,
    #
    # # // - iec60870 - работа с таблицей IEC60870Template - Переписал
    # '/settings/iec60870_5_104/iec60870_cot_values': Functionality_of_Device.settings_IEC60870_COT_Values,
}
