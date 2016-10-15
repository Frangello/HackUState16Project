int lightStatus = 0;   // for incoming serial data
int ledPin;      // the number of a LED pin

void setup() {
  //Origin Airport Pin
  pinMode(1, OUTPUT);
  //Pins are set every other so turn on and off can be done with one number
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {
  digitalWrite(1, LOW);
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    ledPin = Serial.read();
    Serial.println(ledPin);
    if(ledPin == 1){ //Origin Airport LED
      if(digitalRead(ledPin) == LOW){
        digitalWrite(ledPin, HIGH);
      }
      else{
        digitalWrite(ledPin, LOW);
      }
    }
    else if(ledPin % 2 == 0){ //turn pin on
      digitalWrite(ledPin, HIGH);
    }
    else { //turn pin(number passed - 1) off
      digitalWrite(ledPin - 1, LOW);
    }
    
  }
  
}
 
