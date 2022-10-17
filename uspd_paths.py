# файл является признаком синхронизации времени
# удаляется при старте системы
# создается при ручной установке времени и успешной синхронизации
# удаляется при ошибке синхронизации
_time_sync_path = "/tmp/uspd-time-sync"

# файл является признаком надежности времени
# удаляется при старте системы
# создается после старта системы, если проверка RTC показывает отсутствие ошибок
# создается при ручной установке времени и успешной синхронизации
_time_good_path = "/tmp/uspd-time-good"

# файл является процессом для работы c БД настроек ПУ (JSON API)
_meter_db_settings_path = "/etc/opt/uspd/meter_db_settings_api/meter_db_settings_api"

# файл является процессом для работы c БД данных ПУ (JSON API)
_meter_db_data_path = "/etc/opt/uspd/meter_db_data_api/meter_db_data_api"

# файл является процессом для опроса ПУ (JSON API)
_meter_devices_path = "/etc/opt/uspd/meterdev/meterdev"

# файл настроек управления линиями питания интерфейсов
_power_lines_settings_path = "/etc/opt/uspd/powerlines/cfg/powerlines"

# файл настроек chrony
_chrony_path = '/etc/chrony/uspd.conf'

# файл является процессом для работы c БД настроек системы событий (JSON API)
_event_db_settings_path = '/etc/opt/uspd/event_db_api/event_db_api'

# файл настроек TCP серверов
_tcp_nginx_path = '/etc/nginx/conf.d/tcp.conf'

# файл настроек сим-карт
_sim_settings_path = "/etc/opt/uspd/modem/uspd-modem.conf"

# Аккаунты почты - API для работы с БД настроек брокеров MQTT и аккаунтов почты SMTP
_messenger_db_api_path = "/etc/opt/uspd/messenger_db_api/messenger_db_api"

# скрипты настройки cron
_crontab_app_path = '/etc/opt/uspd/cronapp/crontab_refresh.sh'

# файл является процессом для работы c БД iec60870 (JSON API)
_iec60870_db_api_path = "/etc/opt/uspd/iec60870_db_api/iec60870_db_api"

# файл является процессом для работы c БД зарядных станций (JSON API)
_charge_stations_db_api_path = "/etc/opt/uspd/charge_stations_db_api/charge_stations_db_api"

# Файл отвечающий за настройки Интерфейсов
_interfaces_path = "/etc/network/interfaces"

# Скрипт обновления системы
_update_firmware_path = "/opt/uspd/update/run-fwupdate"

# Файл обновления системы
_firmware_file_path = "/opt/uspd/update/update.bin"

# Файл лога обновления системы
_log_update_firmware_path = "/opt/uspd/update/update-status.log"

# Файл лога обновления системы - Весь и подробный
_log_update_uspd_firmware_path = "/update.log"

# файл является процессом для работы c БД журналов УСПД ПУ (JSON API)
_journals_db_api_path = "/etc/opt/uspd/journals_db_api/journals_db_api"

# БД для хранения данных авторизации
_httpauth_db = "/var/opt/uspd/httpauthdb/httpauth.db"
