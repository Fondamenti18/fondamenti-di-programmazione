

PATH:=/opt/anaconda3/bin:$(PATH)

TIMEOUT=60
ULIMIT=ulimit -t $(TIMEOUT) -m 100000 -v 10000000 -f 10000
RADON=radon cc -a -s --show-closures 

STUDENTS=$(wildcard students/*/*/program01.py)
TESTS:=$(STUDENTS:.py=.log)
CYCLOMATIC:=$(STUDENTS:.py=.cyc)
TIME:=$(STUDENTS:.py=.tim)
COGNITIVE:=$(STUDENTS:.py=.cog)

all: cyclomatic cognitive tests # time

tests:		$(TESTS)
cyclomatic:	$(CYCLOMATIC)
cognitive:	$(COGNITIVE)
time:		$(TIME)

# TODO: cosa succede se fallisce? fa il popd o no? (oppure visto che è uno shell separato va bene?)

%/program01.log: %/program01.py grade01.py
	pushd $(dir $<) ; $(ULIMIT) ; PYTHONPATH=. python ../../../grade01.py &> program01.log ; popd

%/program01.cyc: %/program01.py grade01.py
	pushd $(dir $<) ; $(RADON) program01.py > program01.cyc ; popd
	
%/program01.cog: %/program01.py grade01.py
	pushd $(dir $<) ; python ../../../cc.py program01.py > program01.cog ; popd

%/program01.tim: %/program01.py grade01.py
	pushd $(dir $<) ; $(ULIMIT) ; python -u -m timeit -c -v -v -v -v -r 10 ../../../grade01.py > program01.tim ; popd

# TODO: raccogliere i valori in un unico JSON

clean:
	rm -rf students/*/*/*.{log,cyc,tim,cog,csv} students/*/*/__*

commit: 
	git add .
	git commit -m "Q2A"
	git push

# python -u -m timeit -c -v -v -v -v -r 10 -s 'import grade01' 'grade01.runtests(grade01.tests)'
