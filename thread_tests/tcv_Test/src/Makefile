IDIR=../include
CC=gcc
CFLAGS=-I. -g

ODIR=../obj
LDIR=../lib

LIBS=-lcurses

_DEPS = threadtest.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS)) 

_OBJ = main.o threadtest.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))

$(ODIR)/%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

test: $(OBJ) 
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

clean:
	rm -rf $(ODIR)/*.o
	rm -f calc
