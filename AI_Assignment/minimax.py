import chess
import random
from AI_Assignment.evaluate import evaluate_board

def minimax(env, board, depth, is_maximizing, use_randomness=False):
    # Base case: return evaluation for terminal or max-depth position
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    # Get legal moves
    moves = list(env.legal_moves)
    
    # If randomness is enabled, shuffle moves
    if use_randomness:
        random.shuffle(moves)

    best_move = None

    if is_maximizing:
        best_score = float('-inf')

        # Prioritize moves that capture pieces (simple heuristic)
        captures = [move for move in moves if board.is_capture(move)]
        non_captures = [move for move in moves if not board.is_capture(move)]
        
        # First check capturing moves, then non-capturing moves
        ordered_moves = captures + non_captures

        for move in ordered_moves:
            board.push(move)
            score, _ = minimax(env, board, depth - 1, False, use_randomness)
            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    else:
        best_score = float('inf')

        # Prioritize moves that capture pieces (simple heuristic)
        captures = [move for move in moves if board.is_capture(move)]
        non_captures = [move for move in moves if not board.is_capture(move)]
        
        # First check capturing moves, then non-capturing moves
        ordered_moves = captures + non_captures

        for move in ordered_moves:
            board.push(move)
            score, _ = minimax(env, board, depth - 1, True, use_randomness)
            board.pop()

            if score < best_score:
                best_score = score
                best_move = move

        return best_score, best_move

def main():
    # Set up chess board
    board = chess.Board()

    # Define depth for the minimax search
    depth = 3
    
    # Use the minimax function to find the best move
    score, best_move = minimax(board, board, depth, True, use_randomness=True)
    
    # Print the best move
    print("Best move:", best_move)

if __name__ == "__main__":
    main()
