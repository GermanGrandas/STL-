import time
import serial
import principal

#se configura la conexion

puerto = raw_input("Ingrese el puerto COM:")

ser = serial.Serial(puerto-1,9600,serial.EIGHTBITS,serial.PARITY_EVEN,serial.STOPBITS_TWO)

ser.isOpen()

print ('Enter your commands below.\r\nInsert send for send the points\r\nInsert "exit" to leave the application.')

input=1
while 1 :

    puntos = principal.main()
    input = raw_input(">>")
    if input == 'exit':
        ser.close()
        exit()
    if input == 'send':
        print('Sending')
        maxtime = 0
        for elemento in puntos:
            for x in elemento:
                if x > maxtime:
                    maxtime = x
        maxtime = int(round(maxtime))
        print maxtime
        i = 0
        k = 0
        send = True
        while(k < len(puntos)):
            if send:
                if puntos[k][0] <0:
                    ser.write(bytearray([0]) + bytearray([int(abs(puntos[k][0]))]))
                    if puntos[k][1] < 0:
                        ser.write(bytearray([0]) + bytearray([int(abs(puntos[k][1]))]))
                    else:
                        ser.write(bytearray([1])+bytearray([int(abs(puntos[k][1]))]))
                else:
                    ser.write(bytearray([1])+bytearray([int(abs(puntos[k][0]))]))
                    if puntos[k][1] < 0:
                        ser.write(bytearray([0])+bytearray([int(abs(puntos[k][1]))]))
                    else:
                        ser.write(bytearray([1])+bytearray([int(abs(puntos[k][1]))]))
                send = False
            if i < maxtime:
                i +=1
                k+=i
            if i == maxtime:
                send = True
                i= 0

            #ser.write(str(elemento) +'\r\n' )
        print('Finish',k)

    else:
         #is requested by my device)
        ser.write(input + '\r\n')
        out = ''
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)
        if out != '':
            print (">>" + out)
