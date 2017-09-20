import math
print("Nome:Felipe Leao.\nDisciplina:Fisica I.\nCurso:Ciencia da Computacao.\nTurma:3 Periodo.\n")
print("\n")
print("----Lancamento de Projetil----\n")
print("\n")

v0 = float(input("Forneca a velocidade inicial(m/s):\n"))
if v0<0:
	input("Forneca um valor positivo para a velocidade.\n O programa fechará")
	sys.exit(0)
g = float(input("Agora, a aceleracao(m/s^2):\n"))
if g<0:
	input("\aNeste caso, a=-g,a gravidade nao pode ser negativa.\n O programa fechará")
	sys.exit(0)
if g==0:
	input("Forneca outro valor para a aceleracao.\n O programa fechará")
	sys.exit(0)
angulo = float(input("E, finalmente, forneça um angulo em graus(°)\n"))
#radianos = (angulo)
radianos = (angulo * math.pi)/180
print("\n\n")
print("----  Dados  ----\n")
print("Velocidade(m/s):%f\n",v0)
print("Aceleracao(m/s^2):%f\n",g)
print("Angulo(°):%f\n",angulo)
print("----  Dados  ----")
while True:
	print("Escolha uma das opções:\n1)Calcular a Altura Maxima\n2)Calcular o tempo de voo\n3)Calcular o alcance horizontal.\n4)Sair.\n")
	user_input = input("Opção: ")
	if user_input == "1":
		sen= math.sin(radianos)
		yxm= ((math.pow(v0,2)*(math.pow(sen,2)))/(2*g))
		print("\aAltura máxima(m)=\n", + ymax)
		input("")
	elif user_input == "2":
		sen= math.sin(radianos)
		t=((2*v0*sen)/g)
		print("\aTempo de voo(s)=\n", + t)
		input("")
	elif user_input == "3":
		cosen=math.cos(radianos)
		sen= math.sin(radianos)
		xf=(2*math.pow(v0,2)*(cosen*sen)/g)
		print("\aAlcance Horizontal(m)=\n", + xf)
		input("")
	elif user_input == "4":
		break
	else:
		print("Comando desconhecido")
		break