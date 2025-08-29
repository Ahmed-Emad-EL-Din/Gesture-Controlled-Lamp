
// the setup function runs once when you press reset or power the board
void setup() {
  
  // initialize digital pin LED_BUILTIN as an output.  
  Serial.begin(9600);  
  pinMode(3, OUTPUT);  
}

// the loop function runs over and over again forever
void loop() {
  char input = Serial.read();

  if (input == '1'){
    digitalWrite(3,HIGH);
    delay(2);
  }  
  if (input == '0'){
    digitalWrite(3,LOW);
    delay(2);
  }
}
