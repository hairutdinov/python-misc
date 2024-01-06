import operator


class ExtendedStack(list):
    def sum(self):
        self.operation(operator.add)

    def sub(self):
        self.operation(operator.sub)

    def mul(self):
        self.operation(operator.mul)

    def div(self):
        self.operation(operator.floordiv)

    def operation(self, cb):
        e1, e2 = self.pop(), self.pop()
        self.append(cb(e1, e2))


es = ExtendedStack()
es.append(10)
es.append(15)
es.append(20)

es.sum()
# es.div()
print(es)
