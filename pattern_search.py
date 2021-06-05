
def pattern_search(text, pattern):
    num_skips = 0
    match_index = []
    print('Input Text: {}'.format(text))
    print('Input Pattern: {}'.format(pattern))

    for idx in range(len(text)):
        print("Text Index: {}".format(idx))
        match_count = 0
        if num_skips > 0:
            num_skips -= 1
            continue 
        
        for j in range(len(pattern)):
            print('Pattern Index: {}'.format(j))
            if pattern[j] == text[j + idx]:
                print("Match Found! ")
                print('Match count at {}'.format(match_count))
                match_count += 1
            else:
                break 
        if match_count == len(pattern):
            print("Ip found at Index {}".format(idx))
            num_skips = len(pattern) - 1
            match_index.append(idx)
    
    return match_index
            

