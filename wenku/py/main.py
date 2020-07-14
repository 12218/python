from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import library
import webbrowser
import os
import subprocess

class root(QMainWindow):
    def __init__(self):
        super().__init__()
        self.url = ''
        self.error = '000'
        self.setUI()
    def setUI(self):
        icon = QIcon('./resourses/ico.png')
        self.setWindowIcon(icon)

        self.resize(500, 50)
        self.setWindowTitle('百度文库解析')
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.label = QLabel('URL:', self)
        self.label.move(20, 7)
        self.label.setStyleSheet('font-size: 15px; font-family: Microsoft YaHei;')

        self.line = QLineEdit(self)
        self.line.resize(370, 30)
        self.line.setPlaceholderText('输入百度文库的url连接...')
        self.line.move(60, 9)
        self.line.setStyleSheet('font-size: 13px')

        self.button = QPushButton('解析', self)
        self.button.resize(40, 30)
        self.button.move(450, 9)
        self.button.clicked.connect(self.operate)

        self.show()

    def operate(self):
        self.url = self.line.text()
        html = library.wenku(self.url)
        artical = library.write_doc()
        try:
            html.get_HTML()
            if html.response.status_code == 200:
                # html.get_Doc()
                artical.write(html.get_Doc())
                # print('Finished!')
                self.line.setText('完成！！！')
                # print(os.getcwd())
                subprocess.run("explorer.exe %s" % os.getcwd() + '\\artical\\')
            else:
                print('申请出错！！！')
        except:
            print('写入出错！！！')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = root()
    sys.exit(app.exec_())

# https://wenku.baidu.com/view/b2072721ccbff121dd3683a2.html