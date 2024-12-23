
import pigpio
import time

# Set the GPIO pin
SERVO_PIN = 18

# Connect to pigpio daemon
pi = pigpio.pi()

# Check if pigpio is connected
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    exit()

def move_servo():
    # Move from 0 to 90 and back to 0, three times as fast as possible
    for _ in range(3):
        # Move to 0 degrees (500 µs)
        pi.set_servo_pulsewidth(SERVO_PIN, 500)
        time.sleep(0.5)  # You can adjust this sleep time to control the speed
        
        # Move to 90 degrees (1500 µs)
        pi.set_servo_pulsewidth(SERVO_PIN, 1500)
        time.sleep(0.5)  # Adjust the time to control the speed
        
    # Stop the servo by disabling PWM output
    pi.set_servo_pulsewidth(SERVO_PIN, 0)

# Call the function to swing the servo
move_servo()

# Clean up and close the connection to pigpio
pi.stop()