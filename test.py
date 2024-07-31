# This Code Will Test if WV Is Working.
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebView Example")
        self.setGeometry(100, 100, 800, 600)

        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)

        # HTML content with images and styling
        html_content = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #4a4a4a; }
                img { max-width: 100%; height: auto; }
                .container { display: flex; justify-content: space-around; }
                .item { text-align: center; }
            </style>
        </head>
        <body>
            <h1>Welcome to the WebView Example</h1>
            <p>This is a sample page demonstrating the capabilities of the WebView.</p>
            <div class="container">
                <div class="item">
                    <img src="https://picsum.photos/200/300" alt="Random Image 1">
                    <p>Random Image 1</p>
                </div>
                <div class="item">
                    <img src="https://picsum.photos/200/300" alt="Random Image 2">
                    <p>Random Image 2</p>
                </div>
            </div>
            <h2>Features:</h2>
            <ul>
                <li>Support for HTML tags</li>
                <li>CSS styling</li>
                <li>Image display</li>
                <li>And more!</li>
            </ul>
        </body>
        </html>
        """

        # Load the HTML content into the WebView
        self.webview.setHtml(html_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebViewWindow()
    window.show()
    sys.exit(app.exec_())
