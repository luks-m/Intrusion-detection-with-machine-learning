import sys
sys.path.append('./../Finite-State-Machine/')
import finite_state_transducer as fst

def is_accepted(state_machine, log) :
    state = state_machine.initial_state
    for i in range(len(log)):
        input = log[i]
        if input in state_machine.transitions[state] :
            state = state_machine.transitions[state][input]['next_state']
        else:
            return False
    return state_machine.is_final_state(state)
