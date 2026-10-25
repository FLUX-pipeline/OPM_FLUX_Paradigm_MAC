from psychopy import core
from pypixxlib import _libdpx as dp

dp.DPxOpen()
isReady = dp.DPxIsReady
if not(isReady):
    print('Warning! DPxOpen call failed, check connection to hardware')
    

#Create our digital output waveforms. Each button press (rising edge) triggers a 
#1 msec trig on the corresponding dout pin, followed by 2 msec on low. 
#We'll use the dual /MRI as our example. DinChannels will depend on your button box type, you can use the PyPixx Digital I/O demo to verify your channel mappings.
#Note that if PixelModeGB is enabled it will control dout 8-23, dout waveforms which try to alter these will have no effect

#Din0 - Red
redWaveform = [4, 0, 0]

#Din1 - Yellow
yellowWaveform = [2, 0, 0]

#Din2 - Green
greenWaveform = [4, 0, 0]

#Din3 - Blue
blueWaveform = [16, 0, 0]

#Let's write the waveforms into the DPx memory. The address is set by 0 + 4096*channel_of_desired_digital_in_trigger
redAdd = 0+4096*0
yellowAdd = 0+4096*1
greenAdd = 0+4096*2
blueAdd = 0+4096*3

#write schedules into ram
dp.DPxWriteRam(redAdd, redWaveform)
dp.DPxWriteRam(yellowAdd, yellowWaveform)
dp.DPxWriteRam(greenAdd, greenWaveform)
dp.DPxWriteRam(blueAdd, blueWaveform)

#configure buffer-- only need to configure the first one, rest will follow the same format
dp.DPxSetDoutBuff(redAdd, len(redWaveform)*2)
dp.DPxSetDoutSched(0, 10, 'hz', len(redWaveform)+1)
dp.DPxUpdateRegCache()

#turn off debounce so button jitter is suppressed
dp.DPxEnableDinDebounce()

#Enable button schedules, set mode to 1 for RPx /MRI setup
dp.DPxSetDoutButtonSchedulesMode(1)
dp.DPxEnableDoutButtonSchedules()
dp.DPxWriteRegCache()
    
#Shut down
core.wait(100)
dp.DPxDisableDoutButtonSchedules()
dp.DPxWriteRegCache()
dp.DPxClose()
