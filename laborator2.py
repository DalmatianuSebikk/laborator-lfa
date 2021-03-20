import laborator1
import argparse

def get_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "dfa_config_file")
    parser.add_argument('word', help = "word_input")
    args = parser.parse_args()

    return args.file, args.word

dfa_config_file, word_input = get_line_arguments[0], get_line_arguments[1]

transitions, final_states, initial_state = laborator1.validare(dfa_config_file)

if transitions != None and final_states != None and initial_state != None:
    # e ok si poti trece la verificat cuvantul
    current_state = initial_state
    lungime = 0
    ok = 0
    for i in word_input:
        lungime +=1
        for j in transitions:
            if i == j[1] and current_state == j[0]:
                StrCrt = j[2]

                if current_state in final_states and lungime == len(word_input):
                    ok = 1
                    break
        if ok:
            print(">>accept")
            break
    if ok == 0:
        print(">>reject")





