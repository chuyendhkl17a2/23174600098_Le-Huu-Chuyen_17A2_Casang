import random
import csv

def roll_dice():
    return random.randint(1, 6)

def calculate_sum(dice):
    return sum(dice)

def check_result(player_guess, dice_sum):
    return player_guess == dice_sum

def calculate_probabilities(results):
    total_rolls = len(results)
    sum_counts = {i: 0 for i in range(3, 19)}
    for result in results:
        sum_counts[result] += 1
    
    probabilities = {k: v / total_rolls for k, v in sum_counts.items()}
    return probabilities

def save_results_to_csv(results, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Roll', 'Dice1', 'Dice2', 'Dice3', 'Sum'])
        for i, (dice, dice_sum) in enumerate(results):
            writer.writerow([i + 1] + dice + [dice_sum])

roll_results = []

def play_game():
    while True:
        player_guess = int(input("Dự đoán tổng của ba xúc xắc (3-18): "))
        dice = [roll_dice(), roll_dice(), roll_dice()]
        dice_sum = calculate_sum(dice)
        roll_results.append((dice, dice_sum))
        
        print(f"Xúc xắc: {dice}, Tổng: {dice_sum}")
        if check_result(player_guess, dice_sum):
            print("Chúc mừng! Bạn đã đoán đúng.")
        else:
            print("Rất tiếc! Bạn đã đoán sai.")
        
        another_round = input("Bạn có muốn chơi tiếp không? (c/k): ")
        if another_round.lower() != 'c':
            break

play_game()

probabilities = calculate_probabilities([result[1] for result in roll_results])
print("Xác suất xuất hiện của mỗi tổng:")
for sum_value, probability in probabilities.items():
    print(f"Tổng {sum_value}: {probability:.2%}")

save_results_to_csv(roll_results, 'ket_qua.csv')
