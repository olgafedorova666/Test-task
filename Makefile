raidix-task:
        gcc -g -o raidix-task raidix-task.c

clean:
        rm raidix-task

install:
        mkdir -p $(DESTDIR)/usr/bin
        install -m 0755 raidix-task $(DESTDIR)/usr/bin/raidix-task