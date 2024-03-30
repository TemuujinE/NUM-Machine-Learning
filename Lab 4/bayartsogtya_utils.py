# Author: bayartsogtya
import numpy as np
import pandas as pd

from datasets import ClassLabel, load_dataset, Dataset, DatasetDict, load_metric

def unique_tags(lines):
    labels = set()
    for line in lines:
        for s, e, label in line['labels']:
            labels.add(label)

    labels = sorted(list(labels))
    labels = ['O'] + labels
    label2idx = {x:i for i,x in enumerate(labels)}
    idx2label = {i:x for i,x in enumerate(labels)}
    num_labels = len(labels)

    return labels, label2idx, idx2label, num_labels

def ner_tag(lines, label2idx):
    token_list = []
    ner_tag_list = []

    for line in lines:
        labels = line['labels']
        text = line['text']

        labels.sort()
        labels = [[-1, -1, '']] + labels + [[len(text), len(text), '']]

        tokens = []
        tags = []
        for pre, cur in zip(labels, labels[1:]):
            ps, pe, pl = pre
            cs, ce, cl = cur

            ll = text[pe+1: cs].strip().split(' ')
            tokens += ll
            tags += [0] * len(ll)

            if cl:
                ll = text[cs: ce].strip().split(' ')
                tokens += ll
                tags += [label2idx[cl]] * len(ll)
        token_list.append(tokens)
        ner_tag_list.append(tags)

    return token_list, ner_tag_list

def dataset_prep(lines):
    labels, label2idx, idx2label, num_labels = unique_tags(lines)
    token_list, ner_tag_list = ner_tag(lines, label2idx)

    df = pd.DataFrame()
    df['tokens'] = token_list
    df['ner_tags'] = ner_tag_list

    raw_dataset = Dataset.from_pandas(df)

    return raw_dataset, labels, label2idx, idx2label, num_labels