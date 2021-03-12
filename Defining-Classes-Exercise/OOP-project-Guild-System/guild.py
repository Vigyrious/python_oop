from Library.player import Player



class Guild:
    def __init__(self, name):
        self.name = name
        self.members = []


    def assign_player(self, player: Player):
        player_info = player.guild
        if player_info == "Unaffiliated":
            self.members.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player_info == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        player = [p for p in self.members if p.name == player_name]
        if player:
            player[0].guild = "Unaffiliated"
            self.members.remove(player[0])
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."


    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.members:
            result += player.player_info()
        return result

