#Project 8 — Dice Game Statistics Analyzer

#Topics tested: loops, random module, lists, dictionaries, basic stats

#Prompt:
#Write a function dice_game(rolls) that:
#Rolls two six-sided dice rolls times
#Tracks the sum of each roll

#Returns:
#{
#  "total_rolls": rolls,
#  "sum_counts": {sum_value: frequency},
#  "most_common_sum": int,
#  "least_common_sum": int,
#  "average_sum": float
#}

#Constraints / Skills Practiced:
#Nested loops, dictionaries, probability intuition
#Handle empty rolls → return zeros/None logically
#No using libraries like collections

#Extra Challenge:
#Add a histogram string representation of the sums.

import random


def dice_game(rolls) -> dict:

    dice_rolled: list = []
    sums_count: dict = {}
    
    for i in range(rolls):
        dice_roll_1 = random.randint(1, 6)
        dice_roll_2 = random.randint(1,6)
        sum_of_die = dice_roll_1 + dice_roll_2
        dice_rolled.append(sum_of_die)
    

    def counts_of_sums(rolls) -> dict:
        if rolls == 0:
            return None
        
        else:
            for i in dice_rolled:
                if i not in sums_count:
                    sums_count[i] = 1
                elif i in sums_count:
                    sums_count[i] += 1
        
        return sums_count
    
    def most_common_sum() -> int:
        most_common_count:int = 0
        most_common_number: list = []

        for i in sums_count:
            if sums_count[i] > most_common_count:
                most_common_count = sums_count[i]
        for i in sums_count:
            if sums_count[i] == most_common_count:
                most_common_number.append(i)
        
        return most_common_number
    
    def least_common_sum() -> int:
        least_common_count:int = 12
        least_common_number: list = []

        for i in sums_count:
            if sums_count[i] < least_common_count:
                least_common_count = sums_count[i]
        for i in sums_count:
            if sums_count[i] == least_common_count:
                least_common_number.append(i)
        
        return least_common_number
        
    def average_sums() -> float:
        try:
            return sum(dice_rolled) / len(dice_rolled)
        except ZeroDivisionError as e:
            return None
    
    return {

    "total_rolls": rolls,
    "sum_counts": counts_of_sums(rolls),
    "most_common_sum": most_common_sum(),
    "least_common_sum": least_common_sum(),
    "average_sum": average_sums()

    }

def main() -> None:
    print(dice_game(10))
    print(dice_game(0))
    print(dice_game(125000))

if __name__ == '__main__':
    main()

#12/24/25 PASSED GRADE: 77%
