import gym
import gym_chess
import chess
import chess.svg
import cairosvg
import imageio
from AI_Project.ai_algorithms import minimax_algorithm
from AI_Project.ai_algorithms import alphabeta_algorithm
from PIL import Image
import io

def convert_board_to_image(chess_board):
    """Convert a chess.Board object to an image format."""
    svg_content = chess.svg.board(board=chess_board)
    png_content = cairosvg.svg2png(bytestring=svg_content)
    return Image.open(io.BytesIO(png_content))

def select_best_move(game_env, chess_board, strategy, search_depth):
    """Determine the best move based on the given strategy."""
    valid_moves = list(game_env.legal_moves)

    if strategy == 'minimax':
        _, move = minimax_algorithm(game_env, chess_board, search_depth, chess_board.turn)
    elif strategy == 'alphabeta':
        _, move = alphabeta_algorithm(game_env, chess_board, search_depth, float('-inf'), float('inf'), chess_board.turn)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    # If the chosen move is invalid, select a random legal move
    if move not in valid_moves:
        print("Invalid move — selecting a random valid move.")
        move = valid_moves[0]

    return move

def start_chess_game(strategy='minimax', search_depth=2, output_gif='chess_game.gif'):
    chess_env = gym.make('Chess-v0')
    chess_env.reset()

    game_frames = [convert_board_to_image(chess_env._board)]
    game_ongoing = True

    while game_ongoing:
        current_board = chess_env._board
        best_move = select_best_move(chess_env, current_board, strategy, search_depth)
        _, game_reward, game_ongoing, _ = chess_env.step(best_move)
        game_frames.append(convert_board_to_image(chess_env._board))

    print(f"Game Over. Final result: {chess_env._board.result()}")
    chess_env.close()

    game_frames[0].save(
        output_gif,
        save_all=True,
        append_images=game_frames[1:],
        duration=800,
        loop=0
    )
    print(f"Game GIF saved as {output_gif}")

if __name__ == "__main__":
    print("Running Minimax AI Chess Game")
    start_chess_game('minimax', 3, 'minimax_chess.gif')

    print("\nRunning Alpha-Beta AI Chess Game")
    start_chess_game('alphabeta', 3, 'alphabeta_chess.gif')
