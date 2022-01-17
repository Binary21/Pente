
''' the second is the x value the first is the y value'''
class Board:
    
    def __init__(self,size):
        self.board = []
        self.scoreX = 0
        self.scoreO = 0
        for c in range(size):
            row = []
            for r in range(size):
                row.append(' ')
            self.board.append(row)
            
    def draw(self):
        c = 0
        print('')
        for r in self.board:
            letters = 65 + 10
            for x in range(65,letters):
                print(chr(x),'',end = '')   
            break
        print(' ')
        for r in self.board:
            
            for cell in r:
                print(cell,end = "|")
            print(str(c))
            c = c + 1
    def five_straight(self,icon):
        if icon == 'X':
                self.scoreO = 5
                print('scoreO:',self.scoreO)
        elif icon == 'O':
                self.scoreX = 5
                print('scoreX:',self.scoreX)
        return self.scoreX, self.scoreO
            
    def capture_score_anti(self,icon):
        '''keeps score of all the captured pieces'''
        if icon == 'X':
                self.scoreO +=1
                print("scoreX:",self.scoreX)
                print("scoreO:",self.scoreO)
        elif icon == 'O':
                self.scoreX +=1
                print("scoreO:",self.scoreO)
                print("scoreX:",self.scoreX)
        return self.scoreX, self.scoreO
    
    def capture_score(self,icon):
        '''keeps score of all the captured pieces'''
        if icon == 'X':
                self.scoreX +=1
                print("scoreX:",self.scoreX)
                print("scoreO:",self.scoreO)
        elif icon == 'O':
                self.scoreO +=1
                print("scoreO:",self.scoreO)
                print("scoreX:",self.scoreX)
        return self.scoreX, self.scoreO
                
##    def reset(self,capture_lower,capture_upper,capture_left,capture_right,loc_x,loc_y):
##        '''resets the value of captured pieces'''
##        if capture_upper - capture_lower == 10:
##            self.board[loc_y][loc_x] = ' '
##            self.board[loc_y-1][loc_x] = ' '
##            self.capture_score_anti(icon,scoreX,scoreO)
##        elif capture_lower - capture_upper == 10:
##            self.board[loc_y][loc_x] = ' '
##            self.board[loc_y+1][loc_x] = ' '
##            self.capture_score_anti(icon,scoreX,scoreO)
##        else:
##            if capture_lower == 1:
##                self.board[loc_y-1][loc_x] = ' '
##                self.board[loc_y-2][loc_x] = ' '
##                self.capture_score(icon,scoreX,scoreO)
##            if capture_upper == 1:
##                self.board[loc_y+1][loc_x] = ' '
##                self.board[loc_y+2][loc_x] = ' '
##                self.capture_score(icon,scoreX,scoreO)
##            if capture_left == 1:
##                self.board[loc_y][loc_x+1] = ' '
##                self.board[loc_y][loc_x+2] = ' '
##                self.capture_score(icon,scoreX,scoreO)
##            if capture_right == 1:
##                self.board[loc_y][loc_x-1] = ' '
##                self.board[loc_y][loc_x-2] = ' '
##                self.capture_score(icon,scoreX,scoreO)
##    def reset(self,capture_middle_lower,capture_middle_left,capture_middle_upper,capture_middle_right):
##        print('im here')
##        if capture_middle_upper == 3:
##            self.board[loc_y][loc_x] = ' '
##            self.board[loc_y+1][loc_x] = ' '
##            loc_y+1 = other
##            return loc_y,loc_x,other
##        if capture_middle_lower == 3:
##            self.board[loc_y][loc_x] = ' '
##            self.board[loc_y-1][loc_x] = ' '
##        if capture_middle_left == 3:
##            self.board[loc_y][loc_x] = ' '
##            self.board[loc_y][loc_x-1] = ' ' 
##        if capture_middle_right == 3:
##            self.board[loc_y][loc_x] = ' '
##            self.board[loc_y][loc_x+1] = ' '
    
    def down(self,loc_x,loc_y,icon):
        '''searches to the right for all the icons'''
        score_lower = 0
        capture_lower = 0
        dm = [loc_y-1,loc_y-2,loc_y-3,loc_y-4]
        for f in dm:
            #print(f)
            if self.board[int(f)][int(loc_x)] == icon:
                score_lower += 1
                #print('score',score_lower)
            elif self.board[int(f)][int(loc_x)] == ' ':
                break
        return score_lower

    def down_capture(self,loc_x,loc_y,icon,anticon):
        capture_lower = 5
        dm = [loc_y-1,loc_y-2,loc_y-3,loc_y-4]
        for f in dm:
            if self.board[int(f)][int(loc_x)] == icon:
                capture_lower *= 4
            if self.board[int(f)][int(loc_x)] == anticon:
                capture_lower -= 1
            elif self.board[int(f)][int(loc_x)] == ' ':
                break
        return capture_lower
    def down_middle_capture(self,loc_x,loc_y,icon,anticon):
        capture_middle_lower = 0
        if self.board[loc_y-1][loc_x] == ' ':
            return capture_middle_lower
        else:
            #print('anticon:',anticon)
            #print('icon:',icon)
            if loc_y-1 == anticon:
                capture_middle_lower -= 1
                return capture_middle_lower
            elif loc_y-1 != anticon:
                capture_middle_lower += 3
            print('lower:',capture_middle_lower)
        return capture_middle_lower
        
    
    def up(self,loc_x,loc_y,icon):
        '''searches to the right for all the icons'''
        score_upper = 0
        capture_upper = 0
        dm = [loc_y+1,loc_y+2,loc_y+3,loc_y+4]
        try:
            for f in dm:
                #print(f)
                if self.board[int(f)][int(loc_x)] == icon:
                    score_upper += 1
                    #print('score',score_upper)
                elif self.board[int(f)][int(loc_x)] == ' ':
                    break
        except IndexError:
            pass
        return score_upper
    
    def up_capture(self,loc_x,loc_y,icon,anticon):
        capture_upper = 5
        dm = [loc_y+1,loc_y+2,loc_y+3,loc_y+4]
        try:
            for f in dm:
                if self.board[int(f)][int(loc_x)] == icon:
                    capture_upper *= 4
                if self.board[int(f)][int(loc_x)] == anticon:
                    capture_upper -= 1
                elif self.board[int(f)][int(loc_x)] == ' ':
                    break
        except IndexError:
            pass
        return capture_upper
    def up_middle_capture(self,loc_x,loc_y,icon,anticon):
        capture_middle_upper = 0
        #print('upper capture level 1')
        if self.board[loc_y+1][loc_x] == ' ':
            #print('upper capture level 2')
            return capture_middle_upper
        else:
            #print('icon',icon)
            #print('anticon',anticon)
            #print('upper capture level 3')
            if loc_y+1 != anticon:
                #print('upper capture level 4')
                capture_middle_upper -= 1
            elif loc_y+1 == anticon:
                #print('upper capture level 5')
                capture_middle_upper +=3
            print('upper:',capture_middle_upper)
        return capture_middle_upper

    
    def left(self,loc_x,loc_y,icon):
        '''searches to the left for all the icons'''
        score_left = 0
        capture_left = 0
        cm = [loc_x-1,loc_x-2,loc_x-3,loc_x-4]
        for c in cm:
            #makes sure xoxo doesnt count as a capture
            if self.board[int(loc_y)][int(c)] == icon:
                score_left += 1
                #print('score',score_left)
            elif self.board[int(loc_y)][int(c)] == ' ':
                break
        return score_left

    def left_capture(self,loc_x,loc_y,icon,anticon):
        capture_left = 5
        dm = [loc_x-1,loc_x-2,loc_x-3,loc_x-4]
        for f in dm:
            if self.board[int(loc_y)][int(f)] == icon:
                capture_left *= 4
            if self.board[int(loc_y)][int(f)] == anticon:
                capture_left -= 1
            elif self.board[int(loc_y)][int(f)] == ' ':
                break
        return capture_left
    def left_middle_capture(self,loc_x,loc_y,icon,anticon):
        capture_middle_left = 0
        if self.board[loc_y][loc_x-1] == ' ':
            return capture_middle_left
        else:
            if loc_x-1 == anticon:
                capture_middle_left -= 1
                return capture_middle_lower
            elif loc_x-1 != anticon:
                capture_middle_left += 3
            print('lower:',capture_middle_left)
        return capture_middle_left

        print('left:',capture_middle_left)
        return capture_middle_left
    
    def right(self,loc_x,loc_y,icon):
        '''searches to the right for all the icons'''
        score_right = 0
        dm = [loc_x+1,loc_x+2,loc_x+3,loc_x+4]
        try:
            for f in dm:
                #print(f)
                if self.board[int(loc_y)][int(f)] == icon:
                    score_right += 1
                    #print('score',score_right)
                elif self.board[int(loc_y)][int(f)] == ' ':
                    break
        except IndexError:
            pass
        return score_right 
    def right_capture(self,loc_x,loc_y,icon,anticon):
        capture_right = 5
        dm = [loc_x+1,loc_x+2,loc_x+3,loc_x+4]
        try:
            for f in dm:
                if self.board[int(loc_y)][int(f)] == icon:
                    capture_right *= 4
                if self.board[int(loc_y)][int(f)] == anticon:
                    capture_right -= 1
                elif self.board[int(loc_y)][int(f)] == ' ':
                    break
        except IndexError:
            pass
        return capture_right
    def right_middle_capture(self,loc_x,loc_y,icon,anticon):
        capture_middle_right = 0
        if self.board[loc_y][loc_x+1] == ' ':
            #print('upper capture level 2')
            return capture_middle_right
        else:
            #print('icon',icon)
            #print('anticon',anticon)
            #print('upper capture level 3')
            if loc_x+1 != anticon:
                #print('upper capture level 4')
                capture_middle_right -= 1
            elif loc_x+1 == anticon:
                #print('upper capture level 5')
                capture_middle_right +=3
            print('right:',capture_middle_right)
        return capture_middle_right


    def full(self,size):
        ''' Return True if the board is full. '''
        for c in range(size):
            if self.board[c] == ' ':
                return False
        return True
    
    def win(self,loc_x,loc_y,icon,anticon):
        ''' return True for win, check for captures and keep count '''
        score_right  = self.right(loc_x,loc_y,icon)
        score_left = self.left(loc_x,loc_y,icon)
        score_lower = self.down(loc_x,loc_y,icon)
        score_upper = self.up(loc_x,loc_y,icon)
        capture_right = self.right_capture(loc_x,loc_y,icon,anticon)
        capture_left = self.left_capture(loc_x,loc_y,icon,anticon)
        capture_upper = self.up_capture(loc_x,loc_y,icon,anticon)
        capture_lower = self.down_capture(loc_x,loc_y,icon,anticon)
        capture_middle_lower = self.down_middle_capture(loc_x,loc_y,icon,anticon)
        capture_middle_upper = self.up_middle_capture(loc_x,loc_y,icon,anticon)
        capture_middle_right = self.right_middle_capture(loc_x,loc_y,icon,anticon)
        capture_middle_left = self.left_middle_capture(loc_x,loc_y,icon,anticon)
        print('left',capture_middle_left)
        print('right',capture_middle_right)
        print('upper',capture_middle_upper)
        print('lower',capture_middle_lower)
        # checking win

        if score_left + score_right + 1 == 5:
            print('winner')
            self.five_straight(icon)
        if score_upper + score_lower + 1 == 5:
            print('winner')
            self.five_straight(icon)

        if capture_lower + capture_upper == 17:
            self.capture_score(icon)
            #self.reset(capture_middle_lower,capture_middle_left,capture_middle_upper,capture_middle_right)
        elif capture_left + capture_right == 17:
            self.capture_score(icon)
            #self.reset(capture_middle_lower,capture_middle_left,capture_middle_upper,capture_middle_right)

        elif capture_middle_right + capture_middle_left == 2:
            self.capture_score_anti(icon)
            #self.reset(capture_middle_lower,capture_middle_left,capture_middle_upper,capture_middle_right)
        elif capture_middle_upper + capture_middle_lower == 2:
            self.capture_score_anti(icon)
            #self.reset(capture_middle_lower,capture_middle_left,capture_middle_upper,capture_middle_right)
        if self.scoreX == 5:
            print('winner')
        elif self.scoreX == 5:
            print('winner')

       
            
        
                    
    def get_score(self):
        print(self.scoreX,self.scoreO)
        return self.scoreX,self.scoreO

    

    def move(self,loc_x,loc_y,icon):
        #print(loc_y)
        if self.board[loc_y][loc_x] == ' ':
            self.board[loc_y][loc_x] = icon

        else:
            print('sorry that location is full try again')
            if icon == 'O':
                icon = 'X'
            else:
                icon = 'O'
            return False
    
        

print('DO')
if __name__ == '__main__':
        
    size = 10
    b = Board(size)

    b.draw()
    icon = 'O'
    anticon = 'X'
    while True:
        if icon == 'O':
            icon = 'X'
        else:
            icon = 'O'
        if icon == 'O':
            anticon = 'X'
        else:
            anticon = 'O'

        print('player',icon + "'s turn")
        first_answer = True
        while first_answer:
            answer = str.upper(input('x value'))
            char_list = 'ABCDEFGHIJ'
            loc_x = char_list.find(answer)
            if loc_x == -1:
                print('Sorry that isnt in our range please try again')
            else:
                first_answer = False

        second_answer = True
        while second_answer:
            try:
                answer_y = int(input('y value'))
                if answer_y > 9:
                    pass
                else:
                    loc_y = answer_y
                    second_answer = False
            except ValueError:
                print('thats not a number please put in a number, thank you')

 
        print('icon =', icon)
        b.move(loc_x,loc_y,icon)
        print('icon =', icon)
        b.draw()
        b.win(loc_x,loc_y,icon,anticon)
        b.full(size)


        
        

print('do ..........................................')
