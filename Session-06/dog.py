class Dog:
    def __init__(self, the_name, the_age):
        self.name = the_name
        self.age = the_age

    def say_your_name(self):
        print("I'm {}, and I'm sitting down here".format(self.name))

    def show_your_age(self):
        print("I'm {} years old".format(self.age))

    def say_what_you_like(self):
        print("I like aritmetric!")

    def multiply(self, first_operand, second_operand):
        print(f'Easy!, the result is {first_operand * second_operand}')
        # print("The result is", first_operand * second_operand) it is the same thing from ^

ares = Dog('ares',18)
ares.say_your_name()
ares.show_your_age()
ares.say_what_you_like()
ares.multiply(3,5)