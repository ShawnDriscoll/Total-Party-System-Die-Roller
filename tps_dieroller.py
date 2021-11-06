#
#   TPS DieRoller Beta for the Total Party Skills RPG
#   Written for Python 3.9.7
#
##############################################################

"""
TPS DieRoller 0.1.1 Beta for the Total Party Skills RPG
-------------------------------------------------------

This program rolls 6-sided dice and calculates their effects.

The Total Party Skills RPG was written by R. Joshua Holland.
Copyright 2021 - 2022, Total Party Skills.
"""
#import vlc

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5 import uic
#import PyQt5.QtMultimedia as MM
import time
from mainwindow_011b import Ui_MainWindow
from aboutdialog_011b import Ui_aboutDialog
from alertdialog_011b import Ui_alertDialog
from missingdialog_011b import Ui_missingDialog
from random import randint
from rpg_tools.PyDiceroll import roll
import sys
import os
import logging
import json
#import pprint

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'TPS DieRoller 0.1.1 Beta'
__version__ = '0.1.1b'
__py_version__ = '3.9.7'
__expired_tag__ = False

'''
Status Level
3 = Optimal
2 = Hurt
1 = Wounded
0 = Incapacitated
'''

#form_class = uic.loadUiType("mainwindow_011b.ui")[0]

class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self):
        '''
        Open the About dialog window
        '''
        super().__init__()
        log.info('PyQt5 aboutDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 aboutDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the About dialog window
        '''
        log.info('PyQt5 aboutDialog closing...')
        self.close()

class alertDialog(QDialog, Ui_alertDialog):
    def __init__(self):
        '''
        Open the Alert dialog window
        '''
        super().__init__()
        log.info('PyQt5 alertDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 alertDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the Alert dialog window
        '''
        log.info('PyQt5 alertDialog closing...')
        self.close()

class missingDialog(QDialog, Ui_missingDialog):
    def __init__(self):
        '''
        Open the Missing dialog window
        '''
        super().__init__()
        log.info('PyQt5 missingDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 misingDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the Missing dialog window
        '''
        log.info('PyQt5 missingDialog closing...')
        self.close()

#class MainWindow(QMainWindow):
#class MainWindow(QMainWindow, form_class):
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        Display the main app window.
        Connect all the buttons to their functions.
        Initialize their value ranges.
        '''
        super().__init__()
        
        #uic.loadUi("mainwindow_011b.ui", self)
        
        log.info('PyQt5 MainWindow initializing...')
        self.setupUi(self)
        
        # Set the default save folder and file type
        self.char_folder = 'Planet Matriarchy Characters'
        self.file_extension = '.tps'
        self.file_format = 1.2

        self.loadButton.clicked.connect(self.loadButton_clicked)
        self.actionLoad.triggered.connect(self.loadButton_clicked)
        self.rollInitiative_Button.clicked.connect(self.rollInitiative_buttonClicked)
        self.actionRoll_Initiative.triggered.connect(self.rollInitiative_buttonClicked)
        self.rollInitiative_Button.setDisabled(True)
        self.actionRoll_Initiative.setDisabled(True)
        self.rollresult_Button.clicked.connect(self.rollresult_buttonClicked)
        self.actionRoll_Result.triggered.connect(self.rollresult_buttonClicked)
        self.rollresult_Button.setDisabled(True)
        self.actionRoll_Result.setDisabled(True)
        self.bodyRadio.setDisabled(True)
        self.bodyRadio.setChecked(False)
        self.bodyScore.setDisabled(True)
        self.mindRadio.setDisabled(True)
        self.mindRadio.setChecked(False)
        self.mindScore.setDisabled(True)
        self.spiritRadio.setDisabled(True)
        self.spiritRadio.setChecked(False)
        self.spiritScore.setDisabled(True)
        self.agilitySkill.setDisabled(True)
        self.beautySkill.setDisabled(True)
        self.strengthSkill.setDisabled(True)
        self.knowledgeSkill.setDisabled(True)
        self.perceptionSkill.setDisabled(True)
        self.technologySkill.setDisabled(True)
        self.charismaSkill.setDisabled(True)
        self.empathySkill.setDisabled(True)
        self.focusSkill.setDisabled(True)
        self.boxingSkill.setDisabled(True)
        self.meleeSkill.setDisabled(True)
        self.rangedSkill.setDisabled(True)
        self.artSkill.setDisabled(True)
        self.languagesSkill.setDisabled(True)
        self.scienceSkill.setDisabled(True)
        self.clairvoyanceSkill.setDisabled(True)
        self.psychokinesisSkill.setDisabled(True)
        self.telepathySkill.setDisabled(True)
        self.agilityRadio.setDisabled(True)
        self.beautyRadio.setDisabled(True)
        self.strengthRadio.setDisabled(True)
        self.knowledgeRadio.setDisabled(True)
        self.perceptionRadio.setDisabled(True)
        self.technologyRadio.setDisabled(True)
        self.charismaRadio.setDisabled(True)
        self.empathyRadio.setDisabled(True)
        self.focusRadio.setDisabled(True)
        self.boxingRadio.setDisabled(True)
        self.meleeRadio.setDisabled(True)
        self.rangedRadio.setDisabled(True)
        self.artRadio.setDisabled(True)
        self.languagesRadio.setDisabled(True)
        self.scienceRadio.setDisabled(True)
        self.clairvoyanceRadio.setDisabled(True)
        self.psychokinesisRadio.setDisabled(True)
        self.telepathyRadio.setDisabled(True)
        self.agilityRadio.setChecked(False)
        self.beautyRadio.setChecked(False)
        self.strengthRadio.setChecked(False)
        self.knowledgeRadio.setChecked(False)
        self.perceptionRadio.setChecked(False)
        self.technologyRadio.setChecked(False)
        self.charismaRadio.setChecked(False)
        self.empathyRadio.setChecked(False)
        self.focusRadio.setChecked(False)
        self.boxingRadio.setChecked(False)
        self.meleeRadio.setChecked(False)
        self.rangedRadio.setChecked(False)
        self.artRadio.setChecked(False)
        self.languagesRadio.setChecked(False)
        self.scienceRadio.setChecked(False)
        self.clairvoyanceRadio.setChecked(False)
        self.psychokinesisRadio.setChecked(False)
        self.telepathyRadio.setChecked(False)
        self.clearIDR_Button.clicked.connect(self.clearIDR_buttonClicked)
        self.action_ClearIDR.triggered.connect(self.clearIDR_buttonClicked)
        self.actionVisit_Blog.triggered.connect(self.Visit_Blog)
        self.actionFeedback.triggered.connect(self.Feedback)
        self.actionOverview.triggered.connect(self.Overview_menu)
        self.actionAbout_TPSDieRoller.triggered.connect(self.actionAbout_triggered)
        self.actionQuit.triggered.connect(self.quitButton_clicked)
        # self.inputDM.valueChanged.connect(self.inputDM_valueChanged)
        # self.DMbox = True
        # self.inputDM.setDisabled(self.DMbox)
        self.selDiff.addItem('Choose One')
        self.selDiff.addItem('Easy 3')
        self.selDiff.addItem('Average 6')
        self.selDiff.addItem('Hard 10')
        self.selDiff.addItem('Very 14')
        self.selDiff.addItem('Impossible 18')
        self.selDiff.addItem('Random')
        self.selDiff.addItem('Unknown')
        self.selDiff.setCurrentIndex(0)
        self.selDiff.currentIndexChanged.connect(self.selDiff_valueChanged)
        self.selDiff.setDisabled(True)
        self.bodyRadio.toggled.connect(self.bodyRadio_valueChanged)
        self.mindRadio.toggled.connect(self.mindRadio_valueChanged)
        self.spiritRadio.toggled.connect(self.spiritRadio_valueChanged)
        self.agilityRadio.toggled.connect(self.agilityRadio_valueChanged)
        self.beautyRadio.toggled.connect(self.beautyRadio_valueChanged)
        self.strengthRadio.toggled.connect(self.strengthRadio_valueChanged)
        self.knowledgeRadio.toggled.connect(self.knowledgeRadio_valueChanged)
        self.perceptionRadio.toggled.connect(self.perceptionRadio_valueChanged)
        self.technologyRadio.toggled.connect(self.technologyRadio_valueChanged)
        self.charismaRadio.toggled.connect(self.charismaRadio_valueChanged)
        self.empathyRadio.toggled.connect(self.empathyRadio_valueChanged)
        self.focusRadio.toggled.connect(self.focusRadio_valueChanged)
        self.boxingRadio.toggled.connect(self.boxingRadio_valueChanged)
        self.meleeRadio.toggled.connect(self.meleeRadio_valueChanged)
        self.rangedRadio.toggled.connect(self.rangedRadio_valueChanged)
        self.artRadio.toggled.connect(self.artRadio_valueChanged)
        self.languagesRadio.toggled.connect(self.languagesRadio_valueChanged)
        self.scienceRadio.toggled.connect(self.scienceRadio_valueChanged)
        self.clairvoyanceRadio.toggled.connect(self.clairvoyanceRadio_valueChanged)
        self.psychokinesisRadio.toggled.connect(self.psychokinesisRadio_valueChanged)
        self.telepathyRadio.toggled.connect(self.telepathyRadio_valueChanged)
        self.rollInput.returnPressed.connect(self.manual_roll)
        self.clearRollHistory.clicked.connect(self.clearRollHistoryClicked)
        self.action_ClearRollHistory.triggered.connect(self.clearRollHistoryClicked)

        #self.le = QLineEdit()
        #self.le.returnPressed.connect(self.append_text)

        # Is the difficulty known?
        self.unknown = False

        # Set difficulty to not chosen yet
        self.target_num = 0

        self.health_hurt_flag = False
        self.sanity_hurt_flag = False
        self.morale_hurt_flag = False
        self.health_wounded_flag = False
        self.sanity_wounded_flag = False
        self.morale_wounded_flag = False

        # Set the About menu item
        self.popAboutDialog=aboutDialog()

        # Set the Alert menu item
        self.popAlertDialog=alertDialog()

        # Set the Missing menu item
        self.popMissingDialog=missingDialog()

        log.info('PyQt5 MainWindow initialized.')

        if __expired_tag__ is True:
            '''
            Beta for this app has expired!
            '''
            log.warning(__app__ + ' expiration detected...')
            self.alert_window()
            '''
            display alert message and disable all the things
            '''
            self.loadButton.setDisabled(True)
            self.actionLoad.setDisabled(True)
            self.selDiff.setDisabled(True)
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.clearIDR_Button.setDisabled(True)
            self.action_ClearIDR.setDisabled(True)
            self.actionVisit_Blog.setDisabled(True)
            self.actionFeedback.setDisabled(True)
            self.actionOverview.setDisabled(True)
            self.actionAbout_TPSDieRoller.setDisabled(True)
            self.rollInput.setDisabled(True)
            self.clearRollHistory.setDisabled(True)
            self.rollBrowser.setDisabled(True)
            self.action_ClearRollHistory.setDisabled(True)
            self.charnameDisplay.setDisabled(True)
            self.healthDisplay.setDisabled(True)
            self.sanityDisplay.setDisabled(True)
            self.moraleDisplay.setDisabled(True)
        else:
            self.temp_dir = os.path.expanduser('~')
            os.chdir(self.temp_dir)
            if not os.path.exists('.tpsrpg') or not os.path.exists('.tpsrpg\\' + self.char_folder):
                log.info(self.char_folder + ' folder not found!')
                self.missing_window()
                '''
                display alert message and disable all the things
                '''
                self.loadButton.setDisabled(True)
                self.actionLoad.setDisabled(True)
                self.selDiff.setDisabled(True)
                self.rollInitiative_Button.setDisabled(True)
                self.actionRoll_Initiative.setDisabled(True)
                self.clearIDR_Button.setDisabled(True)
                self.action_ClearIDR.setDisabled(True)
                self.actionVisit_Blog.setDisabled(True)
                self.actionFeedback.setDisabled(True)
                self.actionOverview.setDisabled(True)
                self.actionAbout_TPSDieRoller.setDisabled(True)
                self.rollInput.setDisabled(True)
                self.clearRollHistory.setDisabled(True)
                self.rollBrowser.setDisabled(True)
                self.action_ClearRollHistory.setDisabled(True)
                self.charnameDisplay.setDisabled(True)
                self.healthDisplay.setDisabled(True)
                self.sanityDisplay.setDisabled(True)
                self.moraleDisplay.setDisabled(True)
            else:
                os.chdir(self.temp_dir + '\.tpsrpg')
                f = open('tps.ini', 'r')
                read_data = f.readlines()

                self.folder_list =[]
                for index, line in enumerate(read_data):
                    read_line = line.strip()
                    if read_line != '' and read_line != '[CharGen Folders]':
                        self.selectFolder.addItem(read_line)
                        self.folder_list.append(read_line)

                f.close()

                self.selectFolder.setCurrentIndex(0)
                self.char_folder = self.folder_list[self.selectFolder.currentIndex()]
                self.selectFolder.currentIndexChanged.connect(self.selectFolder_valueChanged)
                log.info('TPS folders found')
    
    def loadButton_clicked(self):
        '''
        Load a saved character
        '''
        self.temp_dir = os.path.expanduser('~')
        os.chdir(self.temp_dir + '\.tpsrpg')
        self.filename = QFileDialog.getOpenFileName(self, 'Open TPS Character File', self.char_folder, 'TPS files (*' + self.file_extension + ')')
        if self.filename[0] != '':
            log.info('Loading ' + self.filename[0])
            with open(self.filename[0], 'r') as json_file:
                self.char_data = json.load(json_file)
                #pprint.pprint(self.char_data)
                self.format_read = self.char_data['Fileformat']
                log.info('File format is: ' + str(self.format_read))
                self.charnameDisplay.setText(self.char_data['Name'])
                self.charnameDisplay.setDisabled(False)
                self.selDiff.setCurrentIndex(0)
                self.selDiff.setDisabled(True)
                self.bodyScore.setValue(self.char_data['BODY'])
                self.bodyScore.setDisabled(True)
                self.mindScore.setValue(self.char_data['MIND'])
                self.mindScore.setDisabled(True)
                self.spiritScore.setValue(self.char_data['SPIRIT'])
                self.spiritScore.setDisabled(True)
                self.bodyRadio.setCheckable(False)
                self.bodyRadio.setCheckable(True)
                self.bodyRadio.setDisabled(True)
                self.mindRadio.setCheckable(False)
                self.mindRadio.setCheckable(True)
                self.mindRadio.setDisabled(True)
                self.spiritRadio.setCheckable(False)
                self.spiritRadio.setCheckable(True)
                self.spiritRadio.setDisabled(True)
                self.healthStatus.setText('')
                self.sanityStatus.setText('')
                self.moraleStatus.setText('')
                self.actionMod.setText('')
                self.healthDisplay.setText(self.char_data['HEALTH'])
                if self.healthDisplay.text() == '2':
                    self.actionMod.setText('<span style=" color:#ff0000;">+1</span>')
                    self.healthStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.healthDisplay.text() == '1':
                    self.actionMod.setText('<span style=" color:#ff0000;">+3</span>')
                    self.healthStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.healthDisplay.text() == '0':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Incapacitated</span>')
                    log.debug('Character is incapacitated!')
                if int(self.healthDisplay.text()) < 0:
                    self.healthStatus.setText('<span style=" color:#ff0000;">Expire</span>')
                    log.debug('Character has expired!')
                self.sanityDisplay.setText(self.char_data['SANITY'])
                if self.sanityDisplay.text() == '2':
                    self.actionMod.setText('<span style=" color:#ff0000;">+1</span>')
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.sanityDisplay.text() == '1':
                    self.actionMod.setText('<span style=" color:#ff0000;">+3</span>')
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.sanityDisplay.text() == '0':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Erratic</span>')
                    log.debug('Character is erratic!')
                if int(self.sanityDisplay.text()) < 0:
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Snap</span>')
                    log.debug('Character has snapped!')
                self.moraleDisplay.setText(self.char_data['MORALE'])
                if self.moraleDisplay.text() == '2':
                    self.actionMod.setText('<span style=" color:#ff0000;">+1</span>')
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.moraleDisplay.text() == '1':
                    self.actionMod.setText('<span style=" color:#ff0000;">+3</span>')
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.moraleDisplay.text() == '0':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">In Fear</span>')
                    log.debug('Character is in fear!')
                if int(self.moraleDisplay.text()) < 0:
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Submit</span>')
                    log.debug('Character has submit!')
                self.agilitySkill.setValue(self.char_data['Agility'])
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setValue(self.char_data['Beauty'])
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setValue(self.char_data['Strength'])
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setValue(self.char_data['Knowledge'])
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setValue(self.char_data['Perception'])
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setValue(self.char_data['Technology'])
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setValue(self.char_data['Charisma'])
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setValue(self.char_data['Empathy'])
                self.empathySkill.setDisabled(True)
                self.focusSkill.setValue(self.char_data['Focus'])
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setValue(self.char_data['Boxing'])
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setValue(self.char_data['Melee'])
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setValue(self.char_data['Ranged'])
                self.rangedSkill.setDisabled(True)
                if self.char_folder != 'We Want Soviet Men Characters':
                    self.artSkill.setDisabled(True)
                    self.languagesSkill.setDisabled(True)
                    self.scienceSkill.setDisabled(True)
                    self.clairvoyanceSkill.setDisabled(True)
                    self.psychokinesisSkill.setDisabled(True)
                    self.telepathySkill.setDisabled(True)
                if self.char_folder == 'We Want Soviet Men Characters':
                    self.clairvoyanceSkill.setValue(self.char_data['Clairvoyance'])
                    self.clairvoyanceSkill.setDisabled(True)
                    self.psychokinesisSkill.setValue(self.char_data['Psychokinesis'])
                    self.psychokinesisSkill.setDisabled(True)
                    self.telepathySkill.setValue(self.char_data['Telepathy'])
                    self.telepathySkill.setDisabled(True)
                self.rewardDisplay.setText(self.char_data['Reward'])
                if int(self.healthDisplay.text()) > 0:
                    self.rollInitiative_Button.setDisabled(False)
                else:
                    self.rollInitiative_Button.setDisabled(True)
                self.actionRoll_Initiative.setDisabled(False)
                self.initiativeDisplay.setText('')
                self.rollresult_Button.setDisabled(True)
                self.actionRoll_Result.setDisabled(True)
                self.rollresultDisplay.setText('')
                if int(self.healthDisplay.text()) > 1:
                    self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
                    self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
                    log.debug('Character can move fine.')
                elif int(self.healthDisplay.text()) == 1:
                    self.movementDisplay.setText('<span style=" color:#ff0000;">' + str((1 + self.bodyScore.value() + self.agilitySkill.value()) // 2) + ' spaces</span>')
                    self.rangeDisplay.setText('<span style=" color:#ff0000;">' + str((1 + self.bodyScore.value() + self.strengthSkill.value()) // 2) + ' miles</span>')
                    log.debug("Character's movement is cut in half.")
                elif int(self.healthDisplay.text()) < 1:
                    self.movementDisplay.setText('<span style=" color:#ff0000;">0 spaces</span>')
                    self.rangeDisplay.setText('<span style=" color:#ff0000;">0 miles</span>')
                    log.debug("Character can't move.")
                self.agilityRadio.setCheckable(False)
                self.agilityRadio.setCheckable(True)
                self.agilityRadio.setDisabled(True)
                self.beautyRadio.setCheckable(False)
                self.beautyRadio.setCheckable(True)
                self.beautyRadio.setDisabled(True)
                self.strengthRadio.setCheckable(False)
                self.strengthRadio.setCheckable(True)
                self.strengthRadio.setDisabled(True)
                self.knowledgeRadio.setCheckable(False)
                self.knowledgeRadio.setCheckable(True)
                self.knowledgeRadio.setDisabled(True)
                self.perceptionRadio.setCheckable(False)
                self.perceptionRadio.setCheckable(True)
                self.perceptionRadio.setDisabled(True)
                self.technologyRadio.setCheckable(False)
                self.technologyRadio.setCheckable(True)
                self.technologyRadio.setDisabled(True)
                self.charismaRadio.setCheckable(False)
                self.charismaRadio.setCheckable(True)
                self.charismaRadio.setDisabled(True)
                self.empathyRadio.setCheckable(False)
                self.empathyRadio.setCheckable(True)
                self.empathyRadio.setDisabled(True)
                self.focusRadio.setCheckable(False)
                self.focusRadio.setCheckable(True)
                self.focusRadio.setDisabled(True)
                self.boxingRadio.setCheckable(False)
                self.boxingRadio.setCheckable(True)
                self.boxingRadio.setDisabled(True)
                self.meleeRadio.setCheckable(False)
                self.meleeRadio.setCheckable(True)
                self.meleeRadio.setDisabled(True)
                self.rangedRadio.setCheckable(False)
                self.rangedRadio.setCheckable(True)
                self.rangedRadio.setDisabled(True)
                self.artRadio.setCheckable(False)
                self.artRadio.setCheckable(True)
                self.artRadio.setDisabled(True)
                self.languagesRadio.setCheckable(False)
                self.languagesRadio.setCheckable(True)
                self.languagesRadio.setDisabled(True)
                self.scienceRadio.setCheckable(False)
                self.scienceRadio.setCheckable(True)
                self.scienceRadio.setDisabled(True)
                self.clairvoyanceRadio.setCheckable(False)
                self.clairvoyanceRadio.setCheckable(True)
                self.clairvoyanceRadio.setDisabled(True)
                self.psychokinesisRadio.setCheckable(False)
                self.psychokinesisRadio.setCheckable(True)
                self.psychokinesisRadio.setDisabled(True)
                self.telepathyRadio.setCheckable(False)
                self.telepathyRadio.setCheckable(True)
                self.telepathyRadio.setDisabled(True)

    def selectFolder_valueChanged(self):
        '''
        Choose folder to load characters from
        '''
        self.char_folder = self.folder_list[self.selectFolder.currentIndex()]
        log.info('Selected folder is ' + self.char_folder)

    def selDiff_valueChanged(self):
        '''
        Choose the difficulty for the action
        '''
        # Enable Attribute buttons after difficulty has been chosen
        self.bodyRadio.setDisabled(False)
        self.mindRadio.setDisabled(False)
        self.spiritRadio.setDisabled(False)

        action_difficulty = [0, 3, 6, 10, 14, 18]
        if self.selDiff.currentIndex() == 0:
            self.target_num = 0
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
        elif self.selDiff.currentIndex() == 6:
            
            # A random difficulty has been asked for
            log.debug('Difficulty is random')
            self.unknown = False
            self.selDiff.setCurrentIndex(randint(1,5))
            self.target_num = action_difficulty[self.selDiff.currentIndex()]
        elif self.selDiff.currentIndex() == 7:
            
            # The difficulty is unknown to the player.
            # The Game Master can see the difficulty shown on their console.
            self.unknown = True
            self.target_num = action_difficulty[randint(1,5)]
            log.debug('Difficulty is unknown: %d' % self.target_num)
            print('The unknown Target Number is %d' % self.target_num)
        elif self.selDiff.currentIndex() >= 1 and self.selDiff.currentIndex() <= 5:
            
            # A regular difficulty has been given to the player to input
            self.unknown = False
            self.target_num = action_difficulty[self.selDiff.currentIndex()]
            log.debug('Selected Action Difficulty: %d' % self.target_num)

    def rollInitiative_buttonClicked(self):
        '''
        Roll for Initiative
        '''
        self.initiative = roll(str(self.mindScore.value()) + 'd6')
        self.initiativeDisplay.setText(str(self.initiative))
        self.selDiff.setDisabled(False)
        log.debug('Initiative roll was ' + str(self.initiative))
    
    def bodyRadio_valueChanged(self):
        if self.bodyRadio.isChecked():
            print('Body Roll')
            self.health_hurt_flag = False
            self.health_wounded_flag = False
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.rollresultDisplay.setText('')
            self.selDiff.setDisabled(True)
            self.actionDice = roll(str(self.bodyScore.value()) + 'd6')
            self.agilityRadio.setDisabled(False)
            self.beautyRadio.setDisabled(False)
            self.strengthRadio.setDisabled(False)
            self.knowledgeRadio.setDisabled(False)
            self.perceptionRadio.setDisabled(False)
            self.technologyRadio.setDisabled(False)
            self.charismaRadio.setDisabled(False)
            self.empathyRadio.setDisabled(False)
            self.focusRadio.setDisabled(False)
            self.boxingRadio.setDisabled(False)
            self.meleeRadio.setDisabled(False)
            self.rangedRadio.setDisabled(False)
            if self.char_folder == 'We Want Soviet Men Characters':
                self.artRadio.setDisabled(False)
                self.languagesRadio.setDisabled(False)
                self.scienceRadio.setDisabled(False)
                self.clairvoyanceRadio.setDisabled(False)
                self.psychokinesisRadio.setDisabled(False)
                self.telepathyRadio.setDisabled(False)
            if self.healthDisplay.text() == '2':
                self.health_hurt_flag = True
            if self.healthDisplay.text() == '1':
                self.health_wounded_flag = True
    
    def mindRadio_valueChanged(self):
        if self.mindRadio.isChecked():
            print('Mind Roll')
            self.sanity_hurt_flag = False
            self.sanity_wounded_flag = False
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.rollresultDisplay.setText('')
            self.selDiff.setDisabled(True)
            self.actionDice = roll(str(self.mindScore.value()) + 'd6')
            self.agilityRadio.setDisabled(False)
            self.beautyRadio.setDisabled(False)
            self.strengthRadio.setDisabled(False)
            self.knowledgeRadio.setDisabled(False)
            self.perceptionRadio.setDisabled(False)
            self.technologyRadio.setDisabled(False)
            self.charismaRadio.setDisabled(False)
            self.empathyRadio.setDisabled(False)
            self.focusRadio.setDisabled(False)
            self.boxingRadio.setDisabled(False)
            self.meleeRadio.setDisabled(False)
            self.rangedRadio.setDisabled(False)
            if self.char_folder == 'We Want Soviet Men Characters':
                self.artRadio.setDisabled(False)
                self.languagesRadio.setDisabled(False)
                self.scienceRadio.setDisabled(False)
                self.clairvoyanceRadio.setDisabled(False)
                self.psychokinesisRadio.setDisabled(False)
                self.telepathyRadio.setDisabled(False)
            if self.sanityDisplay.text() == '2':
                self.sanity_hurt_flag = True
            if self.sanityDisplay.text() == '1':
                self.sanity_wounded_flag = True
    
    def spiritRadio_valueChanged(self):
        if self.spiritRadio.isChecked():
            self.morale_hurt_flag = False
            self.morale_wounded_flag = False
            print('Spirit Roll')
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.rollresultDisplay.setText('')
            self.selDiff.setDisabled(True)
            self.actionDice = roll(str(self.spiritScore.value()) + 'd6')
            self.agilityRadio.setDisabled(False)
            self.beautyRadio.setDisabled(False)
            self.strengthRadio.setDisabled(False)
            self.knowledgeRadio.setDisabled(False)
            self.perceptionRadio.setDisabled(False)
            self.technologyRadio.setDisabled(False)
            self.charismaRadio.setDisabled(False)
            self.empathyRadio.setDisabled(False)
            self.focusRadio.setDisabled(False)
            self.boxingRadio.setDisabled(False)
            self.meleeRadio.setDisabled(False)
            self.rangedRadio.setDisabled(False)
            if self.char_folder == 'We Want Soviet Men Characters':
                self.artRadio.setDisabled(False)
                self.languagesRadio.setDisabled(False)
                self.scienceRadio.setDisabled(False)
                self.clairvoyanceRadio.setDisabled(False)
                self.psychokinesisRadio.setDisabled(False)
                self.telepathyRadio.setDisabled(False)
            if self.moraleDisplay.text() == '2':
                self.morale_hurt_flag = True
            if self.moraleDisplay.text() == '1':
                self.morale_wounded_flag = True
    
    def agilityRadio_valueChanged(self):
        if self.agilityRadio.isChecked():
            print('Add Agility Skill')
            self.dice_result = self.actionDice + self.agilitySkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def beautyRadio_valueChanged(self):
        if self.beautyRadio.isChecked():
            print('Add Beauty Skill')
            self.dice_result = self.actionDice + self.beautySkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def strengthRadio_valueChanged(self):
        if self.strengthRadio.isChecked():
            print('Add Strength Skill')
            self.dice_result = self.actionDice + self.strengthSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def knowledgeRadio_valueChanged(self):
        if self.knowledgeRadio.isChecked():
            print('Add Knowledge Skill')
            self.dice_result = self.actionDice + self.knowledgeSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def perceptionRadio_valueChanged(self):
        if self.perceptionRadio.isChecked():
            print('Add Perception Skill')
            self.dice_result = self.actionDice + self.perceptionSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def technologyRadio_valueChanged(self):
        if self.technologyRadio.isChecked():
            print('Add Technology Skill')
            self.dice_result = self.actionDice + self.technologySkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def charismaRadio_valueChanged(self):
        if self.charismaRadio.isChecked():
            print('Add Charisma Skill')
            self.dice_result = self.actionDice + self.charismaSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def empathyRadio_valueChanged(self):
        if self.empathyRadio.isChecked():
            print('Add Empathy Skill')
            self.dice_result = self.actionDice + self.empathySkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def focusRadio_valueChanged(self):
        if self.focusRadio.isChecked():
            print('Add Focus Skill')
            self.dice_result = self.actionDice + self.focusSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def boxingRadio_valueChanged(self):
        if self.boxingRadio.isChecked():
            print('Add Boxing Skill')
            self.dice_result = self.actionDice + self.boxingSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def meleeRadio_valueChanged(self):
        if self.meleeRadio.isChecked():
            print('Add Melee Skill')
            self.dice_result = self.actionDice + self.meleeSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def rangedRadio_valueChanged(self):
        if self.rangedRadio.isChecked():
            print('Add Ranged Skill')
            self.dice_result = self.actionDice + self.rangedSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def artRadio_valueChanged(self):
        if self.artRadio.isChecked():
            print('Add Art Skill')
            self.dice_result = self.actionDice + self.artSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def languagesRadio_valueChanged(self):
        if self.languagesRadio.isChecked():
            print('Add Languages Skill')
            self.dice_result = self.actionDice + self.languagesSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def scienceRadio_valueChanged(self):
        if self.scienceRadio.isChecked():
            print('Add Science Skill')
            self.dice_result = self.actionDice + self.scienceSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def clairvoyanceRadio_valueChanged(self):
        if self.clairvoyanceRadio.isChecked():
            print('Add Clairvoyance Skill')
            self.dice_result = self.actionDice + self.clairvoyanceSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def psychokinesisRadio_valueChanged(self):
        if self.psychokinesisRadio.isChecked():
            print('Add Psychokinesis Skill')
            self.dice_result = self.actionDice + self.psychokinesisSkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def telepathyRadio_valueChanged(self):
        if self.telepathyRadio.isChecked():
            print('Add Telepathy Skill')
            self.dice_result = self.actionDice + self.telepathySkill.value()
            self.bodyRadio.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
    
    def rollresult_buttonClicked(self):
        '''
        Display the roll and action result
        '''
        if self.health_hurt_flag or self.sanity_hurt_flag or self.morale_hurt_flag:
            self.target_num += 1
            log.debug('Hurt character receives +1 to difficulty: ' + str(self.target_num))
            self.health_hurt_flag = False
            self.sanity_hurt_flag = False
            self.morale_hurt_flag = False
        if self.health_wounded_flag or self.sanity_wounded_flag or self.morale_wounded_flag:
            self.target_num += 3
            log.debug('Wounded character receives +3 to difficulty: ' + str(self.target_num))
            self.health_wounded_flag = False
            self.sanity_wounded_flag = False
            self.morale_wounded_flag = False
        if self.dice_result > self.target_num:
            self.action_result = str(self.dice_result) + ' - Successful'
        else:
            self.action_result = str(self.dice_result) + ' - Failed'
        self.rollresultDisplay.setText(self.action_result)
        self.agilitySkill.setDisabled(True)
        self.beautySkill.setDisabled(True)
        self.strengthSkill.setDisabled(True)
        self.knowledgeSkill.setDisabled(True)
        self.perceptionSkill.setDisabled(True)
        self.technologySkill.setDisabled(True)
        self.charismaSkill.setDisabled(True)
        self.empathySkill.setDisabled(True)
        self.focusSkill.setDisabled(True)
        self.boxingSkill.setDisabled(True)
        self.meleeSkill.setDisabled(True)
        self.rangedSkill.setDisabled(True)
        self.agilityRadio.setDisabled(True)
        self.beautyRadio.setDisabled(True)
        self.strengthRadio.setDisabled(True)
        self.knowledgeRadio.setDisabled(True)
        self.perceptionRadio.setDisabled(True)
        self.technologyRadio.setDisabled(True)
        self.charismaRadio.setDisabled(True)
        self.empathyRadio.setDisabled(True)
        self.focusRadio.setDisabled(True)
        self.boxingRadio.setDisabled(True)
        self.meleeRadio.setDisabled(True)
        self.rangedRadio.setDisabled(True)
        self.artRadio.setDisabled(True)
        self.languagesRadio.setDisabled(True)
        self.scienceRadio.setDisabled(True)
        self.telepathyRadio.setDisabled(True)
        self.psychokinesisRadio.setDisabled(True)
        self.telepathyRadio.setDisabled(True)
        log.debug('Displayed action result: ' + self.action_result)

    def clearIDR_buttonClicked(self):
        '''
        Clear initiative, difficulty, and result 
        '''
        log.debug('Cleared I/D/R')
        self.selDiff.setCurrentIndex(0)
        self.selDiff.setDisabled(True)
        self.unknown = False
        self.bodyRadio.setCheckable(False)
        self.bodyRadio.setCheckable(True)
        self.bodyRadio.setDisabled(True)
        self.mindRadio.setCheckable(False)
        self.mindRadio.setCheckable(True)
        self.mindRadio.setDisabled(True)
        self.spiritRadio.setCheckable(False)
        self.spiritRadio.setCheckable(True)
        self.spiritRadio.setDisabled(True)
        if int(self.healthDisplay.text()) > 0:
            self.rollInitiative_Button.setDisabled(False)
        else:
            self.rollInitiative_Button.setDisabled(True)
        self.actionRoll_Initiative.setDisabled(False)
        self.initiativeDisplay.setText('')
        self.rollresult_Button.setDisabled(True)
        self.actionRoll_Result.setDisabled(True)
        self.rollresultDisplay.setText('')
        self.agilityRadio.setDisabled(False)
        self.agilityRadio.setCheckable(False)
        self.agilityRadio.setCheckable(True)
        self.agilityRadio.setDisabled(True)
        self.beautyRadio.setDisabled(False)
        self.beautyRadio.setCheckable(False)
        self.beautyRadio.setCheckable(True)
        self.beautyRadio.setDisabled(True)
        self.strengthRadio.setDisabled(False)
        self.strengthRadio.setCheckable(False)
        self.strengthRadio.setCheckable(True)
        self.strengthRadio.setDisabled(True)
        self.knowledgeRadio.setDisabled(False)
        self.knowledgeRadio.setCheckable(False)
        self.knowledgeRadio.setCheckable(True)
        self.knowledgeRadio.setDisabled(True)
        self.perceptionRadio.setDisabled(False)
        self.perceptionRadio.setCheckable(False)
        self.perceptionRadio.setCheckable(True)
        self.perceptionRadio.setDisabled(True)
        self.technologyRadio.setDisabled(False)
        self.technologyRadio.setCheckable(False)
        self.technologyRadio.setCheckable(True)
        self.technologyRadio.setDisabled(True)
        self.charismaRadio.setDisabled(False)
        self.charismaRadio.setCheckable(False)
        self.charismaRadio.setCheckable(True)
        self.charismaRadio.setDisabled(True)
        self.empathyRadio.setDisabled(False)
        self.empathyRadio.setCheckable(False)
        self.empathyRadio.setCheckable(True)
        self.empathyRadio.setDisabled(True)
        self.focusRadio.setDisabled(False)
        self.focusRadio.setCheckable(False)
        self.focusRadio.setCheckable(True)
        self.focusRadio.setDisabled(True)
        self.boxingRadio.setDisabled(False)
        self.boxingRadio.setCheckable(False)
        self.boxingRadio.setCheckable(True)
        self.boxingRadio.setDisabled(True)
        self.meleeRadio.setDisabled(False)
        self.meleeRadio.setCheckable(False)
        self.meleeRadio.setCheckable(True)
        self.meleeRadio.setDisabled(True)
        self.rangedRadio.setDisabled(False)
        self.rangedRadio.setCheckable(False)
        self.rangedRadio.setCheckable(True)
        self.rangedRadio.setDisabled(True)
        self.artRadio.setDisabled(False)
        self.artRadio.setCheckable(False)
        self.artRadio.setCheckable(True)
        self.artRadio.setDisabled(True)
        self.languagesRadio.setDisabled(False)
        self.languagesRadio.setCheckable(False)
        self.languagesRadio.setCheckable(True)
        self.languagesRadio.setDisabled(True)
        self.scienceRadio.setDisabled(False)
        self.scienceRadio.setCheckable(False)
        self.scienceRadio.setCheckable(True)
        self.scienceRadio.setDisabled(True)
        self.clairvoyanceRadio.setDisabled(False)
        self.clairvoyanceRadio.setCheckable(False)
        self.clairvoyanceRadio.setCheckable(True)
        self.clairvoyanceRadio.setDisabled(True)
        self.psychokinesisRadio.setDisabled(False)
        self.psychokinesisRadio.setCheckable(False)
        self.psychokinesisRadio.setCheckable(True)
        self.psychokinesisRadio.setDisabled(True)
        self.telepathyRadio.setDisabled(False)
        self.telepathyRadio.setCheckable(False)
        self.telepathyRadio.setCheckable(True)
        self.telepathyRadio.setDisabled(True)

    def Visit_Blog(self):
        '''
        open web browser to blog URL
        '''
        os.startfile('http://shawndriscoll.blogspot.com')
        
    def Feedback(self):
        '''
        open an email letter to send as feedback to the author
        '''
        os.startfile('mailto:shawndriscoll@hotmail.com?subject=Feedback: ' + __app__ + ' for Total Party Skills RPG')
        
    def Overview_menu(self):
        '''
        open this app's PDF manual
        '''
        log.info(__app__ + ' looking for PDF manual...')
        os.startfile(CURRENT_DIR + '\\tps_dieroller_manual.pdf')
        log.info(__app__ + ' found PDF manual. Opening...')
        
    def actionAbout_triggered(self):
        '''
        open the About window
        '''
        log.info(__app__ + ' show about...')
        self.popAboutDialog.show()
    
    def manual_roll(self):
        '''
        A roll was inputed manually
        '''
        log.debug('Manually entered')
        dice_entered = self.rollInput.text()
        roll_returned = roll(dice_entered)
        if roll_returned == -9999:
            returned_line = dice_entered + ' = ' + '<span style=" color:#ff0000;">' + str(roll_returned) + '</span>'
        else:
            returned_line = dice_entered + ' = ' + str(roll_returned)
        self.rollBrowser.append(returned_line)

    def clearRollHistoryClicked(self):
        '''
        Clear the roll history
        '''
        log.debug('Roll history cleared')
        self.rollInput.clear()
        self.rollBrowser.clear()
    
    def alert_window(self):
        '''
        open the Alert window
        '''
        log.warning(__app__ + ' show Beta expired PyQt5 alertDialog...')
        self.popAlertDialog.show()

    def missing_window(self):
        '''
        open the Missing window
        '''
        log.warning(__app__ + ' show missing...')
        self.popMissingDialog.show()

    def quitButton_clicked(self):
        '''
        select "Quit" from the drop-down menu
        '''
        log.info(__app__ + ' quiting...')
        log.info(__app__ + ' DONE.')
        self.close()

if __name__ == '__main__':

    '''
    Technically, this program starts right here when run.
    If this program is imported instead of run, none of the code below is executed.
    '''

#     logging.basicConfig(filename = 'TPS DieRoller.log',
#                         level = logging.DEBUG,
#                         format = '%(asctime)s %(levelname)s %(name)s - %(message)s',
#                         datefmt='%a, %d %b %Y %H:%M:%S',
#                         filemode = 'w')

    log = logging.getLogger('TPS DieRoller011b')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/TPS DieRoller.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s', datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info('Logging started.')
    log.info(__app__ + ' starting...')

    trange = time.localtime()

    log.info(__app__ + ' started, and running...')
    
    if len(sys.argv) < 2:

        #if trange[0] > 2022 or trange[1] > 8:
        if trange[0] > 2021:
            __expired_tag__ = True
            __app__ += ' [EXPIRED]'

        app = QApplication(sys.argv)
        
        # Use print(QStyleFactory.keys()) to find a setStyle you like, instead of 'Fusion'

        # app.setStyle('Fusion')
        
        # darkPalette = QPalette()
        # darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        # darkPalette.setColor(QPalette.WindowText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
        # darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        # darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        # darkPalette.setColor(QPalette.ToolTipText, Qt.white)
        # darkPalette.setColor(QPalette.Text, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
        # darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        # darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        # darkPalette.setColor(QPalette.ButtonText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.BrightText, Qt.red)
        # darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        # darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        # darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
        # darkPalette.setColor(QPalette.HighlightedText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
        
        mainApp = MainWindow()
        mainApp.show()

        # app.setPalette(darkPalette)

        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        #print(CURRENT_DIR)        

        app.exec_()
    
    #elif trange[0] > 2022 or trange[1] > 8:
    elif trange[0] > 2021:
        __app__ += ' [EXPIRED]'
        '''
        Beta for this app has expired!
        '''
        log.warning(__app__)
        print()
        print(__app__)
        
    elif sys.argv[1] in ['-h', '/h', '--help', '-?', '/?']:
        log.info('TPS DieRoller was run from the CMD prompt.  Help will be sent if needed.')
        print()
        print('     Using the CMD prompt to make dice rolls:')
        print("     C:\>tps_dieroller.py roll('2d6')")
        print()
        print('     Or just:')
        print('     C:\>tps_dieroller.py 2d6')
    elif sys.argv[1] in ['-v', '/v', '--version']:
        print()
        print('     TPS DieRoller, release version ' + __version__ + ' for Python ' + __py_version__)
        log.info('Reporting: TPS DieRoller release version: %s' % __version__)
    else:
        print()
        dice = ''
        if len(sys.argv) > 2:
            for i in range(len(sys.argv)):
                if i > 0:
                    dice += sys.argv[i]
        else:
            dice = sys.argv[1]
        if "roll('" in dice:
            num = dice.find("')")
            if num != -1:
                dice = dice[6:num]
                dice = str(dice).upper().strip()
                num = roll(dice)
                if dice != 'TEST' and dice != 'INFO':
                    print("Your '%s' roll is %d." % (dice, num))
                    log.info("The direct call to TPS DieRoller with '%s' resulted in %d." % (dice, num))
                elif dice == 'INFO':
                    print('TPS DieRoller, release version ' + __version__ + ' for Python ' + __py_version__)
                    log.info('Reporting: TPS DieRoller release version: %s' % __version__)
        else:
            dice = str(dice).upper().strip()
            num = roll(dice)
            if dice != 'TEST' and dice != 'INFO':
                print("Your '%s' roll is %d." % (dice, num))
                log.info("The direct call to TPS DieRoller with '%s' resulted in %d." % (dice, num))
            elif dice == 'INFO':
                print('TPS DieRoller, release version ' + __version__ + ' for Python ' + __py_version__)
                log.info('Reporting: TPS DieRoller release version: %s' % __version__)
