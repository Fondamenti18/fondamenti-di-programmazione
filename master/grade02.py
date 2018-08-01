#! /usr/bin/env python3 -B

import copy
import unittest
import json
import program02 as program

class Test(unittest.TestCase):
    def dotest02(self, num, expected_result):
        args = num,
        orig = copy.deepcopy(args)
        ret  = program.conv(*args)
        self.__check(ret,   expected_result, orig, 'return')
        return 1


    def test_program_1(self):
        "numero semplice senza elisioni"
        num      = 3
        expected = 'tre'
        return self.dotest02(num, expected)

    def test_program_2(self):
        "numero speciale tra 10 e 20"
        num      = 17
        expected = 'diciassette'
        return self.dotest02(num, expected)


    def test_program_3(self):
        "non-elisione del cento e elisione del venti-otto"
        num      = 128
        expected = 'centoventotto'
        return self.dotest02(num, expected)

    def test_program_4(self):
        "non-elisione del cento"
        num      = 508
        expected = 'cinquecentootto'
        return self.dotest02(num, expected)

    def test_program_5(self):
        "non-elisione del mille e del cento"
        num      = 1501
        expected = 'millecinquecentouno'
        return self.dotest02(num, expected)

    def test_program_6(self):
        "non-elisione del mille e elisione di 80"
        num      = 17081
        expected = 'diciassettemilaottantuno'
        return self.dotest02(num, expected)

    def test_program_7(self):
        "numero grande con molte elisioni e non-elisioni"
        num      = 981008818
        expected = 'novecentottantunomilioniottomilaottocentodiciotto'
        return self.dotest02(num, expected)

    def test_program_8(self):
        "elisioni 800-80 e 80-8"
        num      = 888888888
        expected = 'ottocentottantottomilioniottocentottantottomilaottocentottantotto'
        return self.dotest02(num, expected)

    def test_program_9(self):
        'non elisioni 800-8 e elisioni 800-80'
        num      = 808080808080
        expected = 'ottocentoottomiliardiottantamilioniottocentoottomilaottanta'
        return self.dotest02(num, expected)

    def test_program_10(self):
        'non elisioni 800-1 e elisioni 80-1'
        num      = 801081801081
        expected = 'ottocentounomiliardiottantunomilioniottocentounomilaottantuno'
        return self.dotest02(num, expected)

    def test_program_11(self):
        'elisioni sessanta-otto, cinquanta-otto, quaranta-otto, trenta-otto'
        num      = 68258148238
        expected = 'sessantottomiliardiduecentocinquantottomilionicentoquarantottomiladuecentotrentotto'
        return self.dotest02(num, expected)

    def test_program_12(self):
        'elisioni ottanta-uno,settanta-uno,novanta-uno, venti-uno'
        num      = 81071091021
        expected = 'ottantunomiliardisettantunomilioninovantunomilaventuno'
        return self.dotest02(num, expected)

    def test_program_13(self):
        'numeri speciali tra 10 e 20'
        num      = 11012013014
        expected = 'undicimiliardidodicimilionitredicimilaquattordici'
        return self.dotest02(num, expected)

    def test_program_14(self):
        'numero massimo da convertire'
        num      = 99999999999
        expected = 'novantanovemiliardinovecentonovantanovemilioninovecentonovantanovemilanovecentonovantanove'
        return self.dotest02(num, expected)

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

