#Gabriel Phelipe Costa Freitas
import os

def cria_matriz(boolvet):
#Função para criar a matriz ou o vetor
	# boolvet é uma flag para determinar se é matriz ou vetor
	print()
	print("Qual o tamanho de sua matriz/vetor estocástico?")
	if(boolvet==0): #cria-se uma matriz
		n_linhas=int(input())
		n_colunas=n_linhas
		matriz=[]
		for i in range(n_linhas):
			linha=[]
			for j in range(n_colunas):
				linha.append(0.00) # A matriz se inicializa com zero
			matriz.append(linha)
		return matriz,n_linhas,n_colunas
	else: #cria-se um vetor
		vet=[]
		tam=int(input())
		for i in range(tam):
			vet.append(0.00) # O vetor se inicializa com zero
		return vet,tam

def desenha_menu():
#Função para desenhar o menu
	print()
	print("====================================")
	print("1 - Criar Matriz de Transição")
	print("2 - Criar Vetor Inicial")
	print("3 - Preencher Matriz")
	print("4 - Preencher Vetor")
	print("5 - Mostrar dados já fornecidos")
	print("6 - Realizar predição")
	print("7 - Equação de CHAPMAN")
	print()
	print("8 - Deletar Matriz")
	print("9 - Deletar Vetor")
	print("0 - Sair")
	print("====================================")

def le_matriz(matriz):
#Função para ler a matriz
	print()

	n_linhas=len(matriz)
	n_colunas=len(matriz[0])
	for i in range(n_linhas):
		print()
		for j in range(n_colunas):
			if(j==0):
				print("| " + str(matriz[i][j]), end = " ")
			elif(j==n_colunas-1):
				print(str(matriz[i][j]) + " |")
			else:
				print(matriz[i][j], end=" ")
	print()

def le_vetor(vet,tam):
#Função para ler a matriz
	print()

	for i in range(tam):
			if(i==0):
				print("| " + str(vet[i]), end = " ")
			elif(i==tam-1):
				print(str(vet[i]) + " |")
			else:
				print(vet[i], end=" ")
	print()


def checa_estoc(matriz):
#checa se a matriz é estocástica
	
	n_linhas=len(matriz)
	n_colunas=len(matriz[0])
	cont=0.0
	estocastica=True
	for i in range(n_linhas):
		for j in range(n_colunas):
			print("Matriz na posicao[%d]" %i + "[%d]" %j + " = " + str(matriz[i][j]))
			cont=round(cont,3)+round(matriz[i][j],3)
		if not cont==1:
			estocastica=False
			break
		cont=0.0
	return estocastica


def preenche_matriz(matriz):
#Função para preencher a matriz

	os.system('clear')
	lin=len(matriz)
	col=len(matriz[0])
	print("Informe as probabilidades para cada")
	print("transição solicitada.")
	for i in range(lin):
		for j in range(col):
			print("P" + str(i) +str(j))
			p=float(input())
			p=round(p,3)
			matriz[i][j]=p
	os.system('clear')

def preenche_vetor(vetor,tam):
#Função para preencher a matriz

	os.system('clear')
	print("Informe os valores do vetor inicial")
	for i in range(tam):
		print("P" + str(i))
		p=float(input())
		p=round(p,3)
		vetor[i]=p
	os.system('clear')

def mult_vet_mat(vet,tam_v,mat):
#Função para multiplicar o vetor pela matriz
	lin=len(mat)
	col=len(mat[0])
	result=[]

	if(col==tam_v):
		for j in range(tam_v):
			val=0
			for i in range(lin):
				mult=(round(vet[i],3)*round(mat[i][j],3))
				val=round(val,3)+round(mult,3)
			result.append(round(val,3))
		return result
	else:
		print("ERROR, verifique o tamanho de seu vetor")	

def mult_mat(mat1,mat2):
	lin1=len(mat1)
	col1=len(mat1[0])
	lin2=len(mat1)
	col2=len(mat1[0])

	if(col1==lin2):
		res=[]
		for i in range(lin1):
			linha=[]
			for j in range(col2):
				linha.append(0.0) # A matriz se inicializa com zero
			res.append(linha)
		for i in range(lin1):
			for j in range(col1):
				val=0
				for k in range(col2):
					val=round(val,3)+(round(mat1[i][k],3)*round(mat2[k][j],3))
					res[i][j]=round(val,3)
		return res
	else:
		print("Impossivel realizar operação de multiplicação")


def chapman_call(mat,numes):
#Primeira chamada para a função de chapman
	print()
	print("OBS: Estados vão de 0 até N")
	print()
	print("Dado que Pij^(m) é o que se deseja")
	print("calcular na equação de chapman, forneça")
	print("O valor de i da equação:")
	ei=int(input())
	print("O valor de j da equação:")
	ef=int(input())
	print("o número de passos: ")
	pas=int(input())
	prob=extend_chapman(ei,ef,pas,mat,numes)
	os.system('clear')
	print()
	print("O valor de P%d"%ei + "%d"%ef + " em %d passos é:"%pas)
	print(round(prob,3))

def extend_chapman(ei,ef,pas,mat,numes):
#Função de recursão para chapman
	# mat = matriz de transição
	# ei = estado inicial 
	# ef = stado final
	# pas = numero de passos 
	# numes = numero de estados
	prob=0.0
	if(not pas<=1):
		for k in range(numes):
			prob=round(prob,4)+(round(mat[ei][k],4)*round(extend_chapman(k,ef,pas-1,mat,numes),4))
		return round(prob,3)
	else:
		return round(mat[ei][ef],3)

#================== MAIN ==================#
os.system('clear')
var=-1
cria_m=0
cria_v=0
while(not var==0):
	desenha_menu()
	var=int(input())
	if(var==1):
		if(cria_m==0):
			cria_m=1
			mat,linha,coluna=cria_matriz(0)
			os.system('clear')
			print('~~~~Sua matriz foi criada com valores "0.0"~~~~')
			print('~~~~você pode editá-la preenchendo os valores~~')
		else:
			os.system('clear')
			print("A matriz já foi criada anteriormente")
	elif(var==2):
		if(cria_v==0):
			cria_v=1
			vetor,tam=cria_matriz(1)
			os.system('clear')
			print('~~~~Seu vetor foi criado com valores "0.0"~~~~')
			print('~~~~você pode editá-lo preenchendo os valores~~')
		else:
			os.system('clear')
			print("O vetor já foi criado anteriormente")			
	elif(var==3):
		if(cria_m==0):
			os.system('clear')
			print("Crie sua matriz primeiro :)")
		else:
			os.system('clear')
			preenche_matriz(mat)
			le_matriz(mat)
	elif(var==4):
		if(cria_v==0):
			os.system('clear')
			print("Crie seu vetor primeiro :)")
		else:
			os.system('clear')
			preenche_vetor(vetor,tam)
			le_vetor(vetor,tam)
	elif(var==5):
		os.system('clear')
		if(cria_m==0 and cria_v==0):
			print()
			print("Sem dados fornecidos:(")
		else:
			if(not cria_m==0):
				le_matriz(mat)
			if(not cria_v==0):
				le_vetor(vetor,tam)
	elif(var==6):
		if(not cria_m==0):
			if(checa_estoc(mat)==True):
				os.system('clear')
				print("Em quantos passos deve-se realizar a predição?")
				passos=int(input())
				if(passos>0):
					if(cria_v==0):
						os.system('clear')
						res=mat
						for i in range(passos-1):
							res=mult_mat(res,mat)
						print("Matriz Original:")
						le_matriz(mat)
						print("Matriz de transição gerada:")
						le_matriz(res)
						print("Número de passos:")
						print(passos)
					elif(cria_v==1):
						os.system('clear')
						res=mat
						for i in range(passos-1):
							res=mult_mat(res,mat)
						print("Matriz em %d passos: " %passos)
						le_matriz(res)
						resultado=mult_vet_mat(vetor,tam,res)
						print("Matriz Original:")
						le_matriz(mat)
						print("Vetor inicial:")
						le_vetor(vetor,tam)
						print("Transições geradas:")
						le_vetor(resultado,tam)
						print("Número de passos:")
						print(passos)
				else:
					os.system('clear')
					print("Valor inválido :(")
					print()
			else:
				os.system('clear')
				print("Sua matriz não é estocástica :(")
		else:
			os.system('clear')
			print()
			print("Você precisa da matriz de transição (ツ)")
	elif(var==7):
		os.system('clear')
		chapman_call(mat,linha)
	elif(var==8):
		os.system('clear')
		mat=None
		cria_m=0
	elif(var==9):
		os.system('clear')
		vet=None
		cria_v=0
	elif(var==0):
		break
	else:
		os.system('clear')
		print("???????")
os.system('clear')