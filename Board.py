
from typing import Callable
from time import sleep
import serial


class Board(serial.Serial):
    def __init__(self, port: str, baudrate: int):
        # ? Running the __init__ function of the super class, then setting up the esciental parameters
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        sleep(0.2)
        self.open()

        # * The callbacks array where the functions are located
        self.__predicates: list = [
            lambda: print("You still don't have any predicate")
        ]
        self.__times_predicates = 0

    def __is_callable(self, predicate: Callable):
        if not callable(predicate):
            raise Exception("The predicate is not callable")
        return True

    def __handle_predicates_empty(self):
        if len(self.__predicates) == 0:
            self.add_predicate(lambda: print(
                "You still don't have any predicate"))

    def add_predicate(self, predicate: Callable):
        # Once you've added a predicate, the first predicate needs to be deleted automatically
        self.__is_callable(predicate)
        if self.__times_predicates == 0:
            self.del_predicate(0)
            self.__times_predicates += 1
        self.__predicates.append(predicate)

    def set_predicate(self, predicate: Callable, which: int):
        self.__is_callable(predicate)
        if self.__times_predicates == 0:
            self.del_predicate(0)
            self.__times_predicates += 1
        self.__predicates[which] = predicate

    def del_predicate(self, which: int):
        self.__handle_predicates_empty()
        self.__times_predicates += 1
        self.__predicates[which] = lambda: None

    def delall_predicates(self):
        self.__predicates.clear()
        self.__handle_predicates_empty()
        self.__times_predicates = 0

    def get_predicates(self):
        return self.__predicates

    # ? Important functions

    def start(self, stop: int = -1):
        cont: int = 0
        while True:
            # Run each predicate of the array
            for predicate in self.__predicates:
                predicate()
            if cont == stop:
                break
            cont += 1
            sleep(0.01)
        self.close()

    def str_readline(self):
        return self.readline().decode('utf-8').rstrip()


if __name__ == '__main__':
    def show_predicates():
        for predicate in board.get_predicates():
            predicate()

    board = Board('COM3', 9600)
    show_predicates()

    # Adding a new predicate
    board.add_predicate(lambda: print("Second predicate"))
    print("\nWe've added a new predicate\n")
    show_predicates()

    # Setting a predicate
    board.set_predicate(lambda: print("Modified predicate"), 1)
    print("\nWe've modified a existing predicate\n")
    show_predicates()

    # Deleting a predicate
    board.del_predicate(0)
    print("\nWe've deleted a predicate\n")
    show_predicates()

    # Run the programm
    board.delall_predicates()
    board.add_predicate(lambda: print("Frist predicate"))
    board.add_predicate(lambda: print("Second predicate"))
    board.add_predicate(lambda: print("Third predicate"))
    board.start(100)
