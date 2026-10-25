from psychopy import visual, core
from datapixx import drawPixelModeTrigger, Trigger2RGB
from abort import check_abort

def display_cue(cfgScreen, presentingStr, nstim, cfgStim, cfgExp, cfgTrigger, cfgOutput):

    win=cfgScreen['window']
    vbl =  cfgScreen['vbl'] 
    cue_texture = presentingStr['cueStim'][nstim]
    # Hard-coded cue-onset trigger codes (1 = Right, 2 = Left); see trigger_config.py.
    cue_trigger = 256 if cfgStim['cueRndIdx'][nstim] == 1 else 4096
    fix_dot_big = visual.Circle(win, radius=cfgStim['fixBigSize'], fillColor=cfgStim['fixBigColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')
    fix_dot_small = visual.Circle(win, radius=cfgStim['fixSmallSize'], fillColor=cfgStim['fixSmallColor'], colorSpace='rgb', pos=cfgStim['fixPos'])
    for frm in range(cfgExp['cueFrm']):
        check_abort()
        cue_texture.draw()
        fix_dot_big.draw()
        fix_dot_small.draw()
        if frm == 0 or frm==1 or frm==2:
            drawPixelModeTrigger(win, Trigger2RGB(cue_trigger))
        vbl = win.flip()
        if frm == 0:
            cfgOutput['cueOnTmPnt'][nstim] = core.getTime()

    return cfgOutput
