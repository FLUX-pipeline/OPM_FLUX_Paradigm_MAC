import numpy as np

def duration_to_frames(cfgExp, cfgScreen):

    cfgExp['ITIFrm'] = (np.round(cfgExp['ITIDur'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['cueFrm'] = (np.round(cfgExp['cueDur'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['ISIFrm'] = (np.round(cfgExp['ISIDur'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['stimFrm'] = (np.round(cfgExp['stimDur'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['targetFrm'] = (np.round(cfgExp['targetDur'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['respTimOutFrm'] = (np.round(cfgExp['respTimOut'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['overFrm'] = (np.round(cfgExp['over'] * 0.001 / cfgScreen['ifi'])).astype(int)
    cfgExp['tFrame'] = (np.round(cfgExp['tdur'] * 0.001 / cfgScreen['ifi'])).astype(int)

    return cfgExp
