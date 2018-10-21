# data assimilation using g.a.

from change_rain import *
from deap import base
from deap import creator
from deap import tools
import time
from cfg import *
import cfg

cx_prob = 0.5
mut_prob = 0.02
ngen = 100

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()

def create_individual():
    individual_list = []
    # we only want a random value between min and max
    for i in range(ngauges):
        individual_list.append(random.uniform(inf_lim, sup_lim))
    return individual_list

def crossover (offspring):
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < cx_prob:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

def mutation(offspring):
    for mutant in offspring:
        if random.random() < mut_prob:
            toolbox.mutate(mutant)
            del mutant.fitness.values

def evaluate(offspring):
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

def get_best_ind(pop):
    return tools.selBest(pop, 1)[0]

def calibrate_ga():
    pop = toolbox.population(n=ngauges*4)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("Evaluated {} individuals".format(len(pop)))
    for g in range(ngen):
        print("Generation {}".format(g))

        # choose the next generatioin
        offspring = toolbox.select(pop, len(pop))

        # clone selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # compute the crossover
        crossover(offspring)

        # compute the mutation
        mutation(offspring)

        try:
            # evaluate invalid individuals
            evaluate(offspring)
        except:
            pass

        # offsprint complete replacement strategy
        pop[:] = offspring
        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        mse = min(fits)
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
        best_ind = get_best_ind(pop)
        cfg.global_k = best_ind
        save_best_k(best_ind)
        try:
            changeRainfall(best_ind)
        except:
            pass
        elapsed_time = get_elapsed_time(start_time)
        if elapsed_time > time_limit:
            print('Time exceeded. Finishing the optimisation...')
            save_best_k(best_ind)
            save_k_matrix()
            break
    best_ind = get_best_ind(pop)
    try:
        changeRainfall(best_ind)
        update_best_matrix()
        save_k_matrix()
    except:
        pass
    print ('Finished! Elapsed time [s]: ', get_elapsed_time(start_time))

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", changeRainfall)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=4)

def main():
    cfg.start_time = datetime.datetime.now()
    copy_input_files()
    print('Starting calibration. Start time: ', cfg.start_time);
    print('Please wait...')

    for dt in raindata:
        cfg.start_step_time = datetime.datetime.now()
        process_folder(dt)
        try:
            calibrate_ga()
        except:
            pass
        # run this function only if skip_forward is set as False
        if not skip_forward:
            changeRainfallForwards(cfg.global_k)
        replace_original_rain()
        print ('Finished Elapsed time [s]: ', get_elapsed_time(cfg.start_step_time))
        print ('error: {0:.5f}'.format ( cfg.minor_error))
        print('\n')

if __name__ == '__main__':
    main()
