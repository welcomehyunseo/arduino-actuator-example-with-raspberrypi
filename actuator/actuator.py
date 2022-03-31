import time
from smbus import SMBus

class Actuator:
    def __init__(self, __addr, action_code):
        self.bus = SMBus(1)  # indicates /dev/ic2-1
        self.__addr = __addr  # bus address, private variable
        self.action_code = action_code

    def execute(self):
        self.bus.write_byte(self.__addr, self.action_code)

        print("action", self.action_code, "is just starting!")

    def execute_and_wait(self):
        self.bus.write_byte(self.__addr, self.action_code)

        print("action", self.action_code, "is starting!")
        while self.bus.read_byte(self.__addr) != 0:
            time.sleep(0.01)
        print("action", self.action_code, "is ended...")

    def print_action_code(self):
        print(self.action_code)
