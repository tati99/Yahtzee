__all__ = ['somaColuna','calcularOnes','calcularTwos','calcularThrees','calcularFours',
            'calcularFives','calcularSixes','calcularSmallStraight','calcularLargeStraight',
	        'calcularThreeOfAKind','calcularFourOfAKind','calcularChance','calcularFullHouse',
            'calcularYahtzee','calculaBonusSuperior','calcularBonusYa', 'mostrarOpcoes']

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

def calcularThreeOfAKind(lista_dados):
    for element in lista_dados:
        if (lista_dados.count(element)) >= 3:
            return sum(lista_dados)
    return 0

def calcularFourOfAKind(lista_dados):
    for element in lista_dados:
        if (lista_dados.count(element)) >= 4:
            return sum(lista_dados)
    return 0

def calcularFullHouse(lista_dados):   
    for trio in lista_dados:
        if (lista_dados.count(trio)) == 3:
            for dupla in lista_dados:
                if (lista_dados.count(dupla)) == 2 and dupla != trio:
                    return 25
    return 0

def calcularSmallStraight(l):
    nl = l.copy()
    nl.sort()
    ant = nl[0]
    for i in nl[1:]:
        if ant == i:
            nl.remove(i)
        else:
            ant = i
    if len(nl) < 4:
        return 0
    if nl[0] == 1:
        if nl[1] == 2:
            if nl[2] == 3:
                if nl[3] == 4:
                    return 30
    if nl[0] == 2:
        if nl[1] == 3:
            if nl[2] == 4:
                if nl[3] == 5:
                    return 30
    if nl[0] == 3:
        if nl[1] == 4:
            if nl[2] == 5:
                if nl[3] == 6:
                    return 30
    return 0

def calcularLargeStraight(lista_dados):
    lista_dados.sort()
    if lista_dados[0] == 1:
        if lista_dados[1] == 2:
            if lista_dados[2] == 3:
                if lista_dados[3] == 4:
                    if lista_dados[4] == 5:
                        return 40
    if lista_dados[0] == 2:
        if lista_dados[1] == 3:
            if lista_dados[2] == 4:
                if lista_dados[3] == 5:
                    if lista_dados[4] == 6:
                        return 40  
    return 0

def calcularYahtzee(l):
    ant = l[0]
    for i in l[1:]:
        if ant != i:
            return 0
        ant = i
    return 50

def calcularChance(lista_dados):
    return sum(lista_dados)

def calcularBonusYa(l):
    if calcularYahtzee(l) == 50:
        return 100
    return -1

def calculaBonusSuperior(dic):
    total = dic['ones'] + dic['twos'] + dic['threes'] + dic['fours'] + dic['fives'] + dic['sixes']
    if total >= 63:
        dic['bonus superior'] = 35
    else:
        dic['bonus superior'] = 0
    return dic

def somaColuna(d):
    d = calculaBonusSuperior(d)
    d['total'] = 0
    aux = 0
    for k in d:
        aux += d[k]
    d['total'] = aux
    return d

def mostrarOpcoes(l,dic):
    d = dict()
    d = dic.copy()
    if d['ones'] == None:
        d['ones'] = calcularOnes(l)
    else:
        d['ones'] = -1
    if d['twos'] == None:
        d['twos'] = calcularTwos(l)
    else:
        d['twos'] = -1
    if d['threes'] == None:
        d['threes'] = calcularThrees(l)
    else:
        d['threes'] = -1
    if d['fours'] == None:
        d['fours'] = calcularFours(l)
    else:
        d['fours'] = -1
    if d['fives'] == None:
        d['fives'] = calcularFives(l)
    else:
        d['fives'] = -1
    if d['sixes'] == None:
        d['sixes'] = calcularSixes(l)
    else:
        d['sixes'] = -1
    if d['three of a kind'] == None:
        d['three of a kind'] = calcularThreeOfAKind(l)
    else:
        d['theree of a kind'] = -1
    if d['four of a kind'] == None:
        d['four of a kind'] = calcularFourOfAKind(l)
    else:
        d['four of a kind'] = -1
    if d['full house'] == None:
        d['full house'] = calcularFullHouse(l)
    else:
        d['full house'] = -1
    if d['small straight'] == None:
        d['small straight'] = calcularSmallStraight(l)
    else:
        d['small straight'] = -1
    if d['large straight'] == None:
        d['large straight'] = calcularLargeStraight(l)
    else:
        d['large straight'] = -1
    if d['chance'] == None:
        d['chance'] = calcularChance(l)
    else:
        d['chance'] = -1
    if d['yahtzee'] == None:
        d['yahtzee'] = calcularYahtzee(l)
    else:
        d['yahtzee'] = -1
    if d['yahtzee'] == -1:
        d['bonus yahtzee'] = calcularBonusYa(l)
    return d
    
