# ////////////////////////////////////////////////////////////////////////////////////////////
#                 Здесь работаем с Протоколом УМ-40 SMART
# ///////////////////////////////////////////////////////////////////////////////////////////
#
from USPD_UM40 import Functionality_of_Device

#     По УРЛ определяем наш запрос - Это важно

handlers_UM40 = {
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
    # Настройки ethernet
    '/settings/ip': Functionality_of_Device.method_json_backend,

    # Настройки Настройки цифровых интерфейсов - Не дописмал
    '/settings/uart': Functionality_of_Device.method_json_backend,

    # // Настройки линий питания
    '/settings/dout': Functionality_of_Device.method_json_backend,

    # // Настройки локального времени
    '/settings/time/local': Functionality_of_Device.method_json_backend,

    # //////////////////////   Настройки модема /////////////////////////////////

    # // Настройки СИМ Карты
    '/settings/modem/sim': Functionality_of_Device.method_json_backend,

    # //////////////////////   Клиенты и серверы /////////////////////////////////
    # // - Настройки HTTP сервера
    '/settings/servers/tcp': Functionality_of_Device.method_json_backend,

    # // Сервера синхронизации времени
    '/settings/servers/sntp': Functionality_of_Device.method_json_backend,

    # // - Таблица аккаунтов SMTP - Изначально было  - /settings/smtp
    '/settings/servers/smtp': Functionality_of_Device.method_json_backend,

    # // Настройки MQTT брокера
    '/settings/servers/mqtt': Functionality_of_Device.method_json_backend,

    # //////////////////////   Приборы учета /////////////////////////////////
    # // Переписал - Таблица Счетчиков
    '/settings/meter/table': Functionality_of_Device.method_json_backend,

    # //////////////////////   Система событий /////////////////////////////////

    # // - таблица Calendar в БД системы событий
    '/settings/events/calendar': Functionality_of_Device.method_json_backend,

    # // Настройки расписаний
    '/settings/events/schdl': Functionality_of_Device.method_json_backend,

    # // - Настройки - Настройка системы событий
    '/settings/events/manager': Functionality_of_Device.method_json_backend,

    # // Шаблоны приборов учета
    '/settings/templates/meter': Functionality_of_Device.method_json_backend,

    # //Шаблоны данных приборов учета
    '/settings/templates/arch': Functionality_of_Device.method_json_backend,

    # // - таблица MeterMessages в БД системы событий
    '/settings/templates/messages': Functionality_of_Device.method_json_backend,

    # //  таблица Email в БД системы событий
    '/settings/templates/email': Functionality_of_Device.method_json_backend,

    # // Опрос приборов учета по событиям
    '/settings/actions/meter': Functionality_of_Device.method_json_backend,

    # // Условия синхронизации времени
    # // ПОКА НЕТ ПОДДЕРЖКИ ВО ФРОНТЕНДЕ + НЕТ JSON протокола
    '/settings/actions/sntp': Functionality_of_Device.method_json_backend,

    # // -  таблица SMTPMeterMessages в БД системы событий
    '/settings/actions/smtp': Functionality_of_Device.method_json_backend,

    # // - таблица MQTTMeterMessages в БД системы событий
    '/settings/actions/mqtt': Functionality_of_Device.method_json_backend,
    # //////-----------------------------------------------------------------///////
    #                         Опрос приборов учета
    # //////-----------------------------------------------------------------///////

    # // Считывание - Архивные показатели
    '/meter/data/arch': Functionality_of_Device.method_json_backend,

    # // Считывание - Текущие показатели
    '/meter/data/moment': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                      Управление приборами учета
    # //////-----------------------------------------------------------------///////
    # // Задание времени -
    '/meter/settings/time': Functionality_of_Device.method_json_backend,

    # // Задание положения реле -
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

    # // - Перезагрузка устройства
    '/action/restart': Functionality_of_Device.method_json_backend,

    # //  информации о времени - перезапись
    '/action/time/set': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                            Журналы изделия
    # //////-----------------------------------------------------------------///////

    # // Журнал изменения времени
    '/jrnl/time': Functionality_of_Device.method_json_backend,
    # //Журнал ответов приборов учета
    '/jrnl/meter/answ': Functionality_of_Device.method_json_backend,
    # Журнал перезагрузок
    '/jrnl/reset': Functionality_of_Device.method_json_backend,
    # Журнал Системы событий
    '/jrnl/action': Functionality_of_Device.method_json_backend,
    # Не существующие журналы

    # Журнал сетевых подключений
    '/jrnl/srvconn': Functionality_of_Device.method_json_backend,
    # Журнал подключений PPP клиента (GPRS)
    '/jrnl/ppp/clconn': Functionality_of_Device.method_json_backend,
    # Журнал поднятия PPP-сервера (CSD)
    '/jrnl/ppp/srvconn': Functionality_of_Device.method_json_backend,
    # Журнал входящих вызовов (CSD)
    '/jrnl/call': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/sens': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/pwrline': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/power': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/charge': Functionality_of_Device.method_json_backend,
    # Журнал изменения состояния дискретных входов
    '/jrnl/din/open': Functionality_of_Device.method_json_backend,
    # Журнал авторизации (HTTP-сервер)
    '/jrnl/auth/json': Functionality_of_Device.method_json_backend,

    # Журнал хранилища почтовых сообщений
    '/jrnl/mail/msg': Functionality_of_Device.method_json_backend,
    # Журнал отправки почтовых сообщений
    '/jrnl/mail/send': Functionality_of_Device.method_json_backend,

    # Журнал изменения версии ВПО изделия
    '/jrnl/update/version': Functionality_of_Device.method_json_backend,
    # Журнал обновления ВПО загрузчика изделия
    '/jrnl/update/loader': Functionality_of_Device.method_json_backend,

    # Журнал хранилища исходящих SMS сообщений
    '/jrnl/sms/msg': Functionality_of_Device.method_json_backend,
    # Журнал отправки SMS сообщений
    '/jrnl/sms/send': Functionality_of_Device.method_json_backend,
    # Журнал приема SMS сообщений
    '/jrnl/sms/get': Functionality_of_Device.method_json_backend,

    # Журнал установки связи с MQTT брокером
    '/jrnl/mqtt/connect': Functionality_of_Device.method_json_backend,
    # Журнал обмена сообщениями с MQTT брокером
    '/jrnl/mqtt/message': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                      Информация о состоянии изделия
    # //////-----------------------------------------------------------------///////
    # // Состояние линий питания
    '/state/dout': Functionality_of_Device.method_json_backend,

    # // Настройки информации о времени - получение
    '/state/time': Functionality_of_Device.method_json_backend,

    # // Информация о конфигурации системы
    '/state/system': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                   Зарядные станции
    # //////-----------------------------------------------------------------///////
    # -Таблица зарядных станций
    '/settings/charge/table': Functionality_of_Device.method_json_backend,

    # # - Состояние зарядных станций
    '/charge/data/arch': Functionality_of_Device.method_json_backend,

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
    #                      ПРОТОКОЛ МЭК
    # //////-----------------------------------------------------------------///////
    # // - iec60870 - Работа с таблицей MapIOA
    '/settings/iec60870_5_104/mapioa': Functionality_of_Device.method_json_backend,

    # // - iec60870 - работа с таблицей ValueDescription
    '/settings/iec60870_5_104/value_description': Functionality_of_Device.method_json_backend,
    # // - iec60870 - работа с таблицей TemplateName
    '/settings/iec60870_5_104/template_name': Functionality_of_Device.method_json_backend,
    # // - iec60870 - работа с таблицей COTTypes
    '/settings/iec60870_5_104/cot_types': Functionality_of_Device.method_json_backend,
    # // - iec60870 - работа с таблицей TypeIDTypes
    '/settings/iec60870_5_104/type_id_types': Functionality_of_Device.method_json_backend,

    # // - iec60870 - работа с таблицей Settings
    '/settings/iec60870_5_104/iec60870_settings': Functionality_of_Device.method_json_backend,

    # // - iec60870 - работа с таблицей IEC60870Template
    '/settings/iec60870_5_104/iec60870_template': Functionality_of_Device.method_json_backend,

    # // - iec60870 - работа с таблицей IEC60870Template
    '/settings/iec60870_5_104/iec60870_cot_values': Functionality_of_Device.method_json_backend,

    # //////-----------------------------------------------------------------///////
    #                           Обновление ПО
    # //////-----------------------------------------------------------------///////
    # Обновление ПО + Лог обновления
    '/upload/firmware': Functionality_of_Device.method_json_backend,

    # Подробный лог последней установки, зашифорованный, для передачи в техподдержку
    '/download/fwupdatelog': Functionality_of_Device.method_json_backend,
}
