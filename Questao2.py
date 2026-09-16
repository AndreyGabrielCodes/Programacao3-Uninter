#FEITO POR ANDREY GABRIEL DE ANDRADE MORAES
#4731589

SIGLA_ESTADO_DISTRITO_FEDERAL = 'DF'

def retorna_ascii(caractere):
    """Retorna o número do caractere conforme a Tabela ASCII
    Ex.: a=97, j=106, U=117, etc"""
    bytes = caractere.encode('utf-32-be')
    bytes = int.from_bytes(bytes,byteorder='big')
    return bytes

class No_Estado():

    def __init__(self,sigla,nome_estado):
        self.sigla = sigla
        self.nomeEstado = nome_estado
        self.proximo = None

class Tabela_Hash():

    def __init__(self):
        self.tabela = []
        for i in range(10):
            self.tabela.append(None)

    def hash(self,sigla_estado):
        #Por superstição, retorna Distrito Federal sempre como 7
        if sigla_estado == SIGLA_ESTADO_DISTRITO_FEDERAL:
            return 7

        char1_ascii = retorna_ascii(sigla_estado[0]);
        char2_ascii = retorna_ascii(sigla_estado[1]);

        #Segue a formula posição = (CHAR1 + CHAR2) MOD 10
        posicao =  (char1_ascii + char2_ascii) % 10

        return posicao


lista_estados_brasil = [('AC','Acre'),('AL','Alagoas'),('AP','Amapá'),('AM','Amazonas'),('BA','Bahia'),('CE','Ceará'),('DF','Distrito Federal'),
                        ('ES','Espírito Santo'),('GO','Goiás'),('MA','Maranhão'),('MT','Mato Grosso'),('MS','Mato Grosso do Sul'),('MG','Minas Gerais'),
                        ('PA','Para'),('PB','Paraíba'),('PR','Paraná'),('PE','Pernambuco'),('Pi','piauí'),('RJ','Rio de Janeiro'),
                        ('RN','Rio Grande do Norte'),('RS','Rio Grande do Sul'),('RO','Rondônia'),('RR','Roraima'),('SC','Santa Catarina'),
                        ('SP','São Paulo'), ('SE','Sergipe'),('TO','Tocantins'),]

tabela_estados = Tabela_Hash()

#Main
print('Sistema de emplacamento de veiculos')
print('Andrey Gabriel de Andrade Moraes')
print('4731589')
