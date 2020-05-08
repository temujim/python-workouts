import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# %% Simulating Walks

allwalks = []


# Simulate walk
for i in range(500):

    # initialize walk simulation
    simwalk = [0]

    # simulate dice throws
    for i in range(100):
        dice = np.random.randint(1,7)

        # start walking
        steps = simwalk[-1]

        if dice <= 2:
            # ensure step to not be less than 1
            steps = max(0, steps-1)
        elif dice <= 5:
            steps += 1
        else:
            steps += np.random.randint(1,7)

        # simulate probablity of fall by  0.1%

        if np.random.rand() <= 0.001:
            steps = 0

        simwalk.append(steps)

    allwalks.append(simwalk)

# Convert allwalks to numpy
np_allwalks = np.array(allwalks)
tnp_allwalks = np.transpose(np_allwalks)

# %% Plotting the Walk Simulation
plt.plot(tnp_allwalks)
plt.title("Random Walk Simulation", size=20, weight=800, loc='center' )
plt.ylabel("Step Height")
plt.xlabel("Number of Dice Throws")
plt.axis([0, 100, 0, 150])
plt.show()


# %% Plot the Distribution of Step Height
ends = tnp_allwalks[-1]
plt.hist(ends)
plt.title("Step Height Distribution", size=12, loc='left', weight=300)
plt.ylabel("Count", size='x-small', weight='semibold')
plt.xlabel("Step Height", size=8, weight='demibold')
plt.show()


# %% Calculate the probability of getting up to 60 steps or higher
calculated = np.count_nonzero(ends >= 60)
print("\n---------------")
print("The probability of getting up to 60 steps or higer is: {:.2%}".format(calculated/500))
        



