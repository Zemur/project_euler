"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

if __name__ == '__main__':
    one_to_nine = sum(len(i) for i in [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ])
    ten_to_nineteen = sum(len(i) for i in [
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen'
    ])
    twenty_to_ninety = sum(len(i) for i in [
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety'
    ])
    hundred = len('hundred')
    thousand = len('thousand')
    len_and = len('and')

    print(len('one') + thousand + 900 * hundred + 100 * one_to_nine + 100 * twenty_to_ninety + 891 * len_and +
          80 * one_to_nine + 10 * (one_to_nine + ten_to_nineteen))
