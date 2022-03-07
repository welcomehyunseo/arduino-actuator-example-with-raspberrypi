import time
from smbus import SMBus


class Actuator:
    def __init__(self, _addr, action_code) -> None:
        self.bus = SMBus(1)  # indicates /dev/ic2-1
        self._addr = _addr  # bus address, private variable
        self.action_code = action_code

    def execute(self) -> None:
        self.bus.write_byte(self._addr, self.action_code)

        print("action", self.action_code, "is just starting!")

    def execute_and_wait(self) -> None:
        self.bus.write_byte(self._addr, self.action_code)

        print("action", self.action_code, "is starting!")
        while self.bus.read_byte(self._addr) != 0:
            time.sleep(0.01)
        print("action", self.action_code, "is ended...")

    def print_code(self):
        print(self.action_code)
