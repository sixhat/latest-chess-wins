import sys
import chess
import chess.pgn

def printGame(g):
    board = g.board()
    
    for move in g.mainline_moves():
        c=board.san(move)
        a = board.fen()
        a = a.split()
        a = "".join(a[0:2]).replace("/","")
        board.push(move)
        b = board.fen()
        b = b.split()
        b = "".join(b[0:2]).replace("/","")
        
        print('"{}" -- "{}" [label="{}"]'.format(a,b,c))

if __name__ == "__main__":
    pgn = open(sys.argv[1])

    print("strict graph {")
    game = chess.pgn.read_game(pgn)
    while game is not None:
        printGame(game)
        game = chess.pgn.read_game(pgn)
    print("}")