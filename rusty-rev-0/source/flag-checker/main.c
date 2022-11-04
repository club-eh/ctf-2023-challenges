#include <stdio.h>

#include "libverify.h"


int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf("usage: %s FLAG\n", argv[0]);
		return 2;
	}

	if (verify_flag(argv[1])) {
		printf("Flag is correct\n");
		return 0;
	} else {
		printf("Flag is incorrect\n");
		return 1;
	};
}
