# Здесь описаны основные функции работы с Фронтендом
def FrontendManager(url):
    """
    Менеджер работы со страницами фронтенда
    :return:
    """
    # сам файл контента что возвращаем
    html_path = ""
    url = str(url)
    if url == "/":
        url = "/main"

    # обозначаем путь до папки с пакетом нашего фронтенда
    frontend_path = "C:\\Users\\KDFX Team\\PycharmProjects\\JSON-Backend-Advenched\\frontend\json-frontend\\"


    # получаем HTML страницу по данному URL
    html_name_file = str(url)[1:]
    print(html_name_file)
    # если по данному URL нашли файл - читаем его
    if html_name_file:
        # первое - делаем полный путь
        html_path = frontend_path + html_name_file

    # возвращаем контент
    return html_path

from flask import request

# Первая функция - Работает ТОЛЬКО С HTML Страницами
def Static_File_to_Page():
        """
        :param HTML_content:
        :return:
        """
        url = request.url_rule
        file = str(url)[1:]
        print()
        import os
        from flask import send_from_directory

        html_path = "C:\\Users\\KDFX Team\\PycharmProjects\\JSON-Backend-Advenched\\frontend\json-frontend\\"
        return send_from_directory(html_path,
                                   file, mimetype='image/x-icon')

def Javascript_response():
    """
    :param HTML_content:
        :return:
    """
    url = request.url_rule
    file =  str(url)[1:]
    print()
    import os
    from flask import send_from_directory

    html_path = "C:\\Users\\KDFX Team\\PycharmProjects\\JSON-Backend-Advenched\\frontend\json-frontend\\"
    return send_from_directory(html_path,
                              file, mimetype='application/javascript')


def HTML_Page():
    """
    :param HTML_content:
    :return:
    """
    uri = request.url_rule

    print("---->", uri)
    html_path = FrontendManager(uri) + ".html"
    print("---->", html_path)
    # открываем файл
    html_file = open(html_path, encoding="utf-8")
    # читаем его
    html_content = html_file.read()

    return(html_content, 200, {'Content-Type': "text/html"})