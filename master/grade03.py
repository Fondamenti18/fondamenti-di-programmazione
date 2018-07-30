import copy
import unittest
import os
import importlib
import json
import program03 as program

#program=None

class Test(unittest.TestCase):
    def dotest01(self, lista, num, expected_lista, expected_result):
        args = lista, num
        orig = copy.deepcopy(args)
        ret  = program.modi(*args)
        self.__check(ret,   expected_result, orig, 'return sbagliato')
        self.__check(lista, expected_lista,  orig, 'lista sbagliata')
        return 1

    def test_program01_3(self):
        "lista di valori piccoli max 3 cifre"
        lista           = [70,330,293,154,128,113,178]
        expected_lista  = [70, 154, 128]
        expected_result = [293, 113]
        num             = 6
        return self.dotest01(lista, num, expected_lista, expected_result)

    def test_program01_7(self):
        "lista di valori tutti di 7 cifre"
        lista           = [1234579,1234604,1234613,1234641,1234684,1234687,1234793,1234836,1234837,1234847]
        expected_lista  = [1234579,1234641,1234793,1234847 ]
        expected_result = [1234613,1234687,1234837]
        num             = 6
        return self.dotest01(lista, num, expected_lista, expected_result)
            
    def test_program01_9(self):
        "lista di valori di max 9 cifre"
        lista           = [858659,8640829,777923,178433279,148035889,3125]
        expected_lista  = [3125]
        expected_result = []
        num             = 4
        return self.dotest01(lista, num, expected_lista, expected_result)

    def test_program01_9_2(self):
        "lista di valori tutti da 9 cifre"
        lista           = [100000300, 100000431, 100000463, 100000647, 100000675, 100000687, 100001025, 100001111]
        expected_lista  = [100000431, 100000675, 100001111]
        expected_result = [100000463,100000687]
        num             = 10
        return self.dotest01(lista, num, expected_lista, expected_result)
    

    def test_program01_10(self):
        "lista di valori di max 10 cifre con divisori grandi"
        lista           = [340887623,26237927,2491,777923,5311430407,6437635961,82284023]
        expected_lista  = []
        expected_result = [26237927]
        num             = 4
        return self.dotest01(lista, num, expected_lista, expected_result)
    

    def test_program01_5(self):
        "lista di valori tutti di 5 cifre"
        lista           = [12347,12369,13125, 13127,13202,13750,13751,13838,14406,14407,14421,24010,24019,24035,26364]
        expected_lista  = [ 12369,  13202,  13838,  14421, 24035 ]
        expected_result = [ 12347,  13127,  13751 , 14407, 24019]
        num             = 14
        return self.dotest01(lista, num, expected_lista, expected_result)
            
    def test_program01_11(self):
        "lista di valori tutti di 11 cifre"
        lista           = [10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924]
        expected_lista  = [10000000116, 10000000548, 10000000768]
        expected_result = [10000000469,10000000711]
        num             = 16
        return self.dotest01(lista, num, expected_lista, expected_result)
   
    # TODO: define other checks (perhaps in a superclass?)

    def __check(self, value, expected, params=None, explanation=''):
        # TODO: add deepcopy of value to avoid side effects
        msg = ''
        if params:
            msg += '\twhen input={} '.format(params)
        msg += '\n\t\t%r != %r' % (value, expected)
        if explanation:
            msg += "\t<- correct %s value" % explanation
        self.assertEqual(value, expected, msg)

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    q2a=result.testsRun-len(result.failures)
    print('<q2a>'+json.dumps(q2a)+'</q2a>')   

if __name__ == "__main__":
    main()

    '''
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
    '''
