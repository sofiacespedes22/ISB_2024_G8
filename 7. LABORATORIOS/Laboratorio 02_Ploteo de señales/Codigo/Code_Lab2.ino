/*************************************
 Course: ISB-UPCH
 Date: 29/03/2023
 Autor: Moises Meza

**************************************/
unsigned long lastMsg = 0;
float F=3;                      // 1 hz
double Fs = 10*F;               // 10 hz
double Ts_ms = (1/Fs)*1000;     //  100 ms  

void setup() {
  Serial.begin(9600);
  while (!Serial);
  //Serial.println("R1:,R2:,");
}

void loop() {

  unsigned long now = millis();


 if (now - lastMsg > Ts_ms) {
    lastMsg = now;

    // Read analog input from A0
    int analogValue = analogRead(A0);

    // Print analog reading

    Serial.println(analogValue);
  }
}
