import TCP
import Motor
import Steering
import Status
import time
import os
import Cameras

port = 12345 
ip_address = "10.22.7.247"

motors = None
cameras = None
connection_test = None

cameras = None
try:
    trip_meter = Motor.TripMeter()
    motors = Motor.Motor(trip_meter)
    autoTTCommunication = TCP.AutoTTCommunication(port, ip_address = ip_address)
    steering = Steering.SteeringWithIOSGyro(motors, autoTTCommunication = autoTTCommunication)
    modes = Steering.Modes(autoTTCommunication, steering)
    #cameras = Cameras.Cameras(motors)
    #status = Status.Status(autoTTCommunication, motors, cameras)
    #connection_test = TCP.ConnectionTest(autoTTCommunication, motors, cameras)
    autoTTCommunication.set_receivers(gyro_recv = steering, mode_recv = modes, status_recv = status, stop_cont_recv = steering, 
            disconnect_recv = connection_test, shut_down_recv = connection_test, connection_test_recv = connection_test)
    time.sleep(0.5) # wait for AutoTT iOS app to start the gyro class
    autoTTCommunication.start_gyro_with_update_intervall(1.0/60.0)
    #connection_test.set_intervall(0.05)
    modes.send_modes_and_info_modes()
    
    while connection_test.is_connection_good():
        time.sleep(0.3)
        print trip_meter.get_right_speed()

except:
    if (motors != None):
        motors.turn_off()
    if (cameras != None):
        cameras.turn_off()
    if (connection_test != None):
        connection_test.disconnect()
    
# os.system("sudo reboot")
