import click
from mappers.mapreader import rarefy


class PrimaryBuilder(object):
    '''Builds and transports initial linked representation for the sigil.

    Attributes:
        letter_list: Initial list from the input texts.
        rule_dict: Initial rule list from the input rules.
        substitute_list: Letters substituted with numbers from the ruleset.
        substitute_zip: Letter-number links list of lists.
    '''

    _letter_list = []
    _rule_dict = {}
    _substitute_list = []
    _substitute_zip = []

    def __init__(self):
        pass

    def add_to_letter_list(self, line_set):
        '''Adds one set from the readline of the input text.'''
        self._letter_list += line_set

    def add_to_rule_dict(self, rule_dict):
        '''Sets rule dictionary from the input rules.'''
        self._rule_dict.update(rule_dict)

    def rarefy_letters(self, num):
        '''Rarefy letter list to num length.'''
        self._letter_list = rarefy(self._letter_list, num)

    def generate_substitute_list(self):
        '''Generates substitute list from letters and rules.'''
        try:
            self._substitute_list = list(map(
                lambda x: int(self._rule_dict[x]), self._letter_list))
        except KeyError:
            click.echo(
                click.style(
                    'Letter key doesn\'t exist in a ruleset.', fg="red"))

    def generate_substitute_zip(self):
        '''Generates lists of letter-number links.'''
        self._substitute_zip = list(
            zip(self._letter_list, self._substitute_list))

    @property
    def letter_list(self):
        return self._letter_list

    @property
    def rule_dict(self):
        return self._rule_dict

    @property
    def substitute_list(self):
        return self._substitute_list

    @property
    def substitute_zip(self):
        return self._substitute_zip
