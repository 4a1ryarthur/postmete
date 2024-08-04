import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Browser')
        self.setGeometry(100, 100, 800, 600)
        self.url_field = QLineEdit(self)
        self.go_button = QPushButton('Go', self)

        layout = QVBoxLayout()
        layout.addWidget(self.url_field)
        layout.addWidget(self.go_button)

        self.web = QWebEngineView()
        self.web.setGeometry(0, 50, 800, 550)

        self.go_button.clicked.connect(self.navigate)

        layout.addWidget(self.web)
        self.setLayout(layout)

    def navigate(self):
        url = QUrl(self.url_field.text())
        self.web.setUrl(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
