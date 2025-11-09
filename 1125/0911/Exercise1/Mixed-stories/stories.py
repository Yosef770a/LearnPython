def division(dividend: int, divisor: int):
    num = divmod(dividend, divisor)
    if num[1]:
        return False
    return True

with open('mixed_stories.txt', 'r') as input_file:
    for k,line in enumerate(input_file):
        print(k, line)
        if division(k,2):
            with open("story_A.txt", "a") as f:
                f.write(line)
        else:
            with open("story_B.txt", "a") as f:
                f.write(line)




