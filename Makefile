ILASM := ilasm
SOURCES := $(wildcard *.uk)
OUTPUTS := $(patsubst %.uk,%.exe,$(SOURCES))

.PHONY: all

all: $(OUTPUTS)

%.ukil: %.uk
	./ukelele $<

%.exe: %.ukil
	$(ILASM) /exe /output:$@ $<
	chmod +x $@
	
clean:
	$(RM) *.exe *.ukil

