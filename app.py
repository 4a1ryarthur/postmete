import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Python Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create a widget to hold the web view
        widget = QWidget()
        self.setCentralWidget(widget)

        # Create a vertical layout
        layout = QVBoxLayout(widget)

        # Create a web view
        self.webView = QWebEngineView()
        layout.addWidget(self.webView)

        # Load an initial webpage
        self.webView.load(QUrl("https://www.4a1ryarthur.github.io/postmete/welcome.html"))

        # Set the layout for the widget
        widget.setLayout(layout)
        def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
