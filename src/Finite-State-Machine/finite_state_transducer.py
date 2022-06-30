class FiniteStateTransducer :
    def __init__(self, states, inputs, outputs, transitions, initial_state, final_states) :
        self.states = states
        self.inputs = inputs
        self.outputs = outputs
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def __str__(self) :
        return "FiniteStateTransducer(\n\
            states={}\n\
            inputs={}\n\
            outputs{}\n\
            transitions={}\n\
            initial_state={}\n\
            final_states={})".format(self.states, self.inputs, self.outputs, self.transitions, self.initial_state, self.final_states)

    def add_state(self, state) :
        if state not in self.states :
            self.states.append(state)
    
    def remove_state(self, state) :
        if state not in self.states :
            raise ValueError("Le state {} n'existe pas".format(state))
        else :
            self.states.remove(state)
    
    def add_input(self, input) :
        if input not in self.inputs :
            self.inputs.append(input)
    
    def remove_input(self, input) :
        if input not in self.inputs :
            raise ValueError("L'input {} n'existe pas".format(input))
        else :
            self.inputs.remove(input)

    def add_output(self, output) :
        if output not in self.outputs :
            self.outputs.append(output)
    
    def remove_output(self, output) :
        if output not in self.outputs :
            raise ValueError("L'output {} n'existe pas".format(output))
        else :
            self.outputs.remove(output)

    def add_transition(self, transition) :
        #transition should be in this format {'init_state': 'q0', 'input': 'a', 'output': '0', 'next_state': 'q1'}
        if not 'init_state' in transition or not 'input' in transition or not 'output' in transition or not 'next_state' in transition :
            raise ValueError("La transition doit être de la forme {'init_state': 'q0', 'input': 'a', 'output': '0', 'next_state': 'q1'}")

        init_state = transition['init_state']
        input = transition['input']
        output = transition['output']
        next_state = transition['next_state']

        if init_state not in self.states :
            raise ValueError("Le state {} n'existe pas".format(transition['init_state']))
        elif input not in self.inputs :
            raise ValueError("L'input {} n'existe pas".format(transition['input']))
        elif output not in self.outputs :
            raise ValueError("L'output {} n'existe pas".format(transition['output']))
        elif next_state not in self.states :
            raise ValueError("Le state {} n'existe pas".format(transition['next_state']))
        else :
            if init_state not in self.transitions : #check if a transition from this state does not already exist
                self.transitions[init_state] = {input: {'output': output, 'next_state': next_state}}
                return
            if input not in self.transitions[init_state] : #check if a transition from this state with this input does not already exist
                self.transitions[init_state][input] = {'output': output, 'next_state': next_state}
                return
            else :
                raise ValueError("Une transition existe déjà depuis le state {} avec l'input {}".format(init_state, input))

    
    def remove_transition(self, transition) :
        #transition should be in this format {'init_state': 'q0', 'input': 'a', 'output': '0', 'next_state': 'q1'}
        if not 'init_state' in transition or not 'input' in transition or not 'output' in transition or not 'next_state' in transition :
            raise ValueError("La transition doit être de la forme {'init_state': 'q0', 'input': 'a', 'output': '0', 'next_state': 'q1'}")
        
        init_state = transition['init_state']
        input = transition['input']
        output = transition['output']
        next_state = transition['next_state']

        if init_state not in self.transitions :
            raise ValueError("Aucune transition existe depuis le state {}".format(init_state))
        if input not in self.transitions[init_state] :
            raise ValueError("Aucune transition existe depuis le state {} avec l'input {}".format(init_state, input))
        else :
            del self.transitions[init_state][input]

    def change_initial_state(self, state) :
        if state not in self.states :
            raise ValueError("Le state {} n'existe pas".format(state))
        else :
            self.initial_state = state
    
    def add_final_state(self, state) :
        if state not in self.states :
            raise ValueError("Le state {} n'existe pas".format(state))
        else :
            self.final_states.append(state)
    
    def remove_final_state(self, state) :
        if state not in self.states :
            raise ValueError("Le state {} n'existe pas".format(state))
        elif state not in self.final_states :
            raise ValueError("Le state {} n'est pas un état final".format(state))
        else :
            self.final_states.remove(state)

    

    
