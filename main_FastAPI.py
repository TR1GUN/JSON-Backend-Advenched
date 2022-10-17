from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# ----- страница не найдена -------------
HTML_404_PAGE = "<h1>404</h1>"


def not_found(request, exc):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)


exceptions = {
    404: not_found,
}

# --------------

app = FastAPI(exception_handlers=exceptions)

from Frontend_manager import JSONFrontend
Frontend = JSONFrontend()
app.include_router(Frontend.router)


def do_work():

    print('ujdyj ')

@app.get("/http.js")
def Javascript_response():
    """
    :param HTML_content:
    :return:
    """
    print("ето мой запрос")

    from fastapi.responses import FileResponse
    from Frontend_manager import FrontendJavascriptManager
    from fastapi import requests
    file_path = FrontendJavascriptManager("http.js")

    return FileResponse(path=file_path, status_code=200, media_type="application/javascript")

@app.get("/favicon.ico")
def Icon_response():
    """
    :param HTML_content:
    :return:
    """
    print("ето мой запрос")

    from fastapi.responses import FileResponse
    from Frontend_manager import FrontendStaticFileManager

    from fastapi import requests
    file_path = FrontendStaticFileManager("favicon.ico")

    return FileResponse(path=file_path, status_code=200, media_type="image/x-icon")


@app.get("/settings/{lol1}/{lol2}/{lol3}")
def JSON_proto_response():
    """
    :return:
    """
    from fastapi.responses import JSONResponse
    response = {"Settings":[]}
    return JSONResponse(content = response, status_code=200, media_type="application/json")

# @app.get("/")
# def read_root():
#     html_path = "/Users/trigun-d/PycharmProjects/pythonFlask/frontend/json-frontend/main.html"
#
#     # html_content = open(html_path)
#     #
#     # print(html_content)
#
#     html_content = """
#         <html>
#             <head>
#                 <title>Some HTML in here</title>
#             </head>
#             <body>
#                 <h1>Look ma! HTML!</h1>
#             </body>
#         </html>
#         """
#
#     html_path = "/Users/trigun-d/PycharmProjects/pythonFlask/frontend/json-frontend/main.html"
#
#     html_file = open(html_path)
#     html_content = html_file.read()
#
#     return HTMLResponse(content=html_content, status_code=200)
#
#

