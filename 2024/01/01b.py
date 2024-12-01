def read_input(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as f:
        for line in f:
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    # Count frequency of numbers in right list
    right_freq = {}
    for num in right_list:
        right_freq[num] = right_freq.get(num, 0) + 1
    
    # Calculate similarity score
    total_score = 0
    for num in left_list:
        # Multiply number by its frequency in right list (0 if not present)
        total_score += num * right_freq.get(num, 0)
    
    return total_score

def main():
    # Read input
    left_list, right_list = read_input('01_input.txt')
    
    # Calculate similarity score
    result = calculate_similarity_score(left_list, right_list)
    
    print(f"The similarity score between the lists is: {result}")

if __name__ == "__main__":
    main()
