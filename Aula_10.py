# primeiro criamos uma variável para receber o valor hexadecimal que queremos converter para decimal
    # podia ter sido um do tipo input(), não é mesmo? Podemos mudar isto na continuação da aula
#valor_hexa = input("favor coloque um valor em hexadecimal: \n").upper()
entrada = "ff".upper()

hex_valido = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# para ler cada casa do valor hexa separadamente usamos um loop FOR
# para ler do valor do seu digito menos significativo para o maior invertemos a leitura do valor hexadecimal
    # esta inversão se veio por meio de valor_hexa[::-1]
inverted = entrada[::-1]
valor_final = 0
valor_pos = 0
for digito in inverted:
    #print("item: ", item, 'index do item: ' , inverted.index(item))
    # ^^^imprima a linha acima para ver como a lista está sendo lida e o valor dos seus indices^^^

    #----------------------------------------------------------------------------------------------------
    # para cada digito do valor temos sua equivalencia em decimal para isto usamos o calculo da colinha anexa ao email
    # seu valor será a posição dele na lista HEXADECIMAIS, multiplicado por 16 elevado por sua posição em casa decimal
    if digito in hex_valido:
        hexadecimal = hex_valido.index(digito)
        #print("index",index,"item: ", item, 'index do item: ' , inverted.index(item))
        # ^^^imprima a linha acima para ver tdos valores necessários para calcular a equivalencia hexadecimal^^^
        calculo = hexadecimal * pow(16, valor_pos)
        print("item: ", digito, "valor: ", calculo)
        valor_final = valor_final + calculo
    else:
        print("o valor não é um hexa")
    valor_pos += 1
print("o valor em decimal equivale à: ", valor_final)