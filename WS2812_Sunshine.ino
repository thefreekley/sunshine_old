




#include <iarduino_Encoder_tmr.h>             //  Подключаем библиотеку iarduino_Encoder_tmr для работы с энкодерами через аппаратный таймер
iarduino_Encoder_tmr enc(A1,A4);              //  Объявляем объект enc для работы с энкодером указывая (№ вывода A, № вывода B)
#include <EEPROM.h>                                              //  Если при объявлении объектов перепутать выводы, то поворот влево будет расценен как поворот вправо и наоборот
#include "GyverButton.h"
GButton butt1(A5);       

#include <HCSR04.h>
#define PIN_TRIG 10
#define PIN_ECHO 11
HCSR04 ultrasonicSensor(PIN_TRIG, PIN_ECHO, 20, 300);
         // библиотека для работы с лентой

#define LED_COUNT 120          // число светодиодов в кольце/ленте
#define LED_DT 12             // пин, куда подключен DIN ленты

static byte bright;
static int counting;  
#include "FastLED.h" 
// ---------------СЛУЖЕБНЫЕ ПЕРЕМЕННЫЕ-----------------
int BOTTOM_INDEX = 0;        // светодиод начала отсчёта
int TOP_INDEX = int(LED_COUNT / 2);
int EVENODD = LED_COUNT % 2;
struct CRGB leds[LED_COUNT];
int ledsX[LED_COUNT][3];     //-ARRAY FOR COPYING WHATS IN THE LED LEDS CURRENTLY (FOR CELL-AUTOMATA, MARCH, ETC)

int thisdelay = 20;          //-FX LOOPS DELAY VAR
int thisstep = 10;           //-FX LOOPS DELAY VAR
int thishue = 0;             //-FX LOOPS DELAY VAR
int thissat = 255;           //-FX LOOPS DELAY VAR

int thisindex = 0;
int thisRED = 0;
int thisGRN = 0;
int thisBLU = 0;

int idex = 0;                //-LED INDEX (0 to LED_COUNT-1
int ihue = 0;                //-HUE (0-255)
int ibright = 0;             //-BRIGHTNESS (0-255)
int isat = 0;                //-SATURATION (0-255)
int bouncedirection = 0;     //-SWITCH FOR COLOR BOUNCE (0-1)
float tcount = 0.0;          //-INC VAR FOR SIN LOOPS
int lcount = 0;              //-ANOTHER COUNTING VAR

volatile uint32_t btnTimer;
volatile byte modeCounter;
volatile boolean changeFlag;
int   counter=0;
boolean activity_move;
CRGBPalette16 firePalette;
byte new_bright;
int max_mode=12;

void setup()
{
  ultrasonicSensor.begin();
 randomSeed(analogRead(0));
  counter = random(0, 30000);

  firePalette = CRGBPalette16(
                  getFireColor(0 * 16),
                  getFireColor(1 * 16),
                  getFireColor(2 * 16),
                  getFireColor(3 * 16),
                  getFireColor(4 * 16),
                  getFireColor(5 * 16),
                  getFireColor(6 * 16),
                  getFireColor(7 * 16),
                  getFireColor(8 * 16),
                  getFireColor(9 * 16),
                  getFireColor(10 * 16),
                  getFireColor(11 * 16),
                  getFireColor(12 * 16),
                  getFireColor(13 * 16),
                  getFireColor(14 * 16),
                  getFireColor(15 * 16)
                );
                
   butt1.setDirection(NORM_OPEN);
    butt1.setType(HIGH_PULL);
  butt1.setTickMode(AUTO);
  butt1.setDebounce(90);        // настройка антидребезга (по умолчанию 80 мс)
  butt1.setTimeout(300);
  
  bright=250;
  counting=3;

   LEDS.setBrightness(bright);
  randomSeed(analogRead(0));

                
  enc.begin(); 
  Serial.begin(9600);              // открыть порт для связи
  LEDS.setBrightness(bright);  // ограничить максимальную яркость
  Serial.println(counting);
  LEDS.addLeds<WS2811, LED_DT, GRB>(leds, LED_COUNT);  // настрйоки для нашей ленты (ленты на WS2811, WS2812, WS2812B)
  one_color_all(0, 0, 0);          // погасить все светодиоды
  LEDS.show();                     // отослать команду
  new_bright=bright;
  randomSeed(analogRead(0));
  pinMode(2, INPUT_PULLUP);
//  attachInterrupt(0, btnISR, FALLING);
 change_mode(counting);
   
}

void one_color_all(int cred, int cgrn, int cblu) {       //-SET ALL LEDS TO ONE COLOR
  for (int i = 0 ; i < LED_COUNT; i++ ) {
    leds[i].setRGB( cred, cgrn, cblu);
  }
}

void loop() {
   
    remove_control();
    stay_ease();

  /*
    if (Serial.available() > 0) {     // если что то прислали
      ledMode = Serial.parseInt();    // парсим в тип данных int
      change_mode(ledMode);           // меняем режим через change_mode (там для каждого режима стоят цвета и задержки)
    }
  */
  switch (counting) { //37 бильш нрав
    case 999: break;                           // пазуа
    case  1: rainbow_loop(); break;            // крутящаяся радуга // da
    case  2: flicker(); break;                 // случайный стробоскоп
    case 3: fireLineNoise(); break;
    case 4: new_rainbow_loop(); break;        // крутая плавная вращающаяся радуга // daq!!!
    case 5:fireLine();break; 
     case 6: one_color_all(255, 0, 0); LEDS.show(); break; //---ALL RED
    case 7: one_color_all(0, 255, 0); LEDS.show(); break; //---ALL GREEN
    case 8: one_color_all(0, 0, 255); LEDS.show(); break; //---ALL BLUE
    case 9: one_color_all(255, 255, 0); LEDS.show(); break; //---ALL COLOR X
    case 10: one_color_all(0, 255, 255); LEDS.show(); break; //---ALL COLOR Y
    case 11: one_color_all(255, 0, 255); LEDS.show(); break; //---ALL COLOR Z
    case 12:  one_color_all(255, 91, 0); LEDS.show(); break; //---ALL RED
    case 13:  one_color_all(255, 255, 255); LEDS.show(); break; //---ALL RED
    }
}



void change_mode(int newmode) {
  thissat = 255;
  switch (newmode) {
   case 1: thisdelay = 20; thisstep = 10; break;       //---RAINBOW LOOP
    case 2: thishue = 160; thissat = 50; break;         //--- FLICKER
    case 4: thisdelay = 15; break;                      //---NEW RAINBOW LOOP

    case 6: one_color_all(255, 0, 0); LEDS.show(); break; //---ALL RED
    case 7: one_color_all(0, 255, 0); LEDS.show(); break; //---ALL GREEN
    case 8: one_color_all(0, 0, 255); LEDS.show(); break; //---ALL BLUE
    case 9: one_color_all(255, 255, 0); LEDS.show(); break; //---ALL COLOR X
    case 10: one_color_all(0, 255, 255); LEDS.show(); break; //---ALL COLOR Y
    case 11: one_color_all(255, 0, 255); LEDS.show(); break; //---ALL COLOR Z
    case 12:  one_color_all(255, 91, 0); LEDS.show(); break; //---ALL RED
    case 13:  one_color_all(255, 255, 255); LEDS.show(); break; //---ALL RED
    }
  bouncedirection = 0;
  one_color_all(0, 0, 0);
//  ledMode = newmode;
}


void change_mode_fast(int arg){
  counting=arg;
  EEPROM.write(10,counting);         
  change_mode(counting);   
  changeFlag = true;
}
void stay_ease(){
  static unsigned long time_ease_bright;
  if(millis()-time_ease_bright>2){
  //Serial.println(String(bright) + "-n  " + String(new_bright));
  if(new_bright!=bright){
  if(new_bright<bright)bright-=5;
  else bright+=5;
  }
  //Serial.println(bright);
  time_ease_bright=millis();
  LEDS.setBrightness(bright); 
  }
 
}
/*
int distance_cm(){
  int duration, cm; // назначаем переменную "cm" и "duration" для показаний датчика  
  digitalWrite(TRIG_PIN, LOW); // изначально датчик не посылает сигнал
  delayMicroseconds(2); // ставим задержку в 2 ммикросекунд

  digitalWrite(TRIG_PIN, HIGH); // посылаем сигнал
  delayMicroseconds(10); // ставим задержку в 10 микросекунд
  digitalWrite(TRIG_PIN, LOW); // выключаем сигнал

  duration = pulseIn(ECHO_PIN, HIGH); // включаем прием сигнала

  cm = duration / 58; // вычисляем расстояние в сантиметрах
  
 return cm;

}
*/

void remove_control(){
  static unsigned long time_of_update=millis();
  static unsigned long time_last_move;
  
  static int old_distance;
  int distance_static;

  
  static boolean availability_hand=0;
  boolean availability_hand_in=0;
  boolean availability_hand_out=0;
  static int count_moves=0;
  static boolean change_mode_distace=0;
  if(millis()-time_of_update>50){
    distance_static = int( ultrasonicSensor.getDistance());
    if(distance_static!= -27536){
    if(old_distance-distance_static>50 && availability_hand==0){ availability_hand=1; availability_hand_in=1; } // при різкій зміні дистанції ми вказуэм наявність рукі і зміну стану
    if(distance_static-old_distance>50 && availability_hand==1){ availability_hand=0; availability_hand_out=1; }

    if(millis()-time_last_move<1000 && availability_hand_in){
      count_moves++;
      if(count_moves>1 && new_bright!=0){
        if(counting>max_mode)counting=1;
          else counting++;
            EEPROM.write(10,counting);         
       change_mode(counting);   
       changeFlag = true;
      } 
      Serial.println(count_moves);
    }
    if(millis()-time_last_move>1000){
      if(count_moves==1){
        
       if(new_bright>0)new_bright=0;
       else new_bright=250;
      }
      count_moves=0;
     
    }
    Serial.println(count_moves);
    
    if(availability_hand){
      digitalWrite(5,0);
      digitalWrite(6,0);
    }
    else{
      digitalWrite(5,240);
      digitalWrite(6,240);
      
    }
    //Serial.println("Distance:" + String(distance_static) + " Hand :" + String(availability_hand));
    if(availability_hand_in)time_last_move=millis();

    
    if(millis()-time_last_move>1000 && availability_hand==1){
      //Serial.println(String(distance_static));
      
      int  delta_distance=constrain(distance_static,5,25);
      delta_distance=map(delta_distance,5,25,0,10);
      new_bright=delta_distance*25;

 
    }
    
    
    //Serial.println(availability_hand);
    old_distance=distance_static; // last value of sensor
    time_of_update=millis();
  }
  }
}
