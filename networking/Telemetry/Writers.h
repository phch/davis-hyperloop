#ifndef WRITERS_H
#define WRITERS_H

typedef void (*writer_func)(char *buf);

struct writer_entry {
  const char *tag;
  writer_func writer;
};

// Declare writers here.
// Writers are functions that take a buffer (char *) and write some data to it.

void velocity(char *);

struct writer_entry;
extern struct writer_entry writers[];
extern size_t writer_count;
void prepare_writers(); // must be called before using any writers

#endif
