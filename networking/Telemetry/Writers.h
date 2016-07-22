#ifndef WRITERS_H
#define WRITERS_H

typedef void (*writer_func)(char *buf);

struct writer_entry {
  const char *tag;
  writer_func writer;
};

struct writer_entry;
extern struct writer_entry writers[];
extern size_t writer_count;
void prepare_writers(); // must be called before using any writers

#endif
