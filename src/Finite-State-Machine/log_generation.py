from genericpath import exists
import finite_state_transducer as fst
import random
from pickle import *

states = ['q0', 'q1', 'q2', 'q3']
initial_state = 'q0'
final_states = []

inputs = ['a', 'b']
outputs = ['0', '1']

transitions =  {'q0': {'a': {'output': '0', 'next_state': 'q1'}, 'b': {'output': '1', 'next_state': 'q0'}},
                'q1': {'a': {'output': '1', 'next_state': 'q2'}, 'b': {'output': '0', 'next_state': 'q1'}},
                'q2': {'a': {'output': '0', 'next_state': 'q3'}, 'b': {'output': '1', 'next_state': 'q2'}},
                'q3': {'a': {'output': '1', 'next_state': 'q1'}}}

state_machine = fst.FiniteStateTransducer(states, inputs, outputs, transitions, initial_state, final_states)
print(state_machine)

state_machine.add_transition({'init_state': 'q3', 'input': 'b', 'output': '0', 'next_state': 'q0'})
print(state_machine)

LOG_LENGTH_MIN = 5
LOG_LENGTH_MAX = 15

def get_log(state_machine, length=random.randint(LOG_LENGTH_MIN, LOG_LENGTH_MAX)) :
    log = []
    state = state_machine.initial_state

    for i in range(length) :
        input = random.choice(state_machine.inputs)
        output = state_machine.transitions[state][input]['output']
        log.append((state, input, output))
        state = state_machine.transitions[state][input]['next_state']
        if state in state_machine.final_states :
            break
    return log

def logs_generator(state_machine, n, length=random.randint(LOG_LENGTH_MIN, LOG_LENGTH_MAX)) :
    logs = []
    for i in range(n) :
        logs.append(get_log(state_machine, length))
    return logs

def reformate(logs) :
        new_logs = []
        for log in logs :
            entry = []
            out = []
            for i in range(len(log)) :
                entry.append(log[i][1])
                out.append(log[i][2])
            new_logs.append([entry, out])
        return new_logs

if __name__=="__main__":
    logs = logs_generator(state_machine, 10)

    print()
    print("Génération de {} logs\n".format(len(logs)))
    for log in logs :
        print("Longueur du log : {}".format(len(log)))
        print("Log : {}\n".format(log))
    print(logs)

    new_logs = reformate(logs)
    print(new_logs)

    #get logs
    data = logs_generator(state_machine, 10000, 30)
    data = reformate(data)

    #save data
    f = open("data.txt", "wb")
    dump(data, f)
    f.close
