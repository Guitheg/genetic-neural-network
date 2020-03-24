class NoInformationGenome(Exception): 
    def __init__(self, msg = None):
        if msg:
            self.msg = msg
        else:
            self.msg = "No Arguments given in the init"

    def __str__(self):
        return self.msg

class Genome:

    def __init__(self, chromosomes = None, create = None, *args, **kwargs):
        if chromosomes:
            self.chromosomes = chromosomes
        elif create:
            self.chromosomes = create(*args, **kwargs)
        else :
            raise NoInformationGenome

    def load(self, filename, load_file, *args, **kwargs):
        self.chromosomes = load_file(filename, *args, **kwargs)

    def evaluate(self, rules, *args, **kwargs):
        return rules(self.chromosomes, *args, **kwargs)

    def mutate(self, rules, *args, **kwargs):
        for chromosome in self.chromosomes:
            chromosome.mutate(rules, *args, **kwargs)

    def hybridize(self, genome):
        raise NotImplementedError