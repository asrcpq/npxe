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
	def __init__(self, url, hist_file):
		super(MainWindow, self).__init__()
		webview = NpxeView(self)
		defaultProfile = QWebEngineProfile.defaultProfile();
		defaultProfile.setCachePath(f"{os.environ['XDG_CACHE_HOME']}/npxe/profile");
		defaultProfile.setPersistentStoragePath(f"{os.environ['XDG_DATA_HOME']}/npxe/profile");
		self.hist_file = hist_file
		self.browser = webview
		self.browser.setUrl(QUrl(url))
		self.setWindowTitle("npxe")
		self.setCentralWidget(self.browser)
		self.resize(640, 480)
		self.showMaximized()
	def closeEvent(self, e):
		if not self.hist_file:
			print("History not saved.")
			sys.exit(0)
		for item in self.browser.history().items():
			self.hist_file.write("{} {} {}\n".format(
				item.lastVisited().toString(Qt.ISODate),
				item.originalUrl().toString(),
				item.title(),
			))

def main():
	app = QApplication([])
	hist_file = open(f"{os.environ['NPXE_HISTORY']}", "a")
	url = sys.argv[1]
	if "://" not in url:
		url = "https://" + url
	window = MainWindow(url, hist_file)
	app.exec_()
	hist_file.close()

if __name__ == '__main__':
	main()
