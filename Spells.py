# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 3

class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance'


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'


def study_spell(spell):
    print(spell)

# Changed spell => a_spell, to keep python from being grumpy about study_spell(spell), as spell "shadows name spell from outer scope"
a_spell = Accio()
a_spell.execute()
study_spell(a_spell)
study_spell(Confundo())
