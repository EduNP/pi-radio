import os
import json
import RPi.GPIO as GPIO
import time

#Get user's input and display led colors to give response 
def getUserInput():
    while True:
        #Select a station
        #Led VERDE
        GPIO.output(14,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)

        selectedStation = input("Selecione")
        try:
            selectedStation = int(selectedStation)
            if selectedStation >= 0 and selectedStation < len(stations):
                #Led Azul
                GPIO.output(14,GPIO.LOW)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(18,GPIO.LOW)
                time.sleep(0.5)
                return selectedStation
            else:
                #LED VERMELHO
                GPIO.output(14,GPIO.HIGH)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(18,GPIO.LOW)
                time.sleep(2)
                print("Estacao nao existe")
        except:
            #LED VERMELHO
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            time.sleep(2)
            print("Entrada invalida")
            continue
#Led IO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT) #Vermelho
GPIO.setup(15,GPIO.OUT) #Azul
GPIO.setup(18,GPIO.OUT) #Verde

GPIO.output(14,GPIO.HIGH)
GPIO.output(15,GPIO.LOW)
GPIO.output(18,GPIO.LOW)

#Files Names
stationFile = "TEMP_STATION"
stationsList = "radios.json"

stations = []

#Load json
try:
    with open(stationsList,"r") as file:
        stations = json.load(file)
except:
    #Ocorreu um erro, sem lista
    print("Ocorreu um erro ao ler a lista de estacoes")
    exit()

#Load last selected station
try:
    selectRadio = int(open(stationFile, "r").read())
except:
    selectRadio = 0


while True:
    os.system("killall vlc") #Kill VLC process
    os.system(f"cvlc {stations[selectRadio]['url']} > /dev/null &")#Open VLC process

    #Salva radio selecionada
    with open(stationFile, "w") as file:
        file.write(f"{selectRadio}")

    selectRadio = getUserInput()




