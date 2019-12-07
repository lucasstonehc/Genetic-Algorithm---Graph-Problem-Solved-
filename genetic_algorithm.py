
import numpy as np

class Gene(object):

    def __init__(self, gene):
        self.gene = gene

    def get_gene(self):
        return self.gene

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

class Population(object):

    def __init__(self, size):
        self.population = []
        self.size = size

    def generated_population(self):
        for i in range(0,self.size,1):
            self.population.append(Chromosome().generated_chromosome())
       
        return self.population


class Fitness(object):

    #to selected we use the half of fitest offspring

    def __init__(self, population):
        self.population = population
        self.congenes = {
            '00000010':6,
            '00000011':11,
            '00000100':5,
            '00000001':1,
            '00010010':3,
            '00010011':9,
            '00010100':8,
            '00010000':1,
            '00100011':7,
            '00100000':6,
            '00100001':3,
            '00100100':4,
            '00110100':2,
            '00110000':11,
            '00110010':7,
            '00110001':9,
            '01000000':5,
            '01000001':8,
            '01000010':4,
            '01000011':2
        }
        self.scores = []
        self.nextgeneration = []
        self.generation_crossover = []
    
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
        #return self.all_scores

    def selection(self):
        
        fittest = []
        for i in range(0,len(self.scores)-1,1):
            for j in range(1,len(self.scores),1):
                if(self.scores[i] >= self.scores[j]):
                    index = j
            fittest.append(index)


        for i in range(0,int(len(self.scores)/2),1): #get always 50% better individuals 
                self.nextgeneration.append(self.population[fittest[i]]) # get the fittest. the better 
        
    
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
    