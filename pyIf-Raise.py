def hey(self, message):
    if not message and message != '':
        raise ValueError("message is invalid: {!r}".format(message))

a = 1
xxx = 2
b = 9

# ternary conditional operator
a if xxx else b

falseValue = 7
trueValue = 8
test = trueValue + falseValue
(falseValue, trueValue)[test == True]
