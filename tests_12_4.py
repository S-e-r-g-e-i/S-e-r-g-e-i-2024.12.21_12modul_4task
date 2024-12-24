""" Домашнее задание по теме "Логирование" """

import logging
import unittest
import RunnerTest

if __name__ == "__main__":      # запуск теста
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")

Run_Tour_TS = unittest.TestSuite()
Run_Tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))

Runner_Tournament = unittest.TextTestRunner(verbosity=2)
Runner_Tournament.run(Run_Tour_TS)

