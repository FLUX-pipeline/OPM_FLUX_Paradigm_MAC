from psychopy import core

def screen_setup(cfgScreen):

    win = cfgScreen['window']

    win.blendMode = 'avg'
    cfgScreen['ifi'] = win.getMsPerFrame()[0] / 1000.0
    cfgScreen['waitFrm'] = 1

    core.rush(True)

    cfgScreen['window'].textSize = cfgScreen['fntSize']

    cfgScreen['window'].mouseVisible = False

    return cfgScreen
