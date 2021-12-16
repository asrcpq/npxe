import os
import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
import atexit

class NpxeView(QWebEngineView):
	def __init__(self, parent = None):
		super().__init__(parent)
	def createWindow(self, ty):
		print(ty)
		return self

class MainWindow(QMainWindow):
	def __init__(self, url):
		super(MainWindow, self).__init__()
		webview = NpxeView(self)
		defaultProfile = QWebEngineProfile.defaultProfile();
		defaultProfile.setCachePath(f"{os.environ['XDG_CACHE_HOME']}/npxe/profile");
		defaultProfile.setPersistentStoragePath(f"{os.environ['XDG_DATA_HOME']}/npxe/profile");
		self.browser = webview
		self.browser.setUrl(QUrl(url))
		self.setWindowTitle("npxe")
		self.setCentralWidget(self.browser)
		self.showMaximized()
	def closeEvent(self, e):
		for item in self.browser.history().items():
			hist_file.write("{} {} {}\n".format(
				item.lastVisited().toString(Qt.ISODate),
				item.originalUrl().toString(),
				item.title(),
			))

app = QApplication(sys.argv)
hist_file = open(f"{os.environ['NPXE_HISTORY']}", "a")
url = sys.argv[1]
if "://" not in url:
	url = "https://" + url
window = MainWindow(url)
app.exec_()
hist_file.close()
