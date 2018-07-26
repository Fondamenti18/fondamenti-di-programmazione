
import unittest
import os
import importlib
import json

program=None

class Test(unittest.TestCase):

    def test_program01_3(self):
        #lista di valori piccoli max 3 cifre
        lista=[70,330,293,154,128,113,178]
        orig= [] + lista
        ret= program.modi(lista,6)
        self.__check(ret,   [293, 113],   orig, 'return')
        self.__check(lista, [70,154,128], orig, 'ls')

    def test_program01_7(self):
        "lista di valori tutti di 7 cifre"
        lista=[1234579,1234604,1234613,1234641,1234684,1234687,1234793,1234836,1234837,1234847]
        orig= [] + lista
        ret= program.modi(lista,6)
        self.__check(ret,   [1234613,1234687,1234837],   orig, 'return')
        self.__check(lista, [1234579,1234641,1234793,1234847 ], orig, 'ls')
            
    def test_program01_9(self):
        "lista di valori di max 9 cifre"
        lista=[858659,8640829,777923,178433279,148035889,3125]
        orig= [] + lista
        ret= program.modi(lista,4)
        self.__check(ret,   [],     orig, 'return')
        self.__check(lista, [3125], orig, 'ls')

    def test_program01_9_2(self):
        "lista di valori tutti da 9 cifre"
        lista=[100000300, 100000431, 100000463, 100000647, 100000675, 100000687, 100001025, 100001111]
        orig= [] + lista
        ret= program.modi(lista,10)
        self.__check(ret,   [100000463,100000687],     orig, 'return')
        self.__check(lista, [100000431, 100000675, 100001111], orig, 'ls')
    

    def test_program01_10(self):
        "lista di valori di max 10 cifre con divisori grandi"
        lista=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]
        orig= [] + lista
        ret= program.modi(lista,4)
        self.__check(ret, [26237927], orig, 'return')
        self.__check(lista, [],       orig, 'ls')
    

    def test_program01_5(self):
        "lista di valori tutti di 5 cifre"
        lista=[12347,12369,13125, 13127,13202,13750,13751,13838,14406,14407,14421,24010,24019,24035,26364]
        orig= [] + lista
        ret= program.modi(lista,14)
        self.__check(ret, [ 12347,  13127,  13751 , 14407, 24019], orig, 'return')
        self.__check(lista, [ 12369,  13202,  13838,  14421, 24035 ],       orig, 'ls')
            
    def test_program01_11(self):
        "lista di valori tutti di 11 cifre"
        lista=[10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924]
        orig= [] + lista
        ret= program.modi(lista,16)
        self.__check(ret, [10000000469,10000000711], orig, 'return')
        self.__check(lista, [10000000116, 10000000548, 10000000768],       orig, 'ls')
    
    def __check(self, value, expected, params=None, explanation=''):
        # TODO: add deepcopy of value to avoid side effects
        msg = ''
        if params:
            msg += '\twhen input={}'.format(params)
        msg += '\n\t\t%r != %r' % (value, expected)
        if expl:
            msg += "\t<- correct %s value" % explanation
        self.assertEqual(value, expected, msg)
    
   
if __name__ == "__main__":
    
    f = open(os.devnull,"w", encoding="utf8")
    folder=r'grade01'
    q2a={}
    
    for student in os.listdir(folder):
        code=os.path.splitext(student)[0]

        if code.isalnum():
            filename=folder+'.'+code  
            program = importlib.import_module(filename)  
            suite = unittest.TestSuite()
            suite.addTest(unittest.makeSuite(Test))
            runner = unittest.TextTestRunner(verbosity=0,stream=f)
            result = runner.run(suite)
            q2a[code]=result.testsRun-len(result.failures)
     
    print('<q2a>'+json.dumps(q2a)+'</q2a>')   
