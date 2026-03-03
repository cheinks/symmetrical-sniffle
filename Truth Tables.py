# Recognize that changing the order of P, Q, R in the sentence
# will introduce many duplicate truth tables. For example,
# P ~ (Q & R) behaves the same as (Q & R) ~ P. Thus our input
# will take the form P - Q - R.
from unittest import case


# Create the molecules
def equivalence(a, b): # 00
    return a == b
def implication(a, b): # 01
    if a: return b
    else: return not a
def conjunction(a, b): # 10
    return a and b
def disjunction(a, b): # 11
    return a or b

# Encode the molecules to 0, 1, 2, 3 so we can iterate through
# all the possible combinations of sentence.
def eval_simple(a, b, c):
    if c == 0:
        return equivalence(a, b)
    elif c == 1:
        return implication(a, b)
    elif c == 2:
        return conjunction(a, b)
    else:
        return disjunction(a, b)

# 4 binary operators, 4 options for parity of inputs
# Use first two bits (leftmost) for operator
# Use last two bits (rightmost) for parity
def evaluate(first, second, code):
    not_a = (code[2]=="1")
    not_b = (code[3]=="1")

    if not_a:
        a = not first
    else:
        a = first
    if not_b:
        b = not second
    else:
        b = second

    match code[0:2]:
        case "00":
            return equivalence(a, b)
        case "01":
            return implication(a, b)
        case "10":
            return conjunction(a, b)
        case _:
            return disjunction(a, b)


# Evaluate a sentence with the form (P - Q) - R
def input_left(P, Q, R, c1, c2):
    return eval_simple(eval_simple(P, Q, c1), R, c2)
# Evaluate a sentence with the form P - (Q - R)
def input_right(P, Q, R, c1, c2):
    return eval_simple(P, eval_simple(Q, R, c2), c1)

# Turn the int back into a string for display
def simple_decode(c):
    if c == 0:
        return "~"
    elif c == 1:
        return ">"
    elif c == 2:
        return "&"
    else:
        return "V"

# Convert the binary string into a line of text for display
def decode(code):
    result = " "
    if code[2] == "1":
        result = "\u2014"
    match code[0:2]:
        case "00":
            result += "~"
        case "01":
            result += ">"
        case "10":
            result += "&"
        case _:
            result += "V"
    if code[3] == "1":
        result += "\u2014"
    else:
        result += " "
    return result

# Return a string of the molecule for cataloging
def formula(c1, c2, notp, notq, notr, left):
    result = ""
    if left:
        result += "("
    if notp:
        result += "\u2014"
    result += ("P" + simple_decode(c1))
    if not left:
        result += "("
    if notq:
        result += "\u2014"
    result += "Q"
    if left:
        result += ")"
    result += simple_decode(c2)
    if notr:
        result += "\u2014"
    result += "R"
    if not left:
        result += ")"
    return result

# Construct the truth table for a sentence, provided whether
# an input is being negated
def tabulate_left(c1, c2, notp, notq, notr):
    p_list = [True, False]
    if notp:
        p_list = [False, True]
    q_list = [True, False]
    if notq:
        q_list = [False, True]
    r_list = [True, False]
    if notr:
        r_list = [False, True]

    result = ""
    # Loop through the three inputs
    for P in p_list:
        for Q in q_list:
            for R in r_list:
                # Evaluate the current iteration
                out = input_left(P, Q, R, c1, c2)
                # Append a 0 if true
                if out:
                    result += "0"
                # Or a 1 if false
                else:
                    result += "1"

    return int(result, 2)

def tabulate_right(c1, c2, notp, notq, notr):
    p_list = [True, False]
    if notp:
        p_list = [False, True]
    q_list = [True, False]
    if notq:
        q_list = [False, True]
    r_list = [True, False]
    if notr:
        r_list = [False, True]

    result = ""
    # Loop through the three inputs
    for P in p_list:
        for Q in q_list:
            for R in r_list:
                # Evaluate the current iteration
                out = input_right(P, Q, R, c1, c2)
                # Concat a 0 if True
                if out:
                    result += "0"
                # Or a 1 if False
                else:
                    result += "1"
    return int(result, 2)

# There are 2^8 possible truth tables for 3 inputs. We will
# compare how many can be generated with only two operators.
def first_test():
    final_result = [[] for i in range(256)]
    count = 0
    for i in range(4):
        for j in range(4):
            #  First loop through all the operators
            for np in [False, True]:
                for nq in [False, True]:
                    for nr in [False, True]:
                        # Then loop through all combinations of the inputs
                        index1 = tabulate_left(i, j, np, nq, nr)
                        final_result[index1].append(formula(i, j, np, nq, nr, True))
                        # Lastly account for order of operations
                        index2 = tabulate_right(i, j, np, nq, nr)
                        final_result[index2].append(formula(i, j, np, nq, nr, False))
                        count += 2

    for i in range(256):
        print(final_result[i])


def second_test():
    pass

second_test()
# Now we need to see if changing the order of the inputs,
# (Q - P) - R for example, can give us any more unique results.

