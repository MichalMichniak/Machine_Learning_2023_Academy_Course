#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict

import pandas as pd

def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    path = "data/vocab.txt"
    vocabulary_csv = pd.read_csv(path, sep="\t", names=["idx", 'word'])
    voc_dic = { int(vocabulary_csv["idx"].loc[i]) : vocabulary_csv["word"].loc[i] for i in range(len(vocabulary_csv))}
    return voc_dic