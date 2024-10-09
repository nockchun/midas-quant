from transitions.extensions import GraphMachine
from io import BytesIO
from IPython.display import Image, display


class TradeStateMachine:
    def __init__(self, transitions=None, initial_state=None):
        if transitions is not None and initial_state is not None:
            self.setTransitions(transitions, initial_state)

    def getCriterias(self):
        return self._criterias

    def setTransitions(self, transitions, initial_state):
        states = set()
        for transition in transitions:
            states.add(transition["source"])
            states.add(transition["dest"])

        self._states = list(sorted(states))
        self._transitions = transitions
        self._machine = GraphMachine(
            model=self,
            states=self._states,
            transitions=self._transitions,
            initial=initial_state,
            ignore_invalid_triggers=True
        )

    def getStates(self):
        return self._states
    
    def getTransitions(self):
        return self._transitions
    
    def graph(self):
        graph = self._machine.get_graph()
        buf = BytesIO()
        graph.draw(buf, format='png', prog='dot')
        buf.seek(0)
        
        return Image(buf.read())



