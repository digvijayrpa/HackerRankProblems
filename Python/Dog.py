class Dog:
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
    
    def speak(self):
        return self.speakText
    
    def getName(self):
        return self.name
    
    def birthDate(self):
        return str(self.day)+"/"+str(self.month)+"/"+str(self.year)
    
    def changeBark(self, bark):
        self.speakText = bark

    def __add__(self, otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, \
                   self.month, self.day, self.year + 1, \
                   self.speakText + otherDog.speakText)
def main():
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOF")
    girlDog = Dog("Sequoia", 8, 6, 2004, "barkbark")
    print("BD " + boyDog.speak())
    print("GD " + girlDog.speak())
    print("BD " + boyDog.birthDate())
    print("GD " + girlDog.birthDate())
    boyDog.changeBark("woofywoofy")
    print("BD " + boyDog.speak())
    puppy = boyDog + girlDog
    print("PD " + puppy.speak())
    print("PD " + puppy.getName())
    print("PD " + puppy.birthDate())

if __name__ == "__main__":
    main()