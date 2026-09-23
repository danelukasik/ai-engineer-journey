num_of_questions = int(input("How many practice questions would you like to answer?"))
max_num = int(input("How high should the integers go? (Enter a number greater than 0)"))
import random
import time
correct_answers = 0
elapsed_time = 0
first_nums = []
second_nums = []
user_answers = []
for i in range(num_of_questions):
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    answer = num1 * num2
    first_nums.append(num1)
    second_nums.append(num2)
    start_time = time.time()
    user_answer = int(input(f"What is {num1} x {num2}? "))
    end_time = time.time()
    elapsed_time += end_time - start_time
    user_answers.append(user_answer)
    if user_answer == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is {answer}.")

print(f"Thank you for practicing!")
print(f"You got {correct_answers} out of {num_of_questions} questions correct.")
print(f"Your score is {correct_answers / num_of_questions * 100:.1f}%.")
print(f"Average time per question: {elapsed_time / num_of_questions:.1f} seconds.")
print(f"Total time taken: {elapsed_time:.1f} seconds.")
print("------------Question Recap------------")
for i in range(num_of_questions):
    print(f"Question {i+1}: {first_nums[i]} x {second_nums[i]}")
    print(f"Your answer: {user_answers[i]}")
    print(f"Correct answer: {first_nums[i] * second_nums[i]}")
    print("--------------------------------------")