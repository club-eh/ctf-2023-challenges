#include <stdio.h>

int bcmp(const void *s1, const void *s2, size_t n) {
	// print message with arguments
	printf("-- hooked bcmp('%.*s', '%.*s', %lu)\n", (int)n, (char *)s1, (int)n, (char *)s2, n);
	// dummy return value
	return 0;
}
