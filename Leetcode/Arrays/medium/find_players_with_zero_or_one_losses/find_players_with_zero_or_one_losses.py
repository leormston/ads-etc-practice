class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_dict = {}
        los_dict = {}
        for match in matches:
            winner = match[0]
            loser = match[1]
            if str(winner) in win_dict:
                wins = win_dict[str(winner)]
                win_dict[str(winner)] = wins + 1
            else:
                win_dict[str(winner)] = 1
            if str(loser) in los_dict:
                loss = los_dict[str(loser)] 
                los_dict[str(loser)] = loss+ 1
            else:
                los_dict[str(loser)] = 1

        no_losses = []
        one_loss = []
        for k, v in win_dict.items():
            if k not in los_dict:
                no_losses.append(int(k))
        for k, v in los_dict.items():
            if v == 1:
                one_loss.append(int(k))
        return [sorted(no_losses), sorted(one_loss)]
