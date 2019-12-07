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
  
  Agora vamos criar nossa classe população. O código abaixo demonstra como pode ser feito essa tarefa.
  ```
  class Population(object):

    def __init__(self, size):
        self.population = []
        self.size = size

    def generated_population(self):
        for i in range(0,self.size,1):
            self.population.append(Chromosome().generated_chromosome())
       
        return self.population

  ```
  
  Vamos criar nossa classe Fitness que terá métodos importantes como: Seleção dos indivíduos mais aptos, crossover e scores. Não implementamos a mutação. Futuramente iremos adicionar essa função.
  
  Métodos para contabilizar os scores dos indivíduos.
  ```
  def score(self, individual):
        concatgenes = []
        score = 0
        for i in range(0,len(individual)-1,1):
            concatgenes.append(individual[i]+individual[i+1])

        for i in range(0,len(concatgenes),1):
            score += self.congenes[concatgenes[i]]
        
        return score

    def all_scores(self):
        for individual in range(0,len(self.population),1):
            self.scores.append(self.score(self.population[individual]))
  ```
  
  Método para selecionar os individuos mais aptos:
  ```
  def selection(self):
        
        fittest = []
        for i in range(0,len(self.scores)-1,1):
            for j in range(1,len(self.scores),1):
                if(self.scores[i] >= self.scores[j]):
                    index = j
            fittest.append(index)


        for i in range(0,int(len(self.scores)/2),1): #get always 50% better individuals 
                self.nextgeneration.append(self.population[fittest[i]]) # get the fittest. the better 
 
  ```
 O metodologia utilizada para selecionar os individuos foi: Pegar os 50% dos individuos que possuem os scores mais baixos.
 
 Método para crossover:
```
 def crossover(self):
        first_fistest = None
        second_fistest = None 
        offspring = []
        result = int(len(self.nextgeneration) / 2)
        if(result % 2 != 0):
            self.nextgeneration.append(self.nextgeneration[0])

        for index in range(0,len(self.nextgeneration)-1,2): # next generation always had a size
            first_fistest = self.nextgeneration[index]
            second_fistest = self.nextgeneration[index+1]

            for i in range(0,int(len(first_fistest)/2),1):
                offspring.append(first_fistest[i])

            for i in range(0,int(len(second_fistest)/2),1):
                offspring.append(second_fistest[i])

            self.generation_crossover.append(offspring)
            offspring = []

            for i in range(int(len(first_fistest)/2),len(first_fistest),1):
                offspring.append(first_fistest[i])

            for i in range(int(len(second_fistest)/2),len(second_fistest),1):
                offspring.append(second_fistest[i])

            self.generation_crossover.append(offspring)
            offspring = []
```
Nesse método há um cruzamento dos genes. Exemplo de como esse cruzamento é realizado.
CHROMOSOME 1:
```
 ['0000', '0100', '0011', '0000', '0100', '0011']
```
CHROMOSOME 2:
```
['0011', '0010', '0001', '0011', '0010', '0001']
```
RESULTADOS DE CROSSOVER ENTRE CHROMOSOME 1 E CHORMOSOME 2:
```
['0000', '0100', '0011', '0011', '0010', '0001']
['0000', '0100', '0011', '0011', '0010', '0001']
```
Após cruzar o CHROMOSOME 1  e CHROMOSOME 2 geramos dois novos indivíduos.

E para finalizar temos nossa função que irar controlar todo o fluxo.
Começamos com uma população de 2000 indivíduos.

```
if __name__ == "__main__":
    
    size_of_population = 2000
    first_time = True
    count_generation = 0
    while size_of_population != 0:
        print("GENERATION ", count_generation, " WILL BE STARTED")
        population = Population(size_of_population).generated_population()
        print("The populations is")
        for individual in population:
            print(individual)

        print("How fit an individual, SCORES")
        if first_time == True:
            fitness = Fitness(population)
            first_time = False
        else:
            fitness = Fitness(fitness.nextgeneration)

        fitness.all_scores()
        index = 1
        for individual_score in fitness.scores:
            print("The individual ", index, " had score equals ", individual_score)
            index += 1
        

        print("Selected the totally of population and divide them by two")
        print("The fittest population is ")
        fitness.selection()
        for index in range(0,len(fitness.nextgeneration),1):
            print("The individual selected is ", fitness.nextgeneration[index])

        size_of_population = int(size_of_population / 2)

        print("The Crossover ...")
        fitness.crossover()
        for index in range(0,len(fitness.generation_crossover),1): 
            print("The individual after crossover ", fitness.generation_crossover[index])
        
        count_generation += 1
```
Na imagem abaixo podemos ver que o resultado alcançado pelo AG é de 18.
![SOLUÇÂO](https://github.com/lucasstonehc/Genetic-Algorithm---Graph-Problem-Solved-/blob/master/theresult.png)


  
