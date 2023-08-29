from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    seq_matcher = SequenceMatcher(None, text1, text2).ratio()
    # similarity_ratio = seq_matcher.ratio()
    return seq_matcher

def main():
    with open("Text File1.txt") as file1, open("Text File2.txt") as file2:
        data1 = " ".join(file1.read().split())  
        data2 = " ".join(file2.read().split())  

        print("Text from File 1:\n", data1)
        print("\nText from File 2:\n", data2)

        similarity = calculate_similarity(data1, data2)
        print("\nThe similarity between two files is:", similarity)

if __name__ == "__main__":
    main()
