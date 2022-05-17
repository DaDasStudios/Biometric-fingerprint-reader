
# ! Here is where we will just be listening to serial port and formatting data, depending of the case we can take rules, for example
# ! we can show the user information whenever we listen to a id sent by the board via serial port

from Board import Board
from json import loads, JSONDecodeError
from User import User
from Database import ConnectionDB
from tkinter import Tk, Label, LabelFrame, Frame
from PIL import Image, ImageTk


class App():
    def __init__(self, window: Tk):
        self.wind = window
        self.wind.title("Show user information")
        self.wind.resizable(0, 0)

    def build_user_information(self, user: User):
        print(user.get_dict())
        # Main frame
        self.main = LabelFrame(self.wind, text='Información del usuario')
        self.main.grid(row=0, column=0, pady=5, padx=5)

        # ? Frame of photo
        self.frame_photo = Frame(self.main)
        self.frame_photo.grid(row=0, column=0)

        # Photo
        img = Image.open(user.photo)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)
        panel = Label(self.frame_photo, image=img)
        panel.image = img
        panel.pack()

        # ? Frame of text information
        self.frame_information = Frame(self.main)
        self.frame_information.grid(row=0, column=1)

        # Fingerprint
        Label(self.frame_information, text="Huella N°:").grid(
            row=0, column=0, padx=10, pady=10)
        Label(self.frame_information, text=user.id).grid(
            row=0, column=1, padx=10, pady=10)

        # Code
        Label(self.frame_information, text="Código:").grid(
            row=1, column=0, padx=10, pady=10)
        Label(self.frame_information, text=user.code).grid(
            row=1, column=1, padx=10, pady=10)

        # Name
        Label(self.frame_information, text="Nombre:").grid(
            row=2, column=0, padx=10, pady=10)
        Label(self.frame_information, text=user.name).grid(
            row=2, column=1, padx=10, pady=10)

        # Age
        Label(self.frame_information, text="Edad:").grid(
            row=3, column=0, padx=10, pady=10)
        Label(self.frame_information, text=user.age).grid(
            row=3, column=1, padx=10, pady=10)

        # Carrer
        Label(self.frame_information, text="Carrera:").grid(
            row=4, column=0, padx=10, pady=10)
        Label(self.frame_information, text=user.carrer).grid(
            row=4, column=1, padx=10, pady=10)

        # Semester
        Label(self.frame_information, text="Semestre:").grid(
            row=5, column=0, padx=10, pady=10)
        Label(self.frame_information, text=user.semester).grid(
            row=5, column=1, padx=10, pady=10)

    def run(self):
        self.wind.mainloop()


if __name__ == '__main__':
    def handle_information():
        reading = board.str_readline().replace("'", '"')
        print(reading)
        scope: dict
        try:
            scope = loads(reading)
            if "auth" in scope and "id" in scope:
                if scope["auth"] == "success":
                    # ? If the authentication of doing reading of fingerprint is successful, we can show that user on scree
                    id = scope['id']
                    user_index = Database.check_in_db('id', id)
                    user_information = Database.users[user_index]
                    user = User(
                        user_information['id'],
                        user_information['code'],
                        user_information['name'],
                        user_information['age'],
                        user_information['carrer'],
                        user_information['semester'],
                        user_information['photo']
                    )

                    # ! Creating the window where the information will be located
                    window = Tk()
                    app = App(window)
                    app.build_user_information(user)
                    app.run()
                    print("\n --- Waiting for another fingerprint --- \n")

        except JSONDecodeError:
            pass

    # Initializating the DB
    PATH = "./database/database.json"
    Database = ConnectionDB(PATH)
    users: list = Database.load_db()

    board = 0
    # Initalizating the Board
    board = Board('COM3', 9600)
    board.add_predicate(handle_information)
    board.start(350)
