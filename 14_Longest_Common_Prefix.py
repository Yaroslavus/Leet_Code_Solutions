from Decorator import decorator

tests = [["flowerkrtzxcv","flowkrtzxcv","flightkrtzxcv"], ["dog","racecar","car"]]

@decorator
def longest_common_prefix(l: list) -> str:
    lcs = ""
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            print([ x for x in zip(l[i], l[j]) if x[0] == x[1]])
    return lcs



if __name__ == "__main__":
    for test in tests:
        pref = longest_common_prefix(test)
        print("RES: ", pref)