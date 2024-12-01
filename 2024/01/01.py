def read_input(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as f:
        for line in f:
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate distances between corresponding pairs
    total_distance = 0
    for l, r in zip(left_sorted, right_sorted):
        distance = abs(l - r)
        total_distance += distance
    
    return total_distance

def main():
    # Read input
    left_list, right_list = read_input('day1_input.txt')
    
    # Calculate total distance
    result = calculate_total_distance(left_list, right_list)
    
    print(f"The total distance between the lists is: {result}")

if __name__ == "__main__":
    main()