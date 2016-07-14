#ifndef DEBUG_H
#define DEBUG_H

void _debug(const char *fmt, ...);

#ifndef NDEBUG
# define debug(...) \
do { \
  Serial.print(__func__); \
  Serial.print(": "); \
  _debug(__VA_ARGS__); \
} while (0)
#else
# define debug(...) ((void)0)
#endif

#endif
