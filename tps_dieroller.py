#
#   TPS DieRoller Beta for the Total Party System
#   Written for Python 3.11.6
#
##############################################################

"""
TPS DieRoller 0.5.1 Beta for the Total Party System
-------------------------------------------------------

This program rolls 6-sided dice and calculates their effects.

The Total Party System was written by R. Joshua Holland.
Copyright 2021 - 2023, Total Party Skills.
"""
#import vlc

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5 import uic
#import PyQt5.QtMultimedia as MM
import time
from mainwindow import Ui_MainWindow
from aboutdialog import Ui_aboutDialog
from alertdialog import Ui_alertDialog
from missingdialog import Ui_missingDialog
from random import randint
from rpg_tools.pydice import roll
import sys
import os
import logging
import json

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'TPS DieRoller 0.5.1 (Beta)'
__version__ = '0.5.1b'
__py_version_req__ = (3,11,6)
__expired_tag__ = False

'''
Status Level
3 = Optimal
2 = Hurt
1 = Wounded
0 = Incapacitated
'''

#form_class = uic.loadUiType("mainwindow.ui")[0]

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
        log.info('PyQt5 missingDialog initialized.')
        
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
        
        #uic.loadUi("mainwindow.ui", self)
        
        log.info('PyQt5 MainWindow initializing...')
        self.setupUi(self)
        
        # Set the default save folder and file type
        self.char_folder = 'Planet Matriarchy Characters'
        self.file_extension = '.tps'
        self.file_format = 3.3

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
        self.dodgeSkill.setDisabled(True)
        self.parrySkill.setDisabled(True)
        self.strikeSkill.setDisabled(True)
        self.blessSkill.setDisabled(True)
        self.exorcismSkill.setDisabled(True)
        self.healingSkill.setDisabled(True)
        self.demonologySkill.setDisabled(True)
        self.metamorphosisSkill.setDisabled(True)
        self.necromancySkill.setDisabled(True)
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
        self.dodgeRadio.setDisabled(True)
        self.parryRadio.setDisabled(True)
        self.strikeRadio.setDisabled(True)
        self.blessRadio.setDisabled(True)
        self.exorcismRadio.setDisabled(True)
        self.healingRadio.setDisabled(True)
        self.demonologyRadio.setDisabled(True)
        self.metamorphosisRadio.setDisabled(True)
        self.necromancyRadio.setDisabled(True)
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
        self.dodgeRadio.setChecked(False)
        self.parryRadio.setChecked(False)
        self.strikeRadio.setChecked(False)
        self.blessRadio.setChecked(False)
        self.exorcismRadio.setChecked(False)
        self.healingRadio.setChecked(False)
        self.demonologyRadio.setChecked(False)
        self.metamorphosisRadio.setChecked(False)
        self.necromancyRadio.setChecked(False)
        self.clairvoyanceRadio.setChecked(False)
        self.psychokinesisRadio.setChecked(False)
        self.telepathyRadio.setChecked(False)
        self.clearInit_Button.clicked.connect(self.clearInit_buttonClicked)
        self.clearInit_Button.setDisabled(True)
        self.action_ClearInit.triggered.connect(self.clearInit_buttonClicked)
        self.action_ClearInit.setDisabled(True)
        self.actionVisit_Blog.triggered.connect(self.Visit_Blog)
        self.actionFeedback.triggered.connect(self.Feedback)
        self.actionOverview.triggered.connect(self.Overview_menu)
        self.actionAbout_TPSDieRoller.triggered.connect(self.actionAbout_triggered)
        self.actionQuit.triggered.connect(self.quitButton_clicked)
        # self.inputDM.valueChanged.connect(self.inputDM_valueChanged)
        # self.DMbox = True
        # self.inputDM.setDisabled(self.DMbox)
        self.selDiff.addItem('Choose One')
        self.selDiff.addItem('Easy')            # target naumber 3
        self.selDiff.addItem('Average')         # target naumber 6
        self.selDiff.addItem('Hard')            # target naumber 10
        self.selDiff.addItem('Very')            # target naumber 14
        self.selDiff.addItem('Impossible')      # target naumber 18
        self.selDiff.addItem('Random')          # target naumber is random
        self.selDiff.addItem('Unknown')         # target naumber is unknown
        self.selDiff.setCurrentIndex(0)
        self.selDiff.currentIndexChanged.connect(self.selDiff_valueChanged)
        self.selDiff.setDisabled(True)
        self.clearAction_Button.clicked.connect(self.clearAction_buttonClicked)
        self.clearAction_Button.setDisabled(True)
        self.farrange_Button.clicked.connect(self.farrange_buttonClicked)
        self.farrange_Button.setDisabled(True)
        self.moveattack_Button.clicked.connect(self.moveattack_buttonClicked)
        self.moveattack_Button.setDisabled(True)
        self.fullcover_Button.clicked.connect(self.fullcover_buttonClicked)
        self.fullcover_Button.setDisabled(True)
        self.partialcover_Button.clicked.connect(self.partialcover_buttonClicked)
        self.partialcover_Button.setDisabled(True)
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
        self.dodgeRadio.toggled.connect(self.dodgeRadio_valueChanged)
        self.parryRadio.toggled.connect(self.parryRadio_valueChanged)
        self.strikeRadio.toggled.connect(self.strikeRadio_valueChanged)
        self.blessRadio.toggled.connect(self.blessRadio_valueChanged)
        self.exorcismRadio.toggled.connect(self.exorcismRadio_valueChanged)
        self.demonologyRadio.toggled.connect(self.demonologyRadio_valueChanged)
        self.metamorphosisRadio.toggled.connect(self.metamorphosisRadio_valueChanged)
        self.necromancyRadio.toggled.connect(self.necromancyRadio_valueChanged)
        self.clairvoyanceRadio.toggled.connect(self.clairvoyanceRadio_valueChanged)
        self.psychokinesisRadio.toggled.connect(self.psychokinesisRadio_valueChanged)
        self.telepathyRadio.toggled.connect(self.telepathyRadio_valueChanged)
        self.rollInput.returnPressed.connect(self.manual_roll)
        self.clearRollHistory.clicked.connect(self.clearRollHistoryClicked)
        self.action_ClearRollHistory.triggered.connect(self.clearRollHistoryClicked)

        self.farrange = False
        self.farrange_mod = 0
        self.moveattack = False
        self.moveattack_mod = 0
        self.fullcover = False
        self.fullcover_mod = 0
        self.partialcover = False
        self.partialcover_mod = 0
        self.vampire_flag = False

        #self.le = QLineEdit()
        #self.le.returnPressed.connect(self.append_text)

        # Is the difficulty known?
        self.unknown = False

        # Set difficulty to not chosen yet
        self.target_num = 0
        self.modified_target_num = 0

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
            self.clearInit_Button.setDisabled(True)
            self.action_ClearInit.setDisabled(True)
            self.clearAction_Button.setDisabled(True)
            self.farrange_Button.setDisabled(True)
            self.moveattack_Button.setDisabled(True)
            self.fullcover_Button.setDisabled(True)
            self.partialcover_Button.setDisabled(True)
            self.actionVisit_Blog.setDisabled(True)
            self.actionFeedback.setDisabled(True)
            self.actionOverview.setDisabled(True)
            self.actionAbout_TPSDieRoller.setDisabled(True)
            self.rollInput.setDisabled(True)
            self.clearRollHistory.setDisabled(True)
            self.rollBrowser.setDisabled(True)
            self.action_ClearRollHistory.setDisabled(True)
        else:
            self.temp_dir = os.path.expanduser('~')
            os.chdir(self.temp_dir)
            if not os.path.exists('.tpsrpg') or not os.path.exists('.tpsrpg\\' + 'tps.ini'):
                print('tps.ini not found!')
                log.warning('tps.ini not found!')
                log.warning("You'll need https://github.com/ShawnDriscoll/Planet-Matriarchy-RPG-CharGen to start making characters.")
                self.missing_window()
                '''
                display alert message and disable all the things
                '''
                self.loadButton.setDisabled(True)
                self.actionLoad.setDisabled(True)
                self.selDiff.setDisabled(True)
                self.rollInitiative_Button.setDisabled(True)
                self.actionRoll_Initiative.setDisabled(True)
                self.clearInit_Button.setDisabled(True)
                self.action_ClearInit.setDisabled(True)
                self.clearAction_Button.setDisabled(True)
                self.farrange_Button.setDisabled(True)
                self.moveattack_Button.setDisabled(True)
                self.fullcover_Button.setDisabled(True)
                self.partialcover_Button.setDisabled(True)
                self.actionVisit_Blog.setDisabled(True)
                self.actionFeedback.setDisabled(True)
                self.actionOverview.setDisabled(True)
                self.actionAbout_TPSDieRoller.setDisabled(True)
                self.rollInput.setDisabled(True)
                self.clearRollHistory.setDisabled(True)
                self.rollBrowser.setDisabled(True)
                self.action_ClearRollHistory.setDisabled(True)
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
                log.info('TPS folders found.')
    
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
                self.format_read = self.char_data['Fileformat']
                if self.format_read == self.file_format:
                    log.info('File format read is standard ' + str(self.format_read))
                elif self.format_read < self.file_format:
                    log.warning('[Warning] Reading an older file format of ' + str(self.format_read))
                elif self.format_read > self.file_format:
                    log.warning('[Warning] Reading a (newer?!) file format of ' + str(self.format_read))
                
                if self.format_read == self.file_format:
                    self.vampire_flag = self.char_data['Is_Vampire']
                else:
                    self.vampire_flag = False
                    self.cult = ''

                if self.vampire_flag == True:
                    self.cult = self.char_data['Cult']
                    if self.cult == 'Boeotian Club':
                        self.enc = 3
                        self.mov = 2
                        self.ran = 5
                    else:
                        self.enc = 1
                        self.mov = 1
                        self.ran = 1
                else:
                    self.enc = 1
                    self.mov = 1
                    self.ran = 1
                
                self.charnameDisplay.setText(self.char_data['Name'])
                self.charnameDisplay.setDisabled(False)
                self.selDiff.setCurrentIndex(0)
                self.selDiff.setDisabled(True)
                self.bodyScore.setText(str(self.char_data['BODY']))
                self.bodyScore.setDisabled(False)
                self.mindScore.setText(str(self.char_data['MIND']))
                self.mindScore.setDisabled(False)
                self.spiritScore.setText(str(self.char_data['SPIRIT']))
                self.spiritScore.setDisabled(False)
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
                self.encumberedStatus.setText('')
                self.encumbered_flag = self.char_data['Encumbered']
                self.actionMod.setText('')
                self.healthDisplay.setText(self.char_data['HEALTH'])
                if self.healthDisplay.text() == '2':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.healthDisplay.text() == '1':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.healthDisplay.text() == '0':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Incapacitated</span>')
                    log.debug('Character is incapacitated!')
                if int(self.healthDisplay.text()) < 0:
                    self.healthStatus.setText('<span style=" color:#ff0000;">Expire</span>')
                    log.debug('Character has expired!')
                self.sanityDisplay.setText(self.char_data['SANITY'])
                if self.sanityDisplay.text() == '2':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.sanityDisplay.text() == '1':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.sanityDisplay.text() == '0':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Erratic</span>')
                    log.debug('Character is erratic!')
                if int(self.sanityDisplay.text()) < 0:
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Snap</span>')
                    log.debug('Character has snapped!')
                self.moraleDisplay.setText(self.char_data['MORALE'])
                if self.moraleDisplay.text() == '2':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.moraleDisplay.text() == '1':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.moraleDisplay.text() == '0':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">In Fear</span>')
                    log.debug('Character is in fear!')
                if int(self.moraleDisplay.text()) < 0:
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Submit</span>')
                    log.debug('Character has submit!')
                self.agilitySkill.setText(str(self.char_data['Agility']))
                self.agilitySkill.setDisabled(False)
                self.beautySkill.setText(str(self.char_data['Beauty']))
                self.beautySkill.setDisabled(False)
                self.strengthSkill.setText(str(self.char_data['Strength']))
                self.strengthSkill.setDisabled(False)
                self.knowledgeSkill.setText(str(self.char_data['Knowledge']))
                self.knowledgeSkill.setDisabled(False)
                self.perceptionSkill.setText(str(self.char_data['Perception']))
                self.perceptionSkill.setDisabled(False)
                self.technologySkill.setText(str(self.char_data['Technology']))
                self.technologySkill.setDisabled(False)
                self.charismaSkill.setText(str(self.char_data['Charisma']))
                self.charismaSkill.setDisabled(False)
                self.empathySkill.setText(str(self.char_data['Empathy']))
                self.empathySkill.setDisabled(False)
                self.focusSkill.setText(str(self.char_data['Focus']))
                self.focusSkill.setDisabled(False)
                self.boxingSkill.setText(str(self.char_data['Boxing']))
                self.boxingSkill.setDisabled(False)
                self.meleeSkill.setText(str(self.char_data['Melee']))
                self.meleeSkill.setDisabled(False)
                self.rangedSkill.setText(str(self.char_data['Ranged']))
                self.rangedSkill.setDisabled(False)
                
                if self.char_data['Art'] == -1:
                    self.artSkill.setText('0')
                else:
                    self.artSkill.setText(str(self.char_data['Art']))
                self.artSkill.setDisabled(False)
                
                if self.char_data['Languages'] == -1:
                    self.languagesSkill.setText('0')
                else:
                    self.languagesSkill.setText(str(self.char_data['Languages']))
                self.languagesSkill.setDisabled(False)
                
                if self.char_data['Science'] == -1:
                    self.scienceSkill.setText('0')
                else:
                    self.scienceSkill.setText(str(self.char_data['Science']))
                self.scienceSkill.setDisabled(False)

                if self.char_data['Dodge'] == -1:
                    self.dodgeSkill.setText('0')
                else:
                    self.dodgeSkill.setText(str(self.char_data['Dodge']))
                self.dodgeSkill.setDisabled(False)
                
                if self.char_data['Parry'] == -1:
                    self.parrySkill.setText('0')
                else:
                    self.parrySkill.setText(str(self.char_data['Parry']))
                self.parrySkill.setDisabled(False)
                
                if self.char_data['Strike'] == -1:
                    self.strikeSkill.setText('0')
                else:
                    self.strikeSkill.setText(str(self.char_data['Strike']))
                self.strikeSkill.setDisabled(False)
                
                if self.char_data['Bless'] == -1:
                    self.blessSkill.setText('0')
                else:
                    self.blessSkill.setText(str(self.char_data['Bless']))
                self.blessSkill.setDisabled(False)
                
                if self.char_data['Exorcism'] == -1:
                    self.exorcismSkill.setText('0')
                else:
                    self.exorcismSkill.setText(str(self.char_data['Exorcism']))
                self.exorcismSkill.setDisabled(False)
                
                if self.char_data['Healing'] == -1:
                    self.healingSkill.setText('0')
                else:
                    self.healingSkill.setText(str(self.char_data['Healing']))
                self.healingSkill.setDisabled(False)
                
                if self.char_data['Demonology'] == -1:
                    self.demonologySkill.setText('0')
                else:
                    self.demonologySkill.setText(str(self.char_data['Demonology']))
                self.demonologySkill.setDisabled(False)
                
                if self.char_data['Metamorphosis'] == -1:
                    self.metamorphosisSkill.setText('0')
                else:
                    self.metamorphosisSkill.setText(str(self.char_data['Metamorphosis']))
                self.metamorphosisSkill.setDisabled(False)
                
                if self.char_data['Necromancy'] == -1:
                    self.necromancySkill.setText('0')
                else:
                    self.necromancySkill.setText(str(self.char_data['Necromancy']))
                self.necromancySkill.setDisabled(False)
                
                if self.char_data['Clairvoyance'] == -1:
                    self.clairvoyanceSkill.setText('0')
                else:
                    self.clairvoyanceSkill.setText(str(self.char_data['Clairvoyance']))
                self.clairvoyanceSkill.setDisabled(False)
                
                if self.char_data['Psychokinesis'] == -1:
                    self.psychokinesisSkill.setText('0')
                else:
                    self.psychokinesisSkill.setText(str(self.char_data['Psychokinesis']))
                self.psychokinesisSkill.setDisabled(False)
                
                if self.char_data['Telepathy'] == -1:
                    self.telepathySkill.setText('0')
                else:
                    self.telepathySkill.setText(str(self.char_data['Telepathy']))
                self.telepathySkill.setDisabled(False)
                
                self.rewardDisplay.setText(self.char_data['Reward'])
                if int(self.healthDisplay.text()) < 0 or int(self.sanityDisplay.text()) < 0 or int(self.moraleDisplay.text()) < 0:
                    self.rollInitiative_Button.setDisabled(True)
                    self.actionRoll_Initiative.setDisabled(True)
                    #self.clearInit_Button.setDisabled(True)
                    #self.action_ClearInit.setDisabled(True)
                else:
                    self.rollInitiative_Button.setDisabled(False)
                    self.actionRoll_Initiative.setDisabled(False)
                    #self.clearInit_Button.setDisabled(False)
                    #self.action_ClearInit.setDisabled(False)
                self.clearInit_Button.setDisabled(True)
                self.action_ClearInit.setDisabled(True)
                self.initiativeDisplay.setText('')
                self.rollresult_Button.setDisabled(True)
                self.actionRoll_Result.setDisabled(True)
                self.rollresultDisplay.setText('')
                red_flag = False
                temp_encumbrance = self.enc + int(self.bodyScore.text()) + int(self.strengthSkill.text())
                temp_movement = self.mov + int(self.bodyScore.text()) + int(self.agilitySkill.text())
                temp_range = self.ran + int(self.bodyScore.text()) + int(self.strengthSkill.text())
                if int(self.healthDisplay.text()) > 1 and not self.encumbered_flag:
                    self.movementDisplay.setText(str(self.mov + int(self.bodyScore.text()) + int(self.agilitySkill.text())) + ' spaces')
                    self.rangeDisplay.setText(str(self.ran + int(self.bodyScore.text()) + int(self.strengthSkill.text())) + ' miles')
                    if self.vampire_flag == True and self.cult == 'Boeotian Club' and int(self.psychokinesisSkill.text()) > 0:
                        self.flightDisplay.setText(str(int(self.spiritScore.text()) + int(self.psychokinesisSkill.text())))
                    else:
                        self.flightDisplay.setText('')
                    log.debug('Character can move fine.')
                elif int(self.healthDisplay.text()) == 1:
                    red_flag = True
                    temp_movement = temp_movement // 2
                    temp_range = temp_range // 2
                    log.debug("Wounded character's movement is cut in half.")
                elif int(self.healthDisplay.text()) < 1:
                    red_flag = True
                    temp_movement = 0
                    temp_range = 0
                    log.debug("Character can't move.")
                if self.encumbered_flag:
                    red_flag = True
                    temp_movement = temp_movement // 2
                    temp_range = temp_range // 2
                    log.debug("Encumbered character's movement is cut in half.")
                self.encumbranceDisplay.setText(str(temp_encumbrance) + ' items')
                if self.encumbered_flag:
                    self.encumberedStatus.setText('<span style=" color:#ff0000;">Encumbered</span>')
                else:
                    self.encumberedStatus.setText('')
                if red_flag:
                    self.movementDisplay.setText('<span style=" color:#ff0000;">' + str(temp_movement) + ' spaces</span>')
                    self.rangeDisplay.setText('<span style=" color:#ff0000;">' + str(temp_range) + ' miles</span>')
                else:
                    self.movementDisplay.setText(str(temp_movement) + ' spaces')
                    self.rangeDisplay.setText(str(temp_range) + ' miles')
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
                self.dodgeRadio.setCheckable(False)
                self.dodgeRadio.setCheckable(True)
                self.dodgeRadio.setDisabled(True)
                self.parryRadio.setCheckable(False)
                self.parryRadio.setCheckable(True)
                self.parryRadio.setDisabled(True)
                self.strikeRadio.setCheckable(False)
                self.strikeRadio.setCheckable(True)
                self.strikeRadio.setDisabled(True)
                self.blessRadio.setCheckable(False)
                self.blessRadio.setCheckable(True)
                self.blessRadio.setDisabled(True)
                self.exorcismRadio.setCheckable(False)
                self.exorcismRadio.setCheckable(True)
                self.exorcismRadio.setDisabled(True)
                self.healingRadio.setCheckable(False)
                self.healingRadio.setCheckable(True)
                self.healingRadio.setDisabled(True)
                self.demonologyRadio.setCheckable(False)
                self.demonologyRadio.setCheckable(True)
                self.demonologyRadio.setDisabled(True)
                self.metamorphosisRadio.setCheckable(False)
                self.metamorphosisRadio.setCheckable(True)
                self.metamorphosisRadio.setDisabled(True)
                self.necromancyRadio.setCheckable(False)
                self.necromancyRadio.setCheckable(True)
                self.necromancyRadio.setDisabled(True)
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
        self.farrange_Button.setDisabled(False)
        self.farrange = False
        self.farrangeModDisplay.setText('')
        self.farrange_mod = 0
        self.moveattack_Button.setDisabled(False)
        self.moveattack = False
        self.moveattackModDisplay.setText('')
        self.moveattack_mod = 0
        self.fullcover_Button.setDisabled(False)
        self.fullcover = False
        self.fullcoverModDisplay.setText('')
        self.fullcover_mod = 0
        self.partialcover_Button.setDisabled(False)
        self.partialcover = False
        self.partialcoverModDisplay.setText('')
        self.partialcover_mod = 0
        self.bodyRadio.setDisabled(False)
        self.mindRadio.setDisabled(False)
        self.spiritRadio.setDisabled(False)

        action_difficulty = [0, 3, 6, 10, 14, 18]
        if self.selDiff.currentIndex() == 0:
            self.target_num = 0
            self.targetnumberDisplay.setText('')
            self.farrange_Button.setDisabled(True)
            self.moveattack_Button.setDisabled(True)
            self.fullcover_Button.setDisabled(True)
            self.partialcover_Button.setDisabled(True)
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
        elif self.selDiff.currentIndex() == 6:
            
            # A random difficulty has been asked for
            log.debug('Difficulty is random')
            self.unknown = False
            self.selDiff.setCurrentIndex(randint(1,5))
            self.target_num = action_difficulty[self.selDiff.currentIndex()]
            self.targetnumberDisplay.setText(str(self.target_num))
        elif self.selDiff.currentIndex() == 7:
            
            # The difficulty is unknown to the player.
            # The Game Master can see the difficulty shown on their console.
            self.unknown = True
            self.target_num = action_difficulty[randint(1,5)]
            self.targetnumberDisplay.setText('?')
            log.debug('Difficulty is unknown: %d' % self.target_num)
            print('The unknown Target Number is %d' % self.target_num)
        elif self.selDiff.currentIndex() >= 1 and self.selDiff.currentIndex() <= 5:
            
            # A regular difficulty has been given to the player to input
            self.unknown = False
            self.target_num = action_difficulty[self.selDiff.currentIndex()]
            self.targetnumberDisplay.setText(str(self.target_num))
            log.debug('Selected Action Difficulty: %d' % self.target_num)

    def rollInitiative_buttonClicked(self):
        '''
        Roll for Initiative
        '''
        if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters' or \
                self.char_folder == 'Planet Matriarchy Characters' or self.char_folder == 'Strange Bedfellows Characters' or \
                self.char_folder == 'We Want Soviet Men Characters':
            self.initiative = self.mindScore.text() + 'd6+' + self.charismaSkill.text()
        else:
            self.initiative = self.mindScore.text() + 'd6+' + self.perceptionSkill.text()
        self.dice_result = roll(self.initiative)
        self.print_to_box = self.initiative + ' = ' + str(self.dice_result)
        self.rollInput.setText(self.initiative)
        self.rollBrowser.append(self.print_to_box)
        self.initiativeDisplay.setText(str(self.dice_result))
        self.selDiff.setDisabled(False)
        self.rollInitiative_Button.setDisabled(True)
        self.actionRoll_Initiative.setDisabled(True)
        self.clearInit_Button.setDisabled(False)
        self.action_ClearInit.setDisabled(False)
        log.debug('Initiative roll was ' + str(self.initiative))
    
    def farrange_buttonClicked(self):
        '''
        Toggle far range penalty
        '''
        if self.farrange:
            self.farrange = False
            self.farrangeModDisplay.setText('')
            self.farrange_mod = 0
        else:
            self.farrange = True
            self.farrangeModDisplay.setText('<span style=" color:#ff0000;">+3</span>')
            self.farrange_mod = 3
            
            if self.moveattack:
                self.moveattack = False
                self.moveattackModDisplay.setText('')
                self.moveattack_mod = 0
    
    def moveattack_buttonClicked(self):
        '''
        Toggle move attack penalty
        '''
        if self.moveattack:
            self.moveattack = False
            self.moveattackModDisplay.setText('')
            self.moveattack_mod = 0
        else:
            self.moveattack = True
            self.moveattackModDisplay.setText('<span style=" color:#ff0000;">+1</span>')
            self.moveattack_mod = 1
            
            if self.farrange:
                self.farrange = False
                self.farrangeModDisplay.setText('')
                self.farrange_mod = 0
    
    def fullcover_buttonClicked(self):
        '''
        Toggle full cover penalty
        '''
        if self.fullcover:
            self.fullcover = False
            self.fullcoverModDisplay.setText('')
            self.fullcover_mod = 0
        else:
            self.fullcover = True
            self.fullcoverModDisplay.setText('<span style=" color:#ff0000;">+4</span>')
            self.fullcover_mod = 4
            
            if self.partialcover:
                self.partialcover = False
                self.partialcoverModDisplay.setText('')
                self.partialcover_mod = 0
    
    def partialcover_buttonClicked(self):
        '''
        Toggle partial cover penalty
        '''
        if self.partialcover:
            self.partialcover = False
            self.partialcoverModDisplay.setText('')
            self.partialcover_mod = 0
        else:
            self.partialcover = True
            self.partialcoverModDisplay.setText('<span style=" color:#ff0000;">+2</span>')
            self.partialcover_mod = 2
            
            if self.fullcover:
                self.fullcover = False
                self.fullcoverModDisplay.setText('')
                self.fullcover_mod = 0

    def clearAction_buttonClicked(self):
        '''
        Clear the action (difficulty, modifiers, roll result)
        '''
        log.debug('Cleared D/M/R.')
        self.selDiff.setCurrentIndex(0)
        self.selDiff.setDisabled(False)
        self.clearAction_Button.setDisabled(True)
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
        self.rollresult_Button.setDisabled(True)
        self.actionRoll_Result.setDisabled(True)
        self.rollresultDisplay.setText('')
        self.actionMod.setText('')
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
        self.dodgeRadio.setDisabled(False)
        self.dodgeRadio.setCheckable(False)
        self.dodgeRadio.setCheckable(True)
        self.dodgeRadio.setDisabled(True)
        self.parryRadio.setDisabled(False)
        self.parryRadio.setCheckable(False)
        self.parryRadio.setCheckable(True)
        self.parryRadio.setDisabled(True)
        self.strikeRadio.setDisabled(False)
        self.strikeRadio.setCheckable(False)
        self.strikeRadio.setCheckable(True)
        self.strikeRadio.setDisabled(True)
        self.blessRadio.setDisabled(False)
        self.blessRadio.setCheckable(False)
        self.blessRadio.setCheckable(True)
        self.blessRadio.setDisabled(True)
        self.exorcismRadio.setDisabled(False)
        self.exorcismRadio.setCheckable(False)
        self.exorcismRadio.setCheckable(True)
        self.exorcismRadio.setDisabled(True)
        self.healingRadio.setDisabled(False)
        self.healingRadio.setCheckable(False)
        self.healingRadio.setCheckable(True)
        self.healingRadio.setDisabled(True)
        self.demonologyRadio.setDisabled(False)
        self.demonologyRadio.setCheckable(False)
        self.demonologyRadio.setCheckable(True)
        self.demonologyRadio.setDisabled(True)
        self.metamorphosisRadio.setDisabled(False)
        self.metamorphosisRadio.setCheckable(False)
        self.metamorphosisRadio.setCheckable(True)
        self.metamorphosisRadio.setDisabled(True)
        self.necromancyRadio.setDisabled(False)
        self.necromancyRadio.setCheckable(False)
        self.necromancyRadio.setCheckable(True)
        self.necromancyRadio.setDisabled(True)
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

    def bodyRadio_valueChanged(self):
        '''
        Body Action was chosen
        '''
        if self.bodyRadio.isChecked():
            self.actionMod.setText('')
            self.modified_target_num = self.target_num
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.rollresultDisplay.setText('')
            self.selDiff.setDisabled(True)
            self.farrange_Button.setDisabled(True)
            self.moveattack_Button.setDisabled(True)
            self.fullcover_Button.setDisabled(True)
            self.partialcover_Button.setDisabled(True)
            self.actionDice = self.bodyScore.text() + 'd6'
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
            if self.char_data['Art'] != -1:
                self.artRadio.setDisabled(False)
            if self.char_data['Languages'] != -1:
                self.languagesRadio.setDisabled(False)
            if self.char_data['Science'] != -1:
                self.scienceRadio.setDisabled(False)
            if self.char_data['Dodge'] > 0:
                self.dodgeRadio.setDisabled(False)
            if self.char_data['Parry'] > 0:
                self.parryRadio.setDisabled(False)
            if self.char_data['Strike'] > 0:
                self.strikeRadio.setDisabled(False)
            if self.char_data['Clairvoyance'] > 0:
                self.clairvoyanceRadio.setDisabled(False)
            if self.char_data['Psychokinesis'] > 0:
                self.psychokinesisRadio.setDisabled(False)
            if self.char_data['Telepathy'] > 0:
                self.telepathyRadio.setDisabled(False)
            if self.char_data['Bless'] > 0:
                self.blessRadio.setDisabled(False)
            if self.char_data['Exorcism'] > 0:
                self.exorcismRadio.setDisabled(False)
            if self.char_data['Healing'] > 0:
                self.healingRadio.setDisabled(False)
            if self.char_data['Demonology'] > 0:
                self.demonologyRadio.setDisabled(False)
            if self.char_data['Metamorphosis'] > 0:
                self.metamorphosisRadio.setDisabled(False)
            if self.char_data['Necromancy'] > 0:
                self.necromancyRadio.setDisabled(False)
            if self.healthDisplay.text() == '2':
                if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters':
                    self.actionMod.setText('<span style=" color:#ff0000;">+2</span>')
                    self.modified_target_num += 2
                    log.debug('Hurt character receives +2 to difficulty: ' + str(self.modified_target_num))
                else:
                    self.actionMod.setText('<span style=" color:#ff0000;">+1</span>')
                    self.modified_target_num += 1
                    log.debug('Hurt character receives +1 to difficulty: ' + str(self.modified_target_num))
            if self.healthDisplay.text() == '1':
                if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters':
                    self.actionMod.setText('<span style=" color:#ff0000;">+4</span>')
                    self.modified_target_num += 4
                    log.debug('Hurt character receives +4 to difficulty: ' + str(self.modified_target_num))
                else:
                    self.actionMod.setText('<span style=" color:#ff0000;">+3</span>')
                    self.modified_target_num += 3
                    log.debug('Hurt character receives +3 to difficulty: ' + str(self.modified_target_num))
    
    def mindRadio_valueChanged(self):
        '''
        Mind Action was chosen
        '''
        if self.mindRadio.isChecked():
            self.actionMod.setText('')
            self.modified_target_num = self.target_num
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.rollresultDisplay.setText('')
            self.selDiff.setDisabled(True)
            self.farrange_Button.setDisabled(True)
            self.moveattack_Button.setDisabled(True)
            self.fullcover_Button.setDisabled(True)
            self.partialcover_Button.setDisabled(True)
            self.actionDice = self.mindScore.text() + 'd6'
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
            if self.char_data['Art'] != -1:
                self.artRadio.setDisabled(False)
            if self.char_data['Languages'] != -1:
                self.languagesRadio.setDisabled(False)
            if self.char_data['Science'] != -1:
                self.scienceRadio.setDisabled(False)
            if self.char_data['Dodge'] > 0:
                self.dodgeRadio.setDisabled(False)
            if self.char_data['Parry'] > 0:
                self.parryRadio.setDisabled(False)
            if self.char_data['Strike'] > 0:
                self.strikeRadio.setDisabled(False)
            if self.char_data['Clairvoyance'] > 0:
                self.clairvoyanceRadio.setDisabled(False)
            if self.char_data['Psychokinesis'] > 0:
                self.psychokinesisRadio.setDisabled(False)
            if self.char_data['Telepathy'] > 0:
                self.telepathyRadio.setDisabled(False)
            if self.char_data['Bless'] > 0:
                self.blessRadio.setDisabled(False)
            if self.char_data['Exorcism'] > 0:
                self.exorcismRadio.setDisabled(False)
            if self.char_data['Healing'] > 0:
                self.healingRadio.setDisabled(False)
            if self.char_data['Demonology'] > 0:
                self.demonologyRadio.setDisabled(False)
            if self.char_data['Metamorphosis'] > 0:
                self.metamorphosisRadio.setDisabled(False)
            if self.char_data['Necromancy'] > 0:
                self.necromancyRadio.setDisabled(False)
            if self.sanityDisplay.text() == '2':
                if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters':
                    self.actionMod.setText('<span style=" color:#ff0000;">+2</span>')
                    self.modified_target_num += 2
                    log.debug('Hurt character receives +2 to difficulty: ' + str(self.modified_target_num))
                else:
                    self.actionMod.setText('<span style=" color:#ff0000;">+1</span>')
                    self.modified_target_num += 1
                    log.debug('Hurt character receives +1 to difficulty: ' + str(self.modified_target_num))
            if self.sanityDisplay.text() == '1':
                if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters':
                    self.actionMod.setText('<span style=" color:#ff0000;">+4</span>')
                    self.modified_target_num += 4
                    log.debug('Hurt character receives +4 to difficulty: ' + str(self.modified_target_num))
                else:
                    self.actionMod.setText('<span style=" color:#ff0000;">+3</span>')
                    self.modified_target_num += 3
                    log.debug('Hurt character receives +3 to difficulty: ' + str(self.modified_target_num))
    
    def spiritRadio_valueChanged(self):
        '''
        Spirit Action was chosen
        '''
        if self.spiritRadio.isChecked():
            self.actionMod.setText('')
            self.modified_target_num = self.target_num
            self.rollInitiative_Button.setDisabled(True)
            self.actionRoll_Initiative.setDisabled(True)
            self.rollresultDisplay.setText('')
            self.selDiff.setDisabled(True)
            self.farrange_Button.setDisabled(True)
            self.moveattack_Button.setDisabled(True)
            self.fullcover_Button.setDisabled(True)
            self.partialcover_Button.setDisabled(True)
            self.actionDice = self.spiritScore.text() + 'd6'
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
            if self.char_data['Art'] != -1:
                self.artRadio.setDisabled(False)
            if self.char_data['Languages'] != -1:
                self.languagesRadio.setDisabled(False)
            if self.char_data['Science'] != -1:
                self.scienceRadio.setDisabled(False)
            if self.char_data['Dodge'] > 0:
                self.dodgeRadio.setDisabled(False)
            if self.char_data['Parry'] > 0:
                self.parryRadio.setDisabled(False)
            if self.char_data['Strike'] > 0:
                self.strikeRadio.setDisabled(False)
            if self.char_data['Clairvoyance'] > 0:
                self.clairvoyanceRadio.setDisabled(False)
            if self.char_data['Psychokinesis'] > 0:
                self.psychokinesisRadio.setDisabled(False)
            if self.char_data['Telepathy'] > 0:
                self.telepathyRadio.setDisabled(False)
            if self.char_data['Bless'] > 0:
                self.blessRadio.setDisabled(False)
            if self.char_data['Exorcism'] > 0:
                self.exorcismRadio.setDisabled(False)
            if self.char_data['Healing'] > 0:
                self.healingRadio.setDisabled(False)
            if self.char_data['Demonology'] > 0:
                self.demonologyRadio.setDisabled(False)
            if self.char_data['Metamorphosis'] > 0:
                self.metamorphosisRadio.setDisabled(False)
            if self.char_data['Necromancy'] > 0:
                self.necromancyRadio.setDisabled(False)
            if self.moraleDisplay.text() == '2':
                if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters':
                    self.actionMod.setText('<span style=" color:#ff0000;">+2</span>')
                    self.modified_target_num += 2
                    log.debug('Hurt character receives +2 to difficulty: ' + str(self.modified_target_num))
                else:
                    self.actionMod.setText('<span style=" color:#ff0000;">+1</span>')
                    self.modified_target_num += 1
                    log.debug('Hurt character receives +1 to difficulty: ' + str(self.modified_target_num))
            if self.moraleDisplay.text() == '1':
                #self.morale_wounded_flag = True
                if self.char_folder == 'Expedition to Ancient Aegypt Characters' or self.char_folder == 'Heroes of Aegypt Characters':
                    self.actionMod.setText('<span style=" color:#ff0000;">+4</span>')
                    self.modified_target_num += 4
                    log.debug('Hurt character receives +4 to difficulty: ' + str(self.modified_target_num))
                else:
                    self.actionMod.setText('<span style=" color:#ff0000;">+3</span>')
                    self.modified_target_num += 3
                    log.debug('Hurt character receives +3 to difficulty: ' + str(self.modified_target_num))
    
    def agilityRadio_valueChanged(self):
        if self.agilityRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.agilitySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def beautyRadio_valueChanged(self):
        if self.beautyRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.beautySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def strengthRadio_valueChanged(self):
        if self.strengthRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.strengthSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def knowledgeRadio_valueChanged(self):
        if self.knowledgeRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.knowledgeSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def perceptionRadio_valueChanged(self):
        if self.perceptionRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.perceptionSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def technologyRadio_valueChanged(self):
        if self.technologyRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.technologySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def charismaRadio_valueChanged(self):
        if self.charismaRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.charismaSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def empathyRadio_valueChanged(self):
        if self.empathyRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.empathySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def focusRadio_valueChanged(self):
        if self.focusRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.focusSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def boxingRadio_valueChanged(self):
        if self.boxingRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.boxingSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def meleeRadio_valueChanged(self):
        if self.meleeRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.meleeSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def rangedRadio_valueChanged(self):
        if self.rangedRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.rangedSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def artRadio_valueChanged(self):
        if self.artRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.artSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def languagesRadio_valueChanged(self):
        if self.languagesRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.languagesSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def scienceRadio_valueChanged(self):
        if self.scienceRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.scienceSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def dodgeRadio_valueChanged(self):
        if self.dodgeRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.dodgeSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def parryRadio_valueChanged(self):
        if self.parryRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.parrySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def strikeRadio_valueChanged(self):
        if self.strikeRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.strikeSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def blessRadio_valueChanged(self):
        if self.blessRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.blessSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def exorcismRadio_valueChanged(self):
        if self.exorcismRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.exorcismSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def healingRadio_valueChanged(self):
        if self.healingRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.healingSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def demonologyRadio_valueChanged(self):
        if self.demonologyRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.demonologySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def metamorphosisRadio_valueChanged(self):
        if self.metamorphosisRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.metamorphosisSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def necromancyRadio_valueChanged(self):
        if self.necromancyRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.necromancySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def clairvoyanceRadio_valueChanged(self):
        if self.clairvoyanceRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.clairvoyanceSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def psychokinesisRadio_valueChanged(self):
        if self.psychokinesisRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.psychokinesisSkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def telepathyRadio_valueChanged(self):
        if self.telepathyRadio.isChecked():
            self.rollDice = self.actionDice + '+' + self.telepathySkill.text()
            self.bodyRadio.setDisabled(True)
            self.mindRadio.setDisabled(True)
            self.spiritRadio.setDisabled(True)
            self.rollresult_Button.setDisabled(False)
            self.actionRoll_Result.setDisabled(False)
    
    def rollresult_buttonClicked(self):
        '''
        Display the roll and action result
        '''
        self.dice_result = roll(self.rollDice)
        self.print_to_box = self.rollDice + ' = ' + str(self.dice_result)
        self.rollInput.setText(self.rollDice)
        self.rollBrowser.append(self.print_to_box)
        if self.dice_result > self.modified_target_num + self.farrange_mod + self.moveattack_mod + self.fullcover_mod + self.partialcover_mod:
            self.action_result = str(self.dice_result) + ' - Successful'
        else:
            self.action_result = str(self.dice_result) + ' - Failed'
        self.rollresultDisplay.setText(self.action_result)
        self.rollresult_Button.setDisabled(True)
        self.actionRoll_Result.setDisabled(True)
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
        self.dodgeRadio.setDisabled(True)
        self.parryRadio.setDisabled(True)
        self.strikeRadio.setDisabled(True)
        self.blessRadio.setDisabled(True)
        self.exorcismRadio.setDisabled(True)
        self.healingRadio.setDisabled(True)
        self.demonologyRadio.setDisabled(True)
        self.metamorphosisRadio.setDisabled(True)
        self.necromancyRadio.setDisabled(True)
        self.clairvoyanceRadio.setDisabled(True)
        self.psychokinesisRadio.setDisabled(True)
        self.telepathyRadio.setDisabled(True)
        self.clearAction_Button.setDisabled(False)
        log.debug('Displayed action result: ' + self.action_result + '.')

    def clearInit_buttonClicked(self):
        '''
        Clear Initiative, difficulty, modifiers, and result
        '''
        log.debug('Cleared I/D/M/R.')
        self.selDiff.setCurrentIndex(0)
        self.selDiff.setDisabled(True)
        self.clearInit_Button.setDisabled(True)
        self.action_ClearInit.setDisabled(True)
        self.clearAction_Button.setDisabled(True)
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
        self.rollInitiative_Button.setDisabled(False)
        self.actionRoll_Initiative.setDisabled(False)
        self.initiativeDisplay.setText('')
        self.rollresult_Button.setDisabled(True)
        self.actionRoll_Result.setDisabled(True)
        self.rollresultDisplay.setText('')
        self.actionMod.setText('')
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
        self.dodgeRadio.setDisabled(False)
        self.dodgeRadio.setCheckable(False)
        self.dodgeRadio.setCheckable(True)
        self.dodgeRadio.setDisabled(True)
        self.parryRadio.setDisabled(False)
        self.parryRadio.setCheckable(False)
        self.parryRadio.setCheckable(True)
        self.parryRadio.setDisabled(True)
        self.strikeRadio.setDisabled(False)
        self.strikeRadio.setCheckable(False)
        self.strikeRadio.setCheckable(True)
        self.strikeRadio.setDisabled(True)
        self.blessRadio.setDisabled(False)
        self.blessRadio.setCheckable(False)
        self.blessRadio.setCheckable(True)
        self.blessRadio.setDisabled(True)
        self.exorcismRadio.setDisabled(False)
        self.exorcismRadio.setCheckable(False)
        self.exorcismRadio.setCheckable(True)
        self.exorcismRadio.setDisabled(True)
        self.healingRadio.setDisabled(False)
        self.healingRadio.setCheckable(False)
        self.healingRadio.setCheckable(True)
        self.healingRadio.setDisabled(True)
        self.demonologyRadio.setDisabled(False)
        self.demonologyRadio.setCheckable(False)
        self.demonologyRadio.setCheckable(True)
        self.demonologyRadio.setDisabled(True)
        self.metamorphosisRadio.setDisabled(False)
        self.metamorphosisRadio.setCheckable(False)
        self.metamorphosisRadio.setCheckable(True)
        self.metamorphosisRadio.setDisabled(True)
        self.necromancyRadio.setDisabled(False)
        self.necromancyRadio.setCheckable(False)
        self.necromancyRadio.setCheckable(True)
        self.necromancyRadio.setDisabled(True)
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
        os.startfile('mailto:shawndriscoll@hotmail.com?subject=Feedback: ' + __app__ + ' for Total Party System')
        
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
        dice_entered = self.rollInput.text()
        dice_entered = dice_entered.upper()
        if dice_entered == 'INFO' or dice_entered == 'TEST' or dice_entered == 'MINMAXAVG':
            roll_returned = roll(dice_entered)
        else:
            log.debug('Manual die roll entered.')
            roll_returned = roll(dice_entered)
            
            # Was the roll a valid one?
            if roll_returned == -9999:
                returned_line = dice_entered + ' = ' + '<span style=" color:#ff0000;">' + str(roll_returned) + '</span>'
            else:
                returned_line = dice_entered + ' = ' + str(roll_returned)
                
            # Display the roll result inside the text browser
            self.rollBrowser.append(returned_line)

    def clearRollHistoryClicked(self):
        '''
        Clear the roll history
        '''
        log.debug('Roll history cleared.')
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

    log = logging.getLogger('TPS DieRoller')
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

        if trange[0] > 2024 or trange[1] > 12:
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
    
    elif trange[0] > 2024 or trange[1] > 12:
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
        print('     TPS DieRoller, release version ' + __version__ + ' for Python ' + str(__py_version_req__))
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
                if dice == '':
                    dice = '2D6'
                    log.debug('Default roll was made')
                num = roll(dice)
                if dice != 'TEST' and dice != 'INFO' and dice != 'MINMAXAVG':
                    print("Your '%s' roll is %s." % (dice, num))
                    log.info("The direct call to TPS DieRoller with '%s' resulted in %s." % (dice, num))
                elif dice == 'INFO':
                    print('TPS DieRoller, release version ' + __version__ + ' for Python ' + str(__py_version_req__))
                    log.info('Reporting: TPS DieRoller release version: %s' % __version__)
            else:
                print('Typo of some sort --> ' + dice)
        else:
            dice = str(dice).upper().strip()
            if dice == 'ROLL()':
                dice = '2D6'
                log.debug('Default roll was made')
            num = roll(dice)
            if dice != 'TEST' and dice != 'INFO' and dice != 'MINMAXAVG':
                print("Your '%s' roll is %s." % (dice, num))
                log.info("The direct call to TPS DieRoller with '%s' resulted in %s." % (dice, num))
            elif dice == 'INFO':
                print('TPS DieRoller, release version ' + __version__ + ' for Python ' + str(__py_version_req__))
                log.info('Reporting: TPS DieRoller release version: %s' % __version__)
