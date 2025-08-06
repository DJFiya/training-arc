"""
Given a list of words, return the words that can be typed using letters of the alphabet on only one row of the keyboard.
For example, if the input is ["Hello", "Alaska", "Dad", "Peace"], the output should be ["Alaska", "Dad"].
"""
class KeyboardRow:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [
            set("qwertyuiopQWERTYUIOP"),
            set("asdfghjklASDFGHJKL"),
            set("zxcvbnmZXCVBNM"),
        ]
        def valid(word):
            set_num = 0 if word[0] in rows[0] else 1 if word[0] in rows[1] else 2
            for char in word:
                if char not in rows[set_num]:
                    return False
            return True

        result = [word for word in words if valid(word)]
        return result

        