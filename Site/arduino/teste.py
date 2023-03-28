import serial #Importa a biblioteca
while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM3', 9600)
        print('Arduino conectado')
        break
    except:
        print('a')
while True: #Loop principal
    with open('arduino/comodo.txt','r') as file:
        cmd = file.readline()
        if 'Quarto' in cmd:
            if 'False' in cmd:
                arduino.write('h'.encode())
            elif 'True' in cmd:
                arduino.write('g'.encode())
        if 'Sala' in cmd:
            if 'False' in cmd:
                arduino.write('e'.encode())
            elif 'True' in cmd:
                arduino.write('w'.encode())
        if 'Cozinha' in cmd:
            if 'False' in cmd:
                arduino.write('n'.encode())
            elif 'True' in cmd:
                arduino.write('b'.encode())                                   
        print(str(arduino.readline())[2:-5])
        arduino.flush()