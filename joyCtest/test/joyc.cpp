#include "JoyC.h"
#include "M5StickC.h"

JoyC joyc;
TFT_eSprite img = TFT_eSprite(&M5.Lcd);

uint8_t show_flag = 0;
String joystickValues; // Global variable to store joystick values

const char *ssid = "CGVR Lab_5G";
const char *password = "CatmullRom66";
const char *host = "192.168.0.23";

void setup() {
    M5.begin();
    Wire.begin(0, 26, 400000UL);
    img.createSprite(80, 160);
}

void loop() {
    char text_buff[100];

    M5.update();
    img.fillSprite(TFT_BLACK);

    int leftStickX = joyc.GetX(0);
    int leftStickY = joyc.GetY(0);
    int rightStickX = joyc.GetX(1);
    int rightStickY = joyc.GetY(1);
    int m5ButtonClick = M5.Axp.GetBtnPress() ? 1 : 0;

    // Update the global variable with joystick values
    joystickValues = "P1 " + String(leftStickX) + " " + String(leftStickY) + " " + String(rightStickX) + " " + String(rightStickY) + " " + String(m5ButtonClick);

    // Display left stick values
    img.drawCentreString("Left Stick", 40, 6, 1);
    sprintf(text_buff, "X: %d", leftStickX);
    img.drawCentreString(text_buff, 40, 20, 1);
    sprintf(text_buff, "Y: %d", leftStickY);
    img.drawCentreString(text_buff, 40, 34, 1);

    // Display right stick values
    img.drawCentreString("Right Stick", 40, 62, 1);
    sprintf(text_buff, "X: %d", rightStickX);
    img.drawCentreString(text_buff, 40, 76, 1);
    sprintf(text_buff, "Y: %d", rightStickY);
    img.drawCentreString(text_buff, 40, 90, 1);

    img.pushSprite(0, 0);

    if (M5.BtnA.wasPressed()) {
        joyc.SetLedColor(0x100010);
        show_flag = 1 - show_flag;
    }

    // Access the joystick values through the 'joystickValues' variable
    Serial.println(joystickValues);

    delay(10);
}
