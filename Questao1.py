#FEITO POR ANDREY GABRIEL DE ANDRADE MORAES
#4731589

LETRA_PRIORIDADE = 'A'
LETRA_SEMPRIORIDADE = 'V'
COR_PRIORIDADE = 'Amarelo'
COR_SEMPRIORIDAE = 'Verde'

SenhaAtualPrioridade = 201
SenhaAtualSemPrioridade = 1

def retorna_senha_cor(prioridade):
    if prioridade == LETRA_PRIORIDADE:
        retorno = SenhaAtualPrioridade
        SenhaAtualPrioridade += SenhaAtualPrioridade
        return retorno;
    elif prioridade == LETRA_SEMPRIORIDADE:
        retorno = SenhaAtualSemPrioridade
        SenhaAtualSemPrioridade += SenhaAtualSemPrioridade
        return retorno;

def retorna_descricao_cor(prioridade):
    if prioridade == LETRA_PRIORIDADE:
        return COR_PRIORIDADE;
    elif prioridade == LETRA_SEMPRIORIDADE:
        return COR_SEMPRIORIDAE;

class NoSenhaPaciente:
    def __init__(self,cor):
        self.cor = cor
        self.numero = retorna_senha_cor(cor)
        self.proximo = None

class ListaEncadeadaPacientes:
    
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self,no_novo):
        """Insere ao final da lista"""

        #Caso a lista não possua conteudo
        if not self.head:
            self.head = no_novo
            return

        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = no_novo

        print('Paciente sem prioridade inserido!')

    def inserirComPrioridade(self,no_novo):
        """Insere o nó de prioridade após todos os nós de prioridade já existentes"""

        #Lista vazia ou com head sem prioridade
        if not self.head or self.head.prioridade == LETRA_SEMPRIORIDADE:
            no_novo.proximo = self.head
            self.head = no_novo
            print('Paciente com prioridade inserido!')
            return

        atual = self.head

        while atual.proximo and atual.proximo.prioridade == LETRA_PRIORIDADE:
            atual = atual.proximo

        #Insere o novo conteudo após o ultimo nó de prioridade encontrado
        no_novo.proximo = atual.proximo
        atual.proximo = no_novo

        print('Paciente com prioridade inserido!')

    def atenderPaciente(self):
        """Retira o primeiro paciente da fila e imprime chamada para atendimento"""

        if not self.head:
            raise("Não existentes pacientes na fila para chamar no momento!")

        paciente_atendido = self.head

        #Retira o primeiro paciente e faz a lista apontar para o próximo
        self.head = self.head.proximo

        mensagem = f"Atendendo o paciente cor {paciente_atendido.cor} ({retorna_descricao_cor(paciente_atendido.cor)}) e número {paciente_atendido.numero}"
        print(mensagem)

    def imprimirListaEspera(self):
        elementos_listagem = []
        atual = self.head

        while atual:
            elementos_listagem(f"[{atual.prioridade},{atual.numero}]")
            atual = atual.proximo

        print("Lista -> " + " ".join(elementos_listagem))

FilaPacientes = ListaEncadeadaPacientes()

def inserir():

    prioridade = input(f"Informe a cor/prioridade da senha ({LETRA_PRIORIDADE}/{LETRA_SEMPRIORIDADE}): ")
    prioridade.upper()

    if prioridade not in (LETRA_PRIORIDADE,LETRA_SEMPRIORIDADE):
        raise ValueError("Prioridade informada não existe!")

    paciente_novo = NoSenhaPaciente(prioridade)

    if prioridade == LETRA_SEMPRIORIDADE:
        FilaPacientes.inserirSemPrioridade(paciente_novo)
    else:
        FilaPacientes.inserirComPrioridade(paciente_novo)

    print(f'Inserido paciente de senha {paciente_novo.numero} e cor {paciente_novo.cor} ({retorna_descricao_cor(paciente_novo.cor)})')


#Main
print('Sistema de fila de pacientes com e sem prioridade')
print('Andrey Gabriel de Andrade Moraes')
print('4731589')

while True:

    try:
        print('')
        print('1 - Adicionar paciente a fila')
        print('2 - Mostrar pacientes na fila')
        print('3 - Chamar paciente')
        print('4 - Sair')
        print('')

        opcao = input('Informe a opção desejada: ')

        print('')

        match opcao:
            case 1:
                inserir()
            case 2:
                FilaPacientes.imprimirListaEspera()
            case 3:
                FilaPacientes.atenderPaciente()
            case 4:
                break
            case _: 
                raise ValueError('Opção escolhida não existe, tente novamente')

    except Exception as e:
        print(e)
    else:
        print('Encerrando sistema...')   
