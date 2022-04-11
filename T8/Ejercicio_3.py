from matplotlib import image
import pyfirmata
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image

PAUSA = 2 # Número de segundos entre tomas de lectura
           # de temperatura.

hot = 23
cold = 20

placa = pyfirmata.Arduino('COM3')

pyfirmata.util.Iterator(placa).start()

entrada = placa.get_pin('a:0:i')
entrada.enable_reporting()
Led1 = placa.digital[11]
Led2 = placa.digital[12]
Led3 = placa.digital[13]

def volts_to_celsius(v):
    """Convierte un voltaje v obtenido de un sensor
       TMP36 a grados Celsius.
    """
    return 100 * (v - 0.5)

def imge():
    ventana = Tk()
    ventana.title('Horny')
    ventana.iconbitmap(r'D:\SEMESTRES\5TO SEMESTRE\Programación 3\Python\T8\calorcito.ico')
    
    imagen = ImageTk.PhotoImage(Image.open(r'D:\SEMESTRES\5TO SEMESTRE\Programación 3\Python\T8\Calor.png').resize((500,500)))
    boton = Button(image=imagen, command=ventana.quit)
    boton.pack()
    ventana.mainloop()

try:
    while True:
        d = datetime.now()
        v = entrada.read()
        if v != None:
            v *= 5 # Convertir el valor devuelto por
                   # read() a voltios.

            c = volts_to_celsius(v)
            print('{}, {:.3f} V, {:.2f} °C'
                  .format(d, v, c))
            placa.pass_time(PAUSA)
            if c < cold:
                Led1.write(1)
                Led2.write(0)
                Led3.write(0)

            elif c >= hot:
                Led1.write(0)
                Led2.write(0)
                Led3.write(1)
                print (imge())
            else:
                Led1.write(0)
                Led2.write(1)
                Led3.write(0)

        

except KeyboardInterrupt:
    # Terminar programa cuando se presione Ctrl-C.
    pass

finally:
    placa.exit()