# هم گروهی محمد مهدی کاظمی
import pygame
import copy
class GameState: # روند بازی مثل جا به جایی مهره ها و کیش و مات اینجا انجام میشه
    def __init__(self):
        self.list_1 = []
        self.board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', '--', '--', '--', '--'],['--', '--', '--', '--', '--', '--', '--', '--'],['--', '--', '--', '--', '--', '--', '--', '--'],['--', '--', '--', '--', '--', '--', '--', '--'],['--', '--', '--', '--', '--', '--', '--', '--'],['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', '--', '--', '--'],['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.possible_moves = []
        self.whiteToMove = True
        self.has_moved = False
        self.has_moved_b = False
        self.kastel = False
        self.an_pasan = False

    def make_move(self, move, board = None, white = True, list_1 = []): # این تابع برای جا به جایی مهره هاست 
        for x in self.possible_moves:
            if self.kastel == True and board[move.startRow][move.startCol] == 'wK' and white and move.endRow == 7 and move.endCol == 6 or  self.kastel == True and board[move.startRow][move.startCol] == 'wK' and white and move.endRow == 7 and move.endCol == 2:
                if move.endRow == 7 and move.endCol == 6 and move.endRow == x[0] and move.endCol == x[1]: #  این شرط برای شاه قلعه مهره سفید هستش       
                    board[move.startRow][move.startCol] = '--'  
                    board[move.endRow][move.endCol] = 'wK'  
                    board[7][7] = '--'
                    board[7][5] = 'wR'
                    white = False
                    self.kastel = False  
                    self.has_moved = True  
                    board_1.w = True
                elif move.endRow == 7 and move.endCol == 2 and move.endRow == x[0] and move.endCol == x[1]: # این برای شاه قلعه سفید بزرگ هستش
                    board[move.startRow][move.startCol] = '--'  
                    board[move.endRow][move.endCol] = 'wK'
                    board[7][0] = '--'
                    board[7][3] = 'wR' 
                    white = False  
                    self.kastel = False  
                    self.has_moved = True  
                    board_1.w = True
            elif self.kastel == True and board[move.startRow][move.startCol] == 'bK' and not white and move.endRow == 0 and move.endCol == 6 or self.kastel == True and board[move.startRow][move.startCol] == 'bK' and not white and move.endRow == 0 and move.endCol == 2 :
                if move.endRow == 0 and move.endCol == 6 and move.endRow == x[0] and move.endCol == x[1]: # این شرط برای شاه قلعه مشکی هاست  
                    board[move.startRow][move.startCol] = '--'  
                    board[move.endRow][move.endCol] = 'bK'  
                    board[0][7] = '--'
                    board[0][5] = 'bR'
                    white = True
                    self.kastel = False 
                    self.has_moved_b = True 
                    board_1.w = True
                elif move.endRow == 0 and move.endCol == 2 and move.endRow == x[0] and move.endCol == x[1]: # این برای شاه قلعه بزرگ مشکی هستش
                    board[move.startRow][move.startCol] = '--'  
                    board[move.endRow][move.endCol] = 'bK'   
                    board[0][0] = '--'
                    board[0][3] = 'bR'
                    white = True 
                    self.kastel = False 
                    self.has_moved_b = True 
                    board_1.w = True
            if white and board[move.startRow][move.startCol][0] == 'w': # این شرط برای حرکت عادی مهره های سفید هست 
                    if board[x[0]] == board[move.endRow] and board[x[1]] == board[move.endCol]  and move.endRow == x[0] and move.endCol == x[1]:
                        if white and board[move.endRow][move.endCol] == board[x[0]][x[1]]:
                            if board[move.startRow][move.startCol] == 'wR' and move.startRow == 7 and move.startCol == 0:
                                board_1.rook_w_1 = False
                            elif board[move.startRow][move.startCol] == 'wR' and move.startRow == 7 and move.startCol == 7:
                                board_1.rook_w_2 = False
                            board_1.last_pos = []
                            board[move.startRow][move.startCol] = '--'
                            board[move.endRow][move.endCol] = move.pieceMoved
                            if board_1.an_pasan == True: # این شرط برای آن پاسان سفید
                                board[move.endRow + 1][move.endCol] ='--'
                            self.has_moved = True
                            white = False
                            board_1.w = True
                            board_1.last_pos = [[move.startRow, move.startCol], [move.endRow, move.endCol]]
                            self.king_11_move(board)
                            board_1.an_pasan = False
            elif board[move.startRow][move.startCol][0] == 'b' and not white: # این شرط برای حرکت عادی مهره های مشکی هستش 
                        if not white and board[x[0]][x[1]] == board[move.endRow][move.endCol] and move.endRow == x[0] and move.endCol == x[1]:
                            board_1.last_pos = []
                            if board[move.startRow][move.startCol] == 'bR' and move.startRow == 0 and move.startCol == 0:
                                board_1.rook_b_1 = False
                            elif board[move.startRow][move.startCol] == 'bR' and move.startRow == 0 and move.startCol == 7:
                                board_1.rook_b_2 = False
                            board[move.startRow][move.startCol] = '--'
                            board[move.endRow][move.endCol] = move.pieceMoved
                            if board_1.an_pasan == True: # این شرط برای ان پاسان مشکی
                                board[move.endRow - 1][move.endCol] = '--'
                            white = True
                            self.has_moved_b = True
                            board_1.w = True
                            board_1.last_pos = [[move.startRow, move.startCol], [move.endRow, move.endCol]]
                            self.king_11_move(board)
                            board_1.an_pasan = False
            if move.endRow == 0 and board[move.endRow][move.endCol] == 'wP' or move.endRow == 7 and board[move.endRow][move.endCol] == 'bP': # این شرط برای ترنسفرم سرباز هستش وقتی سرباز برسه اخر اندازه صفحه بازی بزرگتر میشه و 4 مهره که میشه ترنسفرم کرد رو میاره
                if white == False :
                    list_2 = ['wR', 'wN', 'wB', 'wQ']
                    m = 1
                else:
                    list_2 = ['bR', 'bN', 'bB', 'bQ']
                    m = 6
                screen_1 = pygame.display.set_mode((780, 512))
                screen_1.fill(pygame.Color('gray'))
                r = 8
                for i in list_2:
                    screen_1.blit(board_1.IMAGES[i] ,pygame.Rect(r*64 , m*64, 64 , 64))
                    board[m][r] = i
                    r += 1
                list_1.append(move.endRow)
                list_1.append(move.endCol)
                board_1.trans_position = False
                pygame.display.flip()
        if 8 <= board_1.col <= 11 and board_1.row == 1 or 8 <= board_1.col <= 11 and board_1.row == 6: # این شرط برای اینه که وقتی کلیک کرد و مهره برای ترنسفرم جا به جا شد صفحه رو به حالت قبلی برگردونه و ادامه روند بازی انجام بشه
                board[list_1[0]][list_1[1]] = board[board_1.row][board_1.col]
                screen_1 = pygame.display.set_mode((512, 512))
                board_1.draw_board(board_1.screen)
                board_1.draw_pieces(board_1.screen, board)
                if white == False:
                    m = 1
                else:m =6
                for i in range(8, 12):
                    board[m][i] = '--'
                list_1.clear()
                pygame.display.flip()
                k = self.check_in(board, white)
                f = self.check_in(board, not white)
                if k == True or f == True: # وقتی شاه کیش بود رنگیش کنه
                    pygame.draw.rect(board_1.screen, '#9900FF', pygame.Rect(board_1.pos_king[1] * board_1.SQ_SIZE, board_1.pos_king[0] * board_1.SQ_SIZE, board_1.SQ_SIZE, board_1.SQ_SIZE))
                    board_1.screen.blit(board_1.IMAGES[board[board_1.pos_king[0]][board_1.pos_king[1]]], pygame.Rect(board_1.pos_king[1] * board_1.SQ_SIZE, board_1.pos_king[0] * board_1.SQ_SIZE, board_1.SQ_SIZE, board_1.SQ_SIZE))
                    pygame.display.flip()
                board_1.trans_position = True
                self.matee(board, not white)
                self.matee(board, white)
        return white
    
    def check_in(self, board, white): # این تابع برای کچ کردن کیش است 
        board_1.all_possible_moves = []
        for i in range(8):
            for j in range(8):
                if board[i][j][1] == 'P':
                    x = board_1.list_mohre[0]
                elif board[i][j][1] == 'R':
                    x = board_1.list_mohre[1]
                elif board[i][j][1] == 'N':
                    x = board_1.list_mohre[2]
                elif board[i][j][1] == 'Q':
                    x = board_1.list_mohre[3]
                elif board[i][j][1] == 'B':
                    x = board_1.list_mohre[4]
                elif board[i][j][1] == 'K':
                    x = board_1.list_mohre[5]
                elif board[i][j][1] == '-':
                    continue
                move_3 = Move([i, j], [], board)
                x.get_all_possible_moves(move_3, board, white)
                for k in x.possible_moves:
                    board_1.all_possible_moves.append(k)
        for i in board_1.all_possible_moves:
            if board[i[0]][i[1]] == 'bK' or board[i[0]][i[1]] == 'wK':
                board_1.pos_king = []
                board_1.check = True
                board_1.pos_king.append(i[0])
                board_1.pos_king.append(i[1])
                return True
            board_1.check = False
        return False
    
    def back_to_difault(self, board): # اگر حرکت اشتباهی در هنگام کیش انجام داد برگردونه به حالت قبلی
        x = self.check_in(board, board_1.white)
        if x == True:
            board_1.white = not board_1.white
            return True
        return False

    def filter_possible_moves(self, board, move, white): # هنگامی که کیش میشه باید فقد حرکاتی که رفع کیش میکنه رو نشون بده این تابع حرکات رو فیلتر میکنه
        list_pos = []
        for possible_move in self.possible_moves:
            new_board = copy.deepcopy(board)
            piece_moved = new_board[move.startRow][move.startCol]
            new_board[move.startRow][move.startCol] = '--'
            new_board[possible_move[0]][possible_move[1]] = piece_moved
            check_result = self.check_in(new_board, not white)
            if not check_result:
                list_pos.append(possible_move)
        self.possible_moves = list_pos

    def just_2_king(self, board): # این تابع یک حات از پات هستش که اگه فقد دو تا شاه باقی موندن اعلام کنه بازی مساوی هستش
        list_king = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == '--':
                    list_king.append(i)
        if len(list_king) == 62:
            return True
        return False
    
    def king_11_move(self, board): # این تابع هم برای این هستش که وقتی شاه حریف تک مهره بود و 11 باز حرکت کرد بگه بازی مساوی   
        board_1.white_list = []
        board_1.black_list = []
        for i in range(8):
            for j in range(8):
                if board[i][j][0] == 'b':
                    board_1.black_list.append(i)
                elif board[i][j][0] == 'w':
                    board_1.white_list.append(i)
        if len(board_1.white_list) == 1 or len(board_1.black_list) == 1:
            board_1.king_11_move += 1
        if board_1.king_11_move == 22:
            board_1.flag_11_move = True
                    
    def put(self, board, white): # این تابع برای اعلام کردن پات هستش
        x = self.check_in(board, not white)
        u = self.matee(board, white)
        m = self.just_2_king(board)
        if u == True and x == False or m == True or board_1.flag_11_move == True: # قسمت گرافیکی اعلام پات
            pygame.QUIT
            board_1.running = False
            screen_2 = pygame.display.set_mode((200, 200))
            font = pygame.font.Font(None, 56) 
            text_surface = font.render("draw", True, (255, 0, 0)) 
            text_rect = text_surface.get_rect(center=(1 * board_1.SQ_SIZE + board_1.SQ_SIZE // 2, 1 * board_1.SQ_SIZE + board_1.SQ_SIZE // 2))
            screen_2.blit(text_surface, text_rect)
            pygame.display.flip()
            while board_1.running_1:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        board_1.running_1 = False

    def matee(self, board, white): # این تابع برای اعلام مات و پایان بازی هستش
        list_pos = []
        opponent_moves = False
        gh = self.check_in(board, not white)
        for i in range(8):
            for j in range(8):
                if board[i][j][1] == 'P':
                    x = board_1.list_mohre[0]
                elif board[i][j][1] == 'R':
                    x = board_1.list_mohre[1]
                elif board[i][j][1] == 'N':
                    x = board_1.list_mohre[2]
                elif board[i][j][1] == 'Q':
                    x = board_1.list_mohre[3]
                elif board[i][j][1] == 'B':
                    x = board_1.list_mohre[4]
                elif board[i][j][1] == 'K':
                    x = board_1.list_mohre[5]
                elif board[i][j][1] == '-':
                    continue
                move_3 = Move([i, j], [], board)
                x.get_all_possible_moves(move_3, board, white)
                x.filter_possible_moves(board, move_3, white)
                if len(x.possible_moves) == 0:
                    list_pos.append(i)
                else:
                    opponent_moves = True 
                    return False
        if not opponent_moves and gh == True: # قسمت گرافیکی پایان بازی
            pygame.QUIT
            board_1.running = False
            screen_2 = pygame.display.set_mode((200, 200))
            font = pygame.font.Font(None, 36) 
            if  white:
                screen_2.fill(pygame.Color('black'))
                text_surface = font.render("black is winner", True, 'white') 
                text_rect = text_surface.get_rect(center=(1 * board_1.SQ_SIZE + board_1.SQ_SIZE // 2, 1 * board_1.SQ_SIZE + board_1.SQ_SIZE // 2))
                screen_2.blit(text_surface, text_rect)
            if not white:
                screen_2.fill(pygame.Color('white'))
                text_surface = font.render("white is winner", True, 'black') 
                text_rect = text_surface.get_rect(center=(1 * board_1.SQ_SIZE + board_1.SQ_SIZE // 2, 1 * board_1.SQ_SIZE + board_1.SQ_SIZE // 2))
                screen_2.blit(text_surface, text_rect)
            pygame.display.flip()
            while board_1.running_1:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        board_1.running_1 = False
        else :
            if not opponent_moves:
                return True
    def get_all_possible_moves(self, move, board, white): # این تابع برای مشخص کردن حرکات ممکن هستش که توی کلاسایی که ازش ارث بری میکنن تغییر میکنه
        pass
            
    def is_inside_baord(self, startRow, startCol): # این تابع میاد و چک میکنه که مهره حتما توی صفحه باشه
        ROW_COl=[0, 1, 2, 3, 4, 5, 6, 7]
        if startRow in ROW_COl and startCol in ROW_COl: return True 
        else: return False
        
class King(GameState): #  این کلاس برای مهره های مشکی و سفید شاه هستش
    def get_all_possible_moves(self, move, board, white = True): # این تابع برای مشخص کردن حرکات ممکن برای مهره شاه
        self.possible_moves = []
        offsets = [[1, 0], [0, 1], [-1, 0], [0, -1],
                   [1, 1], [-1, 1], [1, -1], [-1, -1]]
        row, col = move.startRow, move.startCol
        if white and board[move.startRow][move.startCol] == 'wK' or not white and board[move.startRow][move.startCol] == 'bK':
            for i in offsets: # حرکات عادی شاه را اضافه میکند
                if self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]] == '--' or  self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]][0] == 'w' and not white or  self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]][0] == 'b' and  white:
                    self.possible_moves.append([row + i[0], col + i[1]])
            if white and not self.has_moved or not white and not self.has_moved_b: # در صورت شرایط شاه قلعه ان را به لیست حرکات ممیکن اضافه میکند
                    if white and board[7][6] == '--' and board[7][5] == '--' and board[7][7] == 'wR' and board_1.rook_w_2 and board[7][4] == 'wK' or not white and board[0][6] == '--' and board[0][5] == '--' and board[0][7] == 'bR' and board[0][4] == 'bK' and board_1.rook_b_2:
                            self.possible_moves.append([row, col + 2])
                            self.kastel= True
                    if white and board[7][1] == '--' and board[7][2] == '--' and board[7][3] == '--' and board[7][0] == 'wR' and board[7][4] == 'wK' and board_1.rook_w_1 or not white and board[0][1] == '--' and board[0][2] == '--' and board[0][3] == '--' and board[0][0] == 'bR' and board[0][4] == 'bK' and board_1.rook_b_1:
                            self.possible_moves.append([row, col - 2])
                            self.kastel = True
        if white == True:
            return True
        return False
          
class Pawn(GameState): # این کلاس برای مشخص کردن حرکات مهره سرباز مشکی و سفید هستش
    def get_all_possible_moves(self, move, board, white=True): # این تابع برای مشخص کردن حرکات ممکن برای سرباز هاست
        row, col = move.startRow, move.startCol
        self.possible_moves = []
        offsets_b=[[1,-1],[1, 1]]
        offsets_w=[[-1,-1],[-1,1]]
        if white and board[move.startRow][move.startCol] == 'wP': # شرط برای مهره های سفید
            if self.is_inside_baord(row - 2, col) and row == 6 and board[6][col] == 'wP'and board[row - 2][col] == '--' and board[row - 1][col] == '--':  # شرط حرکت دوتایی برای اولین حرکت
                self.possible_moves.append([row - 2, col])
            if self.is_inside_baord(row - 1, col) and board[row - 1][col] == '--': # شرط حرکت عادی و یکی رو به جلو سرباز
                self.possible_moves.append([row - 1, col])
            for i in offsets_w:
                if self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]][0] == 'b': # شرط زدن مهره حریف
                    self.possible_moves.append([row + i[0], col + i[1]])
            if len(board_1.last_pos) != 0 and  self.is_inside_baord(board_1.last_pos[1][0] -1 , 2) and board_1.last_pos[1][1] - 1 == col and row == 3 and board_1.last_pos[0][0] == 1 and board_1.last_pos[1][0] == 3 and board[board_1.last_pos[1][0]][board_1.last_pos[1][1]] == 'bP' and board[board_1.last_pos[1][0] - 1][board_1.last_pos[1][1]] == '--' and board[3][col + 1] == 'bP'  or len(board_1.last_pos) != 0 and  self.is_inside_baord(board_1.last_pos[1][0] -1 , 2) and row == 3 and board_1.last_pos[0][0] == 1 and board_1.last_pos[1][0] == 3 and board[board_1.last_pos[1][0]][board_1.last_pos[1][1]] == 'bP' and board[board_1.last_pos[1][0] - 1][board_1.last_pos[1][1]] == '--' and board[3][col - 1] == 'bP' and board_1.last_pos[1][1] + 1 == col:
                self.possible_moves.append([board_1.last_pos[1][0] - 1, board_1.last_pos[1][1]]) # این شرط هم برای آن پاسان هستش
                board_1.an_pasan = True
        if not white and board[move.startRow][move.startCol] == 'bP': # همان شروط برای مهره مشکی هم در این بخش شرط است
            if self.is_inside_baord(row + 2, col) and board[row + 2][col] == '--' and board[row + 1][col] == '--' and row == 1 and board[1][col] == 'bP':
                self.possible_moves.append([row + 2, col])
            if self.is_inside_baord(row + 1, col) and board[row + 1][col] == '--':
                self.possible_moves.append([row + 1, col])
            for i in offsets_b:
                if self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]][0] == 'w':
                    self.possible_moves.append([row + i[0], col + i[1]])  
            if len(board_1.last_pos) != 0 and board_1.last_pos[1][1] - 1 == col  and self.is_inside_baord(board_1.last_pos[1][0] + 1 , 6) and row == 4 and board_1.last_pos[0][0] == 6 and board_1.last_pos[1][0] == 4 and board[board_1.last_pos[1][0]][board_1.last_pos[1][1]] == 'wP' and board[board_1.last_pos[1][0] + 1][board_1.last_pos[1][1]] == '--' and board[4][col + 1] == 'wP' or len(board_1.last_pos) != 0 and  self.is_inside_baord(board_1.last_pos[1][0] -1 , 6) and row == 4 and board_1.last_pos[0][0] == 6 and board_1.last_pos[1][0] == 4 and board[board_1.last_pos[1][0]][board_1.last_pos[1][1]] == 'wP' and board[board_1.last_pos[1][0] + 1][board_1.last_pos[1][1]] == '--' and board[4][col - 1] == 'wP' and board_1.last_pos[1][1] + 1 == col:
                self.possible_moves.append([board_1.last_pos[1][0] + 1, board_1.last_pos[1][1]])
                board_1.an_pasan = True
        if white == True:
            return True
        return False

class Rook(GameState): #  این کلاس برای مشخص کردن حرکت مهره قلعه مشکی و سفید هستش
    def get_all_possible_moves(self, move, board, white = True):
        self.possible_moves = []
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        if white and board[move.startRow][move.startCol] == 'wR' or not white and board[move.startRow][move.startCol] == 'bR':    
            for i in directions: # اگر برای حرکت رو به جلو بعدی هم امکانش باشه اون رو هم اضاغه میکنه در غیر این صورت میره برای عضو بعدی چک کنهwhile با توجه به اعضای درون این لیست با یک حلقه
                row, col = move.startRow, move.startCol
                while self.is_inside_baord(row, col):
                    row += i[0]
                    col += i[1]
                    if not self.is_inside_baord(row, col):
                        break
                    if board[row][col] == '--':
                        self.possible_moves.append([row, col])
                    elif board[row][col][0] == 'w' and not white or board[row][col][0] == 'b' and white:
                        self.possible_moves.append([row, col])
                        break
                    else:
                        break
        if white == True:
            return True
        return False

class Knight(GameState): # این کلاس برای مشخص کردن حرکات ممکن برای مهره اسب سفید و مشکی هستش
    def get_all_possible_moves(self, move, board, white):
        self.possible_moves = []
        offsets = [[2, 1], [2, -1], [1, 2], [1, -2],
                [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        row, col = move.startRow, move.startCol
        if white and board[move.startRow][move.startCol] == 'wN' or not white and board[move.startRow][move.startCol] == 'bN':
            for i in offsets: # با توجه به اعضای داخل این لیست اگر به ازای هرکدام شرایط حرکت ممکن باشد ان را اضافه میکند
                if self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]] == '--' or  white and self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]][0] == 'b' or not white and self.is_inside_baord(row + i[0], col + i[1]) and board[row + i[0]][col + i[1]][0] == 'w':
                    self.possible_moves.append([row + i[0], col + i[1]])
        if white == True:
            return True
        return False

class Queen(GameState): # این کلاس برای مشخص کردن حرکات ممکن برای مهره وزیر مشکی و سفید است که به یک شکلی مانند کلاس قلعه برای مشخص کردن حرکاتش استفاده میشه
    def get_all_possible_moves(self, move, board, white = True):
        self.possible_moves = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        if white and board[move.startRow][move.startCol] == 'wQ' or not white and board[move.startRow][move.startCol] == 'bQ':
            for i in directions:
                row, col = move.startRow, move.startCol
                while self.is_inside_baord(row, col):
                    row += i[0]
                    col += i[1]
                    if not self.is_inside_baord(row, col):
                        break
                    if board[row][col] == '--':
                        self.possible_moves.append([row, col])
                    elif board[row][col][0] == 'w' and not white or board[row][col][0] == 'b' and white:
                        self.possible_moves.append([row, col])
                        break
                    else:
                        break
        if white == True:
            return True
        return False
  
class Bishop(GameState): # این کلاس هم برای مشخص کردن حرکات ممکن برای مهره فیل مشکی و سفید هست که به مانند وزیر و قلعه برای مشخص کردن حرکاتش استفاده میشود
    def get_all_possible_moves(self, move, board, white = True):
        self.possible_moves = []
        directions = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        if white and board[move.startRow][move.startCol] == 'wB' or not white and board[move.startRow][move.startCol] == 'bB':
            for i in directions:
                row, col = move.startRow, move.startCol
                while self.is_inside_baord(row, col):
                    row += i[0]
                    col += i[1]
                    if not self.is_inside_baord(row, col):
                        break
                    if board[row][col] == '--':
                        self.possible_moves.append([row, col])
                    elif board[row][col][0] == 'w' and not white or board[row][col][0] == 'b' and white:
                        self.possible_moves.append([row, col])
                        break
                    else:
                        break
        if white == True:
            return True
        return False
        
class Move: # این کلاس موقعیت های مکانی که انتخاب کردیم رو به یک متغییر نسبت میدن
    def __init__(self, start_sq, end_sq = [], board = []):
        if len(start_sq) != 0:
            self.startRow = start_sq[0] # row کلیک اول
            self.startCol = start_sq[1] # col کلیک اول
            self.pieceMoved = board[self.startRow][self.startCol] # مختصات به ازای کلیک اول در برد بازی
        if len(end_sq) != 0 :
            self.endRow = end_sq[0] # row کلیک دوم
            self.endCol = end_sq[1] # col کلیک دوم
            self.pieceCaptured = board[self.endRow][self.endCol]  # مختصات به ازای کلیک دوم در برد بازی

class Board:
    def __init__(self):   # داخل این تابع هر متغییر ثابت برای صفحه گرافیکی بازی و خود کد نیاز بوده ساخته شده
        self.WIDTH = self.HEIGHT = 512
        self.DIMENSION = 8 
        self.SQ_SIZE = self.HEIGHT // self.DIMENSION
        self.MAX_FPS = 15
        self.IMAGES = {}
        self.load_images()
        self.white = True
        self.white_1 = True
        self.w = True
        self.trans_position = True
        self.check = False
        self.check_possible_moves = []
        self.all_possible_moves = []
        self.pos_king = []
        self.last_pos = []
        self.king_11_move = 0
        self.black_list = []
        self.white_list = []
        self.flag_11_move = False
        self.an_pasan = False
        self.rook_w_1, self.rook_w_2, self.rook_b_1, self.rook_b_2= True, True, True, True
    def load_images(self):   # این تابع برای اینه که عکس هارو لود کنه
        self.pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wP']
        for piece in self.pieces:
            self.IMAGES[piece] = pygame.transform.scale(pygame.image.load(piece+'.png'), (self.SQ_SIZE, self.SQ_SIZE))
    
    def draw_board(self,screen):   # این تابع عم برای رسم کردن برد بازی هستش
        colors = [pygame.Color("#F2DEBC"), pygame.Color("#C7A165")]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                self.color = colors[((r + c) % 2)]
                pygame.draw.rect(screen, self.color, pygame.Rect(c * self.SQ_SIZE, r * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def draw_pieces(self, screen, board):  # این تابع هم برای قرار دادن عکس در مختصات مورد نظر در برد اصلی هستش
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                self.piece = board[r][c]
                if self.piece != '--':
                    screen.blit(self.IMAGES[self.piece], pygame.Rect(c * self.SQ_SIZE, r * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def draw_possible_moves(self, x, screen, board):  # این تابع برای رسم کردن حرکات ممکن برای هر مهره ای که کلیک میشه ساخته شده
            for i in x:
                if board[i[0]][i[1]] == '--':
                    colors = [pygame.Color("#F2DEBC"), pygame.Color('#C7A165')]
                    color = colors[((i[0] + i[1]) % 2)]
                    pygame.draw.rect(screen, color, pygame.Rect(i[1] * self.SQ_SIZE, i[0] * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    font = pygame.font.Font(None, 44) 
                    text_surface = font.render(".", True, 'black')
                    text_rect = text_surface.get_rect(center=(i[1] * self.SQ_SIZE + self.SQ_SIZE // 2, i[0] * self.SQ_SIZE + self.SQ_SIZE  // 2))
                    screen.blit(text_surface, text_rect)
                if board[i[0]][i[1]] != '--':
                    pygame.draw.rect(screen, '#B2323D', pygame.Rect(i[1] * self.SQ_SIZE, i[0] * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    screen.blit(self.IMAGES[board[i[0]][i[1]]], pygame.Rect(i[1] * self.SQ_SIZE, i[0] * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
            pygame.display.flip()
            
    def main(self):  # خب رسیدیم به مهم ترین تابع بازی که اتصال همه توابع داخل این تابع هستش
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.fill(pygame.Color("white"))
        gs, p, r, n, q, m, k = GameState(), Pawn(), Rook(), Knight(), Queen(), Bishop(), King()  # ساخت همه کلاس ها
        i = False
        u = False
        self.board_2 = []
        self.list_mohre = [p, r, n, q, m, k]
        self.load_images()
        self.running = True
        self.running_1 = True
        self.sqSelected = ()  
        self.player_clicks = [] 
        self.draw_board(self.screen)  # ساخت صفحه بازی
        self.draw_pieces(self.screen, gs.board) # قرار دارن مهره ها در برد بازی
        self.clock.tick(self.MAX_FPS)
        pygame.display.flip()
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:  # اگه دکمه ضربدر رو زد از بازی بره بیرون و حلقه رو غیر فعال کنه
                    self.running = False
                elif e.type == pygame.MOUSEBUTTONDOWN:  # وقتی کلیک اول رو میکنیم این دستورات انجام میشه 
                    self.location = pygame.mouse.get_pos()  # موقعیت کلیک رو میگیره
                    self.col = self.location[0] // self.SQ_SIZE
                    self.row = self.location[1] // self.SQ_SIZE
                    move1 = Move([self.row, self.col], [0, 0], gs.board) # این سه خط بعدی برای اینه که وقتی سرباز رفت اخر صفحه هیچ مهره ای در صفحه حرکت نکنه تا وقتی که ما سرباز رو تغییر بدیم
                    board_1.board_2 = copy.deepcopy(gs.board)
                    gs.make_move(move1, gs.board , white=True, list_1=gs.list_1)
                    if self.trans_position == True: 
                        if self.sqSelected != (self.row, self.col):  # شرط بعدی برای اینه که اگه من مهره انتخاب کردم با توجه به اون مهره کلاس مورد نظرش رو فرا بخونه
                                self.sqSelected = (self.row, self.col)
                                self.player_clicks.append(self.sqSelected)    
                                if gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == 'P':
                                    x = p
                                elif gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == 'B':
                                    x = m
                                elif gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == 'R':
                                    x = r
                                elif gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == 'Q':
                                    x = q
                                elif gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == 'N':
                                    x = n
                                elif gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == 'K':
                                    x = k  
                                if gs.board[self.player_clicks[0][0]][self.player_clicks[0][1]][1] == '-':  # اگه هیچ مهره ای انتخاب نکردم کلیک اول بی تاثیر باشه
                                    self.sqSelected = ()  
                                    self.player_clicks = []
                                else: # اگر مهره انتخاب کردم
                                    move = Move(self.player_clicks[0], [0, 0], gs.board)
                                    white = x.get_all_possible_moves(move, gs.board, self.white) #  تابع برای مشخص کردن حرکات ممکن اون مهره
                                    if white == True:
                                        self.white = True
                                    elif white == False:
                                        self.white = False
                                    self.copy_list = copy.deepcopy(gs.board)
                                    x.filter_possible_moves(gs.board, move, white) # در صورت کیش بودن حرکاتی که جلوی کیش رو میگیرن مشخص بشن
                                    gs.board = self.copy_list
                                    self.draw_possible_moves(x.possible_moves, self.screen, gs.board) # رسم کردن حرکات ممکن
                                    if len(self.player_clicks) == 2: # وقتی که کلیک دوم رو کرد
                                        move = Move(self.player_clicks[0], self.player_clicks[1], gs.board) # نسبت میدهstart, end مختصات مهره اول و مهره دوم رو به 
                                        board_1.board_2 = copy.deepcopy(gs.board)
                                        b = x.make_move(move, gs.board, self.white, gs.list_1)  # جابه جا کردن مهره
                                        if b == False:
                                            self.white = False
                                        elif b == True:
                                            self.white = True
                                        ty = x.check_in(gs.board, not white) # چک کردن این که ایا کیش هست یا خیر
                                        if i == True or ty == True:
                                            u = x.back_to_difault(gs.board) # اگر هست که صفحه رو با حالت قبلی با کمک کپی که گرفتیم برگردونه به حالت قبلی
                                        i = x.check_in(gs.board, not self.white)
                                        if u == True:
                                            gs.board = board_1.board_2
                                        self.clock.tick(self.MAX_FPS)
                                        self.draw_board(self.screen) # رسم صفحه
                                        self.draw_pieces(self.screen, gs.board) # رسم مهره ها
                                        pygame.display.flip()
                                        x.put(gs.board, not white) # چک کنه ایا بازی مساوی هستش یا خیر
                                        x.matee(gs.board, not white) # چک کنه که ایا بازی مات هستش یا خیر
                                        kf = x.check_in(gs.board, white)
                                        km = x.check_in(gs.board, not white)
                                        if kf == True or km == True: # وقتی شاه کیش بود رنگیش کنه
                                            pygame.draw.rect(self.screen, '#9900FF', pygame.Rect(self.pos_king[1] * self.SQ_SIZE, self.pos_king[0] * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                                            self.screen.blit(self.IMAGES[gs.board[self.pos_king[0]][self.pos_king[1]]], pygame.Rect(self.pos_king[1] * self.SQ_SIZE, self.pos_king[0] * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                                            pygame.display.flip()
                                        self.sqSelected = ()  # در اخر همه کلیک هارو خالی کنه
                                        self.player_clicks = []

if __name__ == "__main__":
    board_1=Board() # ساخت کلاس برد
    board_1.main() # فرا خواندن مهم ترین تابع بازی تا در ابتدا برد بازی را اجرا کند