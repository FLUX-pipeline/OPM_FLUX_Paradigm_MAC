from psychopy import visual
from abort import check_abort

def display_fixation_dot(cfgScreen, cfgExp, cfgStim, nstim, ITI, cfgOutput):

    win=cfgScreen['window']

    vbl =  cfgScreen['vbl']
    fix_dot_big = visual.Circle(win, radius=cfgStim['fixBigSize'], fillColor=cfgStim['fixBigColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')
    fix_dot_small = visual.Circle(win, radius=cfgStim['fixSmallSize'], fillColor=cfgStim['fixSmallColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')
    if ITI:   
        for _ in range(int(cfgExp['ITIFrm'][nstim])):
            check_abort()
            fix_dot_big.draw()
            fix_dot_small.draw()
            win.flip()
    
    else:
        for _ in range(int(cfgExp['ISIFrm'])):
            check_abort()
            fix_dot_big.draw()
            fix_dot_small.draw()
            win.flip()

    return cfgOutput
