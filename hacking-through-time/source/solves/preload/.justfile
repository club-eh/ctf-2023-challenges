EXE := "../../out/hacking-through-time"
LIB_NAME := "libtimewarp"

run: build
	# run the binary with LD_PRELOAD pointing to our custom library
	env LD_PRELOAD=./{{LIB_NAME}}.so {{EXE}}

build:
	# build our custom library that overrides `nanosleep`
	gcc -Wall -Wextra -Wno-unused-parameter -fPIC -shared -o {{LIB_NAME}}.so {{LIB_NAME}}.c
