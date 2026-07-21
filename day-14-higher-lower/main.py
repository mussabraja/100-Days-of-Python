import random
import game_data
import art

score = 0
total_data = game_data.data

random_index_a = random.randint (0,len(total_data) - 1)
celebrity_a = total_data.pop(random_index_a)

random_index_b = random.randint (0,len(total_data) - 1)
celebrity_b = total_data.pop(random_index_b)

guess = True
while guess:
    print(f"Compare A: {celebrity_a['name']} ,a {celebrity_a['description']} ,from {celebrity_a['country']}")
    print(art.logo)
    print(f"Against B: {celebrity_b['name']} ,a {celebrity_b['description']} ,from {celebrity_b['country']}")
    selected_celebrity = input("Who has more followers? A or B ").lower()
    if selected_celebrity == 'a':
        if celebrity_a['follower_count'] > celebrity_b['follower_count']:
            score += 1
            random_index_b = random.randint(0, len(total_data) - 1)
            celebrity_b = total_data.pop(random_index_b)
        elif celebrity_b['follower_count'] > celebrity_a['follower_count']:
            score = score
            guess = False
            print("Game End")
    elif selected_celebrity == 'b':
        if celebrity_b['follower_count'] > celebrity_a['follower_count']:
            random_index_a = random.randint(0, len(total_data) - 1)
            celebrity_a = total_data.pop(random_index_a)
            score += 1
        elif celebrity_a['follower_count'] > celebrity_b['follower_count']:
            score = score
            guess = False
            print("Game End")
    print(f"Score= {score}")

