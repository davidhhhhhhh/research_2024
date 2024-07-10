from ideaToText import Decision


class RightCanvas(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(), {
            'setSize(600,400+60);': 4,
            "setSize(800,400+60)": 2,
            "setSize(400,400+60)": 1,
        })

    def render(self):
        return self.getChoice(self.getName())