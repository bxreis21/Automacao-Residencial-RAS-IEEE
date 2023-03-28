char cmd;                     
void setup() {
  Serial.begin(9600);         
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT); 
  pinMode(5, OUTPUT);
}
void loop() {
  cmd = Serial.read();        
  Serial.println(cmd);
  if (cmd == 'g') {           
    digitalWrite(7, HIGH); 
  }
   else if (cmd == 'h') {      
    digitalWrite(7, LOW);
  }  
  else if (cmd == 'w') {      
    digitalWrite(6, HIGH);
  } 
  else if (cmd == 'e') {      
    digitalWrite(6, LOW);
  }  
  else if (cmd == 'b') {      
    digitalWrite(5, HIGH);
  }
  else if (cmd == 'n') {      
    digitalWrite(5, LOW);
  }
  delay(10);
}
