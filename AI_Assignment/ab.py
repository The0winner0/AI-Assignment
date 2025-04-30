import chess
from evaluate import E

def alphabeta(env, board, depth, alpha, beta, is_maximizing):
    # Base case: evaluate terminal positions or at depth limit
    if depth == 0 or board.is_game_over():
        return E(board), None

    moves = list(env.legal_moves)
    optimal_move = None

    if is_maximizing:
        current_score = float('-inf')
        for candidate_move in moves:
            board.push(candidate_move)
            score, _ = alphabeta(env, board, depth - 1, alpha, beta, False)
            board.pop()

            if score > current_score:
                current_score = score
                optimal_move = candidate_move

            alpha = max(alpha, current_score)
            if beta <= alpha:
                break  # Beta cut-off
        return current_score, optimal_move

    else:
        current_score = float('inf')
        for candidate_move in moves:
            board.push(candidate_move)
            score, _ = alphabeta(env, board, depth - 1, alpha, beta, True)
            board.pop()

            if score < current_score:
                current_score = score
                optimal_move = candidate_move

            beta = min(beta, current_score)
            if beta <= alpha:
                break # Alpha cut-off
        return current_score, optimal_move

def main():
    # Set up chess board
    board = chess.Board()

    # Define depth for the alpha-beta search
    depth = 3
    
    # Perform the search for the best move
    score, best_move = alphabeta(board, board, depth, float('-inf'), float('inf'), True)
    
    # Print the best move
    print("Best move:", best_move)

if __name__ == "__main__":
    main()
