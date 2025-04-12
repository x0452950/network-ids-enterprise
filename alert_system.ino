int ledPin = 8;
int buzzerPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    if (command == "UNAUTHORIZED") {
      digitalWrite(ledPin, HIGH);
      tone(buzzerPin, 1000); // Normal beep
      delay(1500);
      digitalWrite(ledPin, LOW);
      noTone(buzzerPin);
    } else if (command == "SCAN") {
      digitalWrite(ledPin, HIGH);
      tone(buzzerPin, 2000); // High-pitched alert
      delay(3000);
      digitalWrite(ledPin, LOW);
      noTone(buzzerPin);
    } else {
      // Default response
      digitalWrite(ledPin, HIGH);
      tone(buzzerPin, 500);
      delay(1000);
      digitalWrite(ledPin, LOW);
      noTone(buzzerPin);
    }
  }
}
