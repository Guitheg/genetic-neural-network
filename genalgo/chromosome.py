class NoInformationChromosome(Exception): 
    def __init__(self, msg = None):
        if msg:
            self.msg = msg
        else:
            self.msg = "No Arguments given in the init"

    def __str__(self):
        return self.msg

class Chromosome:

    def __init__(self, genes = None, create = None, *args, **kwargs):
        if genes:
            self.genes = genes
        elif create:
            self.genes = create(*args, **kwargs)
        else :
            raise NoInformationChromosome

    def mutate(self, randomize, *args, **kwargs):
        for gene in self.genes:
            gene.mutate(randomize, *args, **kwargs)

    def hybridize(self, chromosome, hybridization, *args, **kwargs):
        return hybridization(self, chromosome, *args, **kwargs)