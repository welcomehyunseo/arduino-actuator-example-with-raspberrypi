#include <Wire.h>
byte I2C_data;

void setup() {
  Serial.begin(9600);

  Wire.begin(9);  // bus address is 0x1
  Wire.onReceive(receiveEvent);  // add event listener
  Wire.onRequest(sendEvent);
  Serial.println("hello");
}

void loop() {
  // put your main code here, to run repeatedly:
}

void receiveEvent(int howMany)      
{
  I2C_data = Wire.read();
  switch(I2C_data) {
    case 0:
      Serial.println("Action A");
      break;
    case 1:
      Serial.println("Action B");
      break;
    case 2:
      Serial.println("Action C");
      break;
  }
}

void sendEvent()
{
  Wire.write(3);
  Serial.println("send data");
}