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
        self.ser.write(code.encode('ascii'))


    def left(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 X-'+distance)

    def right(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 X'+distance)

    def up(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 Y'+distance)

    def down(self, distance=5):
        '''

        '''
        self.send_gcode('F1000 G91')
        self.send_gcode('G01 U-'+distance)

    def home(self):
        '''

        '''
        self.send_gcode('G0 X0 Y0')

    def set_home(self):
        '''

        '''
        self.send_gcode('G92 X0 Y0 Z0')