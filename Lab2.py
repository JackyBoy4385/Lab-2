

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average(num_list)
    min_max = find_min_max(num_list)
    sorted_list = sort_temperature(num_list)
    median = calc_median_temperature(num_list)

    print("Average:", average)
    print("Minimum:", min_max[0])
    print("Maximum:", min_max[1])
    print("Sorted Temperature:", sorted_list)
    print("Median:", median)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    numbers = input("Enter: ")
    print ("You have entered: " + str(numbers))

    num_list = numbers.split(",")

    float_list = []

    for item in num_list:
        float_list.append(float(item))

    return float_list

def calc_average(num_list):
    print("calc_average")
    total = 0
    for item in num_list:
        total += item

    average = total/len(num_list)
    return average

def find_min_max(num_list):
    min_temp = num_list[0]
    max_temp = num_list[0]

    for item in num_list:
        if item < min_temp:
            min_temp = item

        if item > max_temp:
            max_temp = item

    return [min_temp, max_temp]

def sort_temperature(num_list):
    print("sort_temperature")

    num_list.sort()
    return num_list

def calc_median_temperature(num_list):
    num_list.sort()
    n = len(num_list)

    if n % 2 == 1:
        median = num_list[n // 2]
    else:
        middle1 = num_list[n // 2 - 1]
        middle2 = num_list[n // 2]
        median = (middle1 + middle2) / 2

    return median


if __name__ == "__main__":
    main()