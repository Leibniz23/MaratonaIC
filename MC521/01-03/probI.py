def main():
    string = input()
    four_count = 0
    seven_count = 0
    for a in string:
        if a == '4':
            four_count += 1
        elif a == '7':
            seven_count += 1
    
    if four_count == 0 and seven_count == 0:
        print("-1")
    elif four_count >= seven_count:
        print("4")
    else:
        print("7")

main()