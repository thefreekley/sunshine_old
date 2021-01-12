




#include <iarduino_Encoder_tmr.h>            
           
#include <EEPROM.h>                                              
#include "GyverButton.h"
GButton butt1(A5);       

#include <HCSR04.h>
#define PIN_TRIG 10
#define PIN_ECHO 11
//HCSR04 ultrasonicSensor(PIN_TRIG, PIN_ECHO, 20, 300);
         // библиотека для работы с лентой


                                                                       // 
#include <iarduino_OLED_txt.h>                                         // Подключаем библиотеку iarduino_OLED_txt.
iarduino_OLED_txt myOLED(0x3C);   

#define LED_COUNT 120          // число светодиодов в кольце/ленте
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
int max_mode=12;
extern uint8_t MediumFont[];   
extern uint8_t SmallFont[];
void setup()
{
  
    
 pinMode(A0,INPUT);
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

                

  Serial.begin(9600);              // открыть порт для связи
  LEDS.setBrightness(bright);  // ограничить максимальную яркость
  Serial.println(counting);
  LEDS.addLeds<WS2811, LED_DT, GRB>(leds, LED_COUNT);  // настрйоки для нашей ленты (ленты на WS2811, WS2812, WS2812B)
  one_color_all(0, 0, 0);          // погасить все светодиоды
  LEDS.show();                     // отослать команду
  new_bright=bright;
  randomSeed(analogRead(0));

//  attachInterrupt(0, btnISR, FALLING);
 change_mode(counting);
   screen_info();
}

void one_color_all(int cred, int cgrn, int cblu) {       //-SET ALL LEDS TO ONE COLOR
  for (int i = 0 ; i < LED_COUNT; i++ ) {
    leds[i].setRGB( cred, cgrn, cblu);
  }
}





void frequency_color ( int combination ){
   switch(combination){
      case 1:
        for ( int i =0; i<LED_COUNT; i++){
          leds[i].setRGB( 255, 255, 255); 
        }
      break;
      case 2:
      for ( int i =0; i<LED_COUNT; i++){
          if ( i< LED_COUNT/2) leds[i].setRGB( 255, 255, 255); 
          else leds[i].setRGB( 0, 0, 0); 
        }
      break;
      
      case 3:
      for ( int i = 0 ; i<LED_COUNT; i++){
          if (i> LED_COUNT/2) leds[i].setRGB( 255, 255, 255);
          else leds[i].setRGB( 0, 0, 0); 
        }
      break;

      case 4:
      for ( int i =0; i<LED_COUNT; i++){
          leds[i].setRGB( 0, 0, 0); 
        }
      break;
  }
  LEDS.show();
}




boolean lightMode = false;
boolean themeMode = false;
boolean colorMode = false;
boolean musicLevel = false;
boolean FFTLevel = false;
boolean musicMode = false;

static int musicTheme = 4;

int colorPart[6];
int colorCount=0;

int color1 = 255;
int color2 = 0;
int color3 = 255;
int amplitudeLevel = 0;

int frequencyLevel[4] = {0,0,0,0};
int frequencyCount = 0;
void loop() {
   
      stay_ease();

      if(digitalRead(A0)){
        if(new_bright==0) new_bright=255;
        else new_bright = 0;
        screen_info();
        delay(1000);    
      }

     if (Serial.available() > 0) {  //если есть доступные данные
        
        char incomingByte = Serial.read();
        int number = incomingByte;
        
        if (number == 1) lightMode = true;
        else if (number == 2) themeMode = true;
        else if (number == 3) colorMode = true;
        else if (number == 4) musicLevel = true;
        else if (number == 5) FFTLevel = true;
        else if (number == 6) musicMode = true;
        else{
         if (FFTLevel){
            frequencyLevel[frequencyCount] = number - 10;
            frequencyCount++;
            if (frequencyCount>3){
              frequencyCount=0;
//              frequency_lever_color(frequencyLevel[0],frequencyLevel[1],frequencyLevel[2],frequencyLevel[4]);
            }
         }
         if(lightMode){
          
          new_bright = number;
          screen_info();
          new_bright = map(new_bright, 10, 127, 0, 255);
         LEDS.setBrightness(new_bright);
         }
         if( musicMode ){
          
          if(number>10 && number<15){
          musicTheme = number - 10;
           screen_info();
          
          one_color_all(0,0, 0); LEDS.show();
          }
         }
         if(musicLevel){
          amplitudeLevel = number-10;
          amplitudeLevel = constrain(amplitudeLevel,0,60);
          amplitudeLevel = map(amplitudeLevel, 0, 60, 0, LED_COUNT/2);
         }
         if(themeMode){
          change_mode_fast(number-10);
          screen_info();
         }
      
         if(colorMode){
       
          colorPart[colorCount] = number -10;
          colorCount++;
          if(colorCount>5){
          colorCount=0;
          }
         
         }

        musicMode = false;
        FFTLevel = false;
        lightMode = false;
        themeMode = false;
        colorMode = false;
        themeMode = false;
        }
    
    }
              
          color1 = colorPart[0]*10 + colorPart[1];
          color2 = colorPart[2]*10 + colorPart[3];
          color3 = colorPart[4]*10 + colorPart[5];
  
// one_color_symmetric_bottom(color1,color2, color3,amplitudeLevel);
//frequency_color(fftLevel);


//rainbow_loop_amplitude(amplitudeLevel);
    if (musicTheme==4){
  switch (counting) { //37 бильш нрав
    case 999: break;                           // пазуа
    case  1:new_rainbow_loop();; break;            // крутящаяся радуга // da
    case  2: fireLine(); break;                 // случайный стробоскоп
    case 3: fireLineNoise(); break;
    case 4: rainbow_loop();  break;        // крутая плавная вращающаяся радуга // daq!!!
    case 5: one_color_all(color1,color2, color3); LEDS.show(); break; 
    }
    }
    else{
    
      switch (musicTheme){
        case 1:one_color_symmetric_top(color1,color2, color3,amplitudeLevel); break; 
        case 2: one_color_symmetric_bottom(color1,color2, color3,amplitudeLevel); break;
        case 3: one_color_symmetric_top_beta(amplitudeLevel); break;
      }
    }
  
}

void screen_info(){
   myOLED.clrScr();  
   myOLED.setFont(MediumFont);
    myOLED.setCursor(16,4);   
   myOLED.print("SUNSHINE");
   
  myOLED.setFont(SmallFont);
    myOLED.setCursor(110,1);   
   myOLED.print(new_bright);
   
   if (musicTheme==4){
   myOLED.setCursor(0,1);   
   myOLED.print("Theme mode");
   myOLED.setCursor(0,6);   
   switch(counting){
    case 1:myOLED.print("Rainbow"); break;
    case 2:myOLED.print("Fire"); break;
    case 3:myOLED.print("Fireplase"); break;
    case 4:myOLED.print("Circular Rainbow"); break;
    case 5:myOLED.print("Color"); break;
   }
   }
   else{
   myOLED.setCursor(0,1);   
   myOLED.print("Music mode");
   myOLED.setCursor(0,6);
 
     switch(musicTheme){
    case 1:myOLED.print("Bottom"); break;
    case 2:myOLED.print("Top"); break;
    case 3:myOLED.print("By tone"); break;
        
   } 
   }
}

void change_mode(int newmode) {
  thissat = 255;
  switch (newmode) {
   case 1: thisdelay = 15; break;                      //---NEW RAINBOW LOOP
    //case 2: thishue = 160; thissat = 50; break;         //--- FLICKER
    case 4: thisdelay = 20; thisstep = 10; break;       //---RAINBOW LOOP

    case 5: one_color_all(color1, color2, color3); LEDS.show(); break; //---ALL RED
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
