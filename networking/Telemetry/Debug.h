#ifndef DEBUG_H
#define DEBUG_H

#ifndef NDEBUG
# define DEBUG_PRINT(msg) \
do { \
  Serial.print(__func__); \
  Serial.print(": "); \
  Serial.println(msg); \
} while (0)
#else
# define DEBUG_PRINT(msg) ((void)0)
#endif

#endif
