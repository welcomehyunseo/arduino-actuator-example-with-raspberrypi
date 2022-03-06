#include <Wire.h>

void setup() {
  Serial.begin(9600);

  Wire.begin(1);  // bus address is 0x1
  Wire.onReceive(receiveEvent);  // add event listener
}

void loop() {
  // put your main code here, to run repeatedly:

}

void receiveEvent(int howMany)      
{
  byte I2C_num = Wire.read();
  switch(I2C_num) {
    case 0:
      // action A
      break;
    case 1:
      // action B
      break;
    case 2:
      // action C
      break;
  }
}
