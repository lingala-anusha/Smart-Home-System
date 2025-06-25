class SecuritySystem:
    def __init__(self):
        self.armed = False

    def arm(self):
        self.armed = True
        print("Security system ARMED.")

    def disarm(self):
        self.armed = False
        print("Security system DISARMED.")

    def status(self):
        status = "ARMED" if self.armed else "DISARMED"
        print(f"Security system is {status}.")
        return status