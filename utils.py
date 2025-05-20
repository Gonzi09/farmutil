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