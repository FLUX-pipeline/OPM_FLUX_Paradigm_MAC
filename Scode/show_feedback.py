from psychopy import visual, core
import numpy as np

def show_feedback(cfgOutput, cfgExp, nstim, blk, cfgScreen, cfgTrigger):
    
    start_idx = (blk) * cfgExp['numTrial']
    end_idx = ((blk+1) * cfgExp['numTrial'])
    FB = cfgOutput['presd'][start_idx:end_idx]-cfgExp['corrResp'][start_idx:end_idx]

    TP = np.sum(FB == 1)
    TN = np.sum(FB == 0)
    FP = np.sum(FB == 2)
    FN = np.sum(FB == -1)

    correct_percentage = ((TP+TN)/(TP+TN+FP+FN)) * 100
    feedback_text = f"Correct = {correct_percentage:.2f}%"

    cfgScreen['window'].flip()
    cfgOutput['blkEnd'][nstim] = core.getTime()

    feedback_stim = visual.TextStim(cfgScreen['window'], text=feedback_text, color=cfgScreen['white'], pos=(0, 0),units='deg')
    feedback_stim.draw()
    cfgScreen['window'].flip()
    
    core.wait(3)

    return cfgOutput
