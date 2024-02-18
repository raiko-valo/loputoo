#include "JoyC.h"
#include "M5StickC.h"
#include <WiFi.h>
#include <WiFiClient.h>

JoyC joyc;
TFT_eSprite img = TFT_eSprite(&M5.Lcd);

uint8_t show_flag = 0;
String joystickValues; // Global variable to store joystick values

const char *ssid = "poco_wifi";
const char *password = "1122qqww";
const char *host = "192.168.55.1";
const int port = 12345;  // Replace with your server port

WiFiClient client;

String lastInput = "";

void setup() {
    M5.begin();
    Wire.begin(0, 26, 400000UL);
    img.createSprite(80, 160);

    Serial.begin(115200); // Initialize serial communication for debugging

    // Connect to Wi-Fi
    Serial.println("Connecting to Wi-Fi...");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("Connected to Wi-Fi!");

    // Set up the socket connection
    client.connect(host, port);
}

int lastLeftStickX = 0;
int lastLeftStickY = 0;
int lastrightStickY = 0;
int lastM5ButtonClick = 0;

void loop() {
    char text_buff[100];

    M5.update();
    img.fillSprite(TFT_BLACK);

    int leftStickX = joyc.GetX(0);
    int leftStickY = joyc.GetY(0);
    int rightStickY = joyc.GetY(1);
    int m5ButtonClick = 0;
    if (M5.BtnA.isPressed()) {
        m5ButtonClick = 1;
    }

    // Check if any of the joystick values have changed by 20 or more
    if (abs(leftStickX - lastLeftStickX) >= 10 || 
        abs(leftStickY - lastLeftStickY) >= 10 ||
        abs(rightStickY - lastrightStickY) >= 10 ||
        lastM5ButtonClick != m5ButtonClick) {

        // Update the global variable with joystick values
        joystickValues = "P1 " + String(leftStickX) + " " + String(leftStickY) + " " + String(rightStickY) + " " + String(m5ButtonClick) + ";";

        // Display left stick values
        img.drawCentreString("Left Stick", 40, 6, 1);
        sprintf(text_buff, "X: %d", leftStickX);
        img.drawCentreString(text_buff, 40, 20, 1);
        sprintf(text_buff, "Y: %d", leftStickY);
        img.drawCentreString(text_buff, 40, 34, 1);

        // Display right stick values
        img.drawCentreString("Right Stick", 40, 62, 1);
        sprintf(text_buff, "Y: %d", rightStickY);
        img.drawCentreString(text_buff, 40, 76, 1);
        sprintf(text_buff, "Button: %d", m5ButtonClick);
        img.drawCentreString(text_buff, 40, 90, 1);


        img.pushSprite(0, 0);

        if (M5.BtnA.wasPressed()) {
            joyc.SetLedColor(0x100010);
            show_flag = 1 - show_flag;
        }

        client.print(joystickValues);

        // Update the last joystick values
        lastLeftStickX = leftStickX;
        lastLeftStickY = leftStickY;
        lastrightStickY = rightStickY;
        lastM5ButtonClick = m5ButtonClick;
    }

    delay(10);
}