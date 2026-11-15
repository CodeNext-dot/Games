class Player_status:
    def __init__(self):
        self.name = ""
        self.person = 0
        self.life = 100
        self.damage = 10
        self.money = 0
        self.color = (0, 0, 0)

class Enemy_status:
    def __init__(self):
        self.life = 10
        self.damage = 5
        self.color = (128, 0, 128)
        self.time = 0

class GameData:
    def __init__(self):
        self.resposta = ""