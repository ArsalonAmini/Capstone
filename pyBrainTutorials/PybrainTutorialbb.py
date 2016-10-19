from pybrain.rl.environments.cartpole.balancetask import BalanceTask
from pybrain.tools.shortcuts import buildNetwork
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment
from pybrain.optimization import HillClimber

task = BalanceTask()
net = buildNetwork(task.outdim, 3, task.indim)
HillClimber(task, net, maxEvaluations =100).learn()
agent = OptimizationAgent(net, HillClimber())
exp = EpisodicExperiment(task, agent)
print(exp.doEpisodes(100))