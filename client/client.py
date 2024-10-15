import sys
import window.cwin_1
import window.cwin_2
from GenProf import GenerateKey, EnCode, DeCode
import threading
import socket
from PyQt5 import QtWidgets

global data
data = None

ChatWin = window.cwin_1.ChatWin
Setings = window.cwin_2.Setings

app = QtWidgets.QApplication(sys.argv)

Chat = QtWidgets.QMainWindow()
ui = ChatWin()
ui.setupUi(Chat)
Chat.show()

def OpenSettingsWindow():
    global Sett
    Sett = QtWidgets.QMainWindow()
    ui = Setings()
    ui.setupUi(Sett)
    Chat.close()
    Sett.show()

    def returnToChat():
        Sett.close()
        Chat.show()



    def generait():
        key = GenerateKey(ui.ID_Edit.text(), ui.lineEdit.text())
        ui.label_2.setText("YouProfile Сгенерирован")


    ui.Chat_Window.clicked.connect(returnToChat)
    ui.pushButton.clicked.connect(generait)


def SendMassage():
    text = EnCode(ui.lineEdit.text())
    ServerSend(text)
    ui.plainTextEdit.appendPlainText(f"Вы: {ui.lineEdit.text()}")

def ServerStart():
    print(1)
    file = open('UIProfile.txt')
    print(2)
    content = file.readlines()
    print(3)
    file.close()
    print(4)
    content = str(content)
    print(5)
    content = content.strip("['").split('IOIOI')
    print(6)
    IP = str(content[0])
    print(IP)
    print(type(IP))
    print(7)
    PORT = int(content[1])
    print(PORT)
    print(type(PORT))
    print(8)
    global s
    print(9)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(10)
    try:
        s.connect(('127.0.0.1', 20202))
    except: Exception
    print(11)


def SS():
    print(1)
    while True:
        print(2)
        try:

            data = s.recv(1024).decode()
            if data == "Вы подключены!":
                i = 15
                while i > 0:
                    if i < 2:
                        ui.plainTextEdit.appendPlainText("======================== Chat Version: 0.1 ============================")


                    ui.plainTextEdit.appendPlainText("==================================================================")
                    i = i - 1
                ui.plainTextEdit.appendPlainText(data)
            else:

                text = DeCode(data)
                ui.plainTextEdit.appendPlainText(text)


        except:
            print("ERROR_DATA")
            exit()

def ServerSend(text):
    s.send(text.encode())

def ConSer():
    ServerStart()
    t = threading.Thread(target=SS)
    t.start()


if data != None:
    ui.plainTextEdit.appendPlainText(data)
ui.Settings_window.clicked.connect(OpenSettingsWindow)
ui.pushButton.clicked.connect(SendMassage)
ui.connect.clicked.connect(ConSer)


sys.exit(app.exec_())





