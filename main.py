from evdev import InputDevice, ecodes

# Find the event file corresponding to your keyboard.
# You can find this by checking /dev/input/ directory
# It might be something like /dev/input/eventX
keyboard = InputDevice('/dev/input/eventX')  # Replace 'eventX' with your actual event file

try:
    print("Listening for keyboard events...")
    for event in keyboard.read_loop():
        if event.type == ecodes.EV_KEY:
            # Print the event code and value
            print(f"Event: {event.code}, Value: {event.value}")
            # You can add your own logic here based on the event code and value
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    keyboard.close()
