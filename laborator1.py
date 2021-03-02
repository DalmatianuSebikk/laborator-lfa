sigma = []
states = []
transitions = []
nrErori = 0

with open('fisier.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace('\t', '')

    for i in range(len(lines)):
        if lines[i].startswith('#'):
            pass
        elif lines[i].startswith('Sigma'):
            for j in range(i + 1, len(lines)):
                if lines[j] != '':
                    if 'End' not in lines[j]:
                        sigma.append(lines[j])
                    else:
                        i = j
                        break
        
        elif lines[i].startswith('States'):
            for j in range(i + 1, len(lines)):
                if lines[j] != '':
                    if 'End' not in lines[j]:
                        states.append(lines[j])
                    else:
                        i = j
                        break
        
        elif lines[i].startswith('Transitions'):
            for j in range(i + 1, len(lines)):
                if lines[j] != '':
                    if 'End' not in lines[j]:
                        transitions.append(lines[j])
                    else:
                        i = j
                        break

    aparitiiS = 0
    aparitiiF = 0
    for state in states:
        if state[len(state) - 1] == 'S':
            aparitiiS += 1
        elif state[len(state) - 1] == 'F':
            aparitiiF += 1

    if aparitiiS > 1:
        print("Nu e bine cu state: Mai multe aparitii de S")
    else:
        if aparitiiF > 0:
            pass
        else:
            print("Nu e bine cu state: NU SUNT APARITII DE F")
            nrErori += 1

    for transition in transitions:
        transition = transition.replace(',', '')
        aux = transition.split()

        # verific cuvantul
        if aux[1] not in sigma:
            print('Cuvantul ${aux[1]} nu se regaseste in sigma.')
        
        # verific primul state
        ok = 1
        ind = 0
        while(ok == 1 and ind < len(states)):
            if states[ind].startswith(aux[0]):
                ok = 0
            ind += 1
        if(ok == 1):
            print("Nu am gasit " + aux[0] + "in vreun state")
            nrErori += 1
        
        # verific al doilea state
        ok = 1
        ind = 0
        while(ok == 1 and ind < len(states)):
            if states[ind].startswith(aux[2]):
                ok = 0
            ind += 1
        if(ok == 1):
            print("Nu am gasit " + aux[2] + "in vreun state")
            nrErori += 1

    if nrErori == 0:
        print("E corect, felicitari!")

        



    
    

    
