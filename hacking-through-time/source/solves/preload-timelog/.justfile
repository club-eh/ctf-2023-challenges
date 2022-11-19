EXE := "../../out/hacking-through-time"
LIB_NAME := "libtimewarp"
LOGFILE := `mktemp`

run: build
	# run binary with LD_PRELOAD pointing to our custom library
	env LD_PRELOAD=./{{LIB_NAME}}.so {{EXE}} 2>{{LOGFILE}}

	# calcuate + display total sleep duration
	python analyze_time.py {{LOGFILE}}

	@# cleanup log file
	@rm {{LOGFILE}}

build:
	# build our custom library that overrides `nanosleep`
	gcc -Wall -Wextra -Wno-unused-parameter -fPIC -shared -o {{LIB_NAME}}.so {{LIB_NAME}}.c
