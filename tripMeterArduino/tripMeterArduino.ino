int right_pin = 18;
int left_pin = 17;
int rp_right_pin = 9;
int rp_left_pin = 10;

int right_value = 0;
int left_value = 0;

// sensor max value ~4.3, min value ~2.0
int right_high_limit = 750; // 3.67 / 5.0 * 1023;
int right_low_limit = 610; // 2.98 / 5.0 * 1023;
int left_high_limit = 635; // 3.10 / 5.0 * 1023;
int left_low_limit = 495; // 2.42 / 5.0 * 1023;

bool right_prev_high = false;
bool left_prev_high = false;
unsigned long last_right_time = 0;
unsigned long last_left_time = 0;
unsigned long time_limit = 3;

void setup() {
  pinMode(right_pin, INPUT);
  pinMode(left_pin, INPUT);
  pinMode(rp_right_pin, OUTPUT);
  pinMode(rp_left_pin, OUTPUT);
}


void loop() {
   right_value = analogRead(right_pin);
   if (right_value > right_high_limit && !right_prev_high && millis() - last_right_time > time_limit){
      right_prev_high = true;
      last_right_time = millis();
      digitalWrite(rp_right_pin, HIGH);
   } else if (right_value < right_low_limit && right_prev_high && millis() - last_right_time > time_limit){
      right_prev_high = false;
      last_right_time = millis();
      digitalWrite(rp_right_pin, LOW);
   }
   left_value = analogRead(left_pin);
   if (left_value > left_high_limit && !left_prev_high && millis() - last_left_time > time_limit){
      left_prev_high = true;
      last_left_time = millis();
      digitalWrite(rp_left_pin, HIGH);
   } else if (left_value < left_low_limit && left_prev_high && millis() - last_left_time > time_limit){
      left_prev_high = false;
      last_left_time = millis();
      digitalWrite(rp_left_pin, LOW);
   }
}
