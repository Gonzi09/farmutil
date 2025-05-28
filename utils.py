# from flask import Flask, request
# import serial
# import time
# import serial.tools.list_ports

# app = Flask(__name__)

# def detectar_puerto_arduino():
#     puertos = serial.tools.list_ports.comports()
#     for puerto in puertos:
#         if "Arduino" in puerto.description or "ttyACM" in puerto.device or "ttyUSB" in puerto.device:
#             return puerto.device
#     return None

# puerto = detectar_puerto_arduino()
# if not puerto:
#     print("No se encontró el Arduino.")
#     exit()

# arduino = serial.Serial(puerto, 115200, timeout=2)
# time.sleep(2)

# @app.route("/comando", methods=["POST"])
# def enviar_comando():
#     cmd = request.form.get("cmd")
#     if not cmd:
#         return "No se recibió ningún comando", 400

#     arduino.write((cmd + '\n').encode())
#     time.sleep(0.5)
#     respuesta = ""
#     while arduino.in_waiting:
#         respuesta += arduino.readline().decode()
#     return respuesta or "Comando enviado pero sin respuesta."

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

import serial
import time
import serial.tools.list_ports

def detectar_puerto_arduino():
    puertos = serial.tools.list_ports.comports()
    for puerto in puertos:
        if "Arduino" in puerto.description or "ttyACM" in puerto.device or "ttyUSB" in puerto.device:
            return puerto.device
    return None

puerto = detectar_puerto_arduino()
if not puerto:
    print("❌ No se encontró el Arduino.")
    exit()

arduino = serial.Serial(puerto, 115200, timeout=2)
time.sleep(2)

comando = input("Escribe un comando para enviar (ej: X100, P2000, H, C, R): ")
arduino.write((comando + '\n').encode())

time.sleep(0.5)
while arduino.in_waiting:
    respuesta = arduino.readline().decode().strip()
    print("Arduino:", respuesta)

arduino.close()