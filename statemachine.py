class StateMachine:
    def __init__(self):
        self.dfa = {0:{'0':0, '1':1},
            1:{'0':2, '1':0},
            2:{'0':1, '1':2}}
        self.final_state = {0:0, 1:1, 2:2}

    
    def accepts(self, str):
        state = 0
        for char in str:
            print('Current state = S{0}, Input = {1}, result state = S{2}'.format(state, char, self.dfa[state][char]))
            state = self.dfa[state][char]
        return state
    
    def check(self, string) : 
        # set function convert string into set of characters . 
        p = set(string) 
    
        # declare set of '0', '1' . 
        s = {'0', '1'} 
    
        # check set p is same as set s or set p contains only '0' or set p contains only '1' 
        # or not, if any one conditon is true then string is accepted otherwise not . 
        if s == p or p == {'0'} or p == {'1'}: 
            return True 
        else : 
            return False

    def run(self):
        print("Enter the string: ")
        str = input()
        if self.check(str) :
            state = self.accepts(str)
            if state in self.final_state :
                print('Output for state S{0} = {1}'.format(state, self.final_state[state]))
            else:
                print('Invalid input')
        else:
            print('Input string must be a binary number')

sm = StateMachine()
sm.run()