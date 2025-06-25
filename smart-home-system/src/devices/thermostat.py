class Thermostat:
    def __init__(self):
        self.temperature = 22  # Default temperature in Celsius

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"Thermostat set to {temp}°C.")

    def get_temperature(self):
        print(f"Current temperature: {self.temperature}°C.")
        return self.temperature