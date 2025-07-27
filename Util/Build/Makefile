
.PHONY: all
all: test

programa: main.cpp
	g++ -O2 -std=c++17 -Wshadow -fsanitize=address,undefined -Wall -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-but-set-variable main.cpp -o programa

.PHONY: test
test: programa input.txt
	./programa < input.txt

.PHONY: clean
clean:
	rm -f programa
	if test -e main.cpp; then \
		mv main.cpp /tmp/"$(shell date +%N)"_main.cpp; \
	fi
	echo "" > input.txt
	cp template.cpp main.cpp

