#include <CheapStepper.h>
CheapStepper stepper (8,9,10,11);

char lector;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  stepper.setRpm(12);

}

void loop() {
  // put your main code here, to run repeatedly:
  stepper.moveDegreesCW(360);
  delay(2000);
  stepper.moveDegreesCCW(360);
  delay(2000);
}
