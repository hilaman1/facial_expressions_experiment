#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on November 05, 2024, at 13:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
import sys
import site

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'Jena_scratch'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'TLV-device': ['R52R80KXA4W', 'R52N81LPYSF' , 'R52N90V6WZT', 'R52RA06XJ4W'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\YH006_new\\Desktop\\Jena_scratch_7\\Jena_scratch.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "start" ---
textWelcome1 = visual.TextStim(win=win, name='textWelcome1',
    text='Welcome to the Experiment!\n\nPress SPACEBAR to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
SpaceBarStart = keyboard.Keyboard()

# --- Initialize components for Routine "init" ---
# Run 'Begin Experiment' code from conditions
participant_id = int(expInfo['participant'])
if participant_id % 2 == 0:  # even participant ID
    conditions_file = 'routine_order_even.xlsx'
else:  # odd participant ID
    conditions_file = 'routine_order_odd.xlsx'

sequence_i = participant_id % 7
if sequence_i == 0:
    sequence_i = 7
    
sequence_t = sequence_i + 1 if sequence_i < 7 else 1
sequence_it = sequence_t + 1 if sequence_t < 7 else 1

file_sequence_i = f'images_texts_emotions_sequence_{sequence_i}.xlsx'
file_sequence_t = f'images_texts_emotions_sequence_{sequence_t}.xlsx'
file_sequence_it = f'images_texts_emotions_sequence_{sequence_it}.xlsx'
# Run 'Begin Experiment' code from TLV_EMG
import uiautomator2
from threading import Thread

# print screen in adb : adb exec-out screencap -p > screen.png
# in case of app update, if I need to see the XML of application screen layout:
# adb shell uiautomator dump  
# adb pull /sdcard/window_dump.xml
# search clickable="true" in the XML.


# check this on psychopy inside the lab with 2 deivces connected with a usb hub.

# devices = "R52N81LPYSF" , "R52N90V6WZT", "R52RA06XJ4W"
#deviceSerial = settingsInfo["TLV-device"]
deviceSerial = str(expInfo["TLV-device"])
devices = [uiautomator2.Device(deviceSerial)];

add_button_id = "com.xtrodes.xtrodesapp:id/btn_add"

def addFirstEventContainer(device):
    new_event = device(resourceId=add_button_id)[0];
    new_event.click();

def returnToEventScreen(device):
    sideBar_dashboard_btn = device(resourceId="com.xtrodes.xtrodesapp:id/container")[0];
    sideBar_dashboard_btn.click();
    eventlog_btn = device(resourceId="com.xtrodes.xtrodesapp:id/btn_event_log")[0];
    eventlog_btn.click();

def PrepareEventTextAndButton(device, text):
    add_buttons = device(resourceId=add_button_id);
    if (add_buttons.count == 0):
        returnToEventScreen(device);
        add_buttons = device(resourceId=add_button_id);

    if (add_buttons.count == 1):
        addFirstEventContainer(device);
        add_buttons = device(resourceId=add_button_id);

    send_event = add_buttons[1];
    event_text = device(resourceId="com.xtrodes.xtrodesapp:id/et_name")[0];
    event_text.set_text(text);

    return send_event;


def ButtonClickThread(button):
    button.click()

def sendTriggerInBothDevices(text):
    buttons = [PrepareEventTextAndButton(device, text) for device in devices]
    [Thread(target=ButtonClickThread, args=(x,)).start() for x in buttons];
    
#sendTriggerInBothDevices("Init Sequence");

sendTriggerInBothDevices('ID'+ str(expInfo['participant']))

# --- Initialize components for Routine "trial" ---
movie = visual.MovieStim(
    win, name='movie',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.78, 1), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-1
)

# --- Initialize components for Routine "exp_emo_i" ---
exp_i = visual.TextStim(win=win, name='exp_i',
    text='You will be shown images of \nfacial expressions. \n\nPlease imitate the facial expressions immediately upon seeing the image.\n\nRelax upon seeing a white cross.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "emo_i" ---
cross_Hline1 = visual.Line(
    win=win, name='cross_Hline1',
    start=(-(0.1, 0.1)[0]/2.0, 0), end=(+(0.1, 0.1)[0]/2.0, 0),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
cross_Vline1 = visual.Line(
    win=win, name='cross_Vline1',
    start=(-(0.1, 0.1)[0]/2.0, 0), end=(+(0.1, 0.1)[0]/2.0, 0),
    ori=90.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
three1 = visual.TextStim(win=win, name='three1',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
two1 = visual.TextStim(win=win, name='two1',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
one1 = visual.TextStim(win=win, name='one1',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
image_emo_only = visual.ImageStim(
    win=win,
    name='image_emo_only', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.665, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "QA" ---
qa_text = visual.TextStim(win=win, name='qa_text',
    text='Fill in the questionnaire',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
text_continue = visual.TextStim(win=win, name='text_continue',
    text='Press up or down arrow to continue',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "pause_t" ---
breakText = visual.TextStim(win=win, name='breakText',
    text='Break\n\nPress SPACEBAR to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyPress = keyboard.Keyboard()

# --- Initialize components for Routine "exp_emo_t" ---
v_text_title = visual.MovieStim(
    win, name='v_text_title',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.78, 1.0), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-2
)

# --- Initialize components for Routine "emo_t" ---
cross_Hline2 = visual.Line(
    win=win, name='cross_Hline2',
    start=(-(0.1, 0.1)[0]/2.0, 0), end=(+(0.1, 0.1)[0]/2.0, 0),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
cross_Vline2 = visual.Line(
    win=win, name='cross_Vline2',
    start=(-(0.1, 0.1)[0]/2.0, 0), end=(+(0.1, 0.1)[0]/2.0, 0),
    ori=90.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
three2 = visual.TextStim(win=win, name='three2',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
two2 = visual.TextStim(win=win, name='two2',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
one2 = visual.TextStim(win=win, name='one2',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
emotion_only = visual.TextStim(win=win, name='emotion_only',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "pause_it" ---
textbreak = visual.TextStim(win=win, name='textbreak',
    text='Break\n\nPress SPACEBAR to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
presskey = keyboard.Keyboard()

# --- Initialize components for Routine "exp_emo_it" ---
v__text_it = visual.MovieStim(
    win, name='v__text_it',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1.78, 1.0), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-2
)

# --- Initialize components for Routine "emo_it" ---
cross_Hline3 = visual.Line(
    win=win, name='cross_Hline3',
    start=(-(0.1, 0.1)[0]/2.0, 0), end=(+(0.1, 0.1)[0]/2.0, 0),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
cross_Vline3 = visual.Line(
    win=win, name='cross_Vline3',
    start=(-(0.1, 0.1)[0]/2.0, 0), end=(+(0.1, 0.1)[0]/2.0, 0),
    ori=90.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
three3 = visual.TextStim(win=win, name='three3',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
two3 = visual.TextStim(win=win, name='two3',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
image_emotion_2 = visual.ImageStim(
    win=win,
    name='image_emotion_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.532, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
title_emotion = visual.TextStim(win=win, name='title_emotion',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "end" ---
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Finally - you made it!\n\nThank you for your participation!\n\n:)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start" ---
continueRoutine = True
# update component parameters for each repeat
SpaceBarStart.keys = []
SpaceBarStart.rt = []
_SpaceBarStart_allKeys = []
# keep track of which components have finished
startComponents = [textWelcome1, SpaceBarStart]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome1* updates
    
    # if textWelcome1 is starting this frame...
    if textWelcome1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome1.frameNStart = frameN  # exact frame index
        textWelcome1.tStart = t  # local t and not account for scr refresh
        textWelcome1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textWelcome1.started')
        # update status
        textWelcome1.status = STARTED
        textWelcome1.setAutoDraw(True)
    
    # if textWelcome1 is active this frame...
    if textWelcome1.status == STARTED:
        # update params
        pass
    
    # *SpaceBarStart* updates
    waitOnFlip = False
    
    # if SpaceBarStart is starting this frame...
    if SpaceBarStart.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        SpaceBarStart.frameNStart = frameN  # exact frame index
        SpaceBarStart.tStart = t  # local t and not account for scr refresh
        SpaceBarStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SpaceBarStart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SpaceBarStart.started')
        # update status
        SpaceBarStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SpaceBarStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SpaceBarStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SpaceBarStart.status == STARTED and not waitOnFlip:
        theseKeys = SpaceBarStart.getKeys(keyList=['y','n','left','right','space','return'], waitRelease=False)
        _SpaceBarStart_allKeys.extend(theseKeys)
        if len(_SpaceBarStart_allKeys):
            SpaceBarStart.keys = _SpaceBarStart_allKeys[-1].name  # just the last key pressed
            SpaceBarStart.rt = _SpaceBarStart_allKeys[-1].rt
            SpaceBarStart.duration = _SpaceBarStart_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start" ---
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if SpaceBarStart.keys in ['', [], None]:  # No response was made
    SpaceBarStart.keys = None
thisExp.addData('SpaceBarStart.keys',SpaceBarStart.keys)
if SpaceBarStart.keys != None:  # we had a response
    thisExp.addData('SpaceBarStart.rt', SpaceBarStart.rt)
    thisExp.addData('SpaceBarStart.duration', SpaceBarStart.duration)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "init" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initComponents = []
for thisComponent in initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "init" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "init" ---
for thisComponent in initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('videos_schaede.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sendTrigger_videos
    sendTriggerInBothDevices("ID"+ str(expInfo['participant'])+'_'+videos_name)
    movie.setMovie(videos_schaede)
    # keep track of which components have finished
    trialComponents = [movie]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie* updates
        
        # if movie is starting this frame...
        if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'movie.started')
            # update status
            movie.status = STARTED
            movie.setAutoDraw(True)
            movie.play()
        if movie.isFinished:  # force-end the routine
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movie.stop()
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "exp_emo_i" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from sendTriggerEmoI
sendTriggerInBothDevices("expl_emo_i")
# keep track of which components have finished
exp_emo_iComponents = [exp_i]
for thisComponent in exp_emo_iComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "exp_emo_i" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exp_i* updates
    
    # if exp_i is starting this frame...
    if exp_i.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        exp_i.frameNStart = frameN  # exact frame index
        exp_i.tStart = t  # local t and not account for scr refresh
        exp_i.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exp_i, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'exp_i.started')
        # update status
        exp_i.status = STARTED
        exp_i.setAutoDraw(True)
    
    # if exp_i is active this frame...
    if exp_i.status == STARTED:
        # update params
        pass
    
    # if exp_i is stopping this frame...
    if exp_i.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > exp_i.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            exp_i.tStop = t  # not accounting for scr refresh
            exp_i.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exp_i.stopped')
            # update status
            exp_i.status = FINISHED
            exp_i.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp_emo_iComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "exp_emo_i" ---
for thisComponent in exp_emo_iComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# set up handler to look after randomisation of conditions etc
emo_f = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(file_sequence_i),
    seed=None, name='emo_f')
thisExp.addLoop(emo_f)  # add the loop to the experiment
thisEmo_f = emo_f.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmo_f.rgb)
if thisEmo_f != None:
    for paramName in thisEmo_f:
        exec('{} = thisEmo_f[paramName]'.format(paramName))

for thisEmo_f in emo_f:
    currentLoop = emo_f
    # abbreviate parameter names if possible (e.g. rgb = thisEmo_f.rgb)
    if thisEmo_f != None:
        for paramName in thisEmo_f:
            exec('{} = thisEmo_f[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "emo_i" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sendTrigger_emo_i
    trigger_sent = False
    image_emo_only.setImage(image_emotion)
    # keep track of which components have finished
    emo_iComponents = [cross_Hline1, cross_Vline1, three1, two1, one1, image_emo_only]
    for thisComponent in emo_iComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "emo_i" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 9.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_Hline1* updates
        
        # if cross_Hline1 is starting this frame...
        if cross_Hline1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_Hline1.frameNStart = frameN  # exact frame index
            cross_Hline1.tStart = t  # local t and not account for scr refresh
            cross_Hline1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_Hline1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_Hline1.started')
            # update status
            cross_Hline1.status = STARTED
            cross_Hline1.setAutoDraw(True)
        
        # if cross_Hline1 is active this frame...
        if cross_Hline1.status == STARTED:
            # update params
            pass
        
        # if cross_Hline1 is stopping this frame...
        if cross_Hline1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_Hline1.tStartRefresh + 1.9833-frameTolerance:
                # keep track of stop time/frame for later
                cross_Hline1.tStop = t  # not accounting for scr refresh
                cross_Hline1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_Hline1.stopped')
                # update status
                cross_Hline1.status = FINISHED
                cross_Hline1.setAutoDraw(False)
        
        # *cross_Vline1* updates
        
        # if cross_Vline1 is starting this frame...
        if cross_Vline1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_Vline1.frameNStart = frameN  # exact frame index
            cross_Vline1.tStart = t  # local t and not account for scr refresh
            cross_Vline1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_Vline1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_Vline1.started')
            # update status
            cross_Vline1.status = STARTED
            cross_Vline1.setAutoDraw(True)
        
        # if cross_Vline1 is active this frame...
        if cross_Vline1.status == STARTED:
            # update params
            pass
        
        # if cross_Vline1 is stopping this frame...
        if cross_Vline1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_Vline1.tStartRefresh + 1.9833-frameTolerance:
                # keep track of stop time/frame for later
                cross_Vline1.tStop = t  # not accounting for scr refresh
                cross_Vline1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_Vline1.stopped')
                # update status
                cross_Vline1.status = FINISHED
                cross_Vline1.setAutoDraw(False)
        
        # *three1* updates
        
        # if three1 is starting this frame...
        if three1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            three1.frameNStart = frameN  # exact frame index
            three1.tStart = t  # local t and not account for scr refresh
            three1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'three1.started')
            # update status
            three1.status = STARTED
            three1.setAutoDraw(True)
        
        # if three1 is active this frame...
        if three1.status == STARTED:
            # update params
            pass
        
        # if three1 is stopping this frame...
        if three1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three1.tStartRefresh + 0.9833-frameTolerance:
                # keep track of stop time/frame for later
                three1.tStop = t  # not accounting for scr refresh
                three1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'three1.stopped')
                # update status
                three1.status = FINISHED
                three1.setAutoDraw(False)
        
        # *two1* updates
        
        # if two1 is starting this frame...
        if two1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            two1.frameNStart = frameN  # exact frame index
            two1.tStart = t  # local t and not account for scr refresh
            two1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two1.started')
            # update status
            two1.status = STARTED
            two1.setAutoDraw(True)
        
        # if two1 is active this frame...
        if two1.status == STARTED:
            # update params
            pass
        
        # if two1 is stopping this frame...
        if two1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two1.tStartRefresh + 0.9833-frameTolerance:
                # keep track of stop time/frame for later
                two1.tStop = t  # not accounting for scr refresh
                two1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two1.stopped')
                # update status
                two1.status = FINISHED
                two1.setAutoDraw(False)
        
        # *one1* updates
        
        # if one1 is starting this frame...
        if one1.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            one1.frameNStart = frameN  # exact frame index
            one1.tStart = t  # local t and not account for scr refresh
            one1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one1.started')
            # update status
            one1.status = STARTED
            one1.setAutoDraw(True)
        
        # if one1 is active this frame...
        if one1.status == STARTED:
            # update params
            pass
        
        # if one1 is stopping this frame...
        if one1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one1.tStartRefresh + 0.9833-frameTolerance:
                # keep track of stop time/frame for later
                one1.tStop = t  # not accounting for scr refresh
                one1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'one1.stopped')
                # update status
                one1.status = FINISHED
                one1.setAutoDraw(False)
        # Run 'Each Frame' code from sendTrigger_emo_i
        if t >= 4.0 and not trigger_sent:
            sendTriggerInBothDevices("ID"+ str(expInfo['participant'])+'_'+text_emotion_i)
            trigger_sent = True
        
        # *image_emo_only* updates
        
        # if image_emo_only is starting this frame...
        if image_emo_only.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            image_emo_only.frameNStart = frameN  # exact frame index
            image_emo_only.tStart = t  # local t and not account for scr refresh
            image_emo_only.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_emo_only, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_emo_only.started')
            # update status
            image_emo_only.status = STARTED
            image_emo_only.setAutoDraw(True)
        
        # if image_emo_only is active this frame...
        if image_emo_only.status == STARTED:
            # update params
            pass
        
        # if image_emo_only is stopping this frame...
        if image_emo_only.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_emo_only.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_emo_only.tStop = t  # not accounting for scr refresh
                image_emo_only.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_emo_only.stopped')
                # update status
                image_emo_only.status = FINISHED
                image_emo_only.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in emo_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "emo_i" ---
    for thisComponent in emo_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-9.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'emo_f'


# --- Prepare to start Routine "QA" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from qa_trigger
sendTriggerInBothDevices("ID"+ str(expInfo['participant'])+'_'+"fill_questionnaire_emotion")
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
QAComponents = [qa_text, key_resp, text_continue]
for thisComponent in QAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "QA" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *qa_text* updates
    
    # if qa_text is starting this frame...
    if qa_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        qa_text.frameNStart = frameN  # exact frame index
        qa_text.tStart = t  # local t and not account for scr refresh
        qa_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(qa_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'qa_text.started')
        # update status
        qa_text.status = STARTED
        qa_text.setAutoDraw(True)
    
    # if qa_text is active this frame...
    if qa_text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['up','down'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            key_resp.duration = _key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_continue* updates
    
    # if text_continue is starting this frame...
    if text_continue.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
        # keep track of start time/frame for later
        text_continue.frameNStart = frameN  # exact frame index
        text_continue.tStart = t  # local t and not account for scr refresh
        text_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_continue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_continue.started')
        # update status
        text_continue.status = STARTED
        text_continue.setAutoDraw(True)
    
    # if text_continue is active this frame...
    if text_continue.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "QA" ---
for thisComponent in QAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.duration', key_resp.duration)
thisExp.nextEntry()
# the Routine "QA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditions_file),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pause_t" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_7
    if trials_2.thisTrial['emo_t'] == 0:
        continueRoutine = False
    keyPress.keys = []
    keyPress.rt = []
    _keyPress_allKeys = []
    # keep track of which components have finished
    pause_tComponents = [breakText, keyPress]
    for thisComponent in pause_tComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pause_t" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *breakText* updates
        
        # if breakText is starting this frame...
        if breakText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            breakText.frameNStart = frameN  # exact frame index
            breakText.tStart = t  # local t and not account for scr refresh
            breakText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'breakText.started')
            # update status
            breakText.status = STARTED
            breakText.setAutoDraw(True)
        
        # if breakText is active this frame...
        if breakText.status == STARTED:
            # update params
            pass
        
        # *keyPress* updates
        waitOnFlip = False
        
        # if keyPress is starting this frame...
        if keyPress.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            keyPress.frameNStart = frameN  # exact frame index
            keyPress.tStart = t  # local t and not account for scr refresh
            keyPress.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyPress, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyPress.started')
            # update status
            keyPress.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyPress.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyPress.status == STARTED and not waitOnFlip:
            theseKeys = keyPress.getKeys(keyList=['y','n','left','right','space','return'], waitRelease=False)
            _keyPress_allKeys.extend(theseKeys)
            if len(_keyPress_allKeys):
                keyPress.keys = _keyPress_allKeys[-1].name  # just the last key pressed
                keyPress.rt = _keyPress_allKeys[-1].rt
                keyPress.duration = _keyPress_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_tComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause_t" ---
    for thisComponent in pause_tComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyPress.keys in ['', [], None]:  # No response was made
        keyPress.keys = None
    trials_2.addData('keyPress.keys',keyPress.keys)
    if keyPress.keys != None:  # we had a response
        trials_2.addData('keyPress.rt', keyPress.rt)
        trials_2.addData('keyPress.duration', keyPress.duration)
    # the Routine "pause_t" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp_emo_t" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    if trials_2.thisTrial['emo_t'] == 0:
        continueRoutine = False
    # Run 'Begin Routine' code from sendTriggerEmoT
    if trials_2.thisTrial['emo_t'] == 1:
        sendTriggerInBothDevices("expl_emo_t")
    v_text_title.setMovie('text_title.mp4')
    # keep track of which components have finished
    exp_emo_tComponents = [v_text_title]
    for thisComponent in exp_emo_tComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_emo_t" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *v_text_title* updates
        
        # if v_text_title is starting this frame...
        if v_text_title.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            v_text_title.frameNStart = frameN  # exact frame index
            v_text_title.tStart = t  # local t and not account for scr refresh
            v_text_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(v_text_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'v_text_title.started')
            # update status
            v_text_title.status = STARTED
            v_text_title.setAutoDraw(True)
            v_text_title.play()
        if v_text_title.isFinished:  # force-end the routine
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_emo_tComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_emo_t" ---
    for thisComponent in exp_emo_tComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    v_text_title.stop()
    # the Routine "exp_emo_t" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    emo_o = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(file_sequence_t),
        seed=None, name='emo_o')
    thisExp.addLoop(emo_o)  # add the loop to the experiment
    thisEmo_o = emo_o.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEmo_o.rgb)
    if thisEmo_o != None:
        for paramName in thisEmo_o:
            exec('{} = thisEmo_o[paramName]'.format(paramName))
    
    for thisEmo_o in emo_o:
        currentLoop = emo_o
        # abbreviate parameter names if possible (e.g. rgb = thisEmo_o.rgb)
        if thisEmo_o != None:
            for paramName in thisEmo_o:
                exec('{} = thisEmo_o[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "emo_t" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        if trials_2.thisTrial['emo_t'] == 0:
            continueRoutine = False
        
        
        # Run 'Begin Routine' code from sendTrigger_emo_t
        trigger_sent = False
        emotion_only.setText(text_emotion)
        # keep track of which components have finished
        emo_tComponents = [cross_Hline2, cross_Vline2, three2, two2, one2, emotion_only]
        for thisComponent in emo_tComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "emo_t" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 9.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_Hline2* updates
            
            # if cross_Hline2 is starting this frame...
            if cross_Hline2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_Hline2.frameNStart = frameN  # exact frame index
                cross_Hline2.tStart = t  # local t and not account for scr refresh
                cross_Hline2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_Hline2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_Hline2.started')
                # update status
                cross_Hline2.status = STARTED
                cross_Hline2.setAutoDraw(True)
            
            # if cross_Hline2 is active this frame...
            if cross_Hline2.status == STARTED:
                # update params
                pass
            
            # if cross_Hline2 is stopping this frame...
            if cross_Hline2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_Hline2.tStartRefresh + 1.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_Hline2.tStop = t  # not accounting for scr refresh
                    cross_Hline2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_Hline2.stopped')
                    # update status
                    cross_Hline2.status = FINISHED
                    cross_Hline2.setAutoDraw(False)
            
            # *cross_Vline2* updates
            
            # if cross_Vline2 is starting this frame...
            if cross_Vline2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_Vline2.frameNStart = frameN  # exact frame index
                cross_Vline2.tStart = t  # local t and not account for scr refresh
                cross_Vline2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_Vline2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_Vline2.started')
                # update status
                cross_Vline2.status = STARTED
                cross_Vline2.setAutoDraw(True)
            
            # if cross_Vline2 is active this frame...
            if cross_Vline2.status == STARTED:
                # update params
                pass
            
            # if cross_Vline2 is stopping this frame...
            if cross_Vline2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_Vline2.tStartRefresh + 1.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_Vline2.tStop = t  # not accounting for scr refresh
                    cross_Vline2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_Vline2.stopped')
                    # update status
                    cross_Vline2.status = FINISHED
                    cross_Vline2.setAutoDraw(False)
            
            # *three2* updates
            
            # if three2 is starting this frame...
            if three2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                three2.frameNStart = frameN  # exact frame index
                three2.tStart = t  # local t and not account for scr refresh
                three2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(three2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'three2.started')
                # update status
                three2.status = STARTED
                three2.setAutoDraw(True)
            
            # if three2 is active this frame...
            if three2.status == STARTED:
                # update params
                pass
            
            # if three2 is stopping this frame...
            if three2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > three2.tStartRefresh + 0.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    three2.tStop = t  # not accounting for scr refresh
                    three2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'three2.stopped')
                    # update status
                    three2.status = FINISHED
                    three2.setAutoDraw(False)
            
            # *two2* updates
            
            # if two2 is starting this frame...
            if two2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                two2.frameNStart = frameN  # exact frame index
                two2.tStart = t  # local t and not account for scr refresh
                two2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two2.started')
                # update status
                two2.status = STARTED
                two2.setAutoDraw(True)
            
            # if two2 is active this frame...
            if two2.status == STARTED:
                # update params
                pass
            
            # if two2 is stopping this frame...
            if two2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two2.tStartRefresh + 0.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    two2.tStop = t  # not accounting for scr refresh
                    two2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'two2.stopped')
                    # update status
                    two2.status = FINISHED
                    two2.setAutoDraw(False)
            
            # *one2* updates
            
            # if one2 is starting this frame...
            if one2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                one2.frameNStart = frameN  # exact frame index
                one2.tStart = t  # local t and not account for scr refresh
                one2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'one2.started')
                # update status
                one2.status = STARTED
                one2.setAutoDraw(True)
            
            # if one2 is active this frame...
            if one2.status == STARTED:
                # update params
                pass
            
            # if one2 is stopping this frame...
            if one2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > one2.tStartRefresh + 0.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    one2.tStop = t  # not accounting for scr refresh
                    one2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'one2.stopped')
                    # update status
                    one2.status = FINISHED
                    one2.setAutoDraw(False)
            # Run 'Each Frame' code from sendTrigger_emo_t
            if t >= 4.0 and not trigger_sent:
                sendTriggerInBothDevices("ID"+ str(expInfo['participant'])+'_'+text_emotion_t)
                trigger_sent = True
            
            # *emotion_only* updates
            
            # if emotion_only is starting this frame...
            if emotion_only.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
                # keep track of start time/frame for later
                emotion_only.frameNStart = frameN  # exact frame index
                emotion_only.tStart = t  # local t and not account for scr refresh
                emotion_only.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(emotion_only, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'emotion_only.started')
                # update status
                emotion_only.status = STARTED
                emotion_only.setAutoDraw(True)
            
            # if emotion_only is active this frame...
            if emotion_only.status == STARTED:
                # update params
                pass
            
            # if emotion_only is stopping this frame...
            if emotion_only.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > emotion_only.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    emotion_only.tStop = t  # not accounting for scr refresh
                    emotion_only.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'emotion_only.stopped')
                    # update status
                    emotion_only.status = FINISHED
                    emotion_only.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in emo_tComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "emo_t" ---
        for thisComponent in emo_tComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-9.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'emo_o'
    
    
    # --- Prepare to start Routine "pause_it" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    if trials_2.thisTrial['emo_it'] == 0:
        continueRoutine = False
    presskey.keys = []
    presskey.rt = []
    _presskey_allKeys = []
    # keep track of which components have finished
    pause_itComponents = [textbreak, presskey]
    for thisComponent in pause_itComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pause_it" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbreak* updates
        
        # if textbreak is starting this frame...
        if textbreak.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            textbreak.frameNStart = frameN  # exact frame index
            textbreak.tStart = t  # local t and not account for scr refresh
            textbreak.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbreak, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbreak.started')
            # update status
            textbreak.status = STARTED
            textbreak.setAutoDraw(True)
        
        # if textbreak is active this frame...
        if textbreak.status == STARTED:
            # update params
            pass
        
        # *presskey* updates
        waitOnFlip = False
        
        # if presskey is starting this frame...
        if presskey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            presskey.frameNStart = frameN  # exact frame index
            presskey.tStart = t  # local t and not account for scr refresh
            presskey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presskey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presskey.started')
            # update status
            presskey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(presskey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(presskey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if presskey.status == STARTED and not waitOnFlip:
            theseKeys = presskey.getKeys(keyList=['y','n','left','right','space','return'], waitRelease=False)
            _presskey_allKeys.extend(theseKeys)
            if len(_presskey_allKeys):
                presskey.keys = _presskey_allKeys[-1].name  # just the last key pressed
                presskey.rt = _presskey_allKeys[-1].rt
                presskey.duration = _presskey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_itComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause_it" ---
    for thisComponent in pause_itComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if presskey.keys in ['', [], None]:  # No response was made
        presskey.keys = None
    trials_2.addData('presskey.keys',presskey.keys)
    if presskey.keys != None:  # we had a response
        trials_2.addData('presskey.rt', presskey.rt)
        trials_2.addData('presskey.duration', presskey.duration)
    # the Routine "pause_it" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp_emo_it" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    if trials_2.thisTrial['emo_it'] == 0:
        continueRoutine = False
    # Run 'Begin Routine' code from sendTriggerEmoIT
    if trials_2.thisTrial['emo_it'] == 1:
        sendTriggerInBothDevices("expl_emo_it")
    v__text_it.setMovie('text_emotion_title.mp4')
    # keep track of which components have finished
    exp_emo_itComponents = [v__text_it]
    for thisComponent in exp_emo_itComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_emo_it" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *v__text_it* updates
        
        # if v__text_it is starting this frame...
        if v__text_it.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            v__text_it.frameNStart = frameN  # exact frame index
            v__text_it.tStart = t  # local t and not account for scr refresh
            v__text_it.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(v__text_it, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'v__text_it.started')
            # update status
            v__text_it.status = STARTED
            v__text_it.setAutoDraw(True)
            v__text_it.play()
        if v__text_it.isFinished:  # force-end the routine
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_emo_itComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_emo_it" ---
    for thisComponent in exp_emo_itComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    v__text_it.stop()
    # the Routine "exp_emo_it" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    emo_e = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(file_sequence_it),
        seed=None, name='emo_e')
    thisExp.addLoop(emo_e)  # add the loop to the experiment
    thisEmo_e = emo_e.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEmo_e.rgb)
    if thisEmo_e != None:
        for paramName in thisEmo_e:
            exec('{} = thisEmo_e[paramName]'.format(paramName))
    
    for thisEmo_e in emo_e:
        currentLoop = emo_e
        # abbreviate parameter names if possible (e.g. rgb = thisEmo_e.rgb)
        if thisEmo_e != None:
            for paramName in thisEmo_e:
                exec('{} = thisEmo_e[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "emo_it" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        if trials_2.thisTrial['emo_it'] == 0:
            continueRoutine = False
        
        
        image_emotion_2.setImage(image_emotion_cropped)
        # Run 'Begin Routine' code from sendTrigger_emo_it
        trigger_sent = False
        title_emotion.setText(text_emotion)
        # keep track of which components have finished
        emo_itComponents = [cross_Hline3, cross_Vline3, three3, two3, one, image_emotion_2, title_emotion]
        for thisComponent in emo_itComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "emo_it" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 9.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_Hline3* updates
            
            # if cross_Hline3 is starting this frame...
            if cross_Hline3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_Hline3.frameNStart = frameN  # exact frame index
                cross_Hline3.tStart = t  # local t and not account for scr refresh
                cross_Hline3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_Hline3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_Hline3.started')
                # update status
                cross_Hline3.status = STARTED
                cross_Hline3.setAutoDraw(True)
            
            # if cross_Hline3 is active this frame...
            if cross_Hline3.status == STARTED:
                # update params
                pass
            
            # if cross_Hline3 is stopping this frame...
            if cross_Hline3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_Hline3.tStartRefresh + 1.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_Hline3.tStop = t  # not accounting for scr refresh
                    cross_Hline3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_Hline3.stopped')
                    # update status
                    cross_Hline3.status = FINISHED
                    cross_Hline3.setAutoDraw(False)
            
            # *cross_Vline3* updates
            
            # if cross_Vline3 is starting this frame...
            if cross_Vline3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_Vline3.frameNStart = frameN  # exact frame index
                cross_Vline3.tStart = t  # local t and not account for scr refresh
                cross_Vline3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_Vline3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_Vline3.started')
                # update status
                cross_Vline3.status = STARTED
                cross_Vline3.setAutoDraw(True)
            
            # if cross_Vline3 is active this frame...
            if cross_Vline3.status == STARTED:
                # update params
                pass
            
            # if cross_Vline3 is stopping this frame...
            if cross_Vline3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_Vline3.tStartRefresh + 1.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_Vline3.tStop = t  # not accounting for scr refresh
                    cross_Vline3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_Vline3.stopped')
                    # update status
                    cross_Vline3.status = FINISHED
                    cross_Vline3.setAutoDraw(False)
            
            # *three3* updates
            
            # if three3 is starting this frame...
            if three3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                three3.frameNStart = frameN  # exact frame index
                three3.tStart = t  # local t and not account for scr refresh
                three3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(three3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'three3.started')
                # update status
                three3.status = STARTED
                three3.setAutoDraw(True)
            
            # if three3 is active this frame...
            if three3.status == STARTED:
                # update params
                pass
            
            # if three3 is stopping this frame...
            if three3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > three3.tStartRefresh + 0.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    three3.tStop = t  # not accounting for scr refresh
                    three3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'three3.stopped')
                    # update status
                    three3.status = FINISHED
                    three3.setAutoDraw(False)
            
            # *two3* updates
            
            # if two3 is starting this frame...
            if two3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                two3.frameNStart = frameN  # exact frame index
                two3.tStart = t  # local t and not account for scr refresh
                two3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two3.started')
                # update status
                two3.status = STARTED
                two3.setAutoDraw(True)
            
            # if two3 is active this frame...
            if two3.status == STARTED:
                # update params
                pass
            
            # if two3 is stopping this frame...
            if two3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two3.tStartRefresh + 0.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    two3.tStop = t  # not accounting for scr refresh
                    two3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'two3.stopped')
                    # update status
                    two3.status = FINISHED
                    two3.setAutoDraw(False)
            
            # *one* updates
            
            # if one is starting this frame...
            if one.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                one.frameNStart = frameN  # exact frame index
                one.tStart = t  # local t and not account for scr refresh
                one.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'one.started')
                # update status
                one.status = STARTED
                one.setAutoDraw(True)
            
            # if one is active this frame...
            if one.status == STARTED:
                # update params
                pass
            
            # if one is stopping this frame...
            if one.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > one.tStartRefresh + 0.9833-frameTolerance:
                    # keep track of stop time/frame for later
                    one.tStop = t  # not accounting for scr refresh
                    one.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'one.stopped')
                    # update status
                    one.status = FINISHED
                    one.setAutoDraw(False)
            
            # *image_emotion_2* updates
            
            # if image_emotion_2 is starting this frame...
            if image_emotion_2.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
                # keep track of start time/frame for later
                image_emotion_2.frameNStart = frameN  # exact frame index
                image_emotion_2.tStart = t  # local t and not account for scr refresh
                image_emotion_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_emotion_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_emotion_2.started')
                # update status
                image_emotion_2.status = STARTED
                image_emotion_2.setAutoDraw(True)
            
            # if image_emotion_2 is active this frame...
            if image_emotion_2.status == STARTED:
                # update params
                pass
            
            # if image_emotion_2 is stopping this frame...
            if image_emotion_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_emotion_2.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_emotion_2.tStop = t  # not accounting for scr refresh
                    image_emotion_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_emotion_2.stopped')
                    # update status
                    image_emotion_2.status = FINISHED
                    image_emotion_2.setAutoDraw(False)
            # Run 'Each Frame' code from sendTrigger_emo_it
            if t >= 4.0 and not trigger_sent:
                sendTriggerInBothDevices("ID"+ str(expInfo['participant'])+'_'+text_emotion_it)
                trigger_sent = True
            
            # *title_emotion* updates
            
            # if title_emotion is starting this frame...
            if title_emotion.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                title_emotion.frameNStart = frameN  # exact frame index
                title_emotion.tStart = t  # local t and not account for scr refresh
                title_emotion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(title_emotion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'title_emotion.started')
                # update status
                title_emotion.status = STARTED
                title_emotion.setAutoDraw(True)
            
            # if title_emotion is active this frame...
            if title_emotion.status == STARTED:
                # update params
                pass
            
            # if title_emotion is stopping this frame...
            if title_emotion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > title_emotion.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    title_emotion.tStop = t  # not accounting for scr refresh
                    title_emotion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'title_emotion.stopped')
                    # update status
                    title_emotion.status = FINISHED
                    title_emotion.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in emo_itComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "emo_it" ---
        for thisComponent in emo_itComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-9.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'emo_e'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "end" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thank_you]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    
    # if thank_you is starting this frame...
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you.started')
        # update status
        thank_you.status = STARTED
        thank_you.setAutoDraw(True)
    
    # if thank_you is active this frame...
    if thank_you.status == STARTED:
        # update params
        pass
    
    # if thank_you is stopping this frame...
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thank_you.stopped')
            # update status
            thank_you.status = FINISHED
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from end_trigger
sendTriggerInBothDevices("ID"+ str(expInfo['participant'])+'_experiment_end')
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
