class Dagger:
    def __init__(self):
        # Initialize health using the health property
        self.__health = 5
        # Lambda function to add two numbers
        self.healing_amount = lambda x, y: x + y
        # Private lambda function to multiply two numbers
        self.__multiplier = lambda x, y: x * y

    def do_damage(self):
        return self.__multiplier(5, 3)
    
    def heal(self):
        self.__health += self.healing_amount(self.__health, 5)
        return self.__health

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        print("Health cannot be set directly")
