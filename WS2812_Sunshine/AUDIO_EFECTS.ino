
byte LIGHT_COLOR = 0;             // начальный цвет подсветки
byte LIGHT_SAT = 255;             // начальная насыщенность подсветки
byte COLOR_SPEED = 100;
int RAINBOW_PERIOD = 1;
float RAINBOW_STEP_2 = 0.5;


void one_color_symmetric_top_beta(int count) {       //-SET ALL LEDS TO ONE COLOR
  static byte cobination =0;
  static int old_count = 0;
   if(count - old_count > 10){
  if(cobination >3)cobination=0;
  else cobination++;
  }
  old_count = count;
  for (int i = 0 ; i < LED_COUNT; i++ ) {
    if(i< LED_COUNT/2 + count && i> LED_COUNT/2 - count){
         switch(cobination){
    case 0:leds[i].setRGB(255,0,255); break;
    case 1:leds[i].setRGB(255,0,0); break;
    case 2:leds[i].setRGB(0,0,255); break;
    case 3:leds[i].setRGB(255,255,255); break;
    case 4:leds[i].setRGB(0,255,255); break;
  }
    }
    else leds[i].setRGB(0,0,0);
  }
  LEDS.show();      
}


void one_color_symmetric_top(int cred, int cgrn, int cblu,int count) {       //-SET ALL LEDS TO ONE COLOR
  
  for (int i = 0 ; i < LED_COUNT; i++ ) {
    if(i< LED_COUNT/2 + count && i> LED_COUNT/2 - count) leds[i].setRGB( cred, cgrn, cblu);
    else leds[i].setRGB(0,0,0);
  }
  LEDS.show();      
}


void rainbow_loop_amplitude(int count) {

  ihue -= 1;
  fill_rainbow( leds, LED_COUNT, ihue );
  for (int i=0; i <count ; i++) { leds[i].setRGB(0,0,0); }
  for (int i=LED_COUNT-count; i <= LED_COUNT ; i++){  leds[i].setRGB(0,0,0); }
 
  
  LEDS.show();
  if (safeDelay(thisdelay)) return;
}


void flicker_color(int level){

  static byte cobination =0 ;
  if(level<10){
  if(cobination >4)cobination=0;
  else cobination++;
  
  }
   
  int a = map(level*10,0,600,0,255);
    switch(cobination){
    case 0:one_color_all(a,0,a); break;
    case 1:one_color_all(a,0,0); break;
    case 2:one_color_all(0,0,a); break;
    case 3:one_color_all(a,a,a); break;
    case 4:one_color_all(0,a,a); break;
  }
  
  
  LEDS.show(); 
  
}


void one_color_symmetric_bottom(int cred, int cgrn, int cblu,int count) {       //-SET ALL LEDS TO ONE COLOR
  for (int i = 0 ; i < LED_COUNT; i++ ) {
    if(i< count || i> LED_COUNT - count)leds[i].setRGB( cred, cgrn, cblu);
    else leds[i].setRGB(0,0,0);
  }
  LEDS.show();
}
