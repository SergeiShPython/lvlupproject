import json

class User:
    def __init__(self, username, user_id):
        self.username = username
        self.iser_id = user_id
    def __str__(self):
        return f"{self.username} - {self.iser_id}"
    
    def __repr__(self):
        return self.__str__()

class DB_User:
    def __init__(self):
        self.users = self.__get()

    def add_user(self,user):
        if user not in self.users:
            self.users.append(user)
            self.__save()

    def __save(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file)

    def __get():
        with open('users.json', 'r') as file:
            return json.load(file)
        
    def __str__(self):
        return str(self.users)

db_user = DB_User()