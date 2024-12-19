import sys


class PigStack:
    def __init__(self):
        self.pigs = []
        self.min_pigs = []

    def push(self, pig):
        self.pigs.append(pig)
        if not self.min_pigs or self.min_pigs[-1] >= pig:
            self.min_pigs.append(pig)

    def pop(self):
        if self.pigs:
            if self.pigs[-1] == self.min_pigs[-1]:
                self.min_pigs.pop()
            self.pigs.pop()

    def get(self):
        if self.min_pigs:
            return self.min_pigs[-1]

    def __getitem__(self, name):
        if name == "pop":
            self.pop()
            return
        if name == "min":
            cnt = self.get()
            if cnt is not None:
                print(cnt)
            return
        self.push(int(name.split()[1]))


pig_stack = PigStack()
data = sys.stdin.read().splitlines()
for d in data:
    pig_stack[d]
