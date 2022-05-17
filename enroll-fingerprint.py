
# ! The main thing is to do a connection with the database and show access to the data, in this case it will use a JSON file for simplicity
from Board import Board
from json import loads, JSONDecodeError
from User import User
from Database import ConnectionDB

if __name__ == '__main__':
    # todo: to check out if the information received has the format required to get the ID
    def id_validation():
        id = input("\nInsert a ID to save: ")
        if int(id) <= 0 or int(id) > 127:
            print("Invalid number insert a new one again")
            return id_validation()
        else:
            return id

    def handle_id():
        # ? Reeding each line sent by the Arduino, then replacing the simple quotes for double quotes instead
        reading: str = board.str_readline().replace("'", '"')
        print(reading)

        if reading == "---SOLICITING READING---":
            id = id_validation()
            board.write(bytes(id, 'utf-8'))
        # ? Trying to convert the string into a dictionary
        finger_ID: dict
        try:
            finger_ID = loads(reading)
            # ? If "finger_ID" has "id" key means that is an id, therefore we can create the user and save the db
            if "id" in finger_ID:
                newUser = User(finger_ID['id'])
                Database.add_in_db(newUser)
                Database.save_db()

        except JSONDecodeError:
            #print("There was an error converting to json")
            pass

    # Initializating the DB
    PATH = "./database/database.json"
    Database = ConnectionDB(PATH)
    users: list = Database.load_db()

    # Initalizating the Board
    board = Board('COM3', 9600)
    board.add_predicate(handle_id)
    board.start()
