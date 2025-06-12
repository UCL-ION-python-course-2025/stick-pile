from typing import Any, Dict

from check_submission import check_submission
from game_mechanics import StickPile, choose_move_randomly, play_game

TEAM_NAME = "JR"  # <---- Enter your team name here!
assert TEAM_NAME != "Team Name", "Please change your TEAM_NAME!"


def choose_move(number_of_sticks_remaining):
    """This is the function you need to write!

    Args:
        number_of_sticks_remaining (integer): The number of sticks remaining in the pile.

    Returns:
        number_of_sticks_to_remove (integer): The number of sticks you want to remove from the pile.
    """
    return 3
    # pass


if __name__ == "__main__":

    ## Example workflow, feel free to edit this! ###

    # check_submission(
    #     TEAM_NAME
    # )  # <---- Make sure I pass! Or your solution will not work in the tournament!!

    play_game(
        your_choose_move=choose_move,
        opponent_choose_move=choose_move_randomly,
        game_speed_multiplier=1,
        render=True,
        verbose=True,
    )
