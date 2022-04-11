import serial
import matplotlib.pyplot as plt
import time


arduino = serial.Serial('COM3', 9600, timeout=1)
print('Conectado')
point = 0
fig, ax = plt.subplots()
plt.ion()

maxlen = 40
x = []
y = []

while True:
    data = arduino.readline().decode().strip()
    time.sleep(1)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title('Lecturas de Temperatura')
    if data:
        data = float(data)
        print(data)
        x.append(point)
        y.append(data)
        if len(x) > maxlen:
            x = x[1:]
            y = y[1:]
        plt.plot(x, y, color='r')
        point += 1
        plt.pause(0.05)
      

        ax.clear()
        plt.ylim([0, 50])
        plt.show()