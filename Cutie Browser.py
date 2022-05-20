from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
import os
from PyQt5 import *



class MainWindow (QMainWindow):
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/'))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.url_bar.setText(url.toString())
        
    def __init__ (self):
        super (MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        self.setWindowIcon(QtGui.QIcon('cutie.png'))
        
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.addSeparator()
        
        home_btn = QAction('🏠',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        back_btn = QAction('◄',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        forwd_btn = QAction('►',self)
        forwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forwd_btn)
        
        reload_btn = QAction('⟳',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        stop_btn = QAction('✖',self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)
        
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        navbar.addSeparator()
        self.url_bar = QLineEdit()
        self.url_bar.setFixedWidth(640)
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        
        self.browser.urlChanged.connect(self.update_url)
        self.url_bar.setText('https://www.google.com/')

app = QApplication(sys.argv)
QApplication.setApplicationName("Cutie Browser")
window = MainWindow()
app.exec_()
