
def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0] # lower bound remains the same
        else:
            # otherwise, pop last occurring char
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length
    
def longest_substring_redux(string, k):
    def helper(char_list):
        if len(set(char_list)) == k:
            return char_list

        return max(helper(char_list[1:]), helper(char_list[:len(char_list)-1]), key=len)

    return "".join(helper([s for s in string]))

if __name__ == '__main__':
    s = "abcba" 
    k = 2
    print(longest_substring_with_k_distinct_characters(s, k))
    string = 'abcba'
    # print(longest_substring(string,2))
    print(longest_substring_redux(string, 2))
