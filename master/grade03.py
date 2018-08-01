#! /usr/bin/env python3 -B

import copy
import unittest
import json
import program03 as program

class Test(unittest.TestCase):
    def dotest03A(self, key, text, expected_result):
        args = key, text
        orig = copy.deepcopy(args)
        ret  = program.codifica(*args)
        self.__check(ret,   expected_result, orig, 'return')
        return 1

    def dotest03B(self, key, text, expected_result):
        args = key, text
        orig = copy.deepcopy(args)
        ret  = program.decodifica(*args)
        self.__check(ret,   expected_result, orig, 'return')
        return 1

    def test_codifica_1(self):
        "chiave che contiene tutte le 26 lettere dell'alfabeto"
        key      = 'the quick brown fox jumps over the lazy dog'
        chiaro   = 'papaveri e papere'
        scuro    = 'rqrqzbhx b rqrbhb'
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_1(self):
        "chiave che contiene tutte le 26 lettere dell'alfabeto"
        key      = 'the quick brown fox jumps over the lazy dog'
        chiaro   = 'papaveri e papere'
        scuro    = 'rqrqzbhx b rqrbhb'
        return self.dotest03B(key, scuro, chiaro)


    def test_codifica_2(self):
        "chiave che NON contiene tutte le 26 lettere dell'alfabeto, il testo contiene solo lettere della chiave, la chiave sposta tutte le lettere (nessuna mappa su se stessa)"
        key      = 'abracadabra'
        chiaro   = 'abracadabra'
        scuro    = 'cdacbcrcdac'
        return self.dotest03A(key, chiaro, scuro)


    def test_decodifica_2(self):
        "chiave che NON contiene tutte le 26 lettere dell'alfabeto, il testo contiene solo lettere della chiave, la chiave sposta tutte le lettere (nessuna mappa su se stessa)"
        key      = 'abracadabra'
        chiaro   = 'abracadabra'
        scuro    = 'cdacbcrcdac'
        return self.dotest03B(key, scuro, chiaro)


    def test_codifica_3(self):
        "il testo da codificare contiene caratteri che non appartengono alla chiave, la lettera 'e' non viene modificata (mappa su se stessa)"
        key      = 'chiave crittografica'
        chiaro   = 'Ciao! ben tornato. Rivederti E’ un piacere'
        scuro    = 'Crhf! ben cfinhcf. Rraedeicr E’ un prhveie'
        return self.dotest03A(key, chiaro, scuro)



    def test_decodifica_3(self):
        "il testo da codificare contiene caratteri che non appartengono alla chiave"
        key      = 'chiave crittografica'
        chiaro   = 'Ciao! ben tornato. Rivederti E’ un piacere'
        scuro    = 'Crhf! ben cfinhcf. Rraedeicr E’ un prhveie'
        return self.dotest03B(key, scuro, chiaro)

    def test_codifica_4(self):
        "la chiave contiene l'alfabeto completo una sola volta, invertito, essendo un numero pari di lettere, nessuna mappa su se stessa"
        key    = 'zyxwvutsrqponmlkjihgfedcba'
        chiaro = 'la nebbia agli irti colli'
        scuro  = 'oz mvyyrz ztor rigr xloor'
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_4(self):
        "la chiave contiene l'alfabeto completo una sola volta, invertito, essendo un numero pari di lettere, nessuna mappa su se stessa"
        key    = 'zyxwvutsrqponmlkjihgfedcba'
        chiaro = 'la nebbia agli irti colli'
        scuro  = 'oz mvyyrz ztor rigr xloor'
        return self.dotest03B(key, scuro, chiaro)

    def test_codifica_5(self):
        "la chiave contiene l'alfabeto completo una sola volta"
        key    = 'abcdefghijklmnopqrstuvxywz'
        chiaro = 'papaveri e papere'
        scuro  = 'papaveri e papere'
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_5(self):
        "la chiave contiene l'alfabeto completo una sola volta"
        key    = 'abcdefghijklmnopqrstuvxywz'
        chiaro = 'papaveri e papere'
        scuro  = 'papaveri e papere'
        return self.dotest03B(key, scuro, chiaro)

    def test_codifica_6(self):
        "la chiave non contiene  lettere dell’alfabeto tra ‘a’ e ‘z’ "
        key    = "QUESTA E' UNA CODIFICA DEBOLE"
        chiaro = 'papaveri e papere'
        scuro  = 'papaveri e papere'
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_6(self):
        "la chiave non contiene  lettere dell’alfabeto tra ‘a’ e ‘z’ "
        key    = "QUESTA E' UNA CODIFICA DEBOLE"
        chiaro = 'papaveri e papere'
        scuro  = 'papaveri e papere'
        return self.dotest03B(key, scuro, chiaro)

    def test_codifica_7(self):
        "la chiave e il testo da codificare sono simili"
        key    = "Monti Spognardi e Sterbini"
        chiaro = 'Sterbini Spognardi e Monti'
        scuro  = 'Sianotet Sbrdepngt a Mreit'
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_7(self):
        "la chiave e il testo da codificare sono simili"
        key    = "Monti Spognardi e Sterbini"
        chiaro = 'Sterbini Spognardi e Monti'
        scuro  = 'Sianotet Sbrdepngt a Mreit'
        return self.dotest03B(key, scuro, chiaro)

    def test_codifica_8(self):
        "la chiave contiene solo vocali"
        key    = "Le aiuoLE"
        chiaro = 'verranno codificate solo le vocali'
        scuro  = 'varrennu cudificeta sulu la vuceli'
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_8(self):
        "la chiave contiene solo vocali"
        key    = "Le aiuoLE"
        chiaro = 'verranno codificate solo le vocali'
        scuro  = 'varrennu cudificeta sulu la vuceli'
        return self.dotest03B(key, scuro, chiaro)

    def test_codifica_9(self):
        "chiave che contiene tutte le 26 lettere dell'alfabeto ripetuta 100 volte"
        key    = 'the quick brown fox jumps over the lazy dog'*100
        chiaro = 'papaveri e papere'*100
        scuro  = 'rqrqzbhx b rqrbhb'*100
        return self.dotest03A(key, chiaro, scuro)

    def test_decodifica_9(self):
        "chiave che contiene tutte le 26 lettere dell'alfabeto ripetuta 100 volte"
        key    = 'the quick brown fox jumps over the lazy dog'*100
        chiaro = 'papaveri e papere'*100
        scuro  = 'rqrqzbhx b rqrbhb'*100
        return self.dotest03B(key, scuro, chiaro)

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

