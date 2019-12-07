# Algoritmo Genético

### Grafo.
![Grafo](https://github.com/lucasstonehc/Genetic-Algorithm---Graph-Problem-Solved-/blob/master/graph.png)

### O problema:
  Devemos utilizar o algoritmo genético para resolver o problema do caminho com menor custo no grafo acima.

### Solução do problema:
  Temos uma classe que simula o GENE.
  ```
  class Gene(object):

    def __init__(self, gene):
        self.gene = gene

    def get_gene(self):
        return self.gene
  ```
  
  Cada GENE é representado por um VETEX no grafo. Para criamos um GENE utilizamos o código abaixo:
  ```
  Gene('0000')
  ```
  
  Após a geração de GENES, nós vamos criar o CHROMOSOME. Para criar o CHROMOSOME utilizamos a classe abaixo:
  ```
  class Chromosome(object):

    def generated_chromosome(self):
        genes = []
        chromosome = []
        chromosome_transformation = []

        genes.append(Gene('0000'))
        genes.append(Gene('0001'))
        genes.append(Gene('0010'))
        genes.append(Gene('0011'))
        genes.append(Gene('0100'))

        chromosome =  np.random.choice(5, 5, replace=False)
        chromosome =  np.append(chromosome,chromosome[0])

        for index in range(0,len(chromosome),1):
            chromosome_transformation.append(genes[chromosome[index]].get_gene())

        return chromosome_transformation
  ```
  Essa classe retorna para nós um CHROMOSOME.
  Exemplo de CHORMOSOME
  ```
  ['0011', '0010', '0001', '0000', '0100', '0011']
  ```
  ###IMPORTANTE: Na biologia uma cadeia de GENES gera um CHORMOSOME.
  
  
  
  
  
  
