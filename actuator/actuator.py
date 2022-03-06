from smbus import SMBus

class Actuator:
    addr = 0x1  # bus address, default is 0x1
    bus = SMBus(1)  # indicates /dev/ic2-1

    def __init__(self, addr) -> None:
        self.addr = addr

    def action_a(self) -> None:
        bus.write_byte(addr, 0x0)  # send I2C_num is 0 to arduino actuator

    def action_b(self) -> None:
        bus.write_byte(addr, 0x1)  # send I2C_num is 1 to arduino actuator

    def action_c(self) -> None:
        bus.write_byte(addr, 0x2)  # send I2C_num is 2 to arduino actuator
