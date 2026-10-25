def stim_config():
 
    cfgStim = {
        # --- Gratings ---
        'gratingSize': (6.5, 6.5),
        'gratingPosR': [6.9, -3],
        'gratingPosL': [-6.9, -3],
        'stimRotSpeed': 3,

        # --- Cue (arrow) ---
        'cueSize': 2,
        'cuePos': (0, -2.5),

        # --- Central fixation dot (big white + small black) ---
        'fixBigSize': 0.5,
        'fixBigColor': 'white',
        'fixSmallSize': 0.3,
        'fixSmallColor': 'black',
        'fixPos': [0, -0.5],
        'fixFlashColor': 'white',

        # --- Circle at the centre of each grating ---
        'markerRadius': 0.5,
        'markerColor': 'black',

        # --- Target letter (T/L) ---
        'letterSize': 0.8,
        'letterColor': 'grey',
        'letterBold': True,    # bold = thicker strokes
    }

    # The grating-centre markers and the target letter sit at the grating centres.
    cfgStim['destVisStimR'] = cfgStim['gratingPosR']
    cfgStim['destVisStimL'] = cfgStim['gratingPosL']

    return cfgStim
