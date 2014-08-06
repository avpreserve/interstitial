'''
# -*- coding: UTF-8 -*-
# Interstitial Error Detector
# Version 0.2, 2013-08-28
# Copyright (c) 2013 AudioVisual Preservation Solutions
# All rights reserved.
# Released under the Apache license, v. 2.0
# Created on Aug 6, 2014
# @author: Furqan Wasi <furqan@avpreserve.com>
'''

from PySide.QtCore import *
from PySide.QtGui import *

from Core import SharedApp


''' Class to manage the Filter to be implemented for the files with specific extensions '''

class AboutInterstitialGUI(QDialog):
    
      
    ''' Class to manage the Filter to be implemented for the files with specific extensions '''
    
    '''Contstructor'''
    def __init__(self, parent_win):

        QDialog.__init__(self, parent_win)
        self.Interstitial = SharedApp.SharedApp.App

        self.setWindowTitle('About Intersitial')
        
        self.parent_win = parent_win
        self.setWindowModality(Qt.WindowModal)

        self.parent_win.setWindowTitle('About Intersitial')

        self.setWindowIcon(QIcon(self.Interstitial.Configuration.getLogoSignSmall()))
        self.AboutInterstitialLayout = QVBoxLayout()

        self.widget = QWidget(self)

        self.detail_layout = QVBoxLayout()

        self.close_btn = QPushButton('Close')

        self.about_layout = QGroupBox()
        self.heading = QTextEdit()
        self.content = QTextBrowser()

        self.heading.setReadOnly(True)
        self.content.setReadOnly(False)

        self.main = QHBoxLayout()

    def destroy(self):
        ''' Distructor'''
        del self

    def ShowDialog(self):
        ''' Show Dialog'''
        self.show()
        self.exec_()

    def SetLayout(self, layout):
        ''' Set Layout'''
        self.AboutInterstitialLayout = layout

    def showDescription(self):
        ''' Show Description'''
        self.heading.setText(self.Interstitial.label['description_heading'])
        self.content.setHtml(self.Interstitial.label['description_content'])

    def SetDesgin(self):
        ''' All design Management Done in Here'''

        self.close_btn = QPushButton('Close')

        pic = QLabel(self)

        pic.setFixedSize(300,400)

        '''use full ABSOLUTE path to the image, not relative'''

        pic.setPixmap(QPixmap(self.Interstitial.Configuration.getLogoSignSmall()))

        self.close_btn.clicked.connect(self.Cancel)

        self.detail_layout.addWidget(pic)

        slay = QVBoxLayout()
        if self.Interstitial.Configuration.getOsType() == 'windows':
            self.heading.setFixedSize(555, 40)
            self.content.setFixedSize(555, 260)
        else:
            self.heading.setFixedSize(570, 40)
            self.content.setFixedSize(570, 260)

        self.close_btn.setFixedSize(200, 30)

        slay.addWidget(self.heading)
        slay.addWidget(self.content)

        slay.addWidget(self.close_btn)

        if self.Interstitial.Configuration.getOsType() == 'windows':
            self.about_layout.setFixedSize(580, 360)
        else:
            self.about_layout.setFixedSize(560, 360)

        self.main.addWidget(self.about_layout)

        self.about_layout.setLayout(slay)
        self.setLayout(self.main)
        self.showDescription()

    def Cancel(self):
        """
        Close the Dialog Box
        @return:
        """

        try:self.Interstitial = SharedApp.SharedApp.App
        except:pass

        self.parent_win.setWindowTitle(self.Interstitial.messages['InterErrorDetectTitle'])
        self.destroy()
        self.close()

    def LaunchDialog(self):
        """
        Launch Dialog

        @return:
        """
        self.SetDesgin()
        self.ShowDialog()

