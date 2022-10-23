print("VERDADEIRO OU FALSO");
print("saiba se é alfanumerico,numerico,decinal,letra minuscula,espaço em branco e letras maisculas")

n=input("digite alguma coisa para saber se é verdadeiro ou falso: ");
print("tipo primitivo:{}.".format(type(n)))

print("É alfanumerico?{}.".format(n.isalpha()))

print("É numerico?{}.".format(n.isnumeric()))

print("É decimal?{}.".format(n.isdecimal()))

print("Esta em caixa alta?{}.".format(n.isupper()))

print("Esta em caixa baixa?{}.".format(n.islower()))

print("Esta em branco?{}.".format(n.isspace()))

