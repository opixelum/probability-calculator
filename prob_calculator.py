
import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        drawn_balls_list = copied_hat.draw(num_balls_drawn)
        drawn_balls_dict = {}
        
        for ball in drawn_balls_list:
            if ball in drawn_balls_dict:
                drawn_balls_dict[ball] += 1
            else:
                drawn_balls_dict[ball] = 1
        
        success = True
        for ball, count in expected_balls.items():
            if ball not in drawn_balls_dict or drawn_balls_dict[ball] < count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    return successful_experiments / num_experiments
