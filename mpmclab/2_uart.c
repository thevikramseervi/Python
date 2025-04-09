#include <lpc214x.h>

const char* msg = "HELLO WORLD\r";

int main(void) {
    PINSEL0 = 0x00000005;
    U0LCR = 0X00000083;
    U0DLM = 0X00;
    U0DLL = 0X13;
    U0LCR = 0X00000003;
    while (1) {
        while (*msg != 0x00) {
            while (!(U0LSR & 0X20));
            U0THR = *msg;
            msg++;
        }
    }
}
