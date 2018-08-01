
################# variabili personalizzabili ####################
# Timeout applicato a CIASCUN test eseguito
TIMEOUT=10
# Timeout totale applicato sul calcolo del tempo di esecuzione
MAXTIMEOUT=100

# Homework ed esercizio in ballo
HW=01
EX=02

################### environment #################################
SHELL:=/bin/bash
PATH:=/opt/anaconda3/bin:$(PATH)

################### commands ####################################
RADON=radon cc -a -s --show-closures

COG=python lib/cc.py

GRADE=pytest -v --timeout=$(TIMEOUT) --json program$(EX).log.json grade$(EX).py

# python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade01' 'grade01.runtests(grade01.tests)'
# -u unbuffered I/O	-m module	-n numrun	-r numrepeat	-s startstatement	
TIMEIT=python -u -m timeit -c -v -v -v -v -n 10 -r 10 -s 'import grade$(EX)' 'grade$(EX).main()'

#  ulimit
#	-d        the maximum size of a process's data segment
#	-f        the maximum size of files written by the shell and its children
#	-m        the maximum resident set size
#	-t        the maximum amount of cpu time in seconds
#	-v        the size of virtual memory
ULIMIT=ulimit -m 100000 -v 10000000 -f 10000

################### files to produce #############################
PROGRAMS=$(wildcard students/*/homework$(HW)/program$(EX).py)
STUDENTS=$(wildcard students/*/homework$(HW))
TESTS:=$(PROGRAMS:.py=.log)
CYCLOMATIC:=$(PROGRAMS:.py=.cyc)
TIME:=$(PROGRAMS:.py=.tim)
COGNITIVE:=$(PROGRAMS:.py=.cog)
MASTER:=$(wildcard master/*)
FILES:=$(notdir $(MASTER))

##################################################################
all: link cleanlog cyclomatic cognitive tests time

cyclomatic:	echo_cyc $(CYCLOMATIC)
cognitive:	echo_cog $(COGNITIVE)
tests:		$(TESTS)
time:		$(TIME)

echo_cyc:
	@echo
	@echo "Cyclomatic complexity:"
echo_cog:
	@echo
	@echo "Cognitive complexity:"

ro:
	@echo "Master files changed to read-only"
	@chmod -R a+r-w+X master/*

link: ro
	@echo "Linking Master files: "
	-@for d in $(STUDENTS) ; do \
		(pushd $$d ; ln -s ../../../master/* . ; popd) &> /dev/null ; \
		echo -n '.' ; \
	done

cleanlog:
	@rm -f *.err

dos2unix:
	dos2unix students/*/homework$(HW)/program*.py

results:
	@echo "Student	Intricacy"
	@grep '\-' $(CYCLOMATIC)
	@echo "Student	Readability"
	@grep ':' $(COGNITIVE)
	@echo "Student	Time"
	@grep best $(TIME)
	@echo "Student	Tests"
	@grep 'passed.*seconds' $(TESTS)

#################### RULES ########################################

%.cyc: %.py
	-@if ($(RADON) $< &> $@ ; $(RADON) -j $< &> $@.json) ; then echo -n '.' ; else echo -n '!' ; echo $@ >> cyclomatic.err ; fi
	
%.cog: %.py
	-@if ($(COG) $< $(@D)/$(*F).cog.json &> $@) ; then echo -n '.' ; else echo -n '!' ; echo $@ >> cognitive.err ; fi

# il timeout è gestito dal test/grader
%/program$(EX).log: %/program$(EX).py # link 
	@echo "Testing $<"
	-@cd $(@D) ; $(ULIMIT) ; $(GRADE) &> $(@F)

# i tempi vengono misurati solo se si sono superati tutti i test
%/program$(EX).tim: %/program$(EX).py # link
	@echo "Timing $<"
	-@cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(MAXTIMEOUT) ; $(TIMEIT) &> $(@F) ; \
	fi

# TODO: raccogliere i valori in un unico JSON

clean: cleanlog
	-find students -not -name 'program*.py' -delete
master:
	echo "DONE"

commit: 
	git add .
	git commit -m "Q2A"
	git push

