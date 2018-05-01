def build_filter_list():
    with open("words.txt", "r") as f:
        words = [line.strip() for line in f]
        #print(words)
        return words   
        
if __name__ == '__main__':
   print (build_filter_list())