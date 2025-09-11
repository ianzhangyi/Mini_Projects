import pandas as pd
import numpy as np

with open('readme.txt', 'r', encoding='utf-8') as f:
    content = f.read()


def process_text(text_content):
    
    content_list = text_content.splitlines()

    for line_idx, line in enumerate(content_list):

        if line.split() == ['ID','Name','CRATE','ORATE','Amount']:
            header_index = line_idx
    
    if not header_index:
        print('Cannot find target dataframe header')
        return -1
    
    end_index = len(content_list) - 1
    for line_idx in range(header_index, len(content_list)):
        if content_list[line_idx] == '':
            end_index = line_idx - 1
            break


    result = {}
    result['Header'] = ['ID','Name','CRATE','ORATE','Amount']
    data = []

    for line in content_list[header_index+1:end_index+1]:
        id, rline = line.split(None, 1)
        rline, amount = rline.rsplit(None, 1)
        rline, orate = rline.rsplit(None, 1)
        name, crate = rline.rsplit(None, 1)

        data.append([id, name, crate, orate, amount])

    result['Data'] = data

    return result

print(process_text(content))

