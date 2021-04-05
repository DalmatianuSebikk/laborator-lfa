# cititor pentru elementele din INPUT.TXT
def dfaReader(stringCitire):

    nrNoduri = 0
    nrTranzitii = 0
    states = []
    inputs = []
    transitions = {}
    initial_state = 0 # o sa-i dau valoare mai tarziu
    final_states = []
    words_list = []

    with open(stringCitire) as f:

        lines = f.readlines()
        #1. eliminam \n
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n','')
        
        #2. in functie de linia pe care suntem, facem ceva
        for i in range(len(lines)):

            if i == 0:
                # daca suntem pe prima linie (sau linia 0, na, suntem in lista) luam pe n si m
                nums = lines[i].split()
                nrNoduri = int(nums[0])
                nrTranzitii = int(nums[1])
                # print("noduri:" + str(nrNoduri) + ", tranzitii:" + str(nrTranzitii))

            elif i <= nrTranzitii:
                # altfel, cat timp nu depasesc 
                listOfTransitions = lines[i].split()
                # primele doua sunt stari, a 3-a e tranzitia

                # verificam tranzitiile intai
                if int(listOfTransitions[0]) not in states:
                    states.append(int(listOfTransitions[0]))
                if int(listOfTransitions[1]) not in states:
                    states.append(int(listOfTransitions[1]))
                
                if int(listOfTransitions[2] not in inputs):
                    inputs.append(listOfTransitions[2])

                # facem dictionarul
                if listOfTransitions[0] not in transitions:
                    transitions[listOfTransitions[0]] = []
                    transitions[listOfTransitions[0]].append({listOfTransitions[2]: listOfTransitions[1]})
                else:
                    transitions[listOfTransitions[0]].append({listOfTransitions[2]: listOfTransitions[1]})
            
            # altfel, citesc starea initiala
            elif i == nrTranzitii + 1:
                initial_state = lines[i]
            
            # altfel, citesc nr de stari finale si starile finale
            elif i == nrTranzitii + 2:
                stari_finale = lines[i].split()
                length = stari_finale[0] # nu fac nimic cu el, doar il dau afara

                for j in range(1, len(stari_finale)):
                    final_states.append(stari_finale[j])

            #altfel, citesc cuvintele
            elif i > nrTranzitii + 3:
                words_list.append(lines[i])

    return states, inputs, transitions, initial_state, final_states, words_list

