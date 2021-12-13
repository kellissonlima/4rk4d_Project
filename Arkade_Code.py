from tkinter import *

class No:
     
     def __init__(self, tag, valor, text, date, dir, esq): #construtor da Classe Nó, com o seguintes atributos: Chave(Key), e posicionamento da Árvore Direita e Esquerda (dir,esq)
          self.tag = tag
          self.item = valor
          self.text = text
          self.date = date
          self.dir = dir
          self.esq = esq
class Tree:

     def __init__(self):
          self.root = No(None,None,None,None,None,None)
          self.root = None

     def inserir(self, tag, valor, text, date):# valores que eu quero que tenha em cada nó
          novo = No(tag, valor, text, date, None, None) # cria um novo Nó
          if self.root == None: # Se a raiz for vazia então adicione o novo nó criado como Raiz
               self.root = novo
          else: # se nao for a raiz
               atual = self.root #Pegue a referência do nó atual
               while True:
                    anterior = atual #Pegar a referência para saber quem é o seu anterior
                    n = int(input("Informe o lado que deseja adicionar [0: Esquerdo / 1: Direito]: "))
                    if n == 0: # ir para esquerda
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return
                    # fim da condição ir a esquerda
                    else: # ir para direita
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return
                    
                    # fim da condição ir a direita

     def buscar(self, valor, text):
         if self.root == None:
              return None # se arvore vazia
         atual = self.root # começa a procurar desde raiz
         while (atual.item != valor) and (atual.text != text): # enquanto nao encontrou
               if valor < atual.item:
                    atual = atual.esq # caminha para esquerda
               else:
                    atual = atual.dir # caminha para direita
               if atual == None:
                    return None # encontrou uma folha -> sai
         return atual  # terminou o laço while e chegou aqui é pq encontrou item    

     # O sucessor é o Nó mais a esquerda da subarvore a direita do No que foi passado como parametro do metodo
     def nosucessor(self, apaga, text): # O parametro é a referencia para o No que deseja-se apagar
          paidosucessor = apaga
          sucessor = apaga
          atual = apaga.dir # vai para a subarvore a direita

          while atual != None: # enquanto nao chegar no Nó mais a esquerda
               paidosucessor = sucessor
               sucessor = atual
               atual = atual.esq # caminha para a esquerda

          # *********************************************************************************
          # quando sair do while "sucessor" será o Nó mais a esquerda da subarvore a direita
          # "paidosucessor" será o o pai de sucessor e "apaga" o Nó que deverá ser eliminado
          # *********************************************************************************
          if sucessor != apaga.dir: # se sucessor nao é o filho a direita do Nó que deverá ser eliminado
               paidosucessor.esq = sucessor.dir # pai herda os filhos do sucessor que sempre serão a direita
               # lembrando que o sucessor nunca poderá ter filhos a esquerda, pois, ele sempre será o
               # Nó mais a esquerda da subarvore a direita do Nó apaga.
               # lembrando também que sucessor sempre será o filho a esquerda do pai
               sucessor.dir = apaga.dir # guardando a referencia a direita do sucessor para 
                                        # quando ele assumir a posição correta na arvore
          return sucessor

     def remover(self, valor, text): #parei aqui.
         if self.root == None:
               return False # se arvore vazia
         atual = self.root
         pai = self.root
         filho_esq = True
         # ****** Buscando o valor **********
         while (atual.item != valor) and (atual.text != text.lower()): # enquanto nao encontrou
               pai = atual
               if valor < atual.item: # caminha para esquerda
                    atual = atual.esq
                    filho_esq = True # é filho a esquerda? sim
               else: # caminha para direita
                    atual = atual.dir 
                    filho_esq = False # é filho a esquerda? NAO
               if atual == None:
                    return False # encontrou uma folha -> sai
         # fim laço while de busca do valor

         # **************************************************************
         # se chegou aqui quer dizer que encontrou o valor (v)
         # "atual": contem a referencia ao No a ser eliminado
         # "pai": contem a referencia para o pai do No a ser eliminado
         # "filho_esq": é verdadeiro se atual é filho a esquerda do pai
         # **************************************************************

         # Se nao possui nenhum filho (é uma folha), elimine-o
         if atual.esq == None and atual.dir == None:
               if atual == self.root:
                    self.root = None # se raiz
               else:
                    if filho_esq:
                         pai.esq =  None # se for filho a esquerda do pai
                    else:
                         pai.dir = None # se for filho a direita do pai

         # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
         elif atual.dir == None:
               if atual == self.root:
                    self.root = atual.esq # se raiz
               else:
                    if filho_esq:
                         pai.esq = atual.esq # se for filho a esquerda do pai
                    else:
                         pai.dir = atual.esq # se for filho a direita do pai
         
         # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
         elif atual.esq == None:
               if atual == self.root:
                    self.root = atual.dir # se raiz
               else:
                    if filho_esq:
                         pai.esq = atual.dir # se for filho a esquerda do pai
                    else:
                         pai.dir = atual.dir # se for  filho a direita do pai

         # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
         else:
               sucessor = self.nosucessor(atual)
               # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
               if atual == self.root:
                    self.root = sucessor # se raiz
               else:
                    if filho_esq:
                         pai.esq = sucessor # se for filho a esquerda do pai
                    else:
                         pai.dir = sucessor # se for filho a direita do pai
               sucessor.esq = atual.esq # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
                                        # a posição correta na arvore   

         return True
  
     def inOrder(self, atual):
         if atual != None:
              self.inOrder(atual.esq)
              print(atual.item,end=" ")
              self.inOrder(atual.dir)
  
     def preOrder(self, atual):
         if atual != None:
              print(atual.item,end=" ")
              self.preOrder(atual.esq)
              self.preOrder(atual.dir)
       
     def posOrder(self, atual):
         if atual != None:
              self.posOrder(atual.esq)
              self.posOrder(atual.dir)
              print(atual.item,end=" ")

  
     def altura(self, atual):
          if atual == None or atual.esq == None and atual.dir == None:
               return 0
          else:
             if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq) 
             else:
                return  1 + self.altura(atual.dir) 
  
     def folhas(self, atual):
         if atual == None:
              return 0
         if atual.esq == None and atual.dir == None:
              return 1
         return self.folhas(atual.esq) + self.folhas(atual.dir)

  
     def contarNos(self, atual):
        if atual == None:
             return 0
        else:
             return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

     def minn(self):
         atual = self.root
         anterior = None
         while atual != None:
              anterior = atual
              atual = atual.esq
         return anterior

     def maxx(self):
         atual = self.root
         anterior = None
         while atual != None:
              anterior = atual
              atual = atual.dir
         return anterior

     def caminhar(self):
          print(" Exibindo em ordem: ",end="")
          self.inOrder(self.root)
          print("\n Exibindo em pos-ordem: ",end="")
          self.posOrder(self.root)
          print("\n Exibindo em pre-ordem: ",end="")
          self.preOrder(self.root)
          print("\n Altura da arvore: %d" %(self.altura(self.root)))
          print(" Quantidade de folhas: %d"  %(self.folhas(self.root)))
          print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))
          if self.root != None: # se arvore nao esta vazia
             print(" Valor minimo: %d" %(self.minn().item))
             print(" Valor maximo: %d" %(self.maxx().item))
     
#### fim da classe ####

janela = Tk('janela_1')
janela.geometry('1024x800')
janela.configure(background='#008')
arv = Tree()
# janela.title('Arkad Finanças')
# def donothing():
#    filewin = Toplevel(janela)
#    button = Button(filewin, text="Do nothing button")
#    button.pack()

# menubar = Menu(janela)
# filemenu = Menu(menubar,tearoff=0)
# filemenu.add_command(label='Inserir',command=arv.inserir)
# filemenu.add_separator()
# filemenu.add_command(label='Exibir',command=arv.caminhar)
# filemenu.add_separator()
# filemenu.add_command(label='Excluir',command=arv.remover)
# filemenu.add_separator()
# filemenu.add_command(label='Pesquisar',command=arv.buscar)
# filemenu.add_separator()
# filemenu.add_command(label='Encerrar',command=janela.quit)

imgbkgd = Label(janela,image=)

txt01Janela1 = Label(janela, text="Arkad - Faça o seu Dinheiro Trabalhar para Você!") 
txt01Janela1.place(x=350,y=10,width=300,height=20)

bt01Janela1 = Button(janela, text='Inserir', command= arv.inserir,fg='green')
bt01Janela1.place(x=10,y=50,width=50,height=15)

bt02Janela1 = Button(janela, text='Exibir', command= arv.caminhar)
bt02Janela1.place(x=70,y=50,width=50,height=15)

bt03Janela1 = Button(janela, text='Excluir', command= arv.remover)
bt03Janela1.place(x=130,y=50,width=50,height=15)

bt04Janela1 = Button(janela, text='Buscar', command= arv.buscar)
bt04Janela1.place(x=190,y=50,width=50,height=15)

bt05Janela1 = Button(janela, text='Encerrar', command= arv.buscar,fg='red')
bt05Janela1.place(x=250,y=50,width=50,height=15)

#Parte é pra colocar em uma tela dinâmica na parte de inserir
#Título
Label(janela,text='Título',fg='green').place(x=10,y=100,width=80,height=20)

vnome=Entry(janela)
vnome.place(x=100,y=100,width=200,height=20)
#Valor
Label(janela,text='Valor',fg='green').place(x=120,y=100,width=80,height=20)
vnome=Entry(janela)
vnome.place(x=200,y=100,width=200,height=20)

# print("Programa Arvore Binaria")
# opcao = 0
# while opcao != 5:
#      print("***********************************")
#      print("Entre com a opcao:")
#      print(" --- 1: Inserir")
#      print(" --- 2: Excluir")
#      print(" --- 3: Pesquisar")
#      print(" --- 4: Exibir")
#      print(" --- 5: Sair do programa")
#      print("***********************************")
#      opcao = int(input("-> "))
#      if opcao == 1:
#           print(' ')
#           print('=======================================')
#           valor = float(input(" Informe o valor -> "))
#           tag = str(input("Informe o lado (E - Esquerdo, D - Direito)-> "))
#           text = str(input("Informe a descrição -> "))
#           date = str(input("Informe a Data -> "))
#           print('=======================================')

#           arv.inserir(tag,valor, text, date)
#      elif opcao == 2:
#           x = int(input(" Informe o valor -> "))
#           if arv.remover(x) == False:
#                print(" Valor nao encontrado!")
#      elif opcao == 3:
#           valor = float(input(" Informe o valor -> "))
#           tag = str(input(" Informe a Descrição do valor  -> "))
#           no = arv.buscar(valor,tag)
#           if no != None:
#                print(" ")
#                print('..............................')
#                print("[V] - Nó da Árvore Encontrado! ")
#                print('..............................')
#                print("==============================")
#                print("Valor: ",no.item)
#                print("Descrição: ",no.text)
#                print("Data: ",no.date)
#                print("==============================")       

               
#           else:
#                print(" ")
#                print('..................................')
#                print("[X] - Nó da Árvore Não Encontrado! ")
#                print('..................................')	 
#      elif opcao == 4:
#           arv.caminhar()
#      elif opcao == 5:
#           break
janela.mainloop()