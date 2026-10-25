from psychopy import visual, core, event
from datapixx import drawPixelModeTrigger, Trigger2RGB, read_button_press

def show_instructions(cfgScreen, cfgTxt, cfgExp, presentingStr, cfgStim,cfgTrigger,cfgOutput):
    win = cfgScreen['window']
    win.flip()
    fix_dot_big = visual.Circle(win, radius=cfgStim['fixBigSize'], fillColor=cfgStim['fixBigColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')
    fix_dot_small = visual.Circle(win, radius=cfgStim['fixSmallSize'], fillColor=cfgStim['fixSmallColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')
    marker_R = visual.Circle(win, radius=cfgStim['markerRadius'], fillColor=cfgStim['markerColor'], lineColor=cfgStim['markerColor'], colorSpace='rgb', pos=cfgStim['destVisStimR'], units='deg')
    marker_L = visual.Circle(win, radius=cfgStim['markerRadius'], fillColor=cfgStim['markerColor'], lineColor=cfgStim['markerColor'], colorSpace='rgb', pos=cfgStim['destVisStimL'], units='deg')
    letter_T = visual.TextStim(win, text='T', color=cfgStim['letterColor'], height=cfgStim['letterSize'], bold=cfgStim['letterBold'], pos=cfgStim['destVisStimR'], units='deg')
    letter_L = visual.TextStim(win, text='L', color=cfgStim['letterColor'], height=cfgStim['letterSize'], bold=cfgStim['letterBold'], pos=cfgStim['destVisStimL'], units='deg')
    instrTxt0 = cfgTxt['instrTxt'][4]
    textStim0 = visual.TextStim(win, text=instrTxt0, color=cfgScreen['white'], pos=(0, 0),units='deg')
    textStim0.draw()
    win.flip()

    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)

    fix_dot_big.draw()
    fix_dot_small.draw()
    drawPixelModeTrigger(win, Trigger2RGB(cfgTrigger['reston']))
    win.flip()
    cfgOutput['RestON'] = core.getTime()
    core.wait(5)
    drawPixelModeTrigger(win, Trigger2RGB(cfgTrigger['restoff']))
    win.flip()
    cfgOutput['RestOFF'] = core.getTime()

    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(0.01)

    instrTxt1 = cfgTxt['instrTxt'][0]
    textStim1 = visual.TextStim(win, text=instrTxt1, color=cfgScreen['white'], pos=(0, 0),units='deg')
    textStim1.draw()
    win.flip()

    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)

    instrTxt2 = cfgTxt['instrTxt'][1]
    textStim2 = visual.TextStim(win, text=instrTxt2, color=cfgScreen['white'], pos=(0, 0),units='deg')
    textStim2.draw()
    win.flip()

    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)

    instrTxt3 = cfgTxt['instrTxt'][2]
    textStim3 = visual.TextStim(win, text=instrTxt3, color=cfgScreen['white'], pos=(0, 0),units='deg')
    textStim3.draw()
    win.flip()

    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)

    instrTxt4 = cfgTxt['instrTxt'][3]
    textStim4 = visual.TextStim(win, text=instrTxt4, color=cfgScreen['white'], pos=(0, 0),units='deg')
    textStim4.draw()
    win.flip(cfgScreen['vbl'] + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])

    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)

    image1 = presentingStr['visStimR'][0][1]
    image2 = presentingStr['visStimL'][1][1]
    cueRnd = list(cfgStim['cueRndIdx'])
    cue_right = presentingStr['cueStim'][cueRnd.index(1)]   # cue pointing right
    cue_left = presentingStr['cueStim'][cueRnd.index(2)]    # cue pointing left

    # --- Example 1: a T on the cued (right) grating ---
    fix_dot_big.draw()
    fix_dot_small.draw()
    win.flip()
    core.wait(1)

    cue_right.draw()
    win.flip()
    core.wait(1)

    image1.draw()
    image2.draw()
    fix_dot_big.draw()
    fix_dot_small.draw()
    marker_R.draw()
    marker_L.draw()
    cue_right.draw()
    win.flip()
    core.wait(1)

    image1.draw()
    image2.draw()
    fix_dot_big.draw()
    fix_dot_small.draw()
    marker_R.draw()
    marker_L.draw()
    letter_T.draw()
    cue_right.draw()
    win.flip()
    core.wait(5)

    win.flip()
    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)

    # --- Example 2: an L on the cued (left) grating ---
    cue_left.draw()
    win.flip()
    core.wait(1)

    image1.draw()
    image2.draw()
    fix_dot_big.draw()
    fix_dot_small.draw()
    marker_R.draw()
    marker_L.draw()
    cue_left.draw()
    win.flip()
    core.wait(1)

    image1.draw()
    image2.draw()
    fix_dot_big.draw()
    fix_dot_small.draw()
    marker_R.draw()
    marker_L.draw()
    letter_L.draw()
    cue_left.draw()
    win.flip()
    core.wait(5)

    win.flip()
    event.waitKeys(keyList=cfgExp['kbresp'])
    core.wait(1)
