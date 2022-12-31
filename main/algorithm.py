
import numpy as np
data=""

class State:
    def __init__(self,data,level,fval):
        """ Set the data, state level, and determined fvalue as the state's initial values. """
        self.data = data
        self.level = level
        self.fval = fval
    def generate_child(self):
        """ Create child states by relocating the blank space in one of the four directions (up, down, left, or right) from the supplied state. """
        x,y = self.find(self.data,'_')
        """ val list includes position values for shifting the blank space in one of four directions [up, down, left, right]. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_state = State(child,self.level+1,0)
                children.append(child_state)
        return children
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the provided direction and return None if the position value exceeds the limitations. """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    def copy(self,root):
        """ To construct a duplicate matrix of the given state"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self,puz,x):
        """ finding the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j
class GameSolver:
    def __init__(self,size):
        """ Initialize the game size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []
    def accept(self):
        """ Reading the matrix from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz
    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level
    def h(self,start,goal):
        """ Calculates the difference between the given matrices """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
    def process(self,start, goal):
        """ Reading Start and Goal Game state"""
        global data
        data="Start\n"
        start = State(start,0,0)
        start.fval = self.f(start,goal)
        """ Put the start state in the open list"""
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            data+="  | \n"
            print("  | ")
            data+="  | \n"
            print(" \\\'/ \n")
            data+=" /'\\ \n"
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                    data+=j
                    data+="   "
                print("")
                data+="\n"
            """ If the difference between current and goal state is 0 we have reached the goal state"""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            """ sort the open list based on f_value """
            self.open.sort(key = lambda x:x.fval,reverse=False)


# search function take start and goal values
def searchGame(start, goal):
   global data
   data=""
   print(sorted(start))
   # check if start input from 1 to 8 with -
   if(sorted(start)!=['1','2','3','4','5','6','7','8','_']):
      data="مصفوفة البداية يجب أن تحوي أرقام مختلفة بين 1 و 8 ومحرف _"
      return data
   # check if goal input from 1 to 8 with -
   elif(sorted(goal)!=['1','2','3','4','5','6','7','8','_' ]):
      data="مصفوفة الهدف يجب أن تحوي أرقام مختلفة بين 1 و 8 ومحرف _"
      return data
   else:
    # convert array to 2d array
      start = np.reshape(start, (-1, 3))
      goal = np.reshape(goal, (-1, 3))
      try:
        # call puzzle function
        game = GameSolver(3)
        game.process(start, goal)
      except: 
        data="لم يتم العثورعلى مسار"
   return data