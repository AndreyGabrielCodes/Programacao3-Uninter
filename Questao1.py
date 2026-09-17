#FEITO POR ANDREY GABRIEL DE ANDRADE MORAES
#4731589

LETRA_COR_PRIORIDADE = 'A'
LETRA_COR_SEM_PRIORIDADE = 'V'
COR_PRIORIDADE = 'Amarelo'
COR_SEM_PRIORIDADE = 'Verde'

SenhaAtualPrioridade = 201
SenhaAtualSemPrioridade = 1

def retorna_senha_cor(prioridade):

    global SenhaAtualPrioridade, SenhaAtualSemPrioridade

    if prioridade == LETRA_COR_PRIORIDADE:
        retorno = SenhaAtualPrioridade
        SenhaAtualPrioridade += 1
        return retorno;
    elif prioridade == LETRA_COR_SEM_PRIORIDADE:
        retorno = SenhaAtualSemPrioridade
        SenhaAtualSemPrioridade += 1
        return retorno;

def retorna_descricao_cor(prioridade):
    if prioridade == LETRA_COR_PRIORIDADE:
        return COR_PRIORIDADE;
    elif prioridade == LETRA_COR_SEM_PRIORIDADE:
        return COR_SEM_PRIORIDADE;

class NoSenhaPaciente:
    def __init__(self,cor,numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

class ListaEncadeadaPacientes:
    
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self,no_novo):
        """Insere ao final da lista"""

        atual = self.head
        #Anda pela lista a partir do head
        #Em seguida insere ao final
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = no_novo

    def inserirComPrioridade(self,no_novo):
        """Insere o nó de prioridade após todos os nós de prioridade já existentes"""

        atual = self.head

        #Anda pela lista a partir do head
        #Em seguida insere após todos os elementos de prioridade
        while atual.proximo and atual.proximo.cor == LETRA_COR_PRIORIDADE:
            atual = atual.proximo

        #Insere o novo conteudo após o ultimo nó de prioridade encontrado
        no_novo.proximo = atual.proximo
        atual.proximo = no_novo

    def inserir(self):

        global SenhaAtualPrioridade, SenhaAtualSemPrioridade

        print('\nMENU - OPÇÕES DE SENHA')
        print(f'{LETRA_COR_PRIORIDADE} = {COR_PRIORIDADE} - Com prioridade')
        print(f'{LETRA_COR_SEM_PRIORIDADE} =  {COR_SEM_PRIORIDADE}  - Sem prioridade')
        print('')

        prioridade = input(f"Informe a cor/prioridade da senha ({LETRA_COR_PRIORIDADE}/{LETRA_COR_SEM_PRIORIDADE}): ").upper()

        if prioridade not in (LETRA_COR_PRIORIDADE,LETRA_COR_SEM_PRIORIDADE):
            raise Exception("Prioridade informada não existe!")

        senha_paciente = 0

        #Atribui automaticamente a senha conforme global
        if prioridade == LETRA_COR_PRIORIDADE:
            senha_paciente = SenhaAtualPrioridade
            SenhaAtualPrioridade += 1
        elif prioridade == LETRA_COR_SEM_PRIORIDADE:
            senha_paciente = SenhaAtualSemPrioridade
            SenhaAtualSemPrioridade += 1

        paciente_novo = NoSenhaPaciente(prioridade, senha_paciente)

        #Caso a lista esteja vazia insere primeiro
        #Caso o primeiro da lista seja sem prioridade e vá ser inserido uma prioridade, insere prioridade no head
        #Caso a lista esteja com valor insere conforme prioridade
        if not self.head:
            self.head = paciente_novo
        elif self.head.cor == LETRA_COR_SEM_PRIORIDADE and prioridade == LETRA_COR_PRIORIDADE:
            paciente_novo.proximo = self.head
            self.head = paciente_novo
        elif prioridade == LETRA_COR_PRIORIDADE:
            self.inserirComPrioridade(paciente_novo)
        elif prioridade == LETRA_COR_SEM_PRIORIDADE:
            self.inserirSemPrioridade(paciente_novo)

        print(f'\nInserido paciente de senha {paciente_novo.numero} e cor {paciente_novo.cor} ({retorna_descricao_cor(paciente_novo.cor)})')

    def atenderPaciente(self):
        """Retira o primeiro paciente da fila e imprime chamada para atendimento"""

        if not self.head:
            raise Exception("Não existentes pacientes na fila para chamar no momento!")

        paciente_atendido = self.head

        #Retira o primeiro paciente e faz a lista apontar para o próximo
        self.head = self.head.proximo

        mensagem = f"\nAtendendo o paciente cor {paciente_atendido.cor} ({retorna_descricao_cor(paciente_atendido.cor)}) e número {paciente_atendido.numero}"
        print(mensagem)

    def imprimirListaEspera(self):
        """Imprime todos os pacientes a partir do primeiro"""

        if not self.head:
            raise Exception("Não existentes pacientes na fila no momento!")
        
        elementos_listagem = []
        atual = self.head

        while atual:
            elementos_listagem.append(f"[{atual.cor},{atual.numero}]")
            atual = atual.proximo

        print("\nLista -> " + " ".join(elementos_listagem))

FilaPacientes = ListaEncadeadaPacientes()

#Main
print('Sistema de fila de pacientes com e sem prioridade')
print('Andrey Gabriel de Andrade Moraes')
print('4731589')

while True:

    try:
        print('')
        print('MENU PRINCIPAL')
        print('1 - Adicionar paciente a fila')
        print('2 - Mostrar pacientes na fila')
        print('3 - Chamar paciente')
        print('4 - Sair')
        print('')

        opcao = input('Informe a opção desejada: ')

        match opcao:
            case '1':
                FilaPacientes.inserir()
            case '2':
                FilaPacientes.imprimirListaEspera()
            case '3':
                FilaPacientes.atenderPaciente()
            case '4':
                print('\nEncerrando sistema...')
                break
            case _: 
                raise Exception('Opção escolhida não existe, tente novamente!')

    except Exception as e:
        print('')
        print('Erro! - ' + str(e))
