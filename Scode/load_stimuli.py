import os
import re
import numpy as np
from psychopy import visual

def load_stimuli(cfgFile, cfgExp, cfgStim, cfgTrigger,cfgScreen):
    cfgStim['cueRndIdx']=cfgExp['cueRndIdx']
    win=cfgScreen['window']
    fileDirStim = [f for f in os.listdir(cfgFile['stim']) if f.endswith('.bmp')]
    fileDirCue = [f for f in os.listdir(cfgFile['cue']) if f.endswith('.jpg')]
    # os.listdir() order is filesystem-dependent, not guaranteed to match the
    # leading number in the filename (e.g. "1_right.jpg", "2_left.jpg"), which
    # cueRndIdx - 1 below relies on as an index. Sort explicitly to be safe.
    fileDirCue = sorted(fileDirCue, key=lambda f: int(re.search(r'^\d+', f).group()))

    idx = sorted(range(len(fileDirStim)), key=lambda i: int(re.search(r'(?<=cube3D)\d+', fileDirStim[i]).group()))
    cfgStim['fNameStimSortd'] = [fileDirStim[i] for i in idx]

    cfgStim['visStimL'] = [None] * len(range(0, len(cfgStim['fNameStimSortd']), cfgStim['stimRotSpeed']))
    cfgStim['visStimR'] = [None] * len(range(0, len(cfgStim['fNameStimSortd']), cfgStim['stimRotSpeed']))
    
    for spd in range(0, len(cfgStim['fNameStimSortd']), cfgStim['stimRotSpeed']):
        index = spd // cfgStim['stimRotSpeed']
        if index < len(cfgStim['visStimL']):
            cfgStim['visStimL'][index] = visual.ImageStim(win, size=cfgStim['gratingSize'],image=os.path.join(cfgFile['stim'], cfgStim['fNameStimSortd'][spd]),pos=cfgStim['gratingPosL'],units='deg')
            cfgStim['visStimR'][index] = visual.ImageStim(win,size=cfgStim['gratingSize'], image=os.path.join(cfgFile['stim'], cfgStim['fNameStimSortd'][spd]),pos=cfgStim['gratingPosR'],units='deg')

    cfgStim['visStimL'] = [stim for stim in cfgStim['visStimL'] if stim is not None]
    cfgStim['visStimR'] = [stim for stim in cfgStim['visStimR'] if stim is not None]

    cfgStim['cueStim'] = [None] * cfgExp['numStim']

    for stim in range(cfgExp['numStim']):
        cfgStim['cueStim'][stim] = visual.ImageStim(win,size=cfgStim['cueSize'], image=os.path.join(cfgFile['cue'], fileDirCue[cfgStim['cueRndIdx'][stim] - 1]),pos=cfgStim['cuePos'],units='deg')
        
    cfgExp['cuesDir'] = [None] * cfgExp['numStim']
    cfgTrigger['cuesDir'] = [[None, None] for _ in range(cfgExp['numStim'])]
    cfgTrigger['targetDir'] = [[None, None] for _ in range(cfgExp['numStim'])]

    right_indices = np.where(cfgStim['cueRndIdx'] == 1)[0]
    left_indices = np.where(cfgStim['cueRndIdx'] == 2)[0]

    for idx in right_indices:
        cfgExp['cuesDir'][idx] = 'Right'
        cfgTrigger['cuesDir'][idx][0] = cfgTrigger['cueRight']
        cfgTrigger['cuesDir'][idx][1] = 'Right'
        cfgTrigger['targetDir'][idx][0] = cfgTrigger['targetRight']
        cfgTrigger['targetDir'][idx][1] = 'Right'

    for idx in left_indices:
        cfgExp['cuesDir'][idx] = 'Left'
        cfgTrigger['cuesDir'][idx][0] = cfgTrigger['cueLeft']
        cfgTrigger['cuesDir'][idx][1] = 'Left'
        cfgTrigger['targetDir'][idx][0] = cfgTrigger['targetLeft']
        cfgTrigger['targetDir'][idx][1] = 'Left'

    return cfgStim, cfgExp, cfgTrigger
