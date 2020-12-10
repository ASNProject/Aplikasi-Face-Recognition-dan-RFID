# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pinjaman.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import pickle
import sqlite3
import serial
import time, threading

import datetime

global ser
ser = serial.Serial('COM6', baudrate=9600, timeout=10,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
# Ganti COM sesuai dengan COM dari Arduino yang terbaca

class Ui_Pinjaman(object):
    def __init__(self,message,message2,message3):
        self.message = message
        self.message2= message2
        self.message3= message3
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.message)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 281, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(self.message2)
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 130, 281, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(self.message3)
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 160, 281, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 190, 281, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 220, 281, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 250, 281, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.simpan)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 40, 281, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tambah Pinjaman:"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label_3.setText(_translate("MainWindow", "Nama"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "Kode Buku"))
        self.label_6.setText(_translate("MainWindow", "Nama Buku"))
        self.label_7.setText(_translate("MainWindow", "Tanggal Pinjam"))
        self.label_8.setText(_translate("MainWindow", "Tanggal Kembali"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))
        self.label_9.setText(_translate("MainWindow", "No Pinjaman"))
        DateTime = datetime.datetime.now()
        self.lineEdit_6.setText('%s%s%s' % (DateTime.day, DateTime.month, DateTime.year))
        self.lineEdit_7.setText('%s%s%s' % ((DateTime.day+3), DateTime.month, DateTime.year)) 
        #Ganti angka 3 dengan durasi peminjaman yang diinginkan
        self.timeout = 0
        self.check_serial_event()

    def check_serial_event(self):
        self.timeout += 1
        serial_thread = threading.Timer(1, self.check_serial_event)
       
        
        def getData(kode):
            conn=sqlite3.connect("FacaBase.db")
            cmd = "SELECT * FROM Buku WHERE Kode="+str(kode)
            cursor=conn.execute(cmd)
            profile=None
            for row in cursor:
                profile=row
            conn.close()
            return profile
        
        if ser.is_open == True:
            serial_thread.start()
            if ser.in_waiting:
                eol = b'\n'
                leneol = len(eol)
                line = bytearray()
                while True:
                    c = ser.read(1)
                    if c:
                        line += c
                        if line[-leneol:] == eol:
                            break
                    else:
                        break
                line = line.rstrip()
                distance = line.decode("utf-8")
                self.lineEdit_4.setText(distance)
                profile=getData(distance)
                self.lineEdit_5.setText(str(profile[2]))
                self.timeout = 0
        if self.timeout >= 100:
            ser.close()

    def simpan(self):
        def insertData(Id, Nama, Email, Buku, Kembali):
            conn = sqlite3.connect("database/Harian/"+self.lineEdit_6.text()+".db")
            cmd = "SELECT * FROM Pinjaman WHERE ID="+str(Id)
            cursor = conn.execute(cmd)
            isRecordExist=0
            for row in cursor:
                isRecordExist=1
            if(isRecordExist==1):
                cmd = "UPDATE Pinjaman SET Nama"+str(Email)+"WHERE ID="+str(Id)
                cmd = "UPDATE Pinjaman SET Email"+str(Email)+"WHERE ID="+str(Id)
                cmd = "UPDATE Pinjaman SET Buku"+str(Buku)+"WHERE ID="+str(Id)
                cmd = "UPDATE Pinjaman SET Pengembalian"+str(Kembali)+"WHERE ID="+str(Id)
            else:
                cmd="INSERT INTO Pinjaman(ID,Nama,Email,Buku,Pengembalian) Values("+str(Id)+","+str(Nama)+","+str(Email)+","+str(Buku)+","+str(Kembali)+")"
            conn.execute(cmd)
            conn.commit()
            conn.close()
        def insertID(no,kode, buku, pinjam, kembali):
            conn = sqlite3.connect("database/"+self.lineEdit.text()+".db")
            cmd = "SELECT *FROM BUKU WHERE Kode="+str(kode)
            cursor = conn.execute(cmd)
            isRecordExist=0
            for row in cursor:
                isRecordExist=1
            if(isRecordExist==1):
                cmd = "UPDATE BUKU SET No"+str(no)+"WHERE Kode="+str(kode)
                cmd = "UPDATE BUKU SET Buku"+str(buku)+"WHERE Kode="+str(kode)
                cmd = "UPDATE BUKU SET Pinjam"+str(pinjam)+"WHERE Kode="+str(kode)
                cmd = "UPDATE BUKU SET Kembali"+str(kembali)+"WHERE Kode="+str(kode)
            else:
                 cmd="INSERT INTO BUKU(No,Kode,Buku,Pinjam,Kembali) Values("+str(no)+","+str(kode)+","+str(buku)+","+str(pinjam)+","+str(kembali)+")"
            conn.execute(cmd)
            conn.commit()
            conn.close()
        def insertBuku(id, nama, pinjam, kembali, kode):
            conn = sqlite3.connect("database/Buku/"+str(kode)+".db")
            cmd = "SELECT * FROM BUKU WHERE Nama="+str(nama)
            cursor = conn.execute(cmd)
            isRecordExist=0
            for row in cursor:
                isRecordExist=1
            if(isRecordExist==1):
                cmd = "UPDATE BUKU SET ID"+str(id)+"WHERE Nama="+str(nama)
                cmd = "UPDATE BUKU SET Pinjam"+str(pinjam)+"WHERE Nama="+str(nama)
                cmd = "UPDATE BUKU SET Kembali"+str(kembali)+"WHERE Nama="+str(nama)
            else:
                 cmd="INSERT INTO BUKU(ID,Nama,Pinjam,Kembali) Values("+str(id)+","+str(nama)+","+str(pinjam)+","+str(kembali)+")"
            conn.execute(cmd)
            conn.commit()
            conn.close()
        
        id = self.lineEdit_8.text()    
        nama = "'"+self.lineEdit_2.text()+"'"
        email = "'"+self.lineEdit_3.text()+"'"
        buku = "'"+self.lineEdit_5.text()+"'"
        kembali = self.lineEdit_7.text()
        no = self.lineEdit_8.text()
        kode = self.lineEdit_4.text()
        pinjam = self.lineEdit_6.text()

        insertData(id,nama,email,buku,kembali)
        insertID(no,kode,buku,pinjam,kembali)
        insertBuku(id, nama, pinjam, kembali, kode)

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Peminjaman")
        msgBox.setText("Daftar peminjaman sudah disimpan!!")
        x = msgBox.exec_()
        

