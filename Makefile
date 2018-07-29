
# variabili personalizzabili
#
TIMEOUT=60
# TODO: aggiungere esercizio (oppure tenere gli esercizi in directory separate

# environment
SHELL:=/bin/bash
PATH:=/opt/anaconda3/bin:$(PATH)

# commands
ULIMIT=ulimit -m 100000 -v 10000000 -f 10000
RADON=radon cc -a -s --show-closures
COG=python ../../../cc.py
GRADE=PYTHONPATH=. pytest -v --timeout=$(TIMEOUT) ../../../grade01.py
TIMEIT=PYTHONPATH=../../..:. python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade01' 'grade01.main()'

# -u unbuffered I/O	-m module	-n numrun	-r numrepeat	-s startstatement	

# files to produce
STUDENTS=$(wildcard students/*/*/program01.py)
TESTS:=$(STUDENTS:.py=.log)
CYCLOMATIC:=$(STUDENTS:.py=.cyc)
TIME:=$(STUDENTS:.py=.tim)
COGNITIVE:=$(STUDENTS:.py=.cog)

all: cyclomatic cognitive tests time

tests:		$(TESTS)
cyclomatic:	$(CYCLOMATIC)
cognitive:	$(COGNITIVE)
time:		$(TIME)

# TODO: cosa succede se fallisce? fa il popd o no? (oppure visto che è uno shell separato va bene?)

%/program01.log: %/program01.py grade01.py
	pushd $(dir $<) ; $(ULIMIT) -t $(TIMEOUT) ; $(GRADE) &> program01.log ; popd

%/program01.cyc: %/program01.py grade01.py
	pushd $(dir $<) ; $(RADON) program01.py &> program01.cyc ; popd
	
%/program01.cog: %/program01.py grade01.py
	pushd $(dir $<) ; $(COG) program01.py &> program01.cog ; popd

%/program01.tim: %/program01.py grade01.py
	pushd $(dir $<) ; $(ULIMIT)  -t $(TIMEOUT)0 ; $(TIMEIT) &> program01.tim ; popd

# TODO: raccogliere i valori in un unico JSON
# TODO: commit dei file su github così la prossima volta eseguiamo solo i nuovi e non tutti

clean:
	rm -rf students/*/*/*.{log,cyc,tim,cog,csv} students/*/*/__*

commit: 
	git add .
	git commit -m "Q2A"
	git push

# python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade01' 'grade01.runtests(grade01.tests)'
