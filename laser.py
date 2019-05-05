import serial

class Laser:
    '''

    '''

    def __init__(self, port):
        '''

        '''
        self.ser = serial.Serial(port, 115200)
    
    def send_gcode(self, code):
        '''

        '''
        self.ser.write((code+'\r').encode('ascii'))


    def left(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 X-'+str(distance))

    def right(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 X'+str(distance))

    def up(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 Y'+str(distance))

    def down(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 Y-'+str(distance))

    def home(self):
        '''

        '''
        self.send_gcode('G90')
        self.send_gcode('G0 X0 Y0')
        self.send_gcode('G91')

    def set_home(self):
        '''

        '''
        self.send_gcode('G92 X0 Y0 Z0')

    def laser_on(self):
        '''

        '''
        self.send_gcode('M3')

    def laser_off(self):
        '''
        
        '''
        self.send_gcode('M5')

    def laser_power(self, power):
        '''

        '''
        self.send_gcode('S'+str(power))