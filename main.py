import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JarvZX")
        self.setWindowIcon(QIcon("BrowserIcon.png"))
        self.setGeometry(200, 200, 900, 600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setText("Back")
        # self.backButton.setFixedSize(45, 36)
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setText("Reload")
        # self.backButton.setFixedSize(45, 36)
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setText("Forward")
        # self.forwardButton.setFixedSize(45, 36)
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.homeButton = QPushButton()
        self.homeButton.setText("Home")
        # self.forwardButton.setFixedSize(45, 36)
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 14))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setText("Search")
        # self.forwardButton.setFixedSize(45, 36)
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://google.com'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

    def searchBtn(self):
        myUrl = self.addressLineEdit.text()
        if 'www.' in myUrl:
            if 'https://' not in myUrl:
                myUrl = 'https://' + myUrl
                self.addressLineEdit.setText(myUrl)
        elif 'www.' not in myUrl:
            myUrl = 'https://www.google.com/search?q=' + myUrl
            self.addressLineEdit.setText(myUrl)
        self.webEngineView.load(QUrl(myUrl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(QUrl('https://google.com'))
        self.addressLineEdit.setText('https://google.com')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
