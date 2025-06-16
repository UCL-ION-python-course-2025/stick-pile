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
    raise NotImplementedError(
        "You need to implement this function!"
    )  # <-- Delete this line to get started


if __name__ == "__main__":  # <----------- please don't change this line

    # This runs the game with your solution playing against a randomly
    # moving opponent. Do not touch this until you've got a good solution.
    play_game(
        your_choose_move=choose_move,
        opponent_choose_move=choose_move_randomly,
        game_speed_multiplier=1,  # <--- Change this if you want the game to run faster or slower
    )
