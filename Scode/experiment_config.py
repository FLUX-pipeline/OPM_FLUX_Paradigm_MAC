import numpy as np
from generate_trial_sequence import generate_trial_sequence

def experiment_config(cfgExp):

    cfgExp['numBlock'] = 1
    cfgExp['numTrial'] = 20
    cfgExp['numStim'] = cfgExp['numTrial'] * cfgExp['numBlock']

    cfgExp = generate_trial_sequence(cfgExp)

    cfgOutput = {
        'presd': np.zeros(cfgExp['numStim'], dtype=int),
        'keyName': np.zeros(cfgExp['numStim'], dtype=int),
        'blkStrtTmPnt': np.zeros(cfgExp['numBlock'], dtype=int),
        'trlStrtTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'cueOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'stmOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'targetOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'respStartTime': np.zeros(cfgExp['numStim'], dtype=int),
        'catchOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'respTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'respTmKbQueue': np.zeros(cfgExp['numStim'], dtype=int),
        'RT_KbQueue': np.zeros(cfgExp['numStim'], dtype=int),
        'RT_trig': np.zeros(cfgExp['numStim'], dtype=int),
        'pressedButton': [''] * cfgExp['numStim'],
        'correct': np.zeros(cfgExp['numStim'], dtype=int),
        'abrtTmPoint':[],
        'blkEnd': np.zeros(cfgExp['numStim'], dtype=int),
        'endTmPnt':(),
        'RestON':(),
        'RestOFF':()
    }

    return cfgExp, cfgOutput
