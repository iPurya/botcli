# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
from time import sleep
import telebot
import threading
import random
from datetime import datetime
from essential_generators import DocumentGenerator
gen = DocumentGenerator()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(991, 509)
        self.BotClient = QtWidgets.QWidget(self)
        self.BotClient.setObjectName("BotClient")
        self.BotClientLayout = QtWidgets.QHBoxLayout(self.BotClient)
        self.BotClientLayout.setContentsMargins(0, 0, 0, 0)
        self.BotClientLayout.setSpacing(0)
        self.BotClientLayout.setObjectName("BotClientLayout")
        self.MainLayout = QtWidgets.QHBoxLayout()
        self.MainLayout.setContentsMargins(5, 5, 5, 5)
        self.MainLayout.setSpacing(5)
        self.MainLayout.setObjectName("MainLayout")
        self.dialogFrame = QtWidgets.QFrame(self.BotClient)
        self.dialogFrame.setObjectName("dialogFrame")
        self.dialogLayout = QtWidgets.QVBoxLayout(self.dialogFrame)
        self.dialogLayout.setContentsMargins(0, 0, 0, 0)
        self.dialogLayout.setSpacing(10)
        self.dialogLayout.setObjectName("dialogLayout")
        self.groupBox = QtWidgets.QGroupBox(self.dialogFrame)
        self.groupBox.setObjectName("groupBox")
        self.loginGroupLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.loginGroupLayout.setContentsMargins(5, 0, 0, 0)
        self.loginGroupLayout.setSpacing(5)
        self.loginGroupLayout.setObjectName("loginGroupLayout")
        self.loginLabel = QtWidgets.QLabel(self.groupBox)
        self.loginLabel.setObjectName("loginLabel")
        self.loginGroupLayout.addWidget(self.loginLabel)
        self.TokenInput = QtWidgets.QLineEdit(self.groupBox)
        self.TokenInput.setObjectName("TokenInput")
        self.loginGroupLayout.addWidget(self.TokenInput)
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName("loginButton")
        self.loginGroupLayout.addWidget(self.loginButton)
        self.dialogLayout.addWidget(self.groupBox)
        self.chatsList = QtWidgets.QListWidget(self.dialogFrame)
        self.chatsList.setObjectName("chatsList")
        self.dialogLayout.addWidget(self.chatsList)
        self.dialogLayout.setStretch(0, 1)
        self.dialogLayout.setStretch(1, 9)
        self.MainLayout.addWidget(self.dialogFrame)
        self.chatFrame = QtWidgets.QFrame(self.BotClient)
        self.chatFrame.setObjectName("chatFrame")
        self.chatLayout = QtWidgets.QVBoxLayout(self.chatFrame)
        self.chatLayout.setContentsMargins(0, 0, 0, 0)
        self.chatLayout.setSpacing(5)
        self.chatLayout.setObjectName("chatLayout")
        self.userInfoFrame = QtWidgets.QFrame(self.chatFrame)
        self.userInfoFrame.setStyleSheet("background-color: rgb(255,255,255)")
        self.userInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userInfoFrame.setObjectName("userInfoFrame")
        self.userInfoGridLayout = QtWidgets.QGridLayout(self.userInfoFrame)
        self.userInfoGridLayout.setContentsMargins(10, 2, 2, 2)
        self.userInfoGridLayout.setHorizontalSpacing(10)
        self.userInfoGridLayout.setVerticalSpacing(0)
        self.userInfoGridLayout.setObjectName("userInfoGridLayout")
        self.userPic = QtWidgets.QLabel(self.userInfoFrame)
        self.userPic.setMinimumSize(QtCore.QSize(50, 50))
        self.userPic.setMaximumSize(QtCore.QSize(50, 50))
        self.userPic.setText("")
        self.default_pic = QtGui.QPixmap("default_pic.jpg")
        self.userPic.setPixmap(self.default_pic)
        self.userPic.setScaledContents(True)
        self.userPic.setObjectName("userPic")
        self.userInfoGridLayout.addWidget(self.userPic, 0, 0, 2, 1)
        self.infoLabel = QtWidgets.QLabel(self.userInfoFrame)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.userInfoGridLayout.addWidget(self.infoLabel, 0, 2, 2, 1)
        self.userInfoLabel = QtWidgets.QLabel(self.userInfoFrame)
        self.userInfoLabel.setObjectName("userInfoLabel")
        self.userInfoGridLayout.addWidget(self.userInfoLabel, 0, 1, 2, 1)
        self.userInfoGridLayout.setColumnStretch(0, 1)
        self.userInfoGridLayout.setColumnStretch(1, 2)
        self.userInfoGridLayout.setColumnStretch(2, 6)
        self.chatLayout.addWidget(self.userInfoFrame)
        self.chatHistoryFrame = QtWidgets.QFrame(self.chatFrame)
        self.chatHistoryFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chatHistoryFrame.setObjectName("chatHistoryFrame")
        self.chatHistoryLayout = QtWidgets.QVBoxLayout(self.chatHistoryFrame)
        self.chatHistoryLayout.setContentsMargins(0, 0, 0, 0)
        self.chatHistoryLayout.setSpacing(0)
        self.chatHistoryLayout.setObjectName("chatHistoryLayout")
        self.textEdit = QtWidgets.QTextEdit(self.chatHistoryFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.chatHistoryLayout.addWidget(self.textEdit)
        self.chatLayout.addWidget(self.chatHistoryFrame)
        self.sendFrame = QtWidgets.QFrame(self.chatFrame)
        self.sendFrame.setObjectName("sendFrame")
        self.sendLayout = QtWidgets.QHBoxLayout(self.sendFrame)
        self.sendLayout.setContentsMargins(0, 0, 0, 0)
        self.sendLayout.setSpacing(5)
        self.sendLayout.setObjectName("sendLayout")
        self.sendText = QtWidgets.QTextEdit(self.sendFrame)
        self.sendText.setObjectName("sendText")
        self.sendLayout.addWidget(self.sendText)
        self.sendButton = QtWidgets.QPushButton(self.sendFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setObjectName("sendButton")
        self.sendLayout.addWidget(self.sendButton)
        self.chatLayout.addWidget(self.sendFrame)
        self.chatLayout.setStretch(0, 1)
        self.chatLayout.setStretch(1, 8)
        self.chatLayout.setStretch(2, 1)
        self.MainLayout.addWidget(self.chatFrame)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(1, 2)
        self.BotClientLayout.addLayout(self.MainLayout)
        self.setCentralWidget(self.BotClient)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginLabel.setText(_translate("MainWindow", "Token:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.sendButton.setText(_translate("MainWindow", "Send"))


class MyWin(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loginButton.clicked.connect(self.login_handle)
        self.chatsList.itemClicked.connect(self.chat_clicked)
        self.sendButton.clicked.connect(self.send_message)
        self.sendButton.setEnabled(False)
        self.telebot = None
        self.infoLabel.setText("Please login first!")
        self.bot_id = None
        self.bot_name = None
        self.bot_username = None
        self.open_chat_id = 0
        self.exit = False
        self.unread_messages_count = {}
        self.chat_peer = {}
        
    def add_chat(self,date,title=None,text="",msg_id=None,color=None):
        if not color:
            if not text: color = "#2ECC71"
            elif not title: color = "#0055ff" ; title = "You: "
            else: color = "#ff0000" ; title += ": "
        msg_id = f" {msg_id} |" if msg_id else ""
        text = text.replace("\n", "<br>")
        self.textEdit.insertHtml(f'<p><span style="color:#85929e;">{datetime.strftime(date, "%m/%d/%Y %H:%M")}</span> <span style=" font-weight:700; color:#2e4053;">|{msg_id}</span> <span style=" font-weight:700; color:{color};">{title}</span> {text}<br></p>')
    def clear_chat(self):
        self.textEdit.clear()
    def set_profile_pic(self,chat):
        if chat.photo:
            file_info = self.telebot.get_file(chat.photo.small_file_id)
            photo = urlopen(f'https://api.telegram.org/file/bot{self.token}/{file_info.file_path}').read()
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(photo)
            self.userPic.setPixmap(pixmap)
        else:
            self.userPic.setPixmap(self.default_pic)
    
    def login_handle(self,event):
        if self.loginButton.text() == "Login":
            inp = self.TokenInput.text()
            try:
                self.telebot = telebot.TeleBot(inp)
                me = self.telebot.get_me()
                self.token = inp
                self.bot_id, self.bot_name, self.bot_username = me.id, me.first_name, me.username
                self.userInfoLabel.setText(f"{me.first_name}\n@{me.username}\n{me.id}")
                self.set_profile_pic(self.telebot.get_chat(self.bot_id))
                self.telebot.set_update_listener(self.update_handler)
                self.infoLabel.setText("")
                self.add_chat(datetime.now(),f"Logged in as {me.first_name}")
                self.loginButton.setText("Logout")
                self.TokenInput.setEnabled(False)
            except telebot.apihelper.ApiTelegramException:
                self.add_chat(datetime.now(),"Token invalid!",color="red")
                self.telebot = None
        else: #logout
            self.infoLabel.setText("Please login first!")
            self.add_chat(datetime.now(),"Logged out")
            self.loginButton.setText("Login")
            self.TokenInput.setEnabled(True)
            self.telebot.stop_bot()
            self.telebot = None
    def polling(self):
        while True:
            if self.telebot:
                self.telebot.polling(long_polling_timeout=5)
            if self.exit:
                return
            sleep(1)
    
    def get_chat_name(self,userid):
        return self.chat_peer.get(userid,None)
    def get_chat_id(self,name):
        if not name in self.chat_peer.values():
            return None
        return list(self.chat_peer.keys())[list(self.chat_peer.values()).index(name)]
    def find_in_list(self,chat_id):
        try: 
            for item in self.chatsList.findItems(self.get_chat_name(chat_id),QtCore.Qt.MatchStartsWith):
                if item.whatsThis() == str(chat_id): return item
        except: return None
    def get_title(self,chat):
        return f"{chat.first_name}{' ' + chat.last_name if chat.last_name else ''}" if chat.type == "private" else chat.title

    def update_handler(self,messages):
        for message in messages:
            chat_type = message.chat.type
            chat_id = message.chat.id
            title = self.get_title(message.chat)

            item = QtWidgets.QListWidgetItem()
            self.chatsList.takeItem(
                self.chatsList.row(
                    self.find_in_list(chat_id)))
            self.chat_peer[chat_id] = title

            if self.open_chat_id == chat_id:
                item.setText(title)
                self.add_chat(datetime.fromtimestamp(message.date),title,message.text,msg_id=message.id)
            else:
                self.unread_messages_count[chat_id] = self.unread_messages_count.get(chat_id,0) + 1
                item.setText(f"{title} ({self.unread_messages_count[chat_id]})")
            
            item.setWhatsThis(str(chat_id))
            self.chatsList.insertItem(0, item)
    
    def chat_clicked(self,event):
        chat_id = int(event.whatsThis())        
        chat = self.telebot.get_chat(chat_id)
        title = self.get_title(chat)
        event.setText(title)
        self.unread_messages_count[chat_id] = 0
        username = "@"+chat.username if chat.username else ""
        self.userInfoLabel.setText(f"{title}\n{username}\n{chat.id}")
        self.set_profile_pic(chat)
        self.open_chat_id = chat_id
        self.sendButton.setEnabled(True)
        self.clear_chat()
    def send_message(self,event):
        text = self.sendText.toPlainText()
        if text:
            sent = self.telebot.send_message(self.open_chat_id,text)
            self.add_chat(datetime.fromtimestamp(sent.date),text=text,msg_id=sent.id)
            self.sendText.setPlainText("")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWin()
    threading.Thread(target=ui.polling,daemon=True).start()
    ui.show()
    app.exec_()
    if ui.telebot:
        ui.telebot.stop_bot()
    ui.exit = True
    sleep(2)
    sys.exit(0)    
        