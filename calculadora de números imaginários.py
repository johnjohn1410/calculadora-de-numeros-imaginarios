while True:
    conta= input("Insira aqui o tipo de conta que você quer fazer \n 1=Adição \n 2=Subtração \n 3=Multiplicação\n 4=Produto Notável\n Digite\'sair\' para encerrar o programa \n")

    if conta.lower() == 'sair':
        print("Encerrando o programa...")
        break

    if conta not in ('1', '2', '3', '4'):
        print("Valor inválido, favor selecionar uma das opções abaixo:")
    else:
            if conta=='1':
                a = float(input("Insira o valor real do primeiro número complexo: "))
                b = float(input("Insira o valor imaginário do primeiro número complexo: "))
                c = float(input("Insira o valor real do segundo número complexo: "))
                d = float(input("Insira o valor imaginário do segundo número complexo: "))
                soma_real= a+c
                soma_imag= b+d
                if soma_imag<0:
                    print(f"\nO resultado é: {soma_real}{soma_imag}i\n")
                else:
                    print(f"\nO resultado é: {soma_real}+{soma_imag}i\n")

            if conta=='2':
                a = float(input("Insira o valor real do primeiro número complexo: "))
                b = float(input("Insira o valor imaginário do primeiro número complexo: "))
                c = float(input("Insira o valor real do segundo número complexo: "))
                d = float(input("Insira o valor imaginário do segundo número complexo: "))
                sub_real= a-c
                sub_imag= b-d
                if sub_imag<0:
                    print(f"\nO resultado é: {sub_real}{sub_imag}i\n")
                else:
                    print(f"\nO resultado é: {sub_real}+{sub_imag}i\n")

            if conta=='3':
                a = float(input("Insira o valor real do primeiro número complexo: "))
                b = float(input("Insira o valor imaginário do primeiro número complexo: "))
                c = float(input("Insira o valor real do segundo número complexo: "))
                d = float(input("Insira o valor imaginário do segundo número complexo: "))
                mult_real= (a*c - b*d)
                mult_imag= (a*d + c*b)
                if mult_imag<0:
                    print(f"\nO resultado é: {mult_real}{mult_imag}i\n")
                else:
                    print(f"\nO resultado é: {mult_real}+{mult_imag}i\n")

            if conta=='4':
                a = int(input("Insira o valor real do número complexo: "))
                b = int(input("Insira o valor imaginário do número complexo: "))
                pot=int(input("Qual a potência da conta?"))
                if pot == 2:
                    pot2_pt1= a**2
                    pot2_pt2 = 2*a*b
                    pot2_pt3 = int(-(b ** 2))

                    pot2_sum1=pot2_pt1+pot2_pt3
                    if pot2_pt2<0:
                        print(f"\n O resultado é:{pot2_sum1}{pot2_pt2}i")
                    else:
                        print(f"\n O resultado é:{pot2_sum1}+{pot2_pt2}i")
                if pot == 3:
                    pot3_pt1 = int(a ** 3)
                    pot3_pt2 = int(3 * (a**2) * b)
                    pot3_pt3 = int(-3 * (b**2) * a)
                    pot3_pt4 = int(-b ** 3)

                    pot3_sum1 = int(pot3_pt1 + pot3_pt3)
                    pot3_sum2 = int(pot3_pt2 + pot3_pt4)

                    if pot3_sum2<0:
                        print(f"\n O resultado é:{pot3_sum1}{pot3_sum2}i")
                    else:
                        print(f"\n O resultado é:{pot3_sum1}+{pot3_sum2}i")