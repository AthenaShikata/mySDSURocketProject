const int led1 = 5;
const int led2 = 6;
const int buttonLED = 10;
const int buttonPot = 11;
const int pot = A3;

int buttonStateLED = 0;
int buttonStatePot = 0;
int val = 0;

void setup() {
  Serial.begin(9600);
  pinMode (led1, OUTPUT);
  pinMode (led2, OUTPUT);
  pinMode (buttonLED, INPUT);
  pinMode (buttonPot, INPUT);
  pinMode (pot, INPUT);
  digitalWrite (led1, LOW);
  digitalWrite (led2, LOW);
}

void loop() {
  buttonStateLED = digitalRead(buttonLED);
  buttonStatePot = digitalRead(buttonPot);
  if (buttonStateLED == 1) {
    digitalWrite (led1, HIGH);
  } else {
    digitalWrite (led1, LOW);
  }
  if (buttonStatePot == 1) {
    digitalWrite (led2, HIGH);
    val = analogRead (pot);
    Serial.println(val);
  } else {
    digitalWrite (led2, LOW);
  }
}