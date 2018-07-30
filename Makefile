
################# variabili personalizzabili ####################
#
TIMEOUT=1
# TODO: aggiungere esercizio (oppure tenere gli esercizi in directory separate

################### environment #################################
SHELL:=/bin/bash
PATH:=/opt/anaconda3/bin:$(PATH)

################### commands ####################################
RADON=radon cc -a -s --show-closures
COG=python lib/cc.py
GRADE01=pytest -v --timeout=$(TIMEOUT) --json program01.json grade01.py
GRADE02=pytest -v --timeout=$(TIMEOUT) --json program02.json grade02.py
GRADE03=pytest -v --timeout=$(TIMEOUT) --json program03.json grade03.py
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
PROGRAMS=$(wildcard students/*/*/program0?.py)
STUDENTS=$(wildcard students/*/*)
TESTS:=$(PROGRAMS:.py=.log)
CYCLOMATIC:=$(PROGRAMS:.py=.cyc)
TIME:=$(PROGRAMS:.py=.tim)
COGNITIVE:=$(PROGRAMS:.py=.cog)
MASTER:=$(wildcard master/*)
FILES:=$(notdir $(MASTER))

##################################################################
all: link cyclomatic cognitive tests time

tests:		$(TESTS)
cyclomatic:	$(CYCLOMATIC)
cognitive:	$(COGNITIVE)
time:		$(TIME)

link:
	-for d in $(STUDENTS) ; do \
		pushd $$d ; \
		ln -s ../../../master/* . ; \
		popd ; \
	done

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
	-$(RADON) $< &> $@
	
%.cog: %.py
	-$(COG) $< &> $@

%/program01.log: %/program01.py %/grade01.py
	-cd $(@D) ; $(ULIMIT) ; $(GRADE01) &> $(@F)
%/program02.log: %/program02.py %/grade02.py
	-cd $(@D) ; $(ULIMIT) ; $(GRADE02) &> $(@F)
%/program03.log: %/program03.py %/grade03.py
	-cd $(@D) ; $(ULIMIT) ; $(GRADE03) &> $(@F)

%/program01.tim: %/program01.py %/grade01.py
	-cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(TIMEOUT)0 ; $(TIMEIT01) &> $(@F) ; \
	fi
%/program02.tim: %/program02.py %/grade02.py
	-cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(TIMEOUT)0 ; $(TIMEIT02) &> $(@F) ; \
	fi
%/program03.tim: %/program03.py %/grade03.py
	-cd $(@D) ; \
	if (grep -q FAILED $(basename $(@F)).log) ; then \
		echo "Not timed because some test did not PASS" > $(@F) ; \
	else \
		$(ULIMIT) -t $(TIMEOUT)0 ; $(TIMEIT03) &> $(@F) ; \
	fi

# TODO: raccogliere i valori in un unico JSON

clean:
	-find students -not -name 'program*.py' -delete

commit: 
	git add .
	git commit -m "Q2A"
	git push

