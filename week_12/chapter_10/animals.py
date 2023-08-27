class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
       print("i am a", self.__species)


    def make_sound(self):
        print('Grrrrrrrrrr')


class Dog(Mammal):
  def __init__(self):
     Mammal.__init__(self, 'Dog')

  def make_sound(self):
     print('Woof Woof')

class Cat(Mammal):
   def __init__(self):
      Mammal.__init__(self, 'Cat')

   def make_sound(self):
      print('Meow Meow')


def show_mammal_info(creature):
  if isinstance(creature, Mammal):
    creature.show_species()
    creature.make_sound()
  else:
     print("That is not a Mammal!")


def main():
    dog = Dog()
    show_mammal_info(dog)

    cat = Cat()
    show_mammal_info(cat)

    show_mammal_info('paper');

main()
