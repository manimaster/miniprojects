/*
 * Problem Statement: Create an embedded system to control home lights and fans remotely using an Arduino microcontroller.
 * Dependencies: Arduino IDE, Arduino board (e.g., Arduino Uno), Relays for controlling appliances, Android or web app for remote control
 */

// Include necessary libraries
#include <Arduino.h>

// Define the pins for controlling appliances
const int lightPin = 2; // Example: Connect light control to digital pin 2
const int fanPin = 3;   // Example: Connect fan control to digital pin 3

// Initialize variables to store appliance states
bool isLightOn = false;
bool isFanOn = false;

void setup() {
  // Set the appliance control pins as OUTPUT
  pinMode(lightPin, OUTPUT);
  pinMode(fanPin, OUTPUT);

  // Initialize the appliances to an OFF state
  digitalWrite(lightPin, LOW);
  digitalWrite(fanPin, LOW);

  // Initialize serial communication for debugging
  Serial.begin(9600);
}

void loop() {
  // Check for incoming commands from remote control (e.g., Android app)
  // You'll need to implement a communication protocol for this part
  
  // For simplicity, we'll use Serial communication for simulation purposes
  if (Serial.available() > 0) {
    char command = Serial.read();
    processCommand(command);
  }
}

// Function to process incoming commands
void processCommand(char command) {
  switch (command) {
    case 'L': // Turn on/off the light
      isLightOn = !isLightOn;
      digitalWrite(lightPin, isLightOn ? HIGH : LOW);
      Serial.println(isLightOn ? "Light is ON" : "Light is OFF");
      break;
      
    case 'F': // Turn on/off the fan
      isFanOn = !isFanOn;
      digitalWrite(fanPin, isFanOn ? HIGH : LOW);
      Serial.println(isFanOn ? "Fan is ON" : "Fan is OFF");
      break;
      
    default:
      Serial.println("Invalid command");
      break;
  }
}
