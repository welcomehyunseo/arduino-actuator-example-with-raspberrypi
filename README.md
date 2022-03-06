# Flat Washers Thickness Measurement System

![Flat washers thickness measurement system_220306_145141-1](https://user-images.githubusercontent.com/92869725/156911166-083a6639-1bdf-4b12-b14c-c364bc49a09c.jpg)



# Reference
## Animation of a simplified stepper motor
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/StepperMotor.gif/200px-StepperMotor.gif)
![](https://www.yoctopuce.com/FR/interactive/img/stepper-motor-optimized.gif)

## How to control stepper motor 
```c
// Define pin connections & motor's steps per revolution
const int dirPin = 2;
const int stepPin = 3;
const int stepsPerRevolution = 200;

void setup()
{
	// Declare pins as Outputs
	pinMode(stepPin, OUTPUT);
	pinMode(dirPin, OUTPUT);
}
void loop()
{
	// Set motor direction clockwise
	digitalWrite(dirPin, HIGH);

	// Spin motor slowly
	for(int x = 0; x < stepsPerRevolution; x++)
	{
		digitalWrite(stepPin, HIGH);
		delayMicroseconds(2000);
		digitalWrite(stepPin, LOW);
		delayMicroseconds(2000);
	}
	delay(1000); // Wait a second
	
	// Set motor direction counterclockwise
	digitalWrite(dirPin, LOW);

	// Spin motor quickly
	for(int x = 0; x < stepsPerRevolution; x++)
	{
		digitalWrite(stepPin, HIGH);
		delayMicroseconds(1000);
		digitalWrite(stepPin, LOW);
		delayMicroseconds(1000);
	}
	delay(1000); // Wait a second
}
```
[link](https://lastminuteengineers.com/a4988-stepper-motor-driver-arduino-tutorial/)

## Serial vs I2C in mcu
![](https://embedded-lab.com/blog/wp-content/uploads/2018/08/Comm-types-580x189.png)
![](https://www.mbtechworks.com/hardware/imgs/uart-spi-i2c.png)

## Controlling an Arduino from a Pi3 using I2C
```c
// arduino
#include <Wire.h>

const int ledPin = 13; // onboard LED
static_assert(LOW == 0, "Expecting LOW to be 0");

void setup() {
  Wire.begin(0x8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // turn it off
}

void loop() {
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}
```

```python
from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
bus.write_byte(addr, 0x1) # switch it on
input("Press return to exit")
bus.write_byte(addr, 0x0) # switch it on
```

[link](https://create.arduino.cc/projecthub/aardweeno/controlling-an-arduino-from-a-pi3-using-i2c-59817b)