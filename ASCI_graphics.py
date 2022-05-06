#note: Функции принимают отрицательные координаты и длинну
#Draw позволяет применять три варианта слияния, а также отражать по горизонтали/вертикали

class Drawing:
    def __init__(self, vertical = 10, horizontal = 10, char = '□', fill = True):
        self.canvas = [[char for h in range(horizontal)] for v in range(vertical)]
        self.height = vertical
        self.length = horizontal
        if fill:
            self.filler = char
    def correctCoordinate_V(self, x):
        if x < 0:
            return 0
        if x >= self.height:
            return self.height - 1
        return x
    def correctCoordinate_H(self, x):
        if x < 0:
            return 0
        if x >= self.length:
            return self.length - 1
        return x

    def print(self, sep = ''):
        for i in range(self.height):
            print(*self.canvas[i], sep = sep)
    def setPoint(self, coorsinates = [0,0], char = '◆'):
        #* Y ->
        #X
        #\
        #v
        self.canvas[coorsinates[0]][coorsinates[1]] = char
    def drawHorizontalLine(self, X = [0, 0], len = 1, char = '◆'):
        X[1], len = min(self.correctCoordinate_V(X[1] + len), X[1]), abs(self.correctCoordinate_V(X[1] + len) -
                                                                         self.correctCoordinate_H(X[1])) + 1
        self.canvas[X[0]][X[1]:X[1] + len] = [char for i in range(len)]
    def drawVerticalLine(self, X = [0, 0], len = 1, char = '◆'):
        X[0], len = self.correctCoordinate_V(min(X[0], X[0] + len)), abs(self.correctCoordinate_V(X[0] + len) -
                                                                         self.correctCoordinate_V(X[0])) + 1
        for i in range(len):
            self.setPoint([X[0] + i, X[1]], char)
    def drawRectangle(self, X= [0, 0], Y = [0, 0], char = '◆'):
        X, Y = [self.correctCoordinate_V(X[0]), self.correctCoordinate_H(X[1])],\
               [self.correctCoordinate_V(Y[0]), self.correctCoordinate_H(Y[1])]
        X, hor, vert = [min(X[0], Y[0]), min(X[1], Y[1])], abs(X[0] - Y[0]), abs(X[1] - Y[1]) + 1
        for v in range(vert):
            self.drawHorizontalLine([X[0] + v, X[1]], len = hor, char = char)
    def draw(self, drawing, X=[0,0], set = {'mode':'o', 'reflect':'none'}):
        m_vert = self.correctCoordinate_V(X[0] + drawing.height)
        m_hor = self.correctCoordinate_H(X[1] + drawing.length)
        x = [self.correctCoordinate_V(X[0]), self.correctCoordinate_H(X[1])]
        if 'mode' not in set:
            set['mode'] = 'o'

        _x = x.copy()
        vert_inc = hor_inc = 1
        if 'reflect' in set:
            if set['reflect'] == 'v':
                hor_inc, _x[1], m_hor = -1, m_hor -1 , _x[1] -1
            elif set['reflect'] == 'h':
                vert_inc, _x[0], m_vert = -1, m_vert- 1, _x[0] - 1
            elif set['reflect'] == 'vh':
                hor_inc, _x[1], m_hor = -1, m_hor - 1, _x[1] -1
                vert_inc, _x[0], m_vert = -1, m_vert- 1, _x[0] - 1
            if m_vert == -1:
                m_vert = 0
            if m_hor == -1:
                m_vert = 0

        b_1 = b_2 = 0
        for i_1 in range(_x[0], m_vert, vert_inc):
            b_2 = 0
            for i_2 in range(_x[1], m_hor, hor_inc):
                if set['mode'] == 'o':
                    self.setPoint([i_1, i_2], drawing.canvas[b_1][b_2])
                elif set['mode'] == 'c':
                    if drawing.canvas[i_1 - x[0]][i_2 - x[1]] != drawing.filler:
                        self.setPoint([i_1, i_2], drawing.canvas[b_1][b_2])
                elif set['mode'] == 'fm':
                    self.setPoint([i_1, i_2], drawing.canvas[b_1][b_2])
                    if self.canvas[i_1][i_2] == drawing.filler:
                        self.setPoint([i_1, i_2], self.filler)
                b_2+=1
            b_1+=1

def dem():
    drawin = Drawing()
    drawin.print(sep = '  ')

    secondary = Drawing(4, 4, '■')
    secondary.drawHorizontalLine([0,0], 10)
    secondary.drawVerticalLine([-12,0], 17)
    secondary.print(sep = '  ')

    print('--------------------')
    drawin.draw(secondary, [1, 1], {'mode' : "fm"})
    drawin.print(sep = '  ')
    print('--------------------')
    drawin.draw(secondary, [1, 5], {'mode' : "fm", 'reflect': "v"})
    drawin.print(sep = '  ')
    print('--------------------')
    drawin.draw(secondary, [5, 1], {'mode' : "fm", 'reflect': "h"})
    drawin.print(sep = '  ')
    print('--------------------')
    drawin.draw(secondary, [5, 5], {'mode' : "fm", 'reflect': "vh"})
    drawin.print(sep = '  ')
    print('--------------------')
    drawin.drawRectangle([2,2],[7,7], '+.')
    drawin.print(sep = '  ')
    print('--------------------')

    drawin.draw(secondary, [1, 1], {'mode' : "o"})
    drawin.draw(secondary, [1, 5], {'mode' : "o", 'reflect': "v"})
    drawin.draw(secondary, [5, 1], {'mode' : "o", 'reflect': "h"})
    drawin.draw(secondary, [5, 5], {'mode' : "o", 'reflect': "vh"})
    drawin.print(sep = '  ')
    print('--------------------')





