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

    website = (
        """
    <html>
      <head>
        <title>DHT11 Weather Station</title>
        <meta name="viewport" content="device-width,initial-scale=1" />
        <style>
          body {
              margin-top: 35vh;
              background-color: #000000;
              font-family: "Open Sans", sans-serif;
              font-size: 2rem;
              color: #ffffff;
          }
          h1 {
              text-align: center;
              font-weight: 300;
          }
          p {
              text-align: center;
          }
        </style>
      </head>
      <body>
        <h1>DHT11 Weather Station</h1>
        <p><strong>Temperature:</strong> """
        + temp
        + """°C</p>
        <p><strong>Humidity:</strong> """
        + hum
        + """%</p>
      </body>
    </html>"""
    )

    return website


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
