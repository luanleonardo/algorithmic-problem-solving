"""
https://www.spoj.com/problems/CENCRY/
Marko is going to write a secret letter to a friend. He thought it is better
to encrypt letter so that no other person can read it. After long thought he
came up with an encryption scheme which was lame but he thought it will work anyways.

To encrypt a text he first wrote two infinite strings of characters first string
consists only of vowels and second string consists of consonants only.

aeiouaeiouaeiouaeiouaeiou....................
bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz...

Following is the scheme for encryption :
1. let c be any character to be encrypted.
2. let word_to_check be the count of word_to_check of times c character occurred in text to be encrypted till now.
3. first find which of two infinite string contains that character.
4. then look for kth occurrence of that character in that string.
5. replace character c by corresponding character in second string.

For example encrypted text of "baax" will be "abho".

Input
First line of input will contains t, word_to_check of test cases. Then t test case follows each
test case in a line. Each test case will be a string of small latin alphabets. Length of
string will be less than 5*10^4

Output
For each test case print encrypted text.

Sample :
Input:
2
baax
aaa

Output:
abho
bhn
"""

from collections import Counter
from sys import stdin, stdout

if __name__ == "__main__":

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    number_tests_cases = int(stdin.readline().rstrip())
    for _ in range(number_tests_cases):

        text_to_be_encrypted = stdin.readline().rstrip()
        encrypted_text = ""
        counter = Counter()
        for character_to_be_encrypted in text_to_be_encrypted:

            counter[character_to_be_encrypted] += 1
            encrypted_character = (
                consonants[
                    (
                        vowels.index(character_to_be_encrypted)
                        + (counter[character_to_be_encrypted] - 1) * 5
                    )
                    % 21
                ]
                if character_to_be_encrypted in vowels
                else vowels[
                    (
                        consonants.index(character_to_be_encrypted)
                        + (counter[character_to_be_encrypted] - 1) * 21
                    )
                    % 5
                ]
            )
            encrypted_text += encrypted_character
        stdout.write(encrypted_text + "\n")
