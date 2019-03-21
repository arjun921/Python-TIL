# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    occurances = []
    occurance_at = 0
    index = 0
    chopped = string
    while True:
        occurance_at = chopped.find(sub_string)
        if occurance_at >= 0:
            occurances.append(occurance_at)
            index = occurance_at+1
            chopped = chopped[occurance_at+1:]
        else:
            break
        index += 1
    return len(occurances)



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)