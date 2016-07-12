#ifndef READERS_H
#define READERS_H

typedef void (*reader_func)(const char *message, char *buf);

struct reader_entry {
  const char *tag;
  reader_func reader;
};

// Declare readers here.
// Readers are functions that take a message (const char *) and a buffer (char *),
// and write some data to the buffer.

extern struct reader_entry readers[];
extern size_t reader_count;
void prepare_readers(); // must be called before using any readers

#endif
