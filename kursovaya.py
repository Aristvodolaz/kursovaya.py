import sys
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import math
import pickle



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('курсовая.ui', self)

        #марка бетона
        marbetona = ['B15', 'B20', 'B25', 'B30', 'B35','B40']
        razdiametra = ['6', '8', '10', '12', '14', '16', '18', '20']

        self.Rb = 0
        self.Rbt = 0
        self.Asw = 0

        # значения марок
        self.marbetonaRB = [8.5, 11.5, 14.5, 17, 19.5, 22]
        self.marbetonaRBt = [0.750000, 0.900000, 1.050000, 1.150000, 1.300000, 1.400000]
        self.razdiametraAsw = [57, 101, 157, 226, 308, 402, 509, 628]

        #выпадающ виджет список
        self.comboBox.addItems(marbetona)
        self.comboBox_2.addItems(razdiametra)

        #подключение кнопок
        self.comboBox.activated.connect(self.beton)
        self.comboBox.activated.connect(self.diametr)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.dell)
        self.pushButton_2.clicked.connect(self.chertezh)
        self.action_8.triggered.connect(self.help1)
        self.action.triggered.connect(self.help3)
        self.action_3.triggered.connect(self.help2)
        self.action_2.triggered.connect(self.help4)
        self.action_5.triggered.connect(self.size1)
        self.action_6.triggered.connect(self.size2)
        self.action_7.triggered.connect(self.size3)
        self.actionE_mail.triggered.connect(self.e_mail)
        self.action_4.triggered.connect(self.save)
        self.action_9.triggered.connect(self.vyvod)

    def size1(self):
        self.label.setFont(QFont('Arial', 6))
        self.Diametr.setFont(QFont('Arial', 6))
        self.label_5.setFont(QFont('Arial', 6))
        self.label_6.setFont(QFont('Arial', 6))
        self.label_7.setFont(QFont('Arial', 6))
        self.label_8.setFont(QFont('Arial', 6))
        self.label_9.setFont(QFont('Arial', 6))
        self.label_10.setFont(QFont('Arial', 6))
        self.label_11.setFont(QFont('Arial', 6))
        self.textEdit.setFont(QFont('Arial', 6))
        self.lineEdit.setFont(QFont('Arial', 6))
        self.lineEdit_2.setFont(QFont('Arial', 6))
        self.lineEdit_3.setFont(QFont('Arial', 6))
        self.lineEdit_4.setFont(QFont('Arial', 6))
        self.comboBox.setFont(QFont('Arial', 6))
        self.comboBox_2.setFont(QFont('Arial', 6))
        self.pushButton_2.setFont(QFont('Arial', 6))
        self.pushButton_3.setFont(QFont('Arial', 6))
        self.pushButton.setFont(QFont('Arial', 6))



    def size2(self):
        self.label.setFont(QFont('Arial', 10))
        self.Diametr.setFont(QFont('Arial', 10))
        self.label_5.setFont(QFont('Arial', 10))
        self.label_6.setFont(QFont('Arial', 10))
        self.label_7.setFont(QFont('Arial', 10))
        self.label_8.setFont(QFont('Arial', 10))
        self.label_9.setFont(QFont('Arial', 10))
        self.label_10.setFont(QFont('Arial', 10))
        self.label_11.setFont(QFont('Arial', 10))
        self.textEdit.setFont(QFont('Arial', 10))
        self.lineEdit.setFont(QFont('Arial', 10))
        self.lineEdit_2.setFont(QFont('Arial', 10))
        self.lineEdit_3.setFont(QFont('Arial', 10))
        self.lineEdit_4.setFont(QFont('Arial', 10))
        self.comboBox.setFont(QFont('Arial', 10))
        self.comboBox_2.setFont(QFont('Arial', 10))
        self.pushButton_2.setFont(QFont('Arial', 10))
        self.pushButton_3.setFont(QFont('Arial', 10))
        self.pushButton.setFont(QFont('Arial', 10))

    def size3(self):
        self.label.setFont(QFont('Arial', 16))
        self.Diametr.setFont(QFont('Arial', 16))
        self.label_5.setFont(QFont('Arial', 16))
        self.label_6.setFont(QFont('Arial', 16))
        self.label_7.setFont(QFont('Arial', 16))
        self.label_8.setFont(QFont('Arial', 16))
        self.label_9.setFont(QFont('Arial', 16))
        self.label_10.setFont(QFont('Arial', 16))
        self.label_11.setFont(QFont('Arial', 16))
        self.textEdit.setFont(QFont('Arial', 16))
        self.lineEdit.setFont(QFont('Arial', 16))
        self.lineEdit_2.setFont(QFont('Arial', 16))
        self.lineEdit_3.setFont(QFont('Arial', 16))
        self.lineEdit_4.setFont(QFont('Arial', 16))
        self.comboBox.setFont(QFont('Arial', 16))
        self.comboBox_2.setFont(QFont('Arial', 16))
        self.pushButton_2.setFont(QFont('Arial', 16))
        self.pushButton_3.setFont(QFont('Arial', 16))
        self.pushButton.setFont(QFont('Arial', 16))




        # открываем чертежи
    def chertezh(self):
        self.chertezh = Chertezh(self, '')
        self.chertezh.show()

#передача значений
    def beton(self, index):
        self.Rb = self.marbetonaRB[index]
        self.Rbt = self.marbetonaRBt[index]

    def diametr(self, index):
        self.Asw = self.razdiametraAsw[index]

    def dell(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.textEdit.setText("")

    def run(self):
        c = float()

        Rsw = 170
        Minf = 250000
        Msup = 350000

        sp = "abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sp = list(sp)

        self.b = self.lineEdit.text()
        bb = str(self.b)
        for i in range(len(sp)):
            bb = bb.replace(sp[i], '')
        self.b = str(bb)
        self.lineEdit.setText(str(self.b))


        self.h = self.lineEdit_3.text()
        bb = str(self.h)
        for i in range(len(sp)):
            bb = bb.replace(sp[i], '')
        self.h = str(bb)
        self.lineEdit_3.setText(str(self.h))

        self.N = self.lineEdit_4.text()
        bb = str(self.N)
        for i in range(len(sp)):
            bb = bb.replace(sp[i], '')
        self.N = str(bb)
        self.lineEdit_4.setText(str(self.N))

        self.l = self.lineEdit_2.text()
        bb = str(self.l)
        for i in range(len(sp)):
            bb = bb.replace(sp[i], '')
        self.l = str(bb)
        self.lineEdit_2.setText(str(self.l))


        #проверка
        if float(self.b) > 1500.:
            self.lineEdit.setText('300')
            self.h = self.lineEdit.text()
            self.info = QMessageBox()
            self.info.setWindowTitle("Info")
            self.info.setText('Значение h не входит в указанный диапазон от 300м до 1500м\nВернитесь к прочтению инструкции.\nАвтоматически задано наименьшее значение 300.')
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

        if float(self.b) < 300.:
            self.lineEdit.setText('300')
            self.h = self.lineEdit.text()
            self.info = QMessageBox()
            self.info.setWindowTitle("Info")
            self.info.setText('Значение h не входит в указанный диапазон от 300м до 1500м\nВернитесь к прочтению инструкции.\nАвтоматически задано наименьшее значение 300.')
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

        if float(self.h) > 1500.:
            self.lineEdit_3.setText('300')
            self.h = self.lineEdit_3.text()
            self.info = QMessageBox()
            self.info.setWindowTitle("Info")
            self.info.setText('Значение h не входит в указанный диапазон от 300м до 1500м\nВернитесь к прочтению инструкции.\nАвтоматически задано наименьшее значение 300.')
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

        if float(self.h) < 300.:
            self.lineEdit_3.setText('300')
            self.h = self.lineEdit_3.text()
            self.info = QMessageBox()
            self.info.setWindowTitle("Info")
            self.info.setText('Значение h не входит в указанный диапазон от 300м до 1500м\nВернитесь к прочтению инструкции.\nАвтоматически задано наименьшее значение 300.')
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

        if float(self.N) <= 0.:
            self.lineEdit_4.setText('1')
            self.N = self.lineEdit_4.text()
            self.info = QMessageBox()
            self.info.setWindowTitle("Info")
            self.info.setText('Значение N = 0, решение не может быть выполнено.\nАвтоматически задано наименьшее значение 1.')
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

        if float(self.l) <= 0.:
            self.lineEdit_2.setText('1')
            self.l = self.lineEdit_2.text()
            self.info = QMessageBox()
            self.info.setWindowTitle("Info")
            self.info.setText('Значение l = 0, решение не может быть выполнено.\nАвтоматически задано наименьшее значение 1.')
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

# запуск выполннеия
        a = 20 - 1 / 2 * float(self.h)
        sw = round(float(1/3 * float(self.h) - 3*float(self.h)), 3)
        h0 = round(float(float(self.h) - float(a)), 3)
        Q = round(float((Msup + Minf) / float(self.l)), 3)  # поперечная сила в колонне
        C_max = round(float(3 * h0), 3)

        Nb = round(float(1.3 * self.Rb * float(self.b) * float(self.h)), 3)
        Fin2 = round(float(1 + 3 * (Nb / float(self.N)) - 4 * (Nb / float(self.N))), 3)
        Qb = round(float(-1.5 * self.Rbt * float(self.b) * h0), 3)
        Fin2_Qb = round(float(Fin2 * Qb), 3)
        q_sw = round(float((Rsw * self.Asw) / sw), 3)

        c0 = 2 * h0
        Q_sw = round(float(0.75 * q_sw * c0), 3)

        #передача текста
        self.textEdit.append('Дано наклонное сечение размерами: b =' + str(self.b) + '\nh = ' + str(self.h) +
                             '\nN = ' + str(self.N) + ',\nl = ' + str(self.l))

        self.textEdit.append('Находим значение: h0 =' + str(h0) + '\nQ = ' + str(Q) + '\nC_max = ' + str(C_max) + "\nNb =" +
                             str(Nb) + '\nFi_n2 = ' + str(Fin2) + '\nQb = ' + str(Qb) + '\nFi_n2_Qb = ' + str(Fin2_Qb) +
                             '\nq_sw = ' + str(q_sw) + '\nc0 = ' + str(c0) + '\nQ_sw = ' + str(Q_sw))

        Rbt_Fin = float(0.25 * self.Rbt * float(self.b) * Fin2)
        self.textEdit.append('Полученное значение Rbt_Fin' + str(Rbt_Fin))
        self.textEdit.append('Проверяем условие Rbt_Fin > q_sw')

        if Rbt_Fin > q_sw:
            self.info = QMessageBox()
            self.info.setWindowTitle('Info')
            self.info.setText("Условие не выполняется")
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()


            Rbt_bfin2 = float(4 * q_sw)
            Qb = float(0.5 * h0 * Rbt_bfin2)
            self.textEdit.append("Проверка условия")
            prov = float(Qb + Q_sw)
            if prov > Q:
                self.textEdit.append("Проверка обеспечена")
            else:
                self.textEdit.append("Проверка не обеспечена")
        else:
            self.info = QMessageBox()
            self.info.setWindowTitle('Info')
            self.info.setText("Условие выполняется")
            self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.info.exec_()

    def save(self):

        f  = open (r'file.txt', 'wb')
        lineB = self.lineEdit.text()
        pickle.dump(lineB, f)

        lineH = self.lineEdit_3.text()
        pickle.dump(lineH, f)

        lineN = self.lineEdit_4.text()
        pickle.dump(lineN, f)

        linel = self.lineEdit_2.text()
        pickle.dump(linel, f)
        f.close()

    def vyvod(self):

        f = open('file.txt', 'rb')

        self.lineEdit.setText(pickle.load(f))
        self.lineEdit_3.setText(pickle.load(f))
        self.lineEdit_4.setText(pickle.load(f))
        self.lineEdit_2.setText(pickle.load(f))

        f.close()

    def e_mail(self):

        self.info = QMessageBox()
        self.info.setWindowTitle('Info')
        self.info.setText('E-mail для свзяи с разработчиком: kap.moral@mail.ru')
        self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.info.exec_()

    def help1(self):

        self.info = QMessageBox()
        self.info.setWindowTitle('Info')
        self.info.setText('Дополнительную инормацию по программе \n можно получить у разработчиков')
        self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.info.exec_()

    def help2(self):

        self.info = QMessageBox()
        self.info.setWindowTitle('Info')
        self.info.setText('Программу разработали: \nПрокопенко Арина: ИСТ-201 \nЗгонникова Александра: ИСТ-201 \nПрудникова Анастасия: ИСТ-201')
        self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.info.exec_()

    def help3(self):

        self.info = QMessageBox()
        self.info.setWindowTitle('Info')
        self.info.setText('Введите значение b в интервале от 300м до 1500м\n'
                          'Введите значение h в интервале от 300м до 1500м\nКнопка "Расчитать" выполнит расчет\n'
                          'Кнопка "Сброс" очистит поля\nКопка "Чертеж" - покажет чертеж по задаче')
        self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.info.exec_()

    def help4(self):

        self.info = QMessageBox()
        self.info.setWindowTitle('Info')
        self.info.setText('Программа разработана для расчета обеспечения прочности наклонных сечений')
        self.info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.info.exec_()

class Chertezh(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUi(args)

    def initUi(self, args):

        self.setGeometry(400, 330, 400, 330)
        self.setWindowTitle('Чертеж')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        self.lab = QLabel(self)
        pixmap = QPixmap('kurs.jpg')
        self.lab.setPixmap(pixmap)
        self.lab.move(3, 15)
        self.lab.resize(381, 272)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exeption, traceback)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = MyWidget()
    application.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())