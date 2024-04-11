# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """Sliding window solution"""
        # f1 and f2 store the last indices of the two unique fruit types
        # we have in our baskets so far
        f1, f2 = None, None
        # current and max number of fruits in our baskets
        cl, ml = 0, 0
        for i in range(len(fruits)):
            curr = fruits[i]
            if f1 is not None and curr == fruits[f1]:
                # If current fruit is the same as fruit1,
                # "i" now becomes the last index fruit1 was seen
                f1 = i
                cl += 1
            elif f2 is not None and curr == fruits[f2]:
                # If current fruit is the same as fruit2,
                # "i" now becomes the last index fruit2 was seen
                f2 = i
                cl += 1
            else:
                if f1 is None:
                    # If we haven't started filling basket1, put this fruit there.
                    f1 = i
                    cl += 1
                elif f2 is None:
                    # If we haven't started filling basket2, put this fruit there.
                    f2 = i
                    cl += 1
                elif f1 < f2:
                    # If both fruit baskets have been assigned the fruits, retain the
                    # type of fruit which has appeared the latest because that will 
                    # help maximize the length of the current sequence.
                    # e.g. if the current sequence is "1 2 1 2 3 ...", once you
                    # arrive on 3, you need to discard "1" so that the new current 
                    # sequence can become "2 3" instead. If we'd discarded "2" instead,
                    # the new current sequence would've just become "3".
                    cl = i - f1
                    f1 = i
                else:
                    # In this case, the fruit at f1 has appeared latest; so discard the one
                    # at f2.
                    cl = i - f2
                    f2 = i

            ml = max(ml, cl)

        return ml

