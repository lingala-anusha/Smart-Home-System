# 🏠 Smart Home System

This project is a smart home system built using Python. It allows users to control various devices in their home, such as lights, thermostat, and security systems, through a simple interface.

## ✨ Features

- 💡 Control smart lights (turn on/off and adjust brightness)
- 🌡️ Manage home temperature with a thermostat
- 🔒 Monitor and control the security system (arm/disarm and check status)

## 📂 Project Structure

```
smart-home-system
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── devices
│   │   ├── __init__.py
│   │   ├── lights.py
│   │   ├── thermostat.py
│   │   └── security.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── home_controller.py
│   └── utils
│       ├── __init__.py
│       └── logger.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd smart-home-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

To run the smart home system, execute the following command:
```bash
python src/main.py
```

Follow the on-screen instructions to interact with the smart home devices.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.
```