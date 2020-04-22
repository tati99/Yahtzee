__all__ = ['somaColuna','calcularOnes','calcularTwos','calcularThrees','calcularFours','calcularFives','calcularSixes','calcularSmallStraight','calcularLargeStraight',
	   'calcularThreeOfAKind','calcularFourOfAKind','calcularChance','calcularFullHouse','calcularYahtzee','calculaBonusSuperior','calcularBonusYa']

def somaColuna(d):
    d = calculaBonusSuperior(d)
    d = calculaBonusYa(d)
    aux = 0
    for k in d:
        aux += d[k]
    d['total'] = aux
    return d

def calcularOnes(l): 
    soma = 0
    for i in l:
        if i == 1:
            soma += 1
    return soma

def calcularTwos(l):
    soma = 0
    for i in l:
        if i == 2: 
            soma += 2
    return soma

def calcularThrees(l): 
    soma = 0
    for i in l:
        if i == 3:
            soma += 3
    return soma

def calcularFours(l): 
    soma = 0
    for i in l:
        if i == 4:
            soma += 4
    return soma

def calcularFives(l): 
    soma = 0
    for i in l:
        if i == 5:
            soma += 5
    return soma

def calcularSixes(l): 
    soma = 0
    for i in l:
        if i == 6:
            soma += 6
    return soma

def calcularSmallStraight(l):
    nl = []
    l.sort()
    nl = l.copy()
    ant = nl[0]
    for i in nl[1:]:
        if ant == i:
            nl.remove(i)
        else:
            ant = i
    if nl[0]!=1 and nl[0]!=2 and nl[0]!=3:
        return 0
    if nl[1]!=2 and nl[1]!=3 and nl[1]!=4:
        return 0
    if nl[2]!=3 and nl[2]!=4 and nl[2]!=5:
        return 0
    if nl[3]!=4 and nl[3]!=5 and nl[3]!=6:
        return 0
    return 30

def calcularYahtzee(l): 
    ant = l[0]
    for i in l[1:]:
        if ant != i:
            return 0
        ant = l[i]
    return 50

def calcularThreeOfAKind(lista_dados):
    for element in lista_dados:
        if (lista_dados.count(element)) == 3:
            return sum(lista_dados)
        else:
            return 0

def calcularFourOfAKind(lista_dados):
    for element in lista_dados:
        if (lista_dados.count(element)) == 4:
            return sum(lista_dados)
        else:
            return 0

def calcularLargeStraight(lista_dados):
    if lista_dados[0] == 1 and lista_dados[1] == 2 and lista_dados[2] == 3 and lista_dados[3] == 4 and lista_dados[4] == 5:
        return 40
    elif lista_dados[0] == 2 and lista_dados[1] == 3 and lista_dados[2] == 4 and lista_dados[3] == 5 and lista_dados[4] == 6:
        return 40
    else:
        return 0

def calculaBonusSuperior(dic):
    total = dic['ones'] + dic['twos'] + dic['threes'] + dic['fours'] + dic['fives'] + dic['sixes']
    if total >= 63:
        dic['bonus superior'] = 35
    return dic

def mostrarOpcoes(l,dic):
    d = dict()
    d = dic.copy()
    if d['ones'] == 0:
        d['ones'] = calcularOnes(l)
    if d['twos'] == 0:
        d['twos'] = calcularTwos(l)
    if d['threes'] == 0:
        d['threes'] = calcularThrees(l)
    if d['fours'] == 0:
        d['fours'] = calcularFours(l)
    if d['fives'] == 0:
        d['fives'] = calcularFives(l)
    if d['sixes'] == 0:
        d['sixes'] = calcularSixes(l)
    if d['three of a kind'] == 0:
        d['three of a kind'] = calcularThreeOfAKind(l)
    if d['four of a kind'] == 0:
        d['four of a kind'] = calcularFourOfAKind(l)
    if d['full house'] == 0:
        d['full house'] = calcularFullHouse(l)
    if d['small straight'] == 0:
        d['small straight'] = calcularSmallStraight(l)
    if d['large straight'] == 0:
        d['large straight'] = calcularLargeStraight(l)
    if d['chance'] == 0:
        d['chance'] = calcularChance(l)
    if d['yahtzee'] == 0:
        d['yahtzee'] = calcularYahtzee(l)
    return d
    
