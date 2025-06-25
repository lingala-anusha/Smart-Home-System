from devices.lights import Light
from devices.thermostat import Thermostat
from devices.security import SecuritySystem

class HomeController:
    def __init__(self):
        self.lights = [Light("Living Room"), Light("Bedroom")]
        self.thermostat = Thermostat()
        self.security = SecuritySystem()

    def control_lights(self):
        for idx, light in enumerate(self.lights):
            print(f"{idx+1}. {light.name} (ON)" if light.is_on else f"{idx+1}. {light.name} (OFF)")
        choice = int(input("Select light to control (number): ")) - 1
        if 0 <= choice < len(self.lights):
            action = input("Enter 'on', 'off', or 'brightness': ").strip().lower()
            if action == "on":
                self.lights[choice].turn_on()
            elif action == "off":
                self.lights[choice].turn_off()
            elif action == "brightness":
                value = int(input("Enter brightness (0-100): "))
                self.lights[choice].set_brightness(value)
            else:
                print("Invalid action.")
        else:
            print("Invalid light selection.")

    def control_thermostat(self):
        temp = int(input("Set thermostat temperature (°C): "))
        self.thermostat.set_temperature(temp)

    def control_security(self):
        action = input("Enter 'arm', 'disarm', or 'status': ").strip().lower()
        if action == "arm":
            self.security.arm()
        elif action == "disarm":
            self.security.disarm()
        elif action == "status":
            self.security.status()
        else:
            print("Invalid action.")