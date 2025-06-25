class Light:
    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.brightness = 100

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} light turned ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} light turned OFF.")

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.brightness = value
            print(f"{self.name} light brightness set to {value}%.")
        else:
            print("Brightness must be between 0 and 100.")