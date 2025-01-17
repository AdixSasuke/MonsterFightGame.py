from Animal import *

zoo : Animal = []
dog = Animal()
dog2 = Dog()
bird = Bird()
lion = Lion ()
zoo.append(dog)
zoo.append(dog2)
zoo.append(bird)
zoo.append(lion)

for animal in zoo:
    animal.talk()