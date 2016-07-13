#include "Debug.h"

#define MAXBUF 20

void _debug(const char *fmt, ...) {
  char buf[MAXBUF + 1]; /* +1 for NUL */
  size_t bufend = 0;

#define FLUSH \
  do { \
    buf[bufend] = '\0'; \
    Serial.print(buf); \
    bufend = 0; \
  } while (0)

  va_list ap;
  va_start(ap, fmt);
  for (char c; (c = *fmt) != '\0'; fmt++)
    if (c == '%')
      switch (*++fmt) {
        case 'd':
          FLUSH;
          Serial.print(va_arg(ap, int));
          break;
        case 'u':
          FLUSH;
          Serial.print(va_arg(ap, unsigned int));
          break;
        case 's':
          FLUSH;
          Serial.print(va_arg(ap, char *));
          break;
        case '%':
          goto CHAR;
        default:
          ; /* unrecognized format character */
      }
    else {
CHAR:
      if (bufend == MAXBUF)
        FLUSH;
      buf[bufend++] = c;
    }
  va_end(ap);
  buf[bufend] = '\0';
  Serial.println(buf);

#undef FLUSH
}
