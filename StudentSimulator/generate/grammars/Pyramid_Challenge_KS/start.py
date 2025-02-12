from StudentSimulator.ideaToText import Decision


# "Start" is a special decision which is invoked by the Sampler
# to generate a single sample.
class Start(Decision):

    def registerChoices(self):
        # This sentence creator for Q13 in power grading dataset.
        # It starts with two choices:
        # One choice is correct, including political, religious, or economic reason. The other
        # choice is incorrect, like taxation, exploration, or physical goods.
        self.addChoice('seriousness', {
            'serious': 5000,
            'kidding': 1
        })

        # Choices have two parts, an identifier and a dictionary
        # which maps possible outcomes to their relative likelihood

    def updateRubric(self):
        pass

    def render(self):
        # Mapping choices to their corresponding expanded code
        choice_mapping = {
            'serious': 'Serious',
            'kidding': 'Kidding'
        }

        strategy = self.getChoice('seriousness')
        out_codes = self.expand(choice_mapping[strategy])
        return out_codes
