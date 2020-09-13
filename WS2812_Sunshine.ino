/*
  Скетч создан на основе FASTSPI2 EFFECTS EXAMPLES автора teldredge (www.funkboxing.com)
  А также вот этой статьи https://www.tweaking4all.com/hardware/arduino/adruino-led-LEDS-effects/#cylon
  Доработан, переведён и разбит на файлы 2017 AlexGyver
  Смена выбранных режимов кнопкой. Кнопка подключена на D2 и GND
*/





#include <iarduino_Encoder_tmr.h>             //  Подключаем библиотеку iarduino_Encoder_tmr для работы с энкодерами через аппаратный таймер
iarduino_Encoder_tmr enc(A1,A4);              //  Объявляем объект enc для работы с энкодером указывая (№ вывода A, № вывода B)
#include <EEPROM.h>                                              //  Если при объявлении объектов перепутать выводы, то поворот влево будет расценен как поворот вправо и наоборот
#include "GyverButton.h"
GButton butt1(A5);                                  //  При использовании библиотеки iarduino_Encoder_tmr можно подключить до 8 энкодеров.


         // библиотека для работы с лентой

#define LED_COUNT 65          // число светодиодов в кольце/ленте
#define LED_DT 13             // пин, куда подключен DIN ленты

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
void setup()
{
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
  
  bright=EEPROM.read(1);
  counting=EEPROM.read(10);
  activity_move=EEPROM.read(15);

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
    int max_mode=12;
     bluetooth_();
     if(activity_move){move_sensor(); analogWrite(9,200); }
     else analogWrite(9,0);
     
    int a=enc.read();                         //  Читаем состояние энкодера в переменную a
    if (butt1.isDouble())activity_move=!activity_move;
    if(butt1.isClick()){
          if(counting>max_mode)counting=1;
          else counting++;
      Serial.println( counting);
    }
    if(a){               
        if(butt1.isHold()){
        if(a==encLEFT ){
          if(counting>1)counting--;
          else counting=max_mode;
          } 
        if(a==encRIGHT){
          if(counting>max_mode)counting=1;
          else counting++;
          }
           EEPROM.write(10,counting); 
           Serial.println(String(counting));
       change_mode(counting);   
       changeFlag = true;
        }
        else{
          if(a==encLEFT ){
          if(bright>1)bright-=25;
          else bright=0;
          } 
        if(a==encRIGHT){
          if(bright>=250)bright=250;
          else bright+=25;
          }
             Serial.println("bright   "+String(bright));
          EEPROM.write(1,bright); 
          LEDS.setBrightness(bright);
          new_bright=bright;
        }
         
    }
    
    

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
    case 3:fireLine(); break;
    case 4: new_rainbow_loop(); break;        // крутая плавная вращающаяся радуга // daq!!!
    case 5:fireLineNoise();break; 
     case 6: one_color_all(255, 0, 0); LEDS.show(); break; //---ALL RED
    case 7: one_color_all(0, 255, 0); LEDS.show(); break; //---ALL GREEN
    case 8: one_color_all(0, 0, 255); LEDS.show(); break; //---ALL BLUE
    case 9: one_color_all(255, 255, 0); LEDS.show(); break; //---ALL COLOR X
    case 10: one_color_all(0, 255, 255); LEDS.show(); break; //---ALL COLOR Y
    case 11: one_color_all(255, 0, 255); LEDS.show(); break; //---ALL COLOR Z
    case 12:  one_color_all(255, 91, 0); LEDS.show(); break; //---ALL RED
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
    }
  bouncedirection = 0;
  one_color_all(0, 0, 0);
//  ledMode = newmode;
}

void bluetooth_(){
  static unsigned long sleep_mode=0;
  int val;
 
  stay_ease(); 
  if (Serial.available())
  {
    val = Serial.read();
     unsigned int sleep_sec_time=0;
     if(sleep_mode!=0)sleep_sec_time=trunc((sleep_mode-millis())/60000);  
     else sleep_sec_time=0;
     
    if (val == 'l')new_bright=250;
    else if ( val == 'd')new_bright=0;
    else if(val == 'R' )change_mode_fast(6);
    else if(val == 'G' )change_mode_fast(7);
    else if(val == 'B' )change_mode_fast(8);
    else if(val == 'Y' )change_mode_fast(9);
    else if(val == 'S' )change_mode_fast(10);
    else if(val == 'P' )change_mode_fast(11);
    else if(val == 'O' )change_mode_fast(12);
    else if(val == 'q' )change_mode_fast(1);
    else if(val == 'w' )change_mode_fast(2);
    else if(val == 'e' )change_mode_fast(3);
    else if(val == 'r' )change_mode_fast(4);
    else if(val == 't' )change_mode_fast(5);
    else if(val == '0' )new_bright=25;
  else if(val == '1' )new_bright=50;
  else if(val == '2' )new_bright=75;
  else if(val == '3' )new_bright=100;
  else if(val == '4' )new_bright=125;
  else if(val == '5' )new_bright=150;
  else if(val == '6' )new_bright=175;
  else if(val == '7' )new_bright=200;
  else if(val == '8' )new_bright=225;
  else if(val == '9' )new_bright=250;
  else if(val == 'm' ){
      activity_move=!activity_move;
      EEPROM.write(15,activity_move); 
      if(activity_move)Serial.println("Move sensor active!");
      else Serial.println("Move sensor not active!");
    }
   else if(val=='h'){
      Serial.println(" TFK 2020 \n Lamp for sex functionality;)\n l -100% light \n d - 0% light");
      Serial.println(" R - red \n G - green \n B - blue \n Y - yellow \n S - sky \n P - pink \n O - orange ");
      Serial.println(" q - string rainbow \n w - flicker \n e - noice fire \n r - mild rainbow \n t - zone fire");
      Serial.println(" 0-9 level light (25-250) \n m - on/of move sensor \n s - sleep wait mode(+5 minute) \n h - help:D");
      Serial.println(" Motion sensor activity - " +String(digitalRead(11)) + " \n Motion sensor mode - " + String(activity_move));
      Serial.println(String(sleep_sec_time) +" m. to dark");
    unsigned int hours_= millis()/3600000;
    unsigned int minutes_= (millis()-hours_*3600000)/60000;
    unsigned int seconds_ = trunc((millis()- (hours_*3600000 + minutes_*60000))/1000);  
    Serial.println(String(hours_) + " h. " + String(minutes_) + " m. " + String(seconds_) + " s. - work time"  );
   }
   else if(val == 's' ){
    if(sleep_mode<millis())sleep_mode=millis()+300000;
    else sleep_mode+=300000;
    unsigned int sleep_sec_time=trunc((sleep_mode-millis())/60000);
    Serial.println(String(sleep_sec_time) +" m. to dark");
  }
  }
    long sleep_time_check=sleep_mode-millis()-100;
    if(sleep_time_check<0 && sleep_time_check>(-10)){
    new_bright=0;
    sleep_mode=0;
    Serial.println("Dark.Sweet Dream!");  
  }
  
}
void change_mode_fast(int arg){
  counting=arg;
  EEPROM.write(10,counting);         
  change_mode(counting);   
  changeFlag = true;
}
void stay_ease(){
  
  if(millis()%4==0){
  //Serial.println(String(bright) + "-n  " + String(new_bright));
  if(new_bright!=bright){
  if(new_bright<bright)bright--;
  else bright++;
  }
  }
LEDS.setBrightness(bright);  
}
void move_sensor(){
  static boolean old_move_sensor_activity;
  static unsigned long time_of_move;
  static int count_move;
  
  if(digitalRead(11))count_move++;
  else count_move=0;
  if(count_move>200){
    time_of_move=millis();
    new_bright=250;
  }
  if(!old_move_sensor_activity && digitalRead(11))Serial.print("The motion sensor has detected activity! \n");
  if(old_move_sensor_activity  && !digitalRead(11))Serial.println("activity disappeared \n");
  old_move_sensor_activity=digitalRead(11);
  if(millis()-time_of_move>60000)new_bright=0;
  //Serial.println(String(millis()-time_of_move) +"    "+ String(count_move) );
}
