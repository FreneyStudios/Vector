#ifndef INFO_H
#define INFO_H

#define VEC_VER "0.1 Beta"
#define VEC_PDAT "06/09/24"
#define VEC_DAT "06/09/24"

extern int VEC_DATA_BUS;
extern int GEN_COUNTER;
extern int MAGIC;
extern int VEC_DATA_BUS2;
extern int VEC_LOGCAT;
extern char VEC_DESC[100];

void set_VEC_DATA_BUS(int value);
int get_VEC_DATA_BUS(void);

void set_GEN_COUNTER(int value);
int get_GEN_COUNTER(void);

void set_MAGIC(int value);
int get_MAGIC(void);

void set_VEC_DATA_BUS2(int value);
int get_VEC_DATA_BUS2(void);

void set_VEC_LOGCAT(int value);
int get_VEC_LOGCAT(void);

void set_VEC_DESC(const char *value);
const char* get_VEC_DESC(void);

#endif
