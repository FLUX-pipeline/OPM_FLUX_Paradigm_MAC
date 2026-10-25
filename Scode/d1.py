from psychopy import visual, core
from pixel_trigger import drawPixelModeTrigger, Trigger2RGB
from pypixxlib._libdpx import DPxOpen, DPxUpdateRegCache, DPxStopDinLog
from pypixxlib._libdpx import DPxSetDinLog, DPxStartDinLog, DPxGetDinStatus, DPxEnableDinDebounce

def display_visual_stim(presentingStr, nstim, cfgScreen, cfgExp, cfgOutput, cfgStim, cfgTrigger, cfgEyelink,cfgTxt,cfgFile):

    destvecRL=[cfgStim['destVisStimR'],cfgStim['destVisStimL']]
    
    win=cfgScreen['window']
    vbl =  cfgScreen['vbl']
    #DPxOpen()
   
    # Define button codes (as per your second script)
    #buttonCodes = {64768: 'blue', 64576: 'yellow', 64544: 'red', 64640: 'green', 65024: 'white', 64512: 'button release'}
   
    # Set up digital input logging on the device
    #logStatus = DPxSetDinLog(0, 1000)
    #DPxEnableDinDebounce()
    #DPxStartDinLog()
    #DPxUpdateRegCache()
    #startTime = DPxGetTime()
    #startTime = core.getTime()
   
    win = cfgScreen['window']

    # Initialize the fixation dot stimulus
    fix_dot_big = visual.Circle(win, radius=cfgScreen['fixDotSizeBig'], fillColor='white', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0],units='deg')
    fix_dot_small = visual.Circle(win, radius=cfgScreen['fixDotSizeSmall'], fillColor='black', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0],units='deg')
    fix_dot_flash_stim = visual.Circle(win, radius=cfgScreen['fixDotSizeSmall'], fillColor='white', colorSpace='rgb',units='deg')

    if cfgExp['corrResp'][nstim]:
        for frm in range(cfgExp['stimFrm'][nstim]):
            # Draw the visual stimuli
            presentingStr['visStimR'][nstim][frm].draw()
            presentingStr['visStimL'][nstim][frm].draw()
            fix_dot_big.draw()
            fix_dot_small.draw()
            if frm == 0 or frm == 1:
                #cfgOutput['stmOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['stimOnset'], cfgEyelink, 'stimulus onset')
                drawPixelModeTrigger(win, Trigger2RGB(cfgTrigger['stimOnset']))
            win.flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
            #win.flip()
            if frm == 0:
                cfgOutput['stmOnTmPnt'][nstim] = core.getTime()

        for frmDot in range(cfgExp['stimFrm'][nstim], cfgExp['stimFrm'][nstim] + cfgExp['dotFrm']):
            # Draw the visual stimuli
            presentingStr['visStimR'][nstim][frmDot].draw()
            presentingStr['visStimL'][nstim][frmDot].draw()
            fix_dot_big.draw()
            fix_dot_small.draw()
            if cfgStim['cueRndIdx'][nstim] == 1:  # Assuming index 0 means left
                fix_dot_flash_stim.pos = destvecRL[0]
            else:  # Assuming index 1 means right
                fix_dot_flash_stim.pos = destvecRL[1]
            fix_dot_flash_stim.draw()
            if frmDot == cfgExp['stimFrm'][nstim]:
                #cfgOutput['dotOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, int(cfgTrigger['dotDir'][nstim][0]), cfgEyelink, f'dot onset to {cfgTrigger["dotDir"][nstim][1]}')
                drawPixelModeTrigger(win, Trigger2RGB(int(cfgTrigger['dotDir'][nstim][0])))
            win.flip()
            if frmDot == cfgExp['stimFrm'][nstim]:
                cfgOutput['dotOnTmPnt'][nstim] = core.getTime()

        DPxOpen()
        logStatus = DPxSetDinLog(0, 1000)
        DPxEnableDinDebounce()
        DPxStartDinLog()
        DPxUpdateRegCache()
        cfgOutput['respStartTime'][nstim] = core.getTime()
        for frame_count in range((cfgExp['stimFrm'][nstim] + cfgExp['dotFrm']), max(int(cfgExp['overFrm'][nstim]), int(cfgExp['tFrame']))):
            if frame_count < cfgExp['overFrm'][nstim]:
                presentingStr['visStimR'][nstim][frame_count].draw()
                presentingStr['visStimL'][nstim][frame_count].draw()
                fix_dot_big.draw()
                fix_dot_small.draw()
                cfgScreen['window'].flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
                #cfgScreen['window'].flip()
            else:
                fix_dot_big.draw()
                fix_dot_small.draw()
                cfgScreen['window'].flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
                #cfgScreen['window'].flip()
            DPxUpdateRegCache()
            DPxGetDinStatus(logStatus)
            if logStatus['newLogFrames'] > 0:
                cfgOutput['respTmPnt'][nstim] = core.getTime()
                cfgOutput['respTmKbQueue'][nstim] = cfgOutput['respTmPnt'][nstim]
                cfgOutput['presd'][nstim] = 2
                cfgOutput['RT_KbQueue'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['respStartTime'][nstim]
                if cfgExp['corrResp'][nstim]:
                    cfgOutput['RT_trig'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['dotOnTmPnt'][nstim]
                print('Response Received')
                break
        DPxStopDinLog()

    else:
        # Catch trial
        frame_count = 0

        for frm in range(cfgExp['stimFrm'][nstim] + cfgExp['dotFrm']):
            # Draw the visual stimuli
            presentingStr['visStimR'][nstim][frm].draw()
            presentingStr['visStimL'][nstim][frm].draw()
            fix_dot_big.draw()
            fix_dot_small.draw()
            if frm == 0:
                #cfgOutput['catchOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['catchOnset'], cfgEyelink, 'catch onset')
                drawPixelModeTrigger(win, Trigger2RGB(cfgTrigger['catchOnset']))
            cfgScreen['window'].flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
            #cfgScreen['window'].flip()
            if frm == 0:
                cfgOutput['catchOnTmPnt'][nstim] = core.getTime()
        DPxOpen()
        logStatus = DPxSetDinLog(0, 1000)
        DPxEnableDinDebounce()
        DPxStartDinLog()
        DPxUpdateRegCache()
        cfgOutput['respStartTime'][nstim] = core.getTime()
        for frame_count in range((cfgExp['stimFrm'][nstim] + cfgExp['dotFrm']), max(int(cfgExp['overFrm'][nstim]), int(cfgExp['tFrame']))):
            if frame_count < cfgExp['overFrm'][nstim]:
                presentingStr['visStimR'][nstim][frame_count].draw()
                presentingStr['visStimL'][nstim][frame_count].draw()
                fix_dot_big.draw()
                fix_dot_small.draw()
                win.flip()
            else:
                fix_dot_big.draw()
                fix_dot_small.draw()
                cfgScreen['window'].flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
                #cfgScreen['window'].flip()
            DPxUpdateRegCache()
            DPxGetDinStatus(logStatus)
            if logStatus['newLogFrames'] > 0:
                cfgOutput['respTmPnt'][nstim] = core.getTime()
                cfgOutput['respTmKbQueue'][nstim] = cfgOutput['respTmPnt'][nstim]
                cfgOutput['presd'][nstim] = 2
                cfgOutput['RT_KbQueue'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['respStartTime'][nstim]
                print('Response Received')
                break
        DPxStopDinLog()
        

    return cfgOutput


