#include "info.h"

int VEC_DATA_BUS = 0;
int GEN_COUNTER = 0;
int MAGIC = 212;
int VEC_DATA_BUS2 = 1;
int VEC_LOGCAT = 0;
char VEC_DESC[100] = "Vector Boost module";

void set_VEC_DATA_BUS(int value) {
    VEC_DATA_BUS = value;
}

int get_VEC_DATA_BUS(void) {
    return VEC_DATA_BUS;
}

void set_GEN_COUNTER(int value) {
    GEN_COUNTER = value;
}

int get_GEN_COUNTER(void) {
    return GEN_COUNTER;
}

void set_MAGIC(int value) {
    MAGIC = value;
}

int get_MAGIC(void) {
    return MAGIC;
}

void set_VEC_DATA_BUS2(int value) {
    VEC_DATA_BUS2 = value;
}

int get_VEC_DATA_BUS2(void) {
    return VEC_DATA_BUS2;
}

void set_VEC_LOGCAT(int value) {
    VEC_LOGCAT = value;
}

int get_VEC_LOGCAT(void) {
    return VEC_LOGCAT;
}

void set_VEC_DESC(const char *value) {
    strncpy(VEC_DESC, value, sizeof(VEC_DESC) - 1);
    VEC_DESC[sizeof(VEC_DESC) - 1] = '\0'; // Ensure null termination
}

const char* get_VEC_DESC(void) {
    return VEC_DESC;
}
