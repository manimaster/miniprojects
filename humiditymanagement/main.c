// In this program:

// We define a SensorData structure to hold temperature and humidity readings.
// generateSensorData generates simulated sensor data (you can replace this with actual sensor readings).
// logSensorData logs the sensor data to a file along with a timestamp.
// The main loop continuously generates sensor data, logs it, and displays it on the console.
// This program simulates a simple temperature and humidity monitoring system. For a dissertation, you can extend this program to include real sensor interfaces, networking capabilities for data transmission, and more advanced features like data analysis and visualization.

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

// Sensor data structure
typedef struct {
    float temperature;
    float humidity;
} SensorData;

// Function to simulate sensor data
void generateSensorData(SensorData* data) {
    // Simulate temperature and humidity readings (replace with actual sensor readings)
    data->temperature = 25.0 + ((float)rand() / RAND_MAX) * 10.0; // Random temperature between 25°C and 35°C
    data->humidity = 40.0 + ((float)rand() / RAND_MAX) * 20.0; // Random humidity between 40% and 60%
}

// Function to log sensor data to a file
void logSensorData(const SensorData* data) {
    // Get current timestamp
    time_t current_time;
    struct tm* time_info;
    char time_str[20];
    time(&current_time);
    time_info = localtime(&current_time);
    strftime(time_str, sizeof(time_str), "%Y-%m-%d %H:%M:%S", time_info);

    // Log data to a file (append mode)
    FILE* logFile = fopen("sensor_data.log", "a");
    if (logFile != NULL) {
        fprintf(logFile, "%s - Temperature: %.2f°C, Humidity: %.2f%%\n", time_str, data->temperature, data->humidity);
        fclose(logFile);
    }
}

int main() {
    printf("Temperature and Humidity Monitoring System\n");

    // Initialize random number generator
    srand(time(NULL));

    while (true) {
        SensorData data;

        // Generate simulated sensor data
        generateSensorData(&data);

        // Log sensor data to a file
        logSensorData(&data);

        // Display sensor data
        printf("Temperature: %.2f°C, Humidity: %.2f%%\n", data.temperature, data.humidity);

        // Delay for 5 seconds (adjust as needed for real-time sampling rate)
        usleep(5000000);  // 5 seconds
    }

    return 0;
}
