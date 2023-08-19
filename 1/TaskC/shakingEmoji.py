from sense_hat import SenseHat
import time

sense = SenseHat()

# colors
O = (0,0,0) #nothing
P =  (255, 0, 0) #red

emoji_1 = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]


def detect_shake():
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    magnitude = x*x + y*y + z*z
    if magnitude > 2.0:  #Sensitivity
        return True
    return False

def main():
    while True:
        if detect_shake():
            sense.set_pixels(emoji_1)
            time.sleep(2)
            sense.clear()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
