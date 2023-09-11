#include <stdio.h>
#include <string.h>

// Function to convert decimal to hexadecimal
void decimalToHexadecimal(int decimal) {
    printf("Decimal to Hexadecimal: %d -> 0x%X\n", decimal, decimal);
}

// Function to convert hexadecimal to decimal
void hexadecimalToDecimal(char *hexadecimal) {
    int decimal;
    sscanf(hexadecimal, "%x", &decimal);
    printf("Hexadecimal to Decimal: 0x%s -> %d\n", hexadecimal, decimal);
}

// Function to convert decimal to octal
void decimalToOctal(int decimal) {
    printf("Decimal to Octal: %d -> %o\n", decimal, decimal);
}

// Function to convert octal to decimal
void octalToDecimal(char *octal) {
    int decimal;
    sscanf(octal, "%o", &decimal);
    printf("Octal to Decimal: 0%s -> %d\n", octal, decimal);
}

// Function to convert decimal to binary
void decimalToBinary(int decimal) {
    int binary[32];
    int i = 0;

    while (decimal > 0) {
        binary[i] = decimal % 2;
        decimal /= 2;
        i++;
    }

    printf("Decimal to Binary: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
    printf("\n");
}

// Function to convert hexadecimal or octal to binary
void baseToBinary(char *base, int isHex) {
    int decimal;
    if (isHex) {
        sscanf(base, "%x", &decimal);
    } else {
        sscanf(base, "%o", &decimal);
    }

    decimalToBinary(decimal);
}

// Function to convert binary to decimal
void binaryToDecimal(char *binary) {
    int decimal = 0;
    int length = strlen(binary);

    for (int i = 0; i < length; i++) {
        if (binary[i] == '1') {
            decimal += 1 << (length - i - 1);
        }
    }

    printf("Binary to Decimal: %s -> %d\n", binary, decimal);
}

int main() {
    int decimal;
    char hexadecimal[20];
    char octal[20];
    char binary[20];

    // Example conversions
    decimal = 255;
    decimalToHexadecimal(decimal);
    hexadecimalToDecimal("FF");

    decimal = 63;
    decimalToOctal(decimal);
    octalToDecimal("77");

    decimal = 42;
    decimalToBinary(decimal);
    binaryToDecimal("101010");

    // Convert hexadecimal to binary
    baseToBinary("1A", 1); // Hexadecimal
    baseToBinary("52", 0); // Octal

    return 0;
}
