import os
import json

def getUserInput():
    while True:
        #TODO
        #Selecione uma radio:
        selectedStation = input("Selecione")
        try:
            selectedStation = int(selectedStation)
            if selectedStation >= 0 and selectedStation < len(stations):
                return selectedStation
            else:
                print("Estacao nao existe")
        except:
            #Mensagem erro #TODO
            print("Entrada invalida")
            continue

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
    print("caiu")


while True:
    #os.system("killall vlc") #Kill VLC process
    #os.system(f"vlc {stations[selectRadio]['url']}") #Open VLC process
    os.system(f"start vlc {stations[selectRadio]['url']}")
    print(stations[selectRadio]['nome'])
    print(stations[selectRadio]['url'])
    #Salva radio selecionada
    with open(stationFile, "w") as file:
        file.write(f"{selectRadio}")

    selectRadio = getUserInput()




