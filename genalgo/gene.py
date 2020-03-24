class NoInformationGene(Exception):
    def __init__(self, msg = None):
        if msg:
            self.msg = msg
        else:
            self.msg = "No Arguments given in the init"

    def __str__(self):
        return self.msg

class Gene:
    def __init__(self, value = None, create = None, *args, **kwargs):
        if value:
            self.value = value
        elif create:
            self.value = create(*args, **kwargs)
        else :
            raise NoInformationGene
        
    def mutate(self, randomize, *args, **kwargs):
        self.value = randomize(self.value, *args, **kwargs)

    def hybridize(self, other_gene_value, hybridization_rules, *args, **kwargs):
        return hybridization_rules(self.value, other_gene_value, *args, **kwargs)