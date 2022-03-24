raidix-task:
	g++ -o raidix-task raidix-task.cpp

clean:
	rm raidix-task

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 raidix-task $(DESTDIR)/usr/bin/raidix-task
