from StudentSimulator.ideaToText import Decision

class GoodsNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'gold':5,
            "timber":1,
            'natural resources':2,
            'food':2,
            'noble titles':1
        })

    def render(self):
    	return self.getChoice(self.getName())