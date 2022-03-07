from smbus import SMBus

class Actuator:
    def __init__(self, addr) -> None:
        self.bus = SMBus(1)  # indicates /dev/ic2-1
        self.addr = addr  # bus address

    def action_a(self) -> None:
        self.bus.write_byte(self.addr, 0)  # send I2C_num is 0 to arduino actuator
        print("action a is executed!")

    def action_b(self) -> None:
        self.bus.write_byte(self.addr, 1)  # send I2C_num is 1 to arduino actuator
        print("action b is executed!")

    def action_c(self) -> None:
        self.bus.write_byte(self.addr, 2)  # send I2C_num is 2 to arduino actuator
        print("action c is executed!")
