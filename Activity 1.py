"""Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions."""
class any_class:
    __privateVar = 25

    def __privMeth(self):
        print("This is a private message")
    def hello(self):
        print("The value of the private variable is ", self.__privateVar)

good = any_class()
good.hello()
good.__privMeth()