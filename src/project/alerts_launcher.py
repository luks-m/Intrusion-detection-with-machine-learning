from utils import is_accepted

import finite_state_transducer as fst

from generator import inputs

states=['q0','q1','q2','q3','q4']
initial_state='q0'
final_states=['q4']

outputs=[]

transitions =  {'q0': {'a1': {'next_state': 'q1'}, 'a2': {'next_state': 'q0'}, 'a3': {'next_state': 'q3'}, 'a4': {'next_state': 'q1'}},
                'q1': {'a0': {'next_state': 'q4'}, 'a2': {'next_state': 'q3'}, 'a3': {'next_state': 'q1'}, 'a4': {'next_state': 'q2'}},
                'q2': {'a0': {'next_state': 'q4'}, 'a1': {'next_state': 'q3'}, 'a2': {'next_state': 'q1'}, 'a3': {'next_state': 'q4'}},
                'q3': {'a2': {'next_state': 'q3'}, 'a3': {'next_state': 'q0'}, 'a4': {'next_state': 'q3'}},
                'q4': {'a0': {'next_state': 'q4'}, 'a1': {'next_state': 'q0'}, 'a3': {'next_state': 'q2'}, 'a4': {'next_state': 'q4'}}}

state_machine = fst.FiniteStateTransducer(states, inputs, outputs, transitions, initial_state, final_states)
print(state_machine)

def is_alert(log, state_machine=state_machine) :
    print("\n Alert : \n", log)
    accepted = is_accepted(state_machine, log)
    print("Accepted : \n", accepted)
    return accepted


