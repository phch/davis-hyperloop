#include "Writers.h"

// Define writers here.

void velocity(char *buf) {
  sprintf(buf, "v:5");
}

#define ENTRY(tag, writer_func) (struct writer_entry) {tag, writer_func}

// Put each writer in this list with an appropriate tag.
// Tags must be short and cannot contain colons (":").
struct writer_entry writers[] = {
  ENTRY("v", velocity),
  ENTRY(0, 0) // must be (NULL, _)-terminated
};

#undef ENTRY

size_t writer_count;

void prepare_writers() {
  for (writer_count = 0; writers[writer_count].tag != 0; writer_count++)
    ;
}
