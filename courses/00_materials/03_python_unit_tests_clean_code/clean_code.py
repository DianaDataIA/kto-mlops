import unittest
from typing import List

"""
Count names with more than max_nb_letters
"""
def count_long_names(prenoms: List[str], max_nb_letters: int = 7) -> int:
    """  
    parameters:
    prenoms (List[str]): List of names to check.
    max_nb_letters (int): Length threshold, is equal to 7 by default.

    returns: 
    (int): Nb of names exceeding max_nb_letters.
"""
    count = sum(1 for prenom in prenoms if len(prenom) > max_nb_letters)

    for prenom in prenoms:
        comparison = "supérieur à" if len(prenom) > max_nb_letters else "inférieur ou égal à"
        print(f"{prenom} est un prénom avec un nombre de lettres {comparison} {max_nb_letters}")

    return count

class TestCountLongNames(unittest.TestCase):

     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        count_names = count_long_names(prenoms=prenoms)
        self.assertEqual(count_names, 4)

if __name__ == '__main__':
    unittest.main()