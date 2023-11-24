uint8_t inchar = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // Инициализация Serial - порта
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop() {
  while (Serial.available()) {         // ПОКА есть что то на вход    
    inchar = Serial.read();        // забиваем строку принятыми данными
    delay(1);                              // ЗАДЕРЖКА. Без неё работает некорректно!
  }
  if (inchar == 101){
    digitalWrite(8, HIGH);
  }
  else if (inchar == 111){
    digitalWrite(8, LOW);
  }
  else if (inchar == 102){
    digitalWrite(2, HIGH);
  }
  else if (inchar == 112){
    digitalWrite(2, LOW);
  }
  else if (inchar == 103){
    digitalWrite(3, HIGH);
  }
  else if (inchar == 113){
    digitalWrite(3, LOW);
  }
  // свет
  else if (inchar == 201){
    digitalWrite(4, HIGH);
  }
  else if (inchar == 211){
    digitalWrite(4, LOW);
  }
  else if (inchar == 202){
    digitalWrite(5, HIGH);
  }
  else if (inchar == 212){
    digitalWrite(5, LOW);
  }
  else if (inchar == 203){
    digitalWrite(6, HIGH);
  }
  else if (inchar == 213){
    digitalWrite(6, LOW);
  }
  else if (inchar == 204){
    digitalWrite(7, HIGH);
  }
  else if (inchar == 214){
    digitalWrite(7, LOW);
  }
}