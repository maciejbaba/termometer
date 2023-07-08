from flask import Flask
import serial

app = Flask(__name__)


@app.route("/")
def index():
    arduino = serial.Serial("/dev/ttyUSB0", 9600)
    arduino_data = arduino.readline()
    data = arduino_data.decode("utf-8")
    list = data.split(" ")
    temp = list[0]
    hum = list[1]
    json = '{"temp":' + temp + ',"hum":' + hum + "}"
    return json


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
