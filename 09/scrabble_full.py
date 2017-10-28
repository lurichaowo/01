TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
            
dict = {"aeioulnrst":"1", 
        "dg":"2", 
        "bcmp":"3", 
        "fhvwy":"4",
        "k":"5",
        "kx":"8",
        "qz":"10"}

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ''.join(line))
        
def add_word_across(board, word, r, c):
    string = []
    scores = 0
    i = 0
    while i < len(word):
        for let in word:
            string.append(board[r][c+i])
            board[r][c+i] = let
            i += 1
    scores = score(string, word)
    print(scores)
    
def add_word_down(board, word, r, c):
    string = []
    scores = 0
    i = 0
    while i < len(word):
        for let in word:
            string.append(board[r+i][c])
            board[r+i][c] = let
            i += 1
    scores = score(string, word)
    print(scores)

def score(s,w):
    score = 0
    w = w.lower()
    for index,i in enumerate(w):
        for key,val in dict.items():
          if i in key:
            if (s[index] == 'T'):
                score += int(val) * 3
            elif (s[index] == 'D'):
                score += int(val) * 2
            else:
                score += int(val)
    if "d" in s:
        score = score * 2
    elif "t" in s:
        score = score * 3
    return score
    
    
b = make_scrabble_board()
print_board(b)
add_word_across(b, "hello", 1,2)
add_word_down(b, "super", 5,4)
print_board(b)
