used = [
    '210200',
    '210300', '210w00', '121w00', '032w00', '120w02', '011w02',
    ''
]

def check_used(new: str):
    if new in used:
        print('Used')
        return
    else:
        print('Not used')

check_used('')


class Transition:
    def __init__(self, i, o):
        self.i = i
        self.o = o


class Marking:
    def __init__(self, vals: str):
        self.vals = vals


class MarkedPetriNet:
    def __init__(self, ts, marking):
        self.ts = ts
        self.marking = marking

    def allowed_transitions(self):
        for t in self.ts:
            ...



petri = MarkedPetriNet(
    [Transition([1], [1, 4]), Transition([1, 4], [2, 3]),
     Transition([3, 4], [5]), Transition([1, 2, 5], [6, 6])],
    Marking('210200')
)