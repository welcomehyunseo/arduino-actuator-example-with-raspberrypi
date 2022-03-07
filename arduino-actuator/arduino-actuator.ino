#include <Wire.h>
byte I2C_data;

byte action_code = 0;

void setup()
{
  Serial.begin(9600);
  Wire.begin(9);                // bus address is 0x1
  Wire.onReceive(receiveEvent); // add receive event listener
  Wire.onRequest(sendEvent);    // add send event listener
}

void loop()
{
  switch(action_code) 
  {
    case 1:
      print_action_start(action_code);
      delay(3000);  // some task
      print_action_end(action_code);
      action_code = 0;  // tell that action was ended
      break;
    case 2:
      break;
    case 3:
      break;
  }
}

void receiveEvent(int howMany)
{
  action_code = Wire.read();
}

void sendEvent()
{
  Wire.write(action_code);
}

void print_action_start(int action_code)
{
  Serial.print("action ");
  Serial.print(action_code);
  Serial.print(" is starting!\n");
}

void print_action_end(int action_code)
{
  Serial.print("action ");
  Serial.print(action_code);
  Serial.print(" is ended...\n");
}
