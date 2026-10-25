"""Quick utility to check the response-box (ResponsePixx) button codes.

Run on the lab machine with the VPixx connected:

    python check_buttons.py

Press each button one at a time; its DIN value and name are printed.
If a button shows 'UNKNOWN', note its value and add it to buttonCodes
(here and in datapixx.py). Press Ctrl+C to stop.
"""

import time
from pypixxlib import _libdpx as dp

# Known DIN log values for this response box (same map as datapixx.py).
buttonCodes = {
    65528: 'blue',
    65521: 'red',
    65520: 'release',
}

def main():
    dp.DPxOpen()
    if not dp.DPxIsReady():
        raise ConnectionError('VPixx hardware not detected. Check the connection.')

    logStatus = dp.DPxSetDinLog(0, 1000)
    dp.DPxEnableDinDebounce()
    dp.DPxStartDinLog()
    dp.DPxUpdateRegCache()

    print('Press the response-box buttons one at a time (Ctrl+C to stop)...\n')
    try:
        while True:
            dp.DPxUpdateRegCache()
            dp.DPxGetDinStatus(logStatus)
            if logStatus['newLogFrames'] > 0:
                data = dp.DPxReadDinLog(logStatus, logStatus['newLogFrames'])
                for entry in data:
                    value = entry[1] if isinstance(entry, (list, tuple)) else entry
                    name = buttonCodes.get(value, 'UNKNOWN -> add to buttonCodes')
                    print(f'DIN value: {value:>6}   ->  {name}')
            time.sleep(0.01)
    except KeyboardInterrupt:
        print('\nStopped.')
    finally:
        dp.DPxStopDinLog()
        dp.DPxClose()

if __name__ == '__main__':
    main()
