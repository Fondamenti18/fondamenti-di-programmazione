
################# variabili personalizzabili ####################
# Timeout applicato a CIASCUN test eseguito
TIMEOUT=10
# Timeout totale applicato sul calcolo del tempo di esecuzione
MAXTIMEOUT=100

# Homework ed esercizio in ballo
HW=01
EX=02
STUDENT=*
STUDENT=A*

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
PROGRAMS=$(wildcard students/$(STUDENT)/homework$(HW)/program$(EX).py)
STUDENTS=$(notdir $(wildcard students/$(STUDENT)))
HOMEWORKS=$(wildcard students/$(STUDENT)/homework$(HW))
TESTS:=$(PROGRAMS:.py=.log)
CYCLOMATIC:=$(PROGRAMS:.py=.cyc)
TIME:=$(PROGRAMS:.py=.tim)
COGNITIVE:=$(PROGRAMS:.py=.cog)
COMPILE:=$(PROGRAMS:.py=.compila)
MASTER:=$(wildcard master/*)
FILES:=$(notdir $(MASTER))

##################################################################
all: link cleanlog dos2unix compile cyclomatic cognitive tests time

compile:	echo_comp $(COMPILE)
cyclomatic:	echo_cyc $(CYCLOMATIC)
cognitive:	echo_cog $(COGNITIVE)
tests:		$(TESTS)
time:		$(TIME)

echo_comp:
	@echo
	@echo "Syntax check:"
echo_cyc:
	@echo
	@echo "Cyclomatic complexity:"
echo_cog:
	@echo
	@echo "Cognitive complexity:"

ro:
	@echo "Master files changed to read-only"
	@chmod -R a+r-w+X master/*
	# TODO: mettere tutti i file RO e rendere RW SOLO la directory dello studente in ballo

link: ro
	@echo "Linking Master files: "
	-@for d in $(HOMEWORKS) ; do \
		(pushd $$d ; ln -s ../../../master/* . ; popd) &> /dev/null ; \
		echo -n '.' ; \
	done

dos2unix:
	dos2unix students/$(STUDENT)/homework$(HW)/program*.py # &> /dev/null

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

%.compila: %.py
	-@if (python -m py_compile $< &> $@) ; then echo -n '.' ; else mv $@ $(@D)/$(*F).noncompila ; echo -n '!' ; fi

%.cyc: %.py
	-@if ($(RADON) $< &> $@ ; $(RADON) -j $< &> $@.json) ; then echo -n '.' ; else echo -n '!' ; echo $@ >> cyclomatic.err ; fi
	
%.cog: %.py
	-@if ($(COG) $< $(@D)/$(*F).cog.json &> $@) ; then  \
		echo -n '.' ; \
	else \
		cat $< | sed -e 's/#.*//' -e 's/^\s\+$$//' | tr '\n' '\r' | sed -s 's/\r\+/\n/g' > $(@D)/$(*F).normalized ; \
		if ($(COG) $(@D)/$(*F).normalized $(@D)/$(*F).cog.json &> $@) ; then  \
			echo -n '.' ; \
		else \
			echo -n '!' ; echo $@ >> cognitive.err ; \
		fi \
	fi

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

# TODO: raccogliere i valori  dei risultati in un unico JSON PER STUDENTE

############################## CLEAN ####################################
clean: cleanlog cleanstudents cleantravis

cleanstudents:
	-find students -not -name 'program*.py' -delete
cleanlog:
	@rm -f *.err
cleantravis:
	@rm .travis.yml .travis.yml.students

###################### TRAVIS + COMMIT ##################################

master:
	echo "DONE"

commit: .travis.yml
	# TODO: switch al branch dello studente
	git add .
	git commit -m "Q2A"
	git push

.travis.yml.students: Makefile
	echo $(STUDENTS)
	echo > $@
	for s in $(STUDENTS) ; do \
		for e in 1 2 3 ; do \
			echo "        - STUDENT=$$s EX=$$e TIMEOUT=$(TIMEOUT) HOMEWORK=$(HW)" >> $@ ; \
		done ; \
	done

.travis.yml: .travis.yml.master .travis.yml.students 
	cat $^ > $@

##########################################################################
