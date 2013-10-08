# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    failure=[]
    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST
    explored = []
    
    solution= util.Stack()
    frontier = util.Stack()
    print "Start:", problem.getStartState()
    

    candidates=problem.getSuccessors(problem.getStartState())
    explored.append(problem.getStartState())
    
    d = len(candidates)
    
    n=d
    f=0
    count=0
    for k in range(0,d):
        
        frontier.push(candidates[k])
        
        
        
        
        
        
        
    
    while True:
        if frontier.isEmpty()==True:
            print "failure"
            return failure
        """go to a leaf node"""

        
        
        
        
        node=frontier.pop()
        count=count+1
        
        print node[1]
        if f==d:
            for a in range(0,count):
                    solution.pop()
            count=0
        if n>1:
            count=0
        
        
        solution.push(node[1])
        
        
        
        
                
        
        
        
             
        
        
        
        
        
        if problem.isGoalState(node[0])==True:
            x=0
            sol=[]
            
            
            while solution.isEmpty()==False:

                sol.insert(x,solution.pop())
                x=x+1

            sol.reverse()
            print sol
            return sol    
        
        explored.append(node[0])
        
        candidates=problem.getSuccessors(node[0])
        
        d=len(candidates)
        n=0
        f=0
        for k in range(0, d):
            
            if candidates[k][0] not in explored:
                    
                frontier.push(candidates[k])
                n=n+1
            
            else: 
                f=f+1
        
                
                
            
                
           

                
                 
                    
                    
             

                 
        

    
    
    
    
    
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    failure=[]
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    explored = []
    
    
    
    frontier = util.Queue()
    child=[]
    queue=[]
    solution=[]
    d='s'
    
    

    node=problem.getStartState()
    
    frontier.push(node)
    explored.append(node)
    

    
    
    
   
        
        
        
        
        
        
        
    
    while True:
        if frontier.isEmpty()==True:
            print "failure"
            return failure
        

        
        
        
        
        
        
        node=frontier.pop()
        
        if len(queue)>0:
            solution=queue.pop(0)
        #come to the goal 
            if problem.isGoalState(node)==True:
                    
                return solution
                #####
        
        
        
        
        for action in problem.getSuccessors(node):
            
            
            
            
            
            
            
            
            if action[0] not in explored :

                
                   
                if action[1]=='South':
                    d=s
                if action[1]=='North':
                    d=n
                if action[1]=='East':
                    d=e
                if action[1]=='West':
                    d=w
            
                frontier.push(action[0])
                explored.append(action[0])
                solutions = list(solution)
                solutions.append(d)
                queue.append(solutions)



def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    from game import Directions
    
    failure=[]
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    failure = []
    explored = []
    queue=[]
    solution=[]

    
 
    frontier=util.PriorityQueue()
    pfunction=util.PriorityQueueWithFunction(frontier)
    
    
    
    node=problem.getStartState()
    node2=node
    cost=1
    frontier.push(node,cost)
    frontierlist={node2:cost}
    print frontierlist
    
    
    while True:
        
        if frontier.isEmpty()==True:
            return failure
        
        
        
        if len(frontierlist)>0:
            frontierlist.pop(node2)
            
        node=frontierlist.pop(node2)
        
        if len(queue)>0:
            solution=queue.pop(0)
            
        if problem.isGoalState(node)==True:

                
                return failure
            
        explored.append(node)
        
        
        
        
        for action in problem.getSuccessors(node):
            
            
            if action[0] not in explored :
                if action[0] not in frontierlist:

                
                   
                    if action[1]=='South':
                        d=s
                    if action[1]=='North':
                        d=n
                    if action[1]=='East':
                        d=e
                    if action[1]=='West':
                        d=w
                    
                    frontier.push(action[0],action[2])
                    
                    frontierlist.update({action[0]:action[2]})
                    
                    
                    
                    explored.append(action[0])
                    node2=action[0]
                    
                    solutions = list(solution)
                    solutions.append(d)
                    queue.append(solutions)
            
            if action[0] in frontierlist:
                
                for x, y in frontierlist.items():
                    print x,action[0],y,action[2]  
                    if x == action[0]:
                        
                        if y==action[2]:
                            print "primero:",frontier
                            node2=action[0]
                            pfunction.push(action[0])
                            print "segundo:", frontier
                            
                                

                    

               
                   
                

        
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
