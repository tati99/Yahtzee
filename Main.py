from Pontuacao import *
from Jogada import *

def exibe(d):
     for k in d:
        print(k,':', d[k])


def main(tabela):

     print('Teste - jogar_Dados()')
     d = [0,0,0,0,0]
     d = jogar_Dados(d)
     print(d)

     print('Teste - calcularOnes()')
     d = [1,2,4,5,1]
     r = calcularOnes(d)
     print(r)
     d = [2,2,4,5,6]
     r = calcularOnes(d)
     print(r)

     print('Teste - calcularTwos()')
     d = [2,2,4,5,2]
     r = calcularTwos(d)
     print(r)
     d = [3,3,4,5,6]
     r = calcularTwos(d)
     print(r)

     print('Teste - calcularThrees()')
     d = [1,2,3,5,3]
     r = calcularThrees(d)
     print(r)
     d = [2,2,4,5,6]
     r = calcularThrees(d)
     print(r)

     print('Teste - calcularFours()')
     d = [1,2,4,4,4]
     r = calcularFours(d)
     print(r)
     d = [2,2,5,5,6]
     r = calcularFours(d)
     print(r)

     print('Teste - calcularFives()')
     d = [5,2,4,5,1]
     r = calcularFives(d)
     print(r)
     d = [2,2,4,4,6]
     r = calcularFives(d)
     print(r)

     print('Teste - calcularSixes()')
     d = [1,2,4,5,6]
     r = calcularSixes(d)
     print(r)
     d = [2,2,4,5,1]
     r = calcularSixes(d)
     print(r)

     print('Teste - calcularThreeOfAKind()')
     d = [6,1,6,6,6]
     r = calcularThreeOfAKind(d)
     print(r)
     d = [6,6,2,2,1]
     r = calcularThreeOfAKind(d)
     print(r)

     print('Teste - calcularFourOfAKind()')
     d = [6,6,6,6,6]
     r = calcularFourOfAKind(d)
     print(r)
     d = [6,6,2,2,6]
     r = calcularFourOfAKind(d)
     print(r)

     print('Teste - calcularFullHouse()')
     d = [2,3,3,2,2]
     r = calcularFullHouse(d)
     print(r)
     d = [6,1,2,2,6]
     r = calcularFullHouse(d)
     print(r)

     print('Teste - calcularSmallStraight()')
     d = [1,2,3,2,4]
     r = calcularSmallStraight(d)
     print(r)
     d = [1,2,3,2,5]
     r = calcularSmallStraight(d)
     print(r)

     print('Teste - calcularLargeStraight()')
     d = [1,3,2,5,4]
     r = calcularLargeStraight(d)
     print(r)
     d = [3,1,5,4,6]
     r = calcularLargeStraight(d)
     print(r)

     print('Teste - calcularYahtzee()')
     d = [6,6,6,6,6]
     r = calcularYahtzee(d)
     print(r)
     d = [6,6,6,6,1]
     r = calcularYahtzee(d)
     print(r)

     print('Teste - calcularChance()')
     d = [6,2,3,6,5]
     r = calcularChance(d)
     print(r)
     
     print('Teste - calcularBonusYa()')
     d = [6,6,6,6,6]
     r = calcularBonusYa(d)
     print(r)
     d = [6,6,6,6,1]
     r = calcularBonusYa(d)
     print(r)

     print('Teste - calculaBonusSuperior()')
     tabela['ones'] = 0
     tabela['twos'] = 6
     tabela['threes'] = 12
     tabela['fours'] = 8
     tabela['fives'] = 20
     tabela['sixes'] = 18
     calculaBonusSuperior(tabela)
     print(tabela['bonus superior'])

     tabela['ones'] = 0
     tabela['twos'] = 6
     tabela['threes'] = 3
     tabela['fours'] = 8
     tabela['fives'] = 0
     tabela['sixes'] = 12
     calculaBonusSuperior(tabela)
     print(tabela['bonus superior'])

     print('Teste - somaColuna()')
     d = {
     'ones':4, 
     'twos':0,
     'threes':3,
     'fours':8,
     'fives':10,
     'sixes':18,
     'bonus superior':None,
     'three of a kind':14,
     'four of a kind':25,
     'full house':25,
     'small straight':30,
     'large straight':40,
     'chance':19,
     'yahtzee':50,
     'bonus yahtzee':100,
     'total':None
     }
     somaColuna(d)
     print(d['total'])

     print('Teste - mostrarOpcoes()')
     d = [0,0,0,0,0]
     d = jogar_Dados(d)
     dic = {
     'ones':1, 
     'twos':None,
     'threes':None,
     'fours':None,
     'fives':10,
     'sixes':None,
     'bonus superior':None,
     'three of a kind':14,
     'four of a kind':None,
     'full house':25,
     'small straight':None,
     'large straight':40,
     'chance':None,
     'yahtzee':None,
     'bonus yahtzee':None,
     'total':None
     }
     dic = mostrarOpcoes(d,dic)
     print(d)
     exibe(dic)

tabela = {
     'ones':None, 
     'twos':None,
     'threes':None,
     'fours':None,
     'fives':None,
     'sixes':None,
     'bonus superior':None,
     'three of a kind':None,
     'four of a kind':None,
     'full house':None,
     'small straight':None,
     'large straight':None,
     'chance':None,
     'yahtzee':None,
     'bonus yahtzee':None,
     'total':None
     }

main(tabela)

