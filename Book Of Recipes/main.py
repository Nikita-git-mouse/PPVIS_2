from Interface import ManagingElements
from BookRecipeModel import ModelCookBook
import Model
import Controller
import View


class DisplayingCookBook:
    def __init__(self):
        self.__managing_elements = ManagingElements()
        self.modelCookBook = ModelCookBook()
       

    def work(self):
        self.__managing_elements.window.mainloop()


if __name__ == '__main__':
    DisplayingCookBook().work()
