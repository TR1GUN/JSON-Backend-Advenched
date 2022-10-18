from flask import Flask , request , make_response


app = Flask(__name__)

from USPD_Protocol_Frontend  import handlers_frontend

urls_frontend = list(handlers_frontend.keys())
for url in urls_frontend :
    app.add_url_rule(url, view_func=handlers_frontend[url] , methods=["GET"])

@app.route('/settings/proto/json/auth', methods=["GET", "POST","PUT","DELETE"])
def index():
    html_content = """"""
    code = 200
    print("goovno2")
    print(request.url)
    if request.method == "PUT":
        print(request.json)

    lol = {'Settings': [{'id': 1, 'login': '22', 'password': '22', 'lvl': 0}]}
    return (lol, 200, {'Content-Type': "application/json"})


if __name__ == '__main__':
    app.debug = True
    app.run()
    print("goovno")
