from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(PLAYER_RADIUS)
    