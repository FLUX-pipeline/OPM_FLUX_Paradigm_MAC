import numpy as np

def timing_config(cfgExp):
    
    n = cfgExp['numStim']

    cfgExp['ITIDur'] = 1000 + (1500 - 1000) * np.random.rand(n)   # inter-trial interval (ms), jittered 1000-1500
    cfgExp['cueDur'] = 200                                        # cue duration (ms)
    cfgExp['ISIDur'] = 1000                                       # cue-to-stimulus interval (ms)
    cfgExp['stimDur'] = 100 + (1900 - 100) * np.random.rand(n)    # grating duration before target (ms), jittered 100-1900
    cfgExp['targetDur'] = 200                                      # target letter duration (ms)
    cfgExp['respTimOut'] = 2                                      # response timeout (s)
    cfgExp['tdur'] = 2500                                         # total trial duration (ms)
    cfgExp['over'] = cfgExp['tdur'] - (cfgExp['stimDur'] + cfgExp['targetDur'])

    return cfgExp
