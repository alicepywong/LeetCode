class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # map
        val_list = []
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # constraints
        if len(s) > 15:
            return
        for symbol in s:
            if mapping[symbol] is None:
                return

        sym_list = []

        # separate the symbols
        for symbol in s:
            # the first loop
            if sym_list == []:
                sym_list.append(str(symbol))
            else:
                # 'II', 'III', ...
                if sym_list[-1][-1] == symbol:
                    sym_list[-1] += str(symbol)
                else:
                    tmp = sym_list[-1] + symbol
                    if tmp == 'IV' or tmp == 'IX' or tmp == 'XL' or tmp == 'XC' or tmp == 'CD' or tmp == 'CM':
                        sym_list[-1] += str(symbol)
                    else:
                        sym_list.append(str(symbol))

        # calculate the sum
        sum = 0
        for symbol in sym_list:
            val = 0
            if len(symbol) == 2:
                if symbol[0] != symbol[1]:
                    val = mapping[symbol[1]] - mapping[symbol[0]]
                else:
                    val = mapping[symbol[1]] + mapping[symbol[0]]
            else:
                for s in symbol:
                    val += mapping[s]
            sum += val

        return sum
