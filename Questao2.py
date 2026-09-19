#FEITO POR ANDREY GABRIEL DE ANDRADE MORAES
#4731589

SIGLA_ESTADO_DISTRITO_FEDERAL = 'DF'

def retorna_ascii(caractere):
    """Retorna o número do caractere conforme a Tabela ASCII
    Ex.: a=97, j=106, U=117, etc"""
    try:
        bytes = caractere.encode('utf-32-be')
        bytes = int.from_bytes(bytes,byteorder='big')
        return bytes
    except Exception:
        raise Exception("Valor informado não existe na Tabela ASCII!")

class No_Estado():

    def __init__(self,sigla,nome_estado):
        self.sigla = sigla
        self.nomeEstado = nome_estado
        self.proximo = None

class Tabela_Hash():

    def __init__(self):
        """Instancia a lista já com 10 posições vazias"""
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

    def inserir_estado(self, sigla_estado, nome_estado):
        #Deixa em caixa alta para evitar problemas de posição por informar minusculo
        sigla_estado = sigla_estado.upper()

        # Extrai a posição conforme a tabela ASCII
        posicao = self.hash(sigla_estado)
        novo_estado = No_Estado(sigla_estado, nome_estado)
        head_atual = self.tabela[posicao]

        #Pega quem está atualmente no head, faz o novo estado apontar para esse head
        novo_estado.proximo = head_atual
        self.tabela[posicao] = novo_estado

    #Pergunta a responder: o nome do estado tem que ser impresso ? no exemplo não está
    def imprimir_estados(self):

        print(f'LISTAGEM DE ESTADOS POR POSIÇÃO')
        print('-'*60)
        for posicao in range(10):

            atual = self.tabela[posicao]
            elementos = []

            if atual is not None:
                while atual is not None:
                    elementos.append(f'{atual.sigla}')
                    atual = atual.proximo

                    #Adiciona None quando encontrar o ultimo estado existente na lista
                    if atual is None:
                        elementos.append('None')
            else:
                elementos.append('None')

            print(f'Posição {posicao}: {' -> '.join(elementos)}')
        print('-'*60)

lista_estados_brasil = [('AC','Acre'),('AL','Alagoas'),('AP','Amapá'),('AM','Amazonas'),('BA','Bahia'),('CE','Ceará'),('DF','Distrito Federal'),
                        ('ES','Espírito Santo'),('GO','Goiás'),('MA','Maranhão'),('MT','Mato Grosso'),('MS','Mato Grosso do Sul'),('MG','Minas Gerais'),
                        ('PA','Para'),('PB','Paraíba'),('PR','Paraná'),('PE','Pernambuco'),('PI','Piauí'),('RJ','Rio de Janeiro'),
                        ('RN','Rio Grande do Norte'),('RS','Rio Grande do Sul'),('RO','Rondônia'),('RR','Roraima'),('SC','Santa Catarina'),
                        ('SP','São Paulo'), ('SE','Sergipe'),('TO','Tocantins'),]

tabela_estados = Tabela_Hash()

#Main
print('Sistema de emplacamento de veiculos')
print('Andrey Gabriel de Andrade Moraes')
print('4731589\n')

#Mostra que não há estados inseridos
tabela_estados.imprimir_estados()

#Separa visualmente as listagens
print('\r')

#Preenche os valores
for sigla_estado, nome_estado in lista_estados_brasil:
    tabela_estados.inserir_estado(sigla_estado, nome_estado)

#Mostra os estados preenchidos
tabela_estados.imprimir_estados()

#Preenche estado fictício com o meu nome e sobrenome
#Conforme conversado com o Prof Bruno Kostiuk por Tutoria, meu nome e sobrenome gera AM (Andrey Moraes), 
# que é um estado já existente (Amazonas), o que gera duplicidade na inserção/impressão,
# entretanto ele comentou que isto não é um problema e que pode permanecer assim
tabela_estados.inserir_estado('AM','Andrey Gabriel de Andrade Moraes')

#Separa visualmente as listagens
print('\r')

#Mostra os estados preenchidos com o fictício
tabela_estados.imprimir_estados()

