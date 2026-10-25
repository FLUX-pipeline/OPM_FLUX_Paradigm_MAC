from psychopy import prefs

def psychopy_prefs():
    prefs.general['skipSync'] = True
    prefs.hardware['audioLib'] = ['pyo']
    prefs.general['winType'] = 'pyglet'
