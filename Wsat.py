import random
import copy
'''strSentencia se guarda la sentencia como letras, mientras que en boolSententcia guarda los valores de verdad
    
    strSentencia =  ["CbaA","Cnhc"]
    '''
strSentencia =  ["AbCdf","aBcDE","BD","F","bde","a","A"]
#strSentencia =  ["A","a"]
class Wsat:
    strSentencia =[]
    boolSentencia = []
    literales = set([])
    valorLiterales = []
    
    def __init__(self,sentencia):
        self.strSentencia = sentencia
        
        for elem in self.strSentencia:
            self.literales = self.literales|set(elem.upper())
        
        self.literales = list(self.literales)
        self.randValorVariables()
        self.llenabBoolSent()
    
    
    def randValorVariables(self):
        self.valorLiterales = []
        for literal in self.literales:
            val = random.randint(0,1)
            self.valorLiterales.append(val)
    
    def llenabBoolSent(self):
        self.boolSentencia = []
        for clausula in self.strSentencia:
            for i in range(0,len(self.literales)):
                boolVar = self.valorLiterales[i]
                clausula = clausula.replace(self.literales[i],str(boolVar))
                if(boolVar == 1):
                    clausula = clausula.replace(self.literales[i].lower(),str(0))
                elif(boolVar == 0):
                    clausula = clausula.replace(self.literales[i].lower(),str(1))
            self.boolSentencia.append(clausula)
    
    
    def sustituyeSentencia(self,sentencia,valores):
        boolSentencia = []
        for clausula in sentencia:
            for i in range(0,len(valores)):
                boolVar = valores[i]
                clausula = clausula.replace(self.literales[i],str(boolVar))
                if(boolVar == 1):
                    clausula = clausula.replace(self.literales[i].lower(),str(0))
                elif(boolVar == 0):
                    clausula = clausula.replace(self.literales[i].lower(),str(1))
            boolSentencia.append(clausula)
        return boolSentencia
    
    def evalua(self, clausula):
        if '1' in clausula:
            return True
        else:
            return False
    """Calcula el costo de boolSentencia que esta soncronizado con valorLiterales y strSentencia
        """
    def calculaCosto(self):
        numFalsas=0
        for clausula in self.boolSentencia:
            aux = self.evalua(clausula)
            if not self.evalua(clausula):
                numFalsas = numFalsas + 1
        return numFalsas
    
    def calculaCostoCon(self,boolSentencia):
        """calcula el costo valuando con la sentencia que se le mande"""
        numFalsas=0
        for clausula in boolSentencia:
            if not self.evalua(clausula):
                numFalsas = numFalsas + 1
        return numFalsas
    def calculaCostoVecinosDeClausula(self,NoClausula):
        costoActual = self.calculaCosto()
        valorLiteralesDelVecinoMenorCosto = copy.deepcopy(self.valorLiterales)
        for literal in strSentencia[NoClausula]:
            aCambiar = self.literales.index(literal.upper())
            literalesVecinos = copy.deepcopy(self.valorLiterales)
            literalesVecinos[aCambiar] = (literalesVecinos[aCambiar] + 1)%2
            costoVecino = self.calculaCostoCon(self.sustituyeSentencia(self.strSentencia,literalesVecinos))
            if(costoVecino<=costoActual):
                costoActual = costoVecino
                valorLiteralesDelVecinoMenorCosto = copy.deepcopy(literalesVecinos)
        self.valorLiterales = copy.deepcopy(valorLiteralesDelVecinoMenorCosto)
        self.llenabBoolSent()
        return costoActual
    def CambiaAleatorio(self,NoClausula):
        literal = strSentencia[NoClausula][random.randint(0,len(strSentencia[NoClausula])-1)]
        aCambiar = self.literales.index(literal.upper())
        literalesVecinos = copy.deepcopy(self.valorLiterales)
        literalesVecinos[aCambiar] = (literalesVecinos[aCambiar] + 1)%2
        self.valorLiterales = copy.deepcopy(literalesVecinos)
        self.llenabBoolSent()



n=10
m=20
for i in range(0,n):
    sat = Wsat(strSentencia)
    print(sat.strSentencia,"en booleano es:\n",sat.boolSentencia)
    for i in range(0,len(sat.literales)):
        print(sat.literales[i],"-",sat.valorLiterales[i])
    
    cuenta=0
    while sat.calculaCosto() != 0 and cuenta<m:
        cuenta = cuenta + 1
        C = random.randint(0,len(sat.strSentencia)-1)
        if(random.randint(0,1)==1):
            sat.calculaCostoVecinosDeClausula(C)
        else:
            sat.CambiaAleatorio(C)
    if(sat.calculaCosto()==0):
        print("solucion")
        for i in range(0,len(sat.literales)):
            print(sat.literales[i],"=",sat.valorLiterales[i])
        break
    else:
        print("no se encontro solucion" )
