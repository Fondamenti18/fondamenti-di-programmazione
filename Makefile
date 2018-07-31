
################# variabili personalizzabili ####################
# Timeout applicato a CIASCUN test eseguito
TIMEOUT01=10
TIMEOUT02=10
TIMEOUT03=10

# Homework in ballo
HW=01

################### environment #################################
SHELL:=/bin/bash
PATH:=/opt/anaconda3/bin:$(PATH)

################### commands ####################################
RADON=radon cc -a -s --show-closures

COG=python lib/cc.py

GRADE01=pytest -v --timeout=$(TIMEOUT01) --json program01.log.json grade01.py
GRADE02=pytest -v --timeout=$(TIMEOUT02) --json program02.log.json grade02.py
GRADE03=pytest -v --timeout=$(TIMEOUT03) --json program03.log.json grade03.py

# python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade01' 'grade01.runtests(grade01.tests)'
# -u unbuffered I/O	-m module	-n numrun	-r numrepeat	-s startstatement	
TIMEIT01=python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade01' 'grade01.main()'
TIMEIT02=python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade02' 'grade02.main()'
TIMEIT03=python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade03' 'grade03.main()'

#  ulimit
#	-d        the maximum size of a process's data segment
#	-f        the maximum size of files written by the shell and its children
#	-m        the maximum resident set size
#	-t        the maximum amount of cpu time in seconds
#	-v        the size of virtual memory
ULIMIT=ulimit -m 100000 -v 10000000 -f 10000

################### files to produce #############################
PROGRAMS=$(wildcard students/*/homework$(HW)/program0?.py)
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
%/program01.log: %/program01.py %/grade01.py link 
	@echo "Testing $<"
	-@cd $(@D) ; $(ULIMIT) ; $(GRADE01) &> $(@F)
%/program02.log: %/program02.py %/grade02.py link
	@echo "Testing $<"
	-@cd $(@D) ; $(ULIMIT) ; $(GRADE02) &> $(@F)
%/program03.log: %/program03.py %/grade03.py link
	@echo "Testing $<"
	-@cd $(@D) ; $(ULIMIT) ; $(GRADE03) &> $(@F)

# i tempi vengono misurati solo se si passano tutti i test
# il timeout globale è 100 volte quello del singolo test
%/program01.tim: %/program01.py %/grade01.py
	@echo "Timing $<"
	-@cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(TIMEOUT01)00 ; $(TIMEIT01) &> $(@F) ; \
	fi
%/program02.tim: %/program02.py %/grade02.py
	@echo "Timing $<"
	-@cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(TIMEOUT02)00 ; $(TIMEIT02) &> $(@F) ; \
	fi
%/program03.tim: %/program03.py %/grade03.py
	@echo "Timing $<"
	-@cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(TIMEOUT03)00 ; $(TIMEIT03) &> $(@F) ; \
	fi

# TODO: raccogliere i valori in un unico JSON

clean:
	-find students -not -name 'program*.py' -delete

commit: 
	git add .
	git commit -m "Q2A"
	git push

