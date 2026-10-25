from psychopy import event

class AbortExperiment(Exception):
    pass

def check_abort(keyList=('x',)):
    if event.getKeys(keyList=list(keyList)):
        raise AbortExperiment()
