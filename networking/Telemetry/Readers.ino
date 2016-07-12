#include "Readers.h"

// Define readers here.

// TODO: readers for 

#define ENTRY(tag, reader_func) (struct reader_entry) {tag, reader_func}

// Put each reader in this list with an appropriate tag.
// Tags must be short and cannot contain colons (":").
struct reader_entry readers[] = {
  ENTRY(0, 0) // must be (NULL, _)-terminated
};

#undef ENTRY

size_t reader_count;

int compare_tag(const void *memb1, const void *memb2) {
  const char *tag1 = ((const struct reader_entry *)memb1)->tag;
  const char *tag2 = ((const struct reader_entry *)memb2)->tag;
  return strcmp(tag1, tag2);
}

int find_tag(const void *tag, const void *memb) {
  const char *search_tag = (const char *)tag;
  const char *memb_tag = ((const struct reader_entry *)memb)->tag;
  return strcmp(search_tag, memb_tag);
}

void prepare_readers() {
  for (reader_count = 0; readers[reader_count].tag != 0; reader_count++)
    ;
  qsort(readers, reader_count, sizeof(struct reader_entry), compare_tag);
}
