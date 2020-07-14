from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import downloader
import webbrowser

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
        self.setWindowTitle('视频解析')
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.label = QLabel('URL:', self)
        self.label.move(20, 7)
        self.label.setStyleSheet('font-size: 15px; font-family: Microsoft YaHei;')

        self.line = QLineEdit(self)
        self.line.resize(370, 30)
        self.line.setPlaceholderText('输入视频的url连接...')
        self.line.move(60, 9)
        self.line.setStyleSheet('font-size: 13px')

        self.button = QPushButton('解析', self)
        self.button.resize(40, 30)
        self.button.move(450, 9)
        self.button.clicked.connect(self.operate)

        self.show()

    def operate(self):
        self.url = self.line.text()
        down = downloader.download(self.error, self.url)
        down.Down_1()
        webbrowser.open('https://www.m3u8play.com/?play=' + down.m3u8_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = root()
    sys.exit(app.exec_())