from flask import Flask
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
    # Pulse width for 0 degrees and 30 degrees
    pulse_width_0 = 500   # 0 degrees
    pulse_width_30 = 930  # 30 degrees

    for _ in range(3):
        # Move to 0 degrees (500 µs)
        pi.set_servo_pulsewidth(SERVO_PIN, pulse_width_0)
        time.sleep(0.2)  # Adjust this sleep time to control the speed
        
        # Move to 30 degrees (833 µs)
        pi.set_servo_pulsewidth(SERVO_PIN, pulse_width_30)
        time.sleep(0.2)  # Adjust this sleep time to control the speed
        
    # Stop the servo by disabling PWM output
    pi.set_servo_pulsewidth(SERVO_PIN, 0)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def activate_gpio():
    move_servo()
    return "GOOOOOOONG!", 200  # Return success response

if __name__ == '__main__':
    try:
        # Run the Flask server on all network interfaces, on a specific port (e.g., 5000)
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        pi.stop()  # Ensure cleanup on server shutdown