UI = $(wildcard *.ui)
PY = $(patsubst %.ui,%.py,$(UI))

all: $(PY)
	./makeinit.sh $^

%.py: %.ui
	pyuic4 $< >$@

.PHONY: all
