###############################################################################
## Line Class
###############################################################################
class Line(object):
    """A line of code, with indent recorded, with blanks for variables, and the corresponding abstract variables to fill the blanks."""

    #Line(template, local_names, abstract_variables, indent)
    def __init__(self, template, abstract_variables, indent, line_values):
        self.template = template
        self.abstract_variables = abstract_variables
        #self.local_names = local_names
        self.indent = indent
        self.line_values = line_values

    def __eq__(self, other):
        """Two Lines are equal if they have the same template and abstract variables."""
        assert isinstance(other, Line)
        #print type(other)
        # print 'comparing', self,other
        #same = self.abstract_variables == other.abstract_variables and self.template == other.template
        
        #same = set(self.line_values) == set(other.line_values) and self.template == other.template
        same = self.line_values == other.line_values and self.template == other.template
        
        return same

    def getDict(self):
        return self.__dict__

    def render(self):
        # Replace all the blanks with '{}' so we can use built-in string formatting
        # to fill in the blanks with the list of ordered names
        return self.template.replace('___', '{}').format(*self.abstract_variables) #todo: print cannon name .canon_name

    def __str__(self):
        # DEBUGGING STR METHOD ONLY

        for line_val in line_values:
            print line_val

        raise #this string method should print out a different representation of values

        return self.template + " ||| " + str(self.abstract_variables) + " ||| " + line_values_formatted + "\n" # + " ||| " + str(self.local_names) + "\n"
    __repr__ = __str__