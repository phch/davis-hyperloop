/* Automation Direct QMIC-0P-0F Retroreflective Photoelectric Sensor 
 * Settings - Max, D (Dark On Mode)
 * (The sensor knobs should point toward 'D' and 'MAX')
 * 
 * This code is confirmed working for the Arduino Uno with an Elecfreaks CAN BUS Shield, 
 * with 12 V DC across the sensor and the sensor output connected to any digital pin, except 
 * pins 2 and 3 (those are interrupt pins). Special thanks to Andrew Preston for his research.
 * 
 * Be sure to double check connections when hooking up the sensor.
 * The sensor light should be a soft yellow and blink rapidly.
 *
 * A slight delay before the sensor actually detects light is a known issue, and probably has   
 * to do with the connections (fiddle around with the connections to get a faster response). 
 *
 */

const int RRPE_SENSOR_PIN = 4; // Digital Pin 4
int value = 0; // Value given by the sensor
float p_prev = 0; // Previous position
float v_prev = 0; // Previous velocity
float p_curr = 0; // Current position
float v_curr = 0; // Current velocity

bool insideTape = false;

float t_initial;
float t_final;
float duration;

void setup() {
  Serial.begin(9600);
  pinMode(RRPE_SENSOR_PIN, INPUT);
  Serial.println("Sensor Initialized.");
}

void loop() {
  p_curr = p_prev;

  // Get the current sensor output value
  value = digitalRead(RRPE_SENSOR_PIN);
  if (value) {
    if (insideTape == false) {
      Serial.println("Strip of tape detected.");
      t_initial = millis();
      insideTape = true;
    }
    else {
      Serial.println("Traveling inside tape.");
    }
  }
  else if (!value) {
    if (insideTape == true) {
      insideTape = false;
      t_final = millis();
      duration = (t_final - t_initial); // milliseconds
      p_curr = p_prev + 100;
      v_curr = (p_curr - p_prev) / duration;
      Serial.println("p_curr: " + String(p_curr) + " feet");
      Serial.println("p_prev: " + String(p_prev) + " feet");
      Serial.println("duration: " + String(duration) + " milliseconds");
      Serial.println("v_curr: " + String(v_curr) + " feet/millisecond");
      Serial.println(" ");
    }
    Serial.println("No strips of tape detected.");
  }
  else {
    if (insideTape == true) {
      insideTape = false;
      t_final = millis();
      duration = (t_final - t_initial); // milliseconds
      p_curr = p_prev + 100;
      v_curr = (p_curr - p_prev) / duration;
      Serial.println("p_curr: " + String(p_curr) + " feet");
      Serial.println("p_prev: " + String(p_prev) + " feet");
      Serial.println("duration: " + String(duration) + " milliseconds");
      Serial.println("v_curr: " + String(v_curr) + " feet/millisecond");
      Serial.println(" ");
    }
    Serial.println("No strips of tape detected.");
  }

  p_prev = p_curr;
  delay(500);
}


