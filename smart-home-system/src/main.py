from controllers.home_controller import HomeController

def main():
    controller = HomeController()
    while True:
        print("\nSmart Home System")
        print("1. Control Lights")
        print("2. Control Thermostat")
        print("3. Control Security System")
        print("4. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            controller.control_lights()
        elif choice == "2":
            controller.control_thermostat()
        elif choice == "3":
            controller.control_security()
        elif choice == "4":
            print("Exiting Smart Home System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()