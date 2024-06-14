#include <Arduino.h>
#include <XSpaceBioV10.h>
#include <XSControl.h>

double raw_ecg = 0;
double raw_ecg_2 = 0;
double raw_ecg_3 = 0;
double filtered_ecg = 0;
double filtered_ecg_2 = 0;
double filtered_ecg_3 = 0;

XSpaceBioV10Board Board;

XSFilter Filter;


void FilterTask(void *pv) {
  while (1) {
    raw_ecg = Board.AD8232_GetVoltage(AD8232_XS1);
    raw_ecg_2 = Board.AD8232_GetVoltage(AD8232_XS2);
    filtered_ecg = Filter.SecondOrderLPF(raw_ecg, 120, 0.001);
    filtered_ecg_2 = Filter.SecondOrderLPF(raw_ecg_2, 120, 0.001);
    raw_ecg_3 = raw_ecg_2-raw_ecg;
    filtered_ecg_3 = filtered_ecg_2 - filtered_ecg;
    vTaskDelay(1);
  }
  vTaskDelete(NULL);
}

void setup() {
  Serial.begin(115200);
  Board.init();
  Board.AD8232_Wake(AD8232_XS1);
  Board.AD8232_Wake(AD8232_XS2);
  xTaskCreate(FilterTask, "FilterTask", 3000, NULL, 1, NULL);
}

void loop() {
  Serial.println((String)raw_ecg + " " + (String)filtered_ecg);
  //Serial.println((String)raw_ecg_2 + " " + (String)filtered_ecg_2);
  // Serial.println((String)raw_ecg_3 + " " + (String)filtered_ecg_3);
  delay(10);
}

