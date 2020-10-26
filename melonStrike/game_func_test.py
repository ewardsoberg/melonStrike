from unittest import TestCase
from shutil import copyfile
import os

from game_func import read_high_score, write_high_score


class TestHighScoreFile(TestCase):

    def copy_file(self, from_file, to_file):
        copyfile(from_file, to_file)

    def test_write_high_score_0(self):
        current_score = 0
        copyfile('assets/high_score.txt', 'assets/high_score.backup')
        high_score = read_high_score()
        write_high_score(current_score, high_score)
        self.assertEqual(read_high_score(), high_score[:5])
        copyfile('assets/high_score.backup', 'assets/high_score.txt')
        os.remove('assets/high_score.backup')

    def test_write_high_score_10(self):
        current_score = 10
        copyfile('assets/high_score.txt', 'assets/high_score.backup')
        high_score = read_high_score()
        write_high_score(current_score, high_score)
        self.assertEqual(read_high_score(), high_score[:5])
        copyfile('assets/high_score.backup', 'assets/high_score.txt')
        os.remove('assets/high_score.backup')

    def test_write_high_score_20(self):
        current_score = 20
        copyfile('assets/high_score.txt', 'assets/high_score.backup')
        high_score = read_high_score()
        write_high_score(current_score, high_score)
        self.assertEqual(read_high_score(), high_score[:5])
        copyfile('assets/high_score.backup', 'assets/high_score.txt')
        os.remove('assets/high_score.backup')

    def test_write_high_score_5(self):
        current_score = 5
        copyfile('assets/high_score.txt', 'assets/high_score.backup')
        high_score = read_high_score()
        write_high_score(current_score, high_score)
        self.assertEqual(read_high_score(), high_score[:5])
        copyfile('assets/high_score.backup', 'assets/high_score.txt')
        os.remove('assets/high_score.backup')
