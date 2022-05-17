
from User import User
from json import loads, dumps


class ConnectionDB:

    def __init__(self, path: str):
        self.path = path
        self.users: list = []

    def check_in_db(self, key: str, searched):
        idx = 0
        for e in self.users:
            if e[key] == searched:
                #print('Found!')
                return idx
            idx += 1
        return False

    def add_in_db(self, user: User):
        # Before adding a new user into the db, it's necessary to check out the user id, if that id is already into the db, replace it otherwise append it
        user_index = self.check_in_db('id', user.id)
        if user_index:
            #print("That id already exists, replace that user")
            self.users[user_index] = user.get_dict()
            return
        self.users.append(user.get_dict())

    def load_db(self):
        loaded: list = self.__open_db('r')
        self.users = loads(loaded)

    def __open_db(self, mode: str):
        with open(self.path, mode, encoding='utf-8') as f:
            return f.read()

    def save_db(self):
        dumped_users = dumps(self.users, indent=4)
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(dumped_users)

    def watch_content(self):
        return dumps(self.users, indent=4)
