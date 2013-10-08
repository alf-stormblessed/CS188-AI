# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """
  

  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
    

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    
    newGhostStates = successorGameState.getGhostStates()
    newGhostPositions= successorGameState.getGhostPositions()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    utility=0
    
    
    nearestFood=9999
    nearestGhost=9999
    
    for pellets in newFood.asList():
      if util.manhattanDistance(pellets,newPos)<nearestFood:
        nearestFood=util.manhattanDistance(pellets,newPos)
        
    for ghosts in newGhostPositions:
      
      nearestGhost=util.manhattanDistance(ghosts,newPos)

    if nearestGhost<=2:
      utility=0
    else:
      utility=1/nearestFood+5000/(newFood.count()+1)
    
    
    
    return utility

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
     """
  
    
  
  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
   #for x in range(0,gameState.getNumAgents()):
      
    #  for directions in gameState.getLegalActions(x):
        
     #   print gameState.generateSuccessor(x, directions).data.score,x,directions
    miniactions=[]
    Actionswiththesameutility=[]
    numAgents=gameState.getNumAgents()
    totaldepth=self.depth*numAgents
    LegalActions=gameState.getLegalActions(0)
    #if Directions.STOP in LegalActions:
     #   LegalActions.remove(Directions.STOP)
    for action in LegalActions:
      
      nextState=gameState.generateSuccessor(0, action)  
      miniactions.append(self.minimax(numAgents,nextState,1,totaldepth))
    
    action=max(miniactions)
    for i in range(0,len(miniactions)):
        if miniactions[i]==action:
             Actionswiththesameutility.append(i)
    i = random.randint(0,len(Actionswiththesameutility)-1)
    procedure=LegalActions[Actionswiththesameutility[i]]
    #print "muevo a :",procedure, action

        
    return procedure

  def minimax(self,numAgents,state,agent,depth):
    NextStates=[]
    maximize=[]
    #print agent,depth
    minimize=[]
    LegalActions=state.getLegalActions(agent)
       
    for action in LegalActions:
      
      
      NextStates.append(state.generateSuccessor(agent, action))
     
    if (state.isLose() or state.isWin() or depth==1):
              return self.evaluationFunction(state)
    else:
      if agent==0:
        for nextState in NextStates:
          maximize.append(self.minimax(numAgents,nextState,agent+1,depth-1))
        #print "max:",max(maximize),depth,agent
        return max(maximize)
      else:
        
        for nextState in NextStates:
          minimize.append(self.minimax(numAgents,nextState,(agent+1)%numAgents,depth-1))
        #print "min:",min(minimize),depth,agent
        return min(minimize)
      
      
            
    
      

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """
  def getAction(self, gameState):
    """
Returns the minimax action using self.depth and self.evaluationFunction
"""
    "*** YOUR CODE HERE ***"


    
    score = -1e400
    alpha = -1e400
    beta = 1e400

    legalActions = gameState.getLegalActions(0)
    bestaction = Directions.STOP
    
    for action in legalActions:
      
        nextState = gameState.generateSuccessor(0, action)
        prevscore = score
        score = max(score, self.minimize(nextState, alpha, beta, 1, self.depth))
        if score > prevscore:
            theaction = action
        if score >= beta:
            return theaction
        alpha = max(alpha, score)
    return theaction
  
  def maximize(self,gameState, alpha, beta, depth):
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        v = -(float("inf"))
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            nextState = gameState.generateSuccessor(0, action)
            v = max(v, self.minimize(nextState, alpha, beta, gameState.getNumAgents() - 1, depth))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
  def minimize(self,gameState, alpha, beta, agentindex, depth):
    
        numghosts = gameState.getNumAgents() - 1
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
          
        v = 1e400
        legalActions = gameState.getLegalActions(agentindex)
        for action in legalActions:
            nextState = gameState.generateSuccessor(agentindex, action)
            if agentindex == numghosts:
                v = min(v, self.maximize(nextState, alpha, beta, depth - 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            else:
                v = min(v, self.minimize(nextState, alpha, beta, agentindex + 1, depth))
                if v <= alpha:
                    return v
                beta = min(beta, v)
        return v
    
    

    

    

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
   
   #for x in range(0,gameState.getNumAgents()):
      
    #  for directions in gameState.getLegalActions(x):
        
     #   print gameState.generateSuccessor(x, directions).data.score,x,directions
    miniactions=[]
    Actionswiththesameutility=[]
    numAgents=gameState.getNumAgents()
    totaldepth=self.depth*numAgents
    LegalActions=gameState.getLegalActions(0)
    #if Directions.STOP in LegalActions:
     #   LegalActions.remove(Directions.STOP)
    for action in LegalActions:
      
      nextState=gameState.generateSuccessor(0, action)  
      miniactions.append(self.expectimax(numAgents,nextState,1,totaldepth))
    
    action=max(miniactions)
    for i in range(0,len(miniactions)):
        if miniactions[i]==action:
             Actionswiththesameutility.append(i)
    i = random.randint(0,len(Actionswiththesameutility)-1)
    procedure=LegalActions[Actionswiththesameutility[i]]
    #print "muevo a :",procedure, action

        
    return procedure

  def expectimax(self,numAgents,state,agent,depth):
    NextStates=[]
    maximize=[]
    #print agent,depth
    minimize=[]
    LegalActions=state.getLegalActions(agent)
       
    for action in LegalActions:
      
      
      NextStates.append(state.generateSuccessor(agent, action))
     
    if (state.isLose() or state.isWin() or depth==1):
              return self.evaluationFunction(state)
    else:
      if agent==0:
        for nextState in NextStates:
          maximize.append(self.expectimax(numAgents,nextState,agent+1,depth-1))
        #print "max:",max(maximize),depth,agent
        return max(maximize)
      else:
        expect=0
        for nextState in NextStates:
          expect+=self.expectimax(numAgents,nextState,(agent+1)%numAgents,depth-1)/len(NextStates)
          
        #print "min:",min(minimize),depth,agent
        return expect
    

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """
  
  newPos = currentGameState.getPacmanPosition()
  newFood = currentGameState.getFood()
  
  newGhostStates = currentGameState.getGhostStates()
  newGhostPositions= currentGameState.getGhostPositions()
  newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


  utility=0
    
    
  nearestFood=9999
  nearestGhost=9999
    
  for pellets in newFood.asList():
    if util.manhattanDistance(pellets,newPos)<nearestFood:
      nearestFood=util.manhattanDistance(pellets,newPos)
        
  for ghosts in newGhostPositions:
      
    nearestGhost=util.manhattanDistance(ghosts,newPos)
    
  utility=10/nearestFood+70000/(newFood.count()+1)
  utility+=-10*nearestGhost
  
    
  return utility

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

