#include <stdio.h>
// Required for the struct timespec definition.
#include <time.h>

// Override `nanosleep` from libc
int nanosleep(const struct timespec *rqtp, struct timespec *rmtp) {
	// Log the requested sleep interval in nanoseconds to stderr.
	fprintf(stderr, "%lu ", rqtp->tv_sec * 1000000000 + rqtp->tv_nsec);

	// As `man 3p nanosleep` states (https://man.archlinux.org/man/nanosleep.3p.en#RETURN_VALUE):
	// > If the nanosleep() function returns because the requested time has elapsed, its return value shall be zero.
	return 0;
}
