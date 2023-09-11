// In this program:

// Constants like MAX_SPEED, ACCELERATION, and DECELERATION represent system parameters.
// setDesiredSpeed sets the desired speed for cruise control.
// enableCruiseControl and disableCruiseControl control the cruise control system's state.
// adjustSpeed is used to adjust the vehicle's speed while cruise control is active.

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

// Constants
#define MAX_SPEED 120
#define ACCELERATION 5
#define DECELERATION 5

// Global variables
int currentSpeed = 0;
bool cruiseControlEnabled = false;

// Function to set the desired speed for cruise control
void setDesiredSpeed(int speed) {
    if (speed <= MAX_SPEED) {
        currentSpeed = speed;
        printf("Cruise control speed set to %d mph.\n", currentSpeed);
    } else {
        printf("Invalid speed setting. Maximum speed is %d mph.\n", MAX_SPEED);
    }
}

// Function to enable cruise control
void enableCruiseControl() {
    cruiseControlEnabled = true;
    printf("Cruise control enabled.\n");
}

// Function to disable cruise control
void disableCruiseControl() {
    cruiseControlEnabled = false;
    printf("Cruise control disabled.\n");
}

// Function to adjust speed while cruise control is active
void adjustSpeed(bool accelerate) {
    if (cruiseControlEnabled) {
        if (accelerate) {
            currentSpeed += ACCELERATION;
            if (currentSpeed > MAX_SPEED) {
                currentSpeed = MAX_SPEED;
            }
            printf("Speed increased to %d mph.\n", currentSpeed);
        } else {
            currentSpeed -= DECELERATION;
            if (currentSpeed < 0) {
                currentSpeed = 0;
            }
            printf("Speed decreased to %d mph.\n", currentSpeed);
        }
    } else {
        printf("Cruise control is not enabled.\n");
    }
}

int main() {
    printf("Cruise Control System\n");

    // Enable cruise control
    enableCruiseControl();

    // Set the desired speed for cruise control
    setDesiredSpeed(80);

    // Simulate accelerating
    adjustSpeed(true);

    // Simulate decelerating
    adjustSpeed(false);

    // Disable cruise control
    disableCruiseControl();

    return 0;
}
