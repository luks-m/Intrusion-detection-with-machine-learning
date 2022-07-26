from utils import is_accepted

import finite_state_transducer as fst

from generator import inputs

states=['q0','q1']
initial_state='q0'
final_states=['q1']

outputs=[]

transitions =  {'q0': {'a0': {'next_state': 'q1'}, 'a1': {'next_state': 'q0'}, 'a2': {'next_state': 'q0'}, 'a3': {'next_state': 'q0'}, 'a4': {'next_state': 'q0'}},
                'q1': {'a0': {'next_state': 'q1'}, 'a1': {'next_state': 'q0'}, 'a2': {'next_state': 'q0'}, 'a3': {'next_state': 'q0'}, 'a4': {'next_state': 'q0'}}}

state_machine = fst.FiniteStateTransducer(states, inputs, outputs, transitions, initial_state, final_states)
print(state_machine)

def is_attack(log, state_machine=state_machine) :
    print("\n Received : \n", log)
    accepted = is_accepted(state_machine, log)
    print("Attack : \n", accepted)
    return accepted
