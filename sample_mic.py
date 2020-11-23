
import numpy as np
import time
import explorerhat as hat

def sample(sample_seconds=5):
    # the sampling frequency of the analog input is approx 200Hz
    # which is too low to make a wav file but might still be able
    # to make the bot respond to some changes
    hat_sample_rate = 200
    samples = sample_seconds*hat_sample_rate
    output = np.empty(samples)

    start_time = time.time()

    for i in range(samples):
        output = np.append(output, hat.analog.one.read())

    print(f"Made {samples} readings in {time.time()-start_time} seconds")
    return output
