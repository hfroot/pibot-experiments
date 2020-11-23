import explorerhat as hat
import numpy as np

# if this file is modified again, refactor to use animate fns
def main():
    mic_sample_size = 100
    mic_samples = np.array([])
    while True:
        straight_speed = 100
        turn_speed = 60
        if hat.touch.one.is_pressed():
            hat.motor.one.forward(straight_speed)
            hat.motor.two.forward(straight_speed)
        elif hat.touch.two.is_pressed():
            hat.motor.one.backward(turn_speed)
            hat.motor.two.forward(turn_speed)
        elif hat.touch.three.is_pressed():
            hat.motor.one.forward(turn_speed)
            hat.motor.two.backward(turn_speed)
        elif hat.touch.four.is_pressed():
            hat.motor.one.stop()
            hat.motor.two.stop()

        mic_samples = np.append(mic_samples, hat.analog.one.read())
        if len(mic_samples) == mic_sample_size:
            print(mic_samples.mean())
            mic_samples = np.array([])

main()