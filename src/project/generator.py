import sys
sys.path.append('./../Finite-State-Machine/')
import random

import finite_state_transducer as fst

NB_STATES = 5
NB_INPUTS = 5

LOG_LENGTH = 5
NB_LOGS = 50

#100 states
states = []
for i in range(NB_STATES) :
    states.append('q'+str(i))

initial_state = 'q0'
final_states = []

#200 paquets for inputs
inputs = []
for i in range(NB_INPUTS) :
    inputs.append('a'+str(i))

outputs = []

transitions = {}
for i in range(NB_STATES):
    transitions['q'+str(i)] = {}
    for j in range(NB_INPUTS):
        if (i+j)%2 == 0 :
            transitions['q'+str(i)]['a'+str(j)] = {}
            transitions['q'+str(i)]['a'+str(j)]['next_state'] = 'q'+str((i+j)%NB_STATES)

state_machine = fst.FiniteStateTransducer(states, inputs, outputs, transitions, initial_state, final_states)
print(state_machine)

def get_log(state_machine, length=LOG_LENGTH) :
    log = []
    state = state_machine.initial_state

    for i in range(length) :
        input = random.choice(state_machine.get_current_inputs(state))
        log.append((state, input))
        state = state_machine.transitions[state][input]['next_state']
        if state in state_machine.final_states :
            break

    return log

def generate_logs(state_machine, nb_logs=NB_LOGS, length=LOG_LENGTH) :
    logs = []
    for i in range(nb_logs) :
        logs.append(get_log(state_machine, length))
    return logs

def reformate_logs(str_logs) :
    logs = []
    for log in str_logs :
        new_log = []
        for state, input in log :
            new_log.append(input)
        logs.append(new_log)
    return logs

if __name__=="__main__":
    logs = generate_logs(state_machine, 10, 10)
    print(logs)
    logs = reformate_logs(logs)
    print(logs)

