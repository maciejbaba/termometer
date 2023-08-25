# Arduino DHT11 Thermometer with Python Server

A precise and responsive thermometer system built using the DHT11 sensor with an Arduino Nano microcontroller. This system communicates the temperature readings to a Python-based server which then makes the data accessible within your local WiFi network.

## 🌟 Features

- **DHT11 Sensor**: Accurate temperature readings with low latency.
- **Arduino Nano Integration**: Compact and efficient microcontroller to process and send data.
- **Python Server**: A lightweight server to serve temperature data.
- **Local WiFi Access**: View temperature data on any device connected to your local WiFi.

## 🛠️ Setup and Run

### Prerequisites

- Arduino IDE
- Python 3.x with `pip`
- Arduino Nano with DHT11 sensor connected

### Instructions

1. **Setup the Arduino**:

   - Connect the DHT11 sensor to your Arduino Nano.
   - Load the provided Arduino code onto the Nano using the Arduino IDE.

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/maciejbaba/termometer.git
   ```

3. **Setup the Python Server**:

   - Navigate to the project directory:
     ```bash
     cd termometer
     ```
   - Install necessary Python packages:
     ```bash
     pip install flask pyserial
     ```
   - Run the server:
     ```bash
     python3 server.py
     ```

4. **Accessing Data**:
   - Connect any device to your local WiFi.
   - Open a web browser and navigate to the server IP and port to view the temperature data.

## 📐 How it Works

The DHT11 sensor captures temperature data which is read and processed by the Arduino Nano. The Nano then sends this data to the Python server over a serial connection. The server then makes this data available to any device connected to the local WiFi network by serving simple HTML page with the temperature data.

## 🤝 Contributing

If you have suggestions for how this project could be improved, or want to report a bug, open an issue! Contributions of all kinds are welcomed!

## 📜 License

This project is open-source and is licensed under the MIT License.

## 🙏 Acknowledgements

- [Arduino community](https://www.arduino.cc/) for their extensive resources and examples.
- DHT11 sensor documentation and community.
- Python community for providing an incredible platform for building server applications.
