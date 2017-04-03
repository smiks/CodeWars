class Dictionary:
    def __init__(self,words):
        self.words=words


    def find_most_similar(self, term):
        mw = len(term)
        word = ""
        for w in self.words:
            ld = Dictionary.levenshtein(term, w)
            if ld < mw:
                mw = ld
                word = w

        return word


    @staticmethod
    def levenshtein(s1, s2):
        if len(s1) < len(s2):
            return Dictionary.levenshtein(s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1       # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]


words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
test_dict=Dictionary(words)
assert test_dict.find_most_similar('strawbery') == 'strawberry'
assert test_dict.find_most_similar('berry') == 'cherry'
assert test_dict.find_most_similar('aple') == 'apple'