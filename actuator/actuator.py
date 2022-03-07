from smbus import SMBus


class Actuator:
    def __init__(self, addr, action_code) -> None:
        self.bus = SMBus(1)  # indicates /dev/ic2-1
        self.addr = addr  # bus address
        self.action_code = action_code

    def execute(self) -> None:
        self.bus.write_byte(self.addr, self.action_code)
        print("Action", self.action_code, "is executed!")

    def stop(self) -> None:
        pass

    def execute_during_finish(self) -> None:
        pass
