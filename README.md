# genetic-neural-network
 A genetic algorithm allowing to self determine an optimized architecture of a neural network according to any given problem. It is a personal project with educational purpose.

Nothing has been pushed yet...

Some ideas before begin the code:

How I will implement it ?  
- First, a neural network is a following of layers and function. Layers and functions have several parameters besides its weights determined by training. At the start of the neural network, often we have a normalization function or something like that and at the end we have the cost and the number of bad answer allowing training by backpropagation especially. So we can modelize a neural network by a following of black boxes with several parameters. Theses boxes have some types, some kinds of parameters and some values (weights).  
- Second, a genetic algorithm is an algorithm inspired by evolution theory and setting up three principle : mutation, hybridization and selection (with evaluation).  
We have to represent a neural network as a genome to allow mutation and hybridation to be done easily. In others words, the genome will be an encodage of the black boxes enchainment, easy to hybride and mutate. Chromosomes will composed the genome and will be the black boxes (layers and functions). Genes will composed the chromosome and will be values of the parameters.  
- Genetic algorithm principles :  
 + Hybridization : it is making a mix of two genome to give a third. I have to create the rule of hybridization. In other word, I have to decide how the mix operate.  
 + Mutation : I'll modify, add or delete randomly a random number of gene in the genome. I have to decide some kinds of stuff like the maximum number of genes could be modify or the strength of the modification etc. In the modification, 
 + Evaluation and selection : I have to decide a some way to evaluate the neural network. For example : the time, the number of error, the cost... should I use a confusion matrix too ? Moreover, I hav to decide how selection operate. Should I take always the best ? Or a pourcentage of good eval, of medium eval and bad eval like respectively 80%, 15% and 5% for example.  

A chromosone will be a gene enchainment like : 
```
Cx = ( [Type] [ID] [nOut] [ID_Out1] [...] [ID_Outn] [Arg1] [...] [Argn] [Shape] [Values(weights)] )
```
The gene (Type) tell us the number of arguments, and what kind of function it is, for example : linear layer, conv layer etc. 
 + (ID) is the ID of the chromosome. (we need this because the enchainment is not necesseraly sequential)  
 + (nOut) number of chromosome in output of this one  
 + (ID_Outn) the ID of a chromosome in output of this one  
 + (Argn) an arguments of the function, for example : in convolutional layer it can be the number of kernels, (or the stride etc.)  
 + (Shape) the shape of the values (I have to think about it... I am not sure i'll implement it like this..)  
 + (Values) the weights or the values of the layers (I'm not sure i'll implement it like this either..)  

A genome will be a chromosome enchainment like :  
```
Gx = ( [x] [C1] [x] [C2] [x] [C3] [...] [x] [Cn-1] [x] [Cn] )  
```
 + (x) represent a void waiting to be fulled by I new chromosome and two new void.  
 + (Cn) a chromosome  
 
