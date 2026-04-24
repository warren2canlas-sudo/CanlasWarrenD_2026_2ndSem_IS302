class Animal_wdc:
    def __init__(self_wdc, name_wdc):
        self_wdc.name_wdc = name_wdc

    def speak_wdc(self_wdc):
        print(self_wdc.name_wdc, "makes a sound")


class Dog_wdc(Animal_wdc):
    def bark_wdc(self_wdc):
        print(self_wdc.name_wdc, "barks")


dog1_wdc = Dog_wdc("Buddy")
dog1_wdc.speak_wdc()
dog1_wdc.bark_wdc()