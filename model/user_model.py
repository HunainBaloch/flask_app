import _mysql_connector

class user_model():
    def __init__(self):
        # Connection Establishment code
        try:
            con = _mysql_connector.connect(host="localhost", user="root",password="",database="flask_tutorial")
            print("Connection Sucessful")
        except:
            print("Some Error")
    def user_getall_model(self):
        #Qurey execution code
        return "This is user_getall_model"