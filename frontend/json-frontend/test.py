import os

directory = os.getcwd()

for element in os.scandir(directory):

    if element.is_file():

        # path = str(directory) +"/"+ element.name



        # print(path)
        print("\"" + element.name + "\" : \"" + element.name + "\" , ")



# html_path = "/Users/trigun-d/PycharmProjects/pythonFlask/frontend/json-frontend/main.html"
#
# html_file = open(html_path)
# html_file.read()
#
#
# print()