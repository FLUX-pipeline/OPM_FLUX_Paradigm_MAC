import numpy as np

def prepare_stimuli(cfgScreen, cfgStim, cfgExp):
    presentingStr = {
        'visStimR': [],
        'visStimL': [],
        'cueStim': []
    }

    # Frames each trial must be able to draw (longest stimulus + safety buffer).
    max_stim_frames = max(cfgExp['stimFrm']) + 500

    # Repeat the rotation-speed-sampled grating sequence enough times to always
    # cover max_stim_frames. Computing num_repeats from the ACTUAL base length
    # (not a hardcoded 100) means a higher stimRotSpeed -> fewer base frames ->
    # simply more repeats, so the gratings never run out of frames mid-trial.
    base_len = len(cfgStim['visStimL'])
    num_repeats = int(np.ceil(max_stim_frames / max(base_len, 1)))
    cfgStim['visStimMatL'] = cfgStim['visStimL'] * num_repeats
    cfgStim['visStimMatR'] = cfgStim['visStimR'] * num_repeats

    cfgStim['visStimL'] = []
    cfgStim['visStimR'] = []

    for _ in range(len(cfgExp['stimFrm'])):
        cfgStim['visStimR'].append(cfgStim['visStimMatR'][:max_stim_frames])
        cfgStim['visStimL'].append(cfgStim['visStimMatL'][:max_stim_frames])

    presentingStr['visStimR'] = cfgStim['visStimR']
    presentingStr['visStimL'] = cfgStim['visStimL']
    presentingStr['cueStim'] = cfgStim['cueStim']

    return presentingStr
