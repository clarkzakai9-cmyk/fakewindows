import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class HTMLWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML Viewer - index.htm")

        # Create the web view
        self.browser = QWebEngineView()

        # Absolute path to your desktop.html
        local_file = r"C:\Users\zakeb\Windows\desktop.html"
        url = QUrl.fromLocalFile(local_file)

        # Load the local HTML file
        self.browser.load(url)

        # Set the central widget
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HTMLWindow()
    window.showFullScreen()   # <-- fullscreen instead of windowed
    sys.exit(app.exec_())
