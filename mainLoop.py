import TCP
import Motor
import Steering
import Status
import time

port = 12345 # will change between 12345 and 12346
ip_address = "10.22.8.34"

while True:
    try:
        autoTTCommunication = TCP.AutoTTCommunication(port, ip_address = ip_address)
        trip_meter = Motor.TripMeter()
        motors = Motor.Motor(trip_meter)
        steering = Steering.SteeringWithIOSGyro(motors, autoTTCommunication = autoTTCommunication)
        mode = Steering.Mode(autoTTCommunication, steering)
        status = Status.Status(autoTTCommunication, motors)
        connection_test = Steering.ConnectionTest(autoTTCommunication, motors)
        autoTTCommunication.set_receivers(gyro_recv = steering, mode_recv = mode, status_recv = status, 
                stop_cont_recv = steering, disconnect_recv = connection_test, shut_down_recv = connection_test)
        connection_test.set_intervall(0.05)
        #modes.send_modes_and_info_modes()
        
        print "hei2"
        while connection_test.get_good_connection():
            time.sleep(0.3)

        time.sleep(3)
        print "yes"
        if (port == 12345):
            port += 1
        else:
            port -= 1
            
    except Exception as instance:
        print type(instance)     # the exception instance
        print instance.args      # arguments stored in .args
        print instance
        motors.turn_off()
        connection_test.disconnect()
