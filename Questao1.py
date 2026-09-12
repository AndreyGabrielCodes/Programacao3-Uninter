#FEITO POR ANDREY GABRIEL DE ANDRADE MORAES
#4731589

class No:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None

class ListaEncadeada:
    
    def __init__(self):
        self.head = None

    def inserir_inicio(self,conteudo):
        novo_no = No(conteudo)
        novo_no.proximo = self.head
        self.head = novo_no

    def inserir_fim(self,conteudo):
        novo_no = No(conteudo)

        #Caso a lista não possua conteudo
        if not self.head:
            self.head = novo_no
            return

        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def inserir_antes_de(self,conteudo_alvo,conteudo_novo):
        """Insere conteudo_novo antes de conteudo alvo
        Retorna True se conseguiu encontrar o alvo e inserir ou False se não encontrou o alvo"""

        if not self.head:
            return False

        #Se o alvo é o head da lista
        if self.head.conteudo == conteudo_alvo:
            self.inserir_inicio(conteudo_novo)
            return True

        atual = self.head
        anterior = None

        #Procura o conteudo alvo mantendo o anterior
        while atual and atual.conteudo != conteudo_alvo:
            anterior = atual
            atual = atual.proximo

        #Se não foi encontrado conteudo alvo
        if not atual:
            return False

        #Conecta o conteudo novo entre o anterior e o atual
        novo_no = No(conteudo_novo)
        novo_no.proximo = atual
        anterior.proximo = novo_no

        return True


    def inserir_depois_de(self,conteudo_alvo,conteudo_novo):
        """Insere conteudo_novo depois de conteudo alvo
        Retorna True se conseguiu encontrar o alvo e inserir ou False se não encontrou o alvo"""

        atual = self.head

        #Procura o conteudo alvo
        while atual and atual.conteudo != conteudo_alvo:
            atual = atual.proximo

        #Se não foi encontrado conteudo alvo
        if not atual:
            return False

        #Conecta o conteudo novo entre o anterior e o atual
        novo_no = No(conteudo_novo)
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

        return True

    def remover_no(self,conteudo):
        """Retorna True quando conseguiu retirar ou False quando não encontrou o conteudo a retirar"""

        atual = self.head

        #Caso o conteudo a retirar seja o head
        if atual and atual.conteudo == conteudo:
            self.head = atual.proximo
            return True

        anterior = None
        while atual and atual.conteudo != conteudo:
            anterior = atual
            atual = atual.proximo

        #Se não foi encontrado conteudo
        if not atual:
            return False

        #Desconecta o no da lista
        anterior.proximo = atual.proximo

        return True

    def listar(self):
        elementos_listagem = []
        atual = self.head

        while atual:
            elementos_listagem.append(str(atual.conteudo))
            atual = atual.proximo

        return elementos_listagem

FilaPacientes = ListaEncadeada()