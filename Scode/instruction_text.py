def instruction_text():
    cfgTxt = {}

    cfgTxt['quitTxt'] = 'Are you sure you want to abort the experiment? y/n'
    cfgTxt['startTxt'] = 'Are you ready to start? \n Tell the experimenter to start the task when you are ready'
    cfgTxt['breakTxt'] = 'Take a break \n tell the experimenter to continue when you are ready'
    cfgTxt['endTxt'] = 'Thank you :-)'
    
    instr0='Please sit comfortably and try to relax. \n A dot will appear on the screen shortly and will remain there for 3 minutes.\n Try to keep your gaze on the dot without moving your eyes or body, and simply let your mind rest. \n There is no task to perform. Just stay as still as possible until the dot disappears'
    instr1 = 'First a dot appears at the centre of the screen. \n\n Please look at that dot for the duration of the task.'
    instr2 = 'Then an arrow will appear below the fixation point. \n\n The arrow shows the direction to which you should attend.'
    instr3 = 'Then you will see two circular moving gratings \n on the two sides of the screen. \n\n Please attend to the grating that was cued by the arrow \n without moving your eyes.'
    instr4 = 'A letter (T or L) will briefly appear at the centre of the attended grating. \n\n Press the Yellow button for T and the Green button for L, as quickly and accurately as you can.\n\n The next trial will be an example'
    
    cfgTxt['instrTxt'] = [instr1, instr2, instr3, instr4, instr0]

    return cfgTxt
