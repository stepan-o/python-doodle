#!/usr/bin/python
# based on starter code by D. Vrajitoru, C463/B551 Spring 2008
# found at https://www.cs.iusb.edu/~danav/teach/c463/goat.py

################################################################################################################
#                                                                                                              #
#                                    Game simulation: River Crossing                                           #
#                                                                                                              #
#                                                                                                              #
#       Game description:                                                                                      #
#             A farmer needs to get three items across a river: a goose, a big bag of beans, and a fox.        #
#                                                                                                              #
#       Victory conditions:                                                                                    #
#               Victory condition #1:                                                                          #
#                   goose, fox, and beans on the right side of the river                                       #
#                                                                                                              #
#       Loss conditions                                                                                        #
#               Loss condition #1:                                                                             #
#                   If left alone unsupervised with the beans, the goose will eat the beans.                   #
#               Loss condition #2:                                                                             #
#                   If left alone unsupervised with the goose, the fox will eat the goose.                     #
#               Loss condition #3:                                                                             #
#                   The boat needed to cross the river is small and rickety; the farmer and                    #
#                   one other item are all that will fit in the boat (only one item in the                     #
#                   boat at all times).                                                                        #
#                                                                                                              #
################################################################################################################
#                                                                                                              #
#                               Solution: Depth-First Search (DFS) algorithm                                   #
#                                                                                                              #
################################################################################################################


# Returns the state of the symbol who in the dictionary al. It
# returns its value and not a reference to it so it can be used for
# testing but not modified. If the symbol who is not part of the list
# it return nil.
def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


# Verifies if the state defined as an dictionary is safe. If the
# goat is on the same side as the man, then we're safe. Otherwise if
# the cabbage or the wolf is also on the other side, then we're not
# safe.
def safe_state(state):
    if (state_of('fox', state) == state_of('goose', state)) \
            and (state_of('farmer', state) != state_of('fox', state)):
        return False
    elif (state_of('goose', state) == state_of('beans', state)) \
            and state_of('farmer', state) != state_of('goose', state):
        return False
    else:
        return True


# Moves the entity from one side to the other in the sate al. It is a
# list mutator. The positions of all the entities are defined by 0
# and 1 so the move replaces the current position with 1 - it. It
# returns the resulting list.
def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


# Tests if the state has reached the goal. This is the case if all
# four entities are on the other side.
def goal_reach(state):
    if not state:
        return False
    return (state_of('farmer', state) == 'right'
            and state_of('fox', state) == 'right'
            and state_of('goose', state) == 'right'
            and state_of('beans',state) == 'right')


# Checks if child is a safe state to move into, and if it is, it adds
# it to the list of states.
def check_add_child(child, list_states):
    if safe_state(child):
        list_states.append(child)
    return list_states


def expand_states(state):
    children = []
    child = state.copy()
    # the man can also move alone
    move('farmer', child)
    check_add_child(child, children)
    for ent in entity:
        # Move one object on the same side as the man
        if state_of(ent, state) == state_of('farmer', state):
            child = state.copy()
            move('farmer', child)
            move(ent, child)
            check_add_child(child, children)
    return children


# Searches for a solution from the initial state
def search_sol(state):
    path.append(state)
    next_ = state.copy()
    while next_ and not goal_reach(next_):
        nl = expand_states(next_)
        next_ = {}
        for child in nl:
            if not (child in path):
                next_ = child
                path.append(next_)
                break
    return next_


entity = ['beans', 'goose', 'fox']
path = []
# Initialization of the global variables
initial_state = {'farmer': 'left'}
for e in entity:
    initial_state[e] = 'left'


# Construct the full olution after evaluating the previous statements
print("\n--------------- River crossing, depth-first search --------------")
print("\n------ Searching for a solution from the initial state:\n")
print(initial_state)

# To see what all the child states from the current one look like
print("\n-- First expansion of the initial state\n")
print(expand_states(initial_state))

print("\n--- Goal state reached:\n")
print(search_sol(initial_state))

# Evaluate the variable path to see the solution backwards.
print("\n--- The full path is:\n")
for s in path:
    print(s)
