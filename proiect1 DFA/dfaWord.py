import dfaReader

states, inputs, transitions, initial_state, final_states, words_list = dfaReader.dfaReader("input.txt")

# codul devine un spaghetti, deci o sa l comentez cat de mult pot
for word in words_list:
    # traseul e lista de noduri pe care o vom afisa
    traseu = []
    #consideram current_state starea initiala, pentru ca de acolo pornim mereu
    current_state = initial_state
    traseu.append(initial_state) # adaugam ca sa nu avem probleme, pt ca de la starea initiala incepem clar :))

    # trecem prin fiecare simbol din cuvantul dat
    for simbol in word:
        # gasit are rolul de a monitoriza daca gasim sau nu probleme pe parcurs (de ex un simbol care nu are treaba)
        gasit = 0
        # traversam lista de dictionare a carei cheie este current_state
        for index in range(len(transitions[current_state])):
            # traversam lista si verificam fiecare dictionar (mai bine cred ca faceam tuplu)
            if simbol in transitions[current_state][index]:
                #daca gasim un dictionar cu cheie simbol, modificam current_state, il adaugam in traseu si plecam la urmatorul simbol
                current_state = transitions[current_state][index][simbol]
                traseu.append(current_state)
                gasit = 1

                # mai verificam daca ajungem la final sa putem afisa tot traseul si iesim
                if current_state in final_states:
                    # e ok, putem afisa
                    print("DA")
                    stringPrint = ""
                    for nod in traseu:
                        stringPrint += nod
                        stringPrint += ' '
                    print(stringPrint)
                    break
                else:
                    break
        #daca exista probleme cu gasitul, iesim din cuvant, ca nu e acceptat
        if gasit == 0:
            print("NU")
            break

    

        
        
        
                    



