"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import sys


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass

def custom_score(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return custom_score_heuristic_flex_strategy(game, player)

def custom_score_heuristic_flex_strategy(game, player):
    total_space = game.width * game.height
    third_of_total = total_space / 3
    number_of_blank_space = len(game.get_blank_spaces())

    # if number_of_blank_space > (third_of_total * 2):
    #     # print("1/3:Start")
    #     return custom_score_heuristic_avoid_edge(game, player)
    # elif number_of_blank_space > third_of_total:
    #     # print("2/3:Mid")
    #     return custom_score_heuristic_more_weighted_opp_moves(game, player, 2)
    # else:
    #     # print("3/3:End")
    #     return custom_score_heuristic_more_weighted_opp_moves(game, player, 1)

    half_of_total = total_space / 2
    if number_of_blank_space > half_of_total:
        return custom_score_heuristic_avoid_edge(game, player)
    else:
        return custom_score_heuristic_more_weighted_opp_moves(game, player, 2)

def custom_score_heuristic_avoid_edge(game, player):
    edge_weighted = 0

    row, column = game.get_player_location(player)
    if row == 0 or column == 0 or row == (game.height-1) or column == (game.width-1):
        edge_weighted = -4
    elif row == 1 or column == 1 or row == (game.height-2) or column == (game.width-2):
        edge_weighted = -2
    elif row == 2 or column == 2 or row == (game.height-3) or column == (game.width-3):
        edge_weighted = -1

    row, column = game.get_player_location(game.get_opponent(player))
    if row == 0 or column == 0 or row == (game.height-1) or column == (game.width-1):
        edge_weighted += 4
    elif row == 1 or column == 1 or row == (game.height-2) or column == (game.width-2):
        edge_weighted += 2
    elif row == 2 or column == 2 or row == (game.height-3) or column == (game.width-3):
        edge_weighted += 1

    # return edge_weighted
    return float(custom_score_heuristic_more_weighted_opp_moves(game, player, 2) + edge_weighted)

def custom_score_heuristic_more_weighted_opp_moves(game, player, opp_weighted):
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    if own_moves is 0:
        return float("-inf")

    if opp_moves is 0:
        return float("inf")

    return float(own_moves - (opp_weighted * opp_moves))

# def custom_score(game, player):
#     """Calculate the heuristic value of a game state from the point of view
#     of the given player.

#     Note: this function should be called from within a Player instance as
#     `self.score()` -- you should not need to call this function directly.

#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).

#     player : object
#         A player instance in the current game (i.e., an object corresponding to
#         one of the player objects `game.__player_1__` or `game.__player_2__`.)

#     Returns
#     -------
#     float
#         The heuristic value of the current game state to the specified player.
#     """
#     if game.is_loser(player):
#         return float("-inf")

#     if game.is_winner(player):
#         return float("inf")

#     selected_heuristic_number = 4

#     if selected_heuristic_number == 1:
#         return custom_score_heuristic_only_defense(game, player)
#     elif selected_heuristic_number == 2:
#         return custom_score_heuristic_more_weighted_opp_moves(game, player)
#     elif selected_heuristic_number == 3:
#         return custom_score_heuristic_avoid_edge(game, player)
#     elif selected_heuristic_number == 4:
#         return custom_score_heuristic_flex_strategy(game, player)

#     return custom_score_heuristic_flex_strategy(game, player)

# def custom_score_heuristic_flex_strategy(game, player):
#     """We can take a different strategy in first-half and second-half of game.
#     If the game is in the first-half, then try not to go edge of board.
#     However if the game is going to be a second-half,
#     then take the weighted moves of opponent player strategy.

#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).

#     player : hashable
#         One of the objects registered by the game object as a valid player.
#         (i.e., `player` should be either game.__player_1__ or
#         game.__player_2__).

#     Returns
#     ----------
#     float
#         The heuristic value of the current game state
#     """
#     total_space = game.width * game.height

#     if (total_space/2) < len(game.get_blank_spaces()):
#         return custom_score_heuristic_avoid_edge(game, player)
#     else:
#         return custom_score_heuristic_more_weighted_opp_moves(game, player)

# def custom_score_heuristic_avoid_edge(game, player):
#     """There will be less moves in edge of board.
#     So if the current location is the edge of board,
#     then decerese the score.

#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).

#     player : hashable
#         One of the objects registered by the game object as a valid player.
#         (i.e., `player` should be either game.__player_1__ or
#         game.__player_2__).

#     Returns
#     ----------
#     float
#         The heuristic value of the current game state
#     """
#     edge_weighted = 0

#     row, column = game.get_player_location(player)
#     if row == 0 or column == 0 or row == (game.height-1) or column == (game.width-1):
#         edge_weighted = 4
#     elif row == 1 or column == 1 or row == (game.height-2) or column == (game.width-2):
#         edge_weighted = 2

#     return float(custom_score_heuristic_more_weighted_opp_moves(game, player) - edge_weighted)

# def custom_score_heuristic_more_weighted_opp_moves(game, player):
#     """Let's put higher priority in oppenent moves.
#     So we will subtract the 2 times score of oppoenent's moves from customer score.

#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).

#     player : hashable
#         One of the objects registered by the game object as a valid player.
#         (i.e., `player` should be either game.__player_1__ or
#         game.__player_2__).

#     Returns
#     ----------
#     float
#         The heuristic value of the current game state
#     """
#     own_moves = len(game.get_legal_moves(player))
#     opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

#     return float(own_moves - (2*opp_moves))

# def custom_score_heuristic_only_defense(game, player):
#     """The best defense is a good offense!
#     https://en.wikipedia.org/wiki/The_best_defense_is_a_good_offense
#     So, choose the move having opppnent's minimum legal moves.

#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).

#     player : hashable
#         One of the objects registered by the game object as a valid player.
#         (i.e., `player` should be either game.__player_1__ or
#         game.__player_2__).

#     Returns
#     ----------
#     float
#         The heuristic value of the current game state
#     """
#     max_legal_moves = 8
#     opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

#     return float(max_legal_moves - opp_moves)

class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=20.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        best_move = (-1, -1)

        if not legal_moves:
            return best_move

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if self.iterative is True:
                # Must perform iterative deepening
                depth = 0
                while True:
                    # Get the best move with the increasing depth.
                    if self.method is 'minimax':
                        # Must use the search method minimax
                        best_score, best_move = self.minimax(game, depth)
                    elif self.method is 'alphabeta':
                        # Must use the search method alphabeta
                        best_score, best_move = self.alphabeta(game, depth)
                    else:
                        break

                    # If there is no place to move,
                    # then stop the loop and return (-1, -1).
                    if best_move is (-1, -1):
                        break

                    depth += 1
            else:
                if self.method is 'minimax':
                    # Must use the search method minimax
                    best_score, best_move = self.minimax(game, self.search_depth)
                elif self.method is 'alphabeta':
                    # Must use the search method alphabeta
                    best_score, best_move = self.alphabeta(game, self.search_depth)
                else:
                    pass

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return best_move

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # Initialize
        best_score = float("-inf")
        best_move = (-1, -1)

        # If the game board is empty, then return initail value.
        if self.is_terminal_state(game, depth):
            return (best_score, best_move)

        # Check all sub-state and choose the max score as best move.
        for next_move in game.get_legal_moves():
            new_game = game.forecast_move(next_move)
            new_score = self.minimax_get_min_score(new_game, depth-1)
            if new_score > best_score:
                best_score = new_score
                best_move = next_move

        return (best_score, best_move)

    def minimax_get_max_score(self, game, depth):
        """Get maximum score in current state using Minimax algorithm.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        float
            Maximum score.

        """
        if self.is_terminal_state(game, depth):
            return self.score(game, self)

        # If the time lefts less than TIMER_THRESHOLD,
        # then immediately return the best move so far.
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        max_score = float("-inf")

        for next_move in game.get_legal_moves():
            new_game = game.forecast_move(next_move)
            new_score = self.minimax_get_min_score(new_game, depth-1)
            if new_score > max_score:
                max_score = new_score

        return max_score

    def minimax_get_min_score(self, game, depth):
        """Get minimum score in current state using Minimax algorithm.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        float
            Minimum score.

        """
        if self.is_terminal_state(game, depth):
            return self.score(game, self)

        # If the time lefts less than TIMER_THRESHOLD,
        # then immediately return the best move so far.
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        min_score = float("inf")

        for next_move in game.get_legal_moves():
            new_game = game.forecast_move(next_move)
            new_score = self.minimax_get_max_score(new_game, depth-1)
            if new_score < min_score:
                min_score = new_score

        return min_score

    def is_terminal_state(self, game, depth):
        """Check whether current state is terminal state or not.

        Returns
        -------
        bool
            Return True if current state is a terminal state, otherwise return False.

        """
        if not game.get_legal_moves() or depth is 0:
            return True
        return False

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # Initialize
        best_score = float("-inf")
        best_move = (-1, -1)

        # If the game board is empty, then return initail value.
        if self.is_terminal_state(game, depth):
            return (best_score, best_move)

        # # Check all sub-state and choose the max score as best move.
        # for next_move in game.get_legal_moves():
        #     new_game = game.forecast_move(next_move)
        #     new_score = self.alphabeta_get_min_score(new_game, depth-1, alpha, beta)
        #     if new_score > best_score:
        #         best_score = new_score
        #         best_move = next_move

        # Get best score of current state.
        best_score, best_move = self.alphabeta_get_max_score(game, depth, alpha, beta)

        return (best_score, best_move)

    def alphabeta_get_max_score(self, game, depth, alpha, beta):
        """Get maximum score in current state using Alpha-Beta Pruning algorithm.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        float
            Maximum score.

        """
        if self.is_terminal_state(game, depth):
            return self.score(game, self), game.get_player_location(self)

        # If the time lefts less than TIMER_THRESHOLD,
        # then immediately return the best move so far.
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        max_score = float("-inf")
        best_move = (-1, -1)

        for next_move in game.get_legal_moves():
            new_game = game.forecast_move(next_move)
            new_score, move = self.alphabeta_get_min_score(new_game, depth-1, alpha, beta)
            if new_score > max_score:
                max_score = new_score
                best_move = next_move
            if max_score >= beta:
                return max_score, best_move
            else:
                if alpha < max_score:
                    alpha = max_score

        return max_score, best_move

    def alphabeta_get_min_score(self, game, depth, alpha, beta):
        """Get minimum score in current state Alpha-Beta Pruning algorithm.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        float
            Minimum score.

        """
        if self.is_terminal_state(game, depth):
            return self.score(game, self), game.get_player_location(self)

        # If the time lefts less than TIMER_THRESHOLD,
        # then immediately return the best move so far.
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        min_score = float("inf")
        best_move = (-1, -1)

        for next_move in game.get_legal_moves():
            new_game = game.forecast_move(next_move)
            new_score, move = self.alphabeta_get_max_score(new_game, depth-1, alpha, beta)
            if new_score < min_score:
                min_score = new_score
                best_move = next_move
            if min_score <= alpha:
                return min_score, best_move
            else:
                if beta > min_score:
                    beta = min_score

        return min_score, best_move
