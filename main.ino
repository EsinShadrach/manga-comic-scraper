#include <Wire.h>
#include <RTC.h>
#include <U8g2lib.h>

U8G2_ST7920_128X64_F_SW_SPI u8g2(U8G2_R0, /* clock=*/ 13, /* data=*/ 11, /* CS=*/ 10, /* reset=*/ 8);
static DS1307 RTC;
void setup() {
   // put your setup code here, to run once:
   Serial.begin(9600);
   u8g2.begin();
   RTC.begin();
/*   Serial.println();
   RTC.begin();
   
      u8g2.clearBuffer();          // clear the internal memory
      
      String text = String(RTC.getYear(), DEC).substring(0,2);
      int text1 = int(text.toInt());
        uint8_t gYear = text1;
  char m_gYear[3];
  strcpy(m_gYear, u8x8_u8toa(gYear, 2));
  u8g2.setFont(u8g2_font_ncenB08_tr); // choose a suitable font
  u8g2.drawStr(0,10,m_gYear); // write something to the internal memory
  u8g2.sendBuffer();          // transfer internal memory to the display

  delay(100);  
   int x = 2022;
   int y = 2023;
//   stringOne =  String(45, HEX);

   Serial.println((String)bitRead(x,0) + (String)bitRead(x,1) + (String)bitRead(x,2) + (String)bitRead(x,3) + (String)bitRead(x,4) + (String)bitRead(x,5) + (String)bitRead(x,6) + (String)bitRead(x,7));
   Serial.println((String)bitRead(y,0) + (String)bitRead(y,1) + (String)bitRead(y,2) + (String)bitRead(y,3) + (String)bitRead(y,4) + (String)bitRead(y,5) + (String)bitRead(y,6) + (String)bitRead(y,7));
   Serial.println(String(2022, DEC));
   Serial.println(String(RTC.getYear(), DEC).substring(0,2));
   Serial.println(text1);*/
}


void loop() {
  // put your main code here, to run repeatedly:
    uint8_t gHours = RTC.getHours();
  char m_gHours[3];
  strcpy(m_gHours, u8x8_u8toa(gHours, 2));
  
  uint8_t gMinutes = RTC.getMinutes();
  char m_gMinutes[3];
  strcpy(m_gMinutes, u8x8_u8toa(gMinutes, 2));
 
  uint8_t gSeconds = RTC.getSeconds();
  char m_gSeconds[3];
  strcpy(m_gSeconds, u8x8_u8toa(gSeconds, 2));

    uint8_t gDay = RTC.getDay();
  char m_gDay[3];
  strcpy(m_gDay, u8x8_u8toa(gDay, 2));
  
  uint8_t gMonth = RTC.getMonth();
  char m_gMonth[3];
  strcpy(m_gMonth, u8x8_u8toa(gMonth, 2));

      String text = String(RTC.getYear()/*, DEC*/).substring(0,2);
      int text1 = /*int(*/text.toInt()/*)*/;
        uint8_t gYear = text1;
  char m_gYear[3];
  strcpy(m_gYear, u8x8_u8toa(gYear, 2));



        String text2 = String(RTC.getYear()/*, DEC*/).substring(2,4);
      int text3 = int(text2.toInt());
        uint8_t gYear1 = text3;
  char m_gYear1[3];
  strcpy(m_gYear1, u8x8_u8toa(gYear1, 2));
  
  u8g2.clearBuffer();          // clear the internal memory
  //if(RTC.isRunning()) {
    u8g2.setFont(/*u8g2_font_crox4hb_tr u8g2_font_balthasar_titling_nbp_tr u8g2_font_helvB14_tn u8g2_font_courB18_tf u8g2_font_luBS19_tn u8g2_font_logisoso20_tn u8g2_font_fub30_tf*/ u8g2_font_logisoso32_tn ); // choose a suitable font
    //Run1 = false;
    u8g2.drawStr(0,32,m_gHours); // write something to the internal memory
    u8g2.drawStr(45,32,m_gMinutes); // write something to the internal memory
    u8g2.drawStr(89,32,m_gSeconds); // write something to the internal memory
    u8g2.setFont( u8g2_font_8x13B_mr);
    u8g2.drawStr(0,43,m_gDay); // write something to the internal memory
    u8g2.drawStr(23,43,m_gMonth); // write something to the internal memory
    u8g2.drawStr(45,43, m_gYear); // write something to the internal memory
    u8g2.drawStr(45+16,43, m_gYear1); // write something to the internal memory

   /* if (RTC.getMonth() == 1) {
      u8g2.drawStr(60,43, "January");
    } if (RTC.getMonth() == 2) {
      u8g2.drawStr(60,43, "February");
    } if (RTC.getMonth() == 3) {
      u8g2.drawStr(60,43, "March");
    } if (RTC.getMonth() == 4) {
      u8g2.drawStr(60,43, "April");
    } if (RTC.getMonth() == 5) {
      u8g2.drawStr(60,43, "May");
    } if (RTC.getMonth() == 6) {
      u8g2.drawStr(60,43, "June");
    } if (RTC.getMonth() == 7) {
      u8g2.drawStr(60,43, "July");
    } if (RTC.getMonth() == 8) {
      u8g2.drawStr(60,43, "August");
    } if (RTC.getMonth() == 9) {
      u8g2.drawStr(60,43, "September");
    } if (RTC.getMonth() == 10) {
      u8g2.drawStr(60,43, "October");
    } if (RTC.getMonth() == 11) {
      u8g2.drawStr(60,43, "November");
    } if (RTC.getMonth() == 12) {
      u8g2.drawStr(60,43, "December");
    }*/
    

      switch(RTC.getMonth()) {
      case 1:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Jan");
        break;
      case 2:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Feb");
        break;
      case 3:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Mar");
        break;
      case 4:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Apr");
        break;
      case 5:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"May");
        break;
      case 6:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Jun");
        break;
      case 7:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Jul");
        break;
      case 8:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Aug");
        break;
      case 9:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Sep");
        break;
      case 10:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Oct");
        break;
      case 11:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Nov");
        break;
      case 12:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(80,43,"Dec");
        break;
      default:
      u8g2.setFont( u8g2_font_8x13B_mr);
        u8g2.drawStr(79,43,"what?");
        break;
    }


    
    
/*  } else if(!Run && !Run1) {
    //Run = true;
    u8g2.setFont(u8g2_font_logisoso32_tr ); // choose a suitable font

    u8g2.drawStr(0,32,"WH"); // write something to the internal memory
    u8g2.drawStr(45,32,"AT"); // write something to the internal memory
    u8g2.drawStr(89,32,"?!"); // write something to the internal memory
  } else {
    u8g2.setFont(4u8g2_font_logisoso32_tr ); // choose a suitable font
    Run = false;
    Run1 = true;
    u8g2.drawStr(0,32,"OH"); // write something to the internal memory
    u8g2.drawStr(45,32,"NO"); // write something to the internal memory
    u8g2.drawStr(89,32,"!!"); // write something to the internal memory
  }*/
    u8g2.setFont(/*u8g2_font_helvB24_tf*/ u8g2_font_logisoso24_tr); // choose a suitable font
  u8g2.drawStr(38,28,":"); // write something to the internal memory
  u8g2.drawStr(82,28,":"); // write something to the internal memory



  
  u8g2.setFont( u8g2_font_8x13B_mr);
    switch(RTC.getWeek()) {
      case 1:
        u8g2.drawStr(0,54,"Sun");
        break;
      case 2:
        u8g2.drawStr(0,54,"Mon");
        break;
      case 3:
        u8g2.drawStr(0,54,"Tues");
        break;
      case 4:
        u8g2.drawStr(0,54,"Wedness");
        break;
      case 5:
        u8g2.drawStr(0,54,"Thrus");
        break;
      case 6:
        u8g2.drawStr(0,54,"Fri");
        break;
      case 7:
        u8g2.drawStr(0,54,"Satur");
        break;
      default:
        u8g2.drawStr(0,54,"what?");
        break;   
    }

    
        switch(RTC.getWeek()) {
      case 1:
        u8g2.drawStr(24,54,"day");
        break;
      case 2:
        u8g2.drawStr(24,54,"day");
        break;
      case 3:
        u8g2.drawStr(32,54,"day");
        break;
      case 4:
        u8g2.drawStr(56,54,"day");
        break;
      case 5:
        u8g2.drawStr(40,54,"day");
        break;
      case 6:
        u8g2.drawStr(24,54,"day");
        break;
      case 7:
        u8g2.drawStr(40,54,"day");
        break;
      default:
        //u8g2.drawStr(0,54,"what?");
        break;   
    }
    if(RTC.getWeek() < 8) {
      /*if (RTC.getWeek() == 1 or 2 or 6) {
        u8g2.drawStr(24,54,"day");
      }
      if (RTC.getWeek() == 5 or 7 and not 6) {
        u8g2.drawStr(40,54,"day");
      }
      if (RTC.getWeek() == 3) {
        u8g2.drawStr(32,54,"day");
      }
      if (RTC.getWeek() == 4) {
        u8g2.drawStr(56,54,"day");
      }*/
  }
/*  if(!RTC.isRunning() && !Fault) {
    u8g2.setFont(u8g2_font_7x14B_tf);
    u8g2.drawStr(0,55,"ERR:RTC INVAILD");
    u8g2.setFont(u8g2_font_squeezed_b6_tr);
    u8g2.drawStr(0,64,"Restarting RTC...");
    Fault = true;
    RTC.startClock();
  } else if(!RTC.isRunning()) {
    u8g2.setFont(u8g2_font_7x14B_tf);
    u8g2.drawStr(0,55,"ERR:RTC CANT START");
    u8g2.setFont(u8g2_font_squeezed_b6_tr);
    u8g2.drawStr(0,64,"Unable to start RTC");
  } else {
    Fault = false;
  }
  /*u8g2.setFont(u8g2_font_open_iconic_www_2x_t);
  u8g2.drawStr(82,60,"A"); // write something to the internal memory*/
  u8g2.sendBuffer();          // transfer internal memory to the display
  delay(1000);  

}