from random import randint
class Snake:
    def __init__(self,size=8) -> None:
        self.size=size
        # x,y
        self.dots=[[0,0]]
        self.actions=['Up','Down','Right','Left']
        self.x_y_action=[(0,-1),(0,1),(1,0),(-1,0)]
        self.last_dir=-1
        self.apple=self.gen_apple()
        self.score=0
        self.isgameovered=0
        self.apply()
    def _move(self,x,y):
        new_dot=self.dots[-1]
        new_dot[0]+=x
        new_dot[1]+=y
        self.dots.append(new_dot)
        del self.dots[0]
        # self.apply()
    def move(self,action):
        if self.isgameovered:return
        self._move(*self.x_y_action[action])
        # print(self.dots)
        self.last_dir=action
        if self.dots[-1]==self.apple:
            self.score+=1
            # new_dot=list(self.dots[-1])
            # new_dot[0]+=self.x_y_action[self.last_dir][0]
            # new_dot[1]+=self.x_y_action[self.last_dir][1]
            # self.dots.append(new_dot)
            self.apple=self.gen_apple()
        self.apply()
    def isgameover(self):
        return (self.dots[-1] in self.dots[:-1]) or min(self.dots[-1])<0 or max(self.dots[-1])==self.size
    def apply(self):
        self.vector=[[0]*self.size for i in range(self.size)]
        self.vector[self.apple[1]][self.apple[0]]=2
        for i in self.dots:
            self.vector[i[1]][i[0]]=1
        self.isgameovered=self.isgameover()
    def gen_apple(self,random=1,pos=[0,0]):
        if random:
            return [randint(0,self.size-1),randint(0,self.size-1)]
        return pos
    def print_out(self):
        print('-'*self.size*3)
        print('Score:',self.score,'          Control:',self.actions[self.last_dir])
        for i in self.vector:
            print(i)

# mysnake=Snake()
# # mysnake.apple=[1,0]
# mysnake.apply()
# mysnake.print_out()
# mysnake.move(2)
# mysnake.print_out()
# print(mysnake.dots)