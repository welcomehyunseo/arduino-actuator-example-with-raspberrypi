#include <Wire.h>

boolean hold = false;

void setup()
{
  Serial.begin(9600);

  Wire.begin(9);                // bus address is 0x1
  Wire.onReceive(receiveEvent); // add receive event listener
  Wire.onRequest(sendEvent);    // add send event listener
}

void loop()
{
  // put your main code here, to run repeatedly:
}

void receiveEvent(int howMany)
{
  byte action_code = Wire.read();
  switch (action_code)
  {
  case 0:
    print_action_start(action_code);
    hold = true;
    delay(3000); // delay
    print_action_end(action_code);
    hold = false;
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
  Wire.write(hold);
}

void print_action_start(int action_code)
{
  Serial.print("action which code is");
  Serial.print(action_code);
  Serial.print("was starting!\n");
}

void print_action_end(int action_code)
{
  Serial.print("action which code is");
  Serial.print(action_code);
  Serial.print("was ended\n");
}
