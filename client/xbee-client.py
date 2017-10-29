import serial


class Client:
    serial_connection = serial.Serial(port="/dev/ttyUSB0", timeout=None)

    def run(self):
        while True:
            try:
                reading = self.serial_connection.read()

                if reading == "":
                    continue
                print "THIS> " + reading

            except Exception as err:
                print Exception, err


client = Client()
client.run()
