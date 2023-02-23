from selene import have
from selene.core import command
from selene import command


class Dropdown:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def select(self, value):
        self.element.perform(command.js.scroll_into_view).click()
        self.elements.element_by(have.exact_text(value)).click()
