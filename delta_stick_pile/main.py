from check_submission import check_submission
from game_mechanics import choose_move_randomly, play_game

TEAM_NAME = "Team Name"  # <---- Enter your team name here!

# This just checks that you've entered a team name. Don't change this.
assert TEAM_NAME != "Team Name", "Please change your TEAM_NAME!"


def choose_move(number_of_sticks_remaining):
    """This is the function you need to write!

    Args:
        number_of_sticks_remaining (integer): The number of sticks remaining in the pile.

    Returns:
        number_of_sticks_to_remove (integer): The number of sticks you want to remove from the pile.
    """
    raise NotImplementedError("You need to implement this function!")


if __name__ == "__main__":

    ## Example workflow, feel free to edit this! ###

    check_submission(
        TEAM_NAME
    )  # <---- Make sure I pass! Or your solution will not work in the tournament!!

    play_game(
        your_choose_move=choose_move,
        opponent_choose_move=choose_move_randomly,
        game_speed_multiplier=1,
    )
