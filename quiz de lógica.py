print("Seja bem vindo ao Quiz de Lógica!")
answer_user = input("Quer começar? (S/N) ")
print(answer_user)

if answer_user.upper() != "S":
    quit()

score = 0

print("Começando...")
print("Num avião há 4 romanos e 1 inglês. Qual o nome da aeromoça? \n (A) Ivanir \n (B) Ivana \n (C) Ivone \n (D) Ivete \n")
answer_1 = input ("Resposta: ")

if answer_1.upper() == "C":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print("Uma vela pode ficar acesa durante duas horas. Por quantas horas ficariam acesas duas velas do mesmo tamanho e acesas ao mesmo tempo? \n (A) 4 horas \n (B) 2 horas e meia \n (C) 3 horas \n (D) 2 horas \n")
answer_2 = input ("Resposta: ")

if answer_2.upper() == "D":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print("Um ciclista correu dois quilômetros numa antiga bicicleta de roda grande na frente e pequena atrás. Qual das duas rodas andou mais depressa? \n (A) As de trás \n (B) As da frente \n (C) As duas andam iguais \n (D) Nenhuma das duas \n")
answer_3 = input ("Resposta: ")

if answer_3.upper() == "C":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print("Se à 5 dias foi um dia antes de sábado, que dia será depois de amanhã? \n (A) Quarta-feira \n (B) Domingo \n (C) Terça-feira \n (D) Quinta-feira \n")
answer_4 = input ("Resposta: ")

if answer_4.upper() == "A":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print("Quantos noves tem de 0 a 100? \n (A) 10 \n (B) 20 \n (C) 09 \n (D) 19 \n")
answer_5 = input ("Resposta: ")

if answer_5.upper() == "B":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")


print(f"O quiz acabou! Sua pontuação é... {score} de 5!")
