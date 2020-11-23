# this bot tries to outrun noises

import explorerhat as hat
import numpy as np
from time import sleep
import animate as mv

MID = 1.6 # V hovers around this when quiet
# bot will 'get scared' beyond the following deviation
# in the 0.3-0.4 range that's the sound of it moving on a hard floor
ACCEPTANCE = 0.4
SAMPLING_RATE = 200 # determined by speed of hat.analog.one.read()
SAMPLE_COUNT = 100
SUPPLY_V = 3.3 # assuming the mic's output is the same as the supply

def main():
    samples = np.empty(SAMPLE_COUNT)
    currently_fleeing = False

    while True:
        for s in range(SAMPLE_COUNT):
            samples[s] = hat.analog.one.read()
        # normalised_samples = np.add(samples, -MID)
        # normalised_samples = np.multiply(samples, 1/SUPPLY_V)
        sample_range = samples.max()-samples.min()
        print(sample_range)
        if sample_range > ACCEPTANCE and not currently_fleeing:
            mv.stop() # best to mv.stop before changing direction
            mv.left(80, 0.2); mv.stop(); sleep(0.2)
            mv.right(80, 0.3); mv.stop(); sleep(0.2)
            mv.left(80, 0.2); mv.stop()
            mv.forward(100, 2)
            currently_fleeing = True
        elif sample_range < ACCEPTANCE:
            mv.stop()
            currently_fleeing = False
main()