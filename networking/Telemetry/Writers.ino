#include "Writers.h"

char *ftoa(char *a, double f, int precision) {
 long p[] = {0,10,100,1000,10000,100000,1000000,10000000,100000000};
 long heiltal = (long)f;
 itoa(heiltal, a, 10);
 while (*a != '\0')
   a++;
 *a++ = '.';
 long decimal = abs((long)((f - heiltal) * p[precision]));
 itoa(decimal, a, 10);
 while (*a != '\0')
  a++;
 return a;
}

// Define writers here.

void imu_acc_x(char *buf) {
  int i = sprintf(buf, "imu.a.x:");
  char *c = ftoa(buf + i, can.accelAngleX, 2);
  *c++ = '\n';
  *c = '\0';
}

void imu_acc_y(char *buf) {
  int i = sprintf(buf, "imu.a.x:");
  char *c = ftoa(buf + i, can.accelAngleY, 2);
  *c++ = '\n';
  *c = '\0';
}

#define ENTRY(tag, writer_func) (struct writer_entry) {tag, writer_func}

// Put each writer in this list with an appropriate tag.
// Tags must be short and cannot contain colons (":").
struct writer_entry writers[] = {
  ENTRY("imu.a.x", imu_acc_x),
  ENTRY("imu.a.y", imu_acc_y),
  ENTRY(0, 0) // must be (NULL, _)-terminated
};

#undef ENTRY

size_t writer_count;

void prepare_writers() {
  for (writer_count = 0; writers[writer_count].tag != 0; writer_count++)
    ;
}
