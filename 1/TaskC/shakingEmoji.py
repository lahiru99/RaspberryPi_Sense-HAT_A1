from sense_hat import SenseHat
import time
from animatedEmoji import raspi_logo, sad_face, circle, heart, smiley_face

sense = SenseHat()

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
    emojis = [raspi_logo, sad_face, circle, heart, smiley_face]
    current_emoji_index = 0
    
    while True:
        if detect_shake():
            sense.set_pixels(emojis[current_emoji_index])
            current_emoji_index = (current_emoji_index + 1) % len(emojis)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
