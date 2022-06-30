def maquinaDeTuring (inicial = None,
                     regras = [],
                     fitas = [],
                     final = None,
                     numfitas = 1):
    posicao = 0
    branco = '□'
    #Armazena o estado atual
    st = inicial
    #Armazena a quantidade de fitas
    numfitas = len(fitas)
    i = 0
    
    for fita in fitas:
        print(i)

        if numfitas == 2 :
            #Reorganiza as regras de transições
            if i == 0 : regras = dict (((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, v2, v3, dr1, s1) in regras)
            else :
                posicao = 0
                #Reorganiza as regras de transições
                dict (((s0, v2), (v3, dr1, s1)) for (s0, v0, v1, dr, v2, v3, dr1, s1) in regras)
        #Reorganiza as regras de transições
        else : regras = dict (((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in regras)
        
        if not fita: fita = [branco]
        if posicao < 0 : posicao += len(fita)
        if posicao >= len(fita) or posicao < 0 : raise Error ("A fita se inícia em uma posição inválida")

        while True:
            print (st, '\t', end = " ")
            for i, v in enumerate(fita):
                if i == posicao : print ("[%s]" %(v, ), end = " ")
                else : print (v, end = " ")
            print()

            if st == final : break
            if (st, fita[posicao]) not in regras : break

            (v1, dr, s1) = regras[(st, fita[posicao])]
            fita[posicao] = v1

            if dr == 'left':
                if posicao > 0 : posicao -= 1
                else : fita.insert(0, branco)
            if dr == 'right':
                posicao += 1
                if posicao >= len(fita) : fita.append(branco)
            if dr == 'static':
                posicao = posicao

            st = s1
        i += 1

    #Se for máquina por estado final
    if final != None :
        #Se for o estado for final Aceita
        if st == final : print("Aceita")
        else: print("Rejeita")


print ("\n Máquina 1:")

maquinaDeTuring(inicial = 'q0',
                    fitas = [list("□abb□")],
                    final = 'q6',
                    regras = map(tuple,
                                 [
                                     "q0 □ □ right q1".split(),
                                     "q1 a □ right q2".split(),
                                     "q1 □ □ right q6".split(),
                                     "q2 a a right q2".split(),
                                     "q2 b b right q2".split(),
                                     "q2 □ □ left q3".split(),
                                     "q3 b □ left q4".split(),
                                     "q4 b □ left q5".split(),
                                     "q5 a a left q5".split(),
                                     "q5 b b left q5".split(),
                                     "q5 □ □ right q1".split(),
                                 ]
                                )
                    )


print ("\n Máquina 2:")

maquinaDeTuring(inicial = 'q0',
                    fitas = [list("□aabbaabb□")],
                    final = 'q7',
                    regras = map(tuple,
                                 [
                                     "q0 □ □ right q1".split(),
                                     "q1 X X right q1".split(),
                                     "q1 Y Y right q1".split(),
                                     "q1 a X right q2".split(),
                                     "q1 b Y right q6".split(),
                                     "q1 □ □ right q7".split(),
                                     "q2 Y Y right q2".split(),
                                     "q2 a a right q2".split(),
                                     "q2 b Y right q3".split(),
                                     "q3 X X right q3".split(),
                                     "q3 b b right q3".split(),
                                     "q3 a X right q4".split(),
                                     "q4 Y Y right q4".split(),
                                     "q4 a a right q4".split(),
                                     "q4 b Y right q5".split(),
                                     "q5 X X left q5".split(),
                                     "q5 Y Y left q5".split(),
                                     "q5 a a left q5".split(),
                                     "q5 b b left q5".split(),
                                     "q6 X X right q6".split(),
                                     "q6 Y Y right q6".split(),
                                     "q6 b Y left q5".split(),
                                     "q5 □ □ right q1".split(),
                                 ]
                                )
                    )

print ("\n Máquina 3:")

maquinaDeTuring(inicial = 'q0',
                    fitas = [list("□aabbbbaabbbb□")],
                    final = None,
                    regras = map(tuple,
                                 [
                                     "q0 □ □ right q1".split(),
                                     "q1 X X right q1".split(),
                                     "q1 Y Y right q1".split(),
                                     "q1 a X right q2".split(),
                                     "q1 b Y right q6".split(),
                                     "q1 □ □ right q7".split(),
                                     "q2 Y Y right q2".split(),
                                     "q2 a a right q2".split(),
                                     "q2 b Y right q3".split(),
                                     "q2 X X right q9".split(),
                                     "q2 □ □ right q9".split(),
                                     "q3 X X right q3".split(),
                                     "q3 b b right q3".split(),
                                     "q3 a X right q4".split(),
                                     "q3 Y Y right q9".split(),
                                     "q3 □ □ right q9".split(),
                                     "q4 Y Y right q4".split(),
                                     "q4 a a right q4".split(),
                                     "q4 b Y right q5".split(),
                                     "q4 X X right q9".split(),
                                     "q4 □ □ right q9".split(),
                                     "q5 X X left q5".split(),
                                     "q5 Y Y left q5".split(),
                                     "q5 a a left q5".split(),
                                     "q5 b b left q5".split(),
                                     "q6 X X right q6".split(),
                                     "q6 Y Y right q6".split(),
                                     "q6 b Y left q5".split(),
                                     "q6 a a right q8".split(),
                                     "q6 □ □ right q8".split(),
                                     "q5 □ □ right q1".split(),
                                     "q9 □ □ right q9".split(),
                                     "q9 a a right q9".split(),
                                     "q9 b b right q9".split(),
                                     "q9 Y Y right q9".split(),
                                     "q9 X X right q9".split(),
                                 ]
                                )
                    )


print ("\n Máquina 5:")

maquinaDeTuring(inicial = 'q0',
                    fitas = [list("□aaaabc□")],
                    final = None,
                    regras = map(tuple,
                                 [
                                     "q0 □ □ right q1".split(),
                                     "q1 □ □ right q1".split(),
                                     "q1 a a right q1".split(),
                                     "q1 b b right q1".split(),
                                     "q1 c c left q2".split(),
                                     "q2 a b left q2".split(),
                                     "q2 b a left q2".split(),
                                 ]
                                )
                    )

print ("\n Máquina 4:")

maquinaDeTuring(inicial = 'q0',
                    fitas = [list("□abc□"), list("□□")],
                    final = 'q4',
                    regras = map(tuple,
                                 [
                                     "q0 □ □ right □ □ right q1".split(),
                                     "q1 a a right a □ right q1".split(),
                                     "q1 b b static □ □ left q2".split(),
                                     "q2 b b right a X left q2".split(),
                                     "q2 c c static □ □ right q3".split(),
                                     "q3 c c right X Z right q3".split(),
                                     "q3 □ □ static □ □ static q4".split(),
                                 ]
                                )
                    )
        
    
