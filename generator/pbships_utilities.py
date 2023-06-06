#!/usr/bin/python3

from string import ascii_letters, digits
from pbships_predefines import *

def calculate_score(ship_size: str, slot: str, rank: int) -> int:
    result = int(vanilla_section_score_dict[ship_size][slot] * (1.2 ** (rank - 1)))
    return result

def calculate_cost(ship_size: str, rank: int) -> int:
    result = 0
    if ship_size in section_cost_dict:
        result = int(section_cost_dict[ship_size] * (1.5 ** (rank - 1)))
    return result

def sort_components_by_score(components: dict) -> dict:
    return dict(sorted(components.items(), key = lambda x: component_score_dict[x[0]] * x[1], reverse=True))

def parse_key_str(key_str: str) -> dict:
    result = {}
    component_type = ""
    compoennt_quantity = 0
    prev_is_digits = False
    for i in range(len(key_str)):
        if key_str[i] in ascii_letters and prev_is_digits:
            result[component_type] = compoennt_quantity
            component_type = ""
            compoennt_quantity = 0
            component_type = component_type + key_str[i].upper()
            prev_is_digits = False
        elif key_str[i] in ascii_letters and not prev_is_digits:
            component_type = component_type + key_str[i].upper()
        elif key_str[i] in digits:
            compoennt_quantity = compoennt_quantity * 10 + int(key_str[i])
            prev_is_digits = True
        else:
            raise RuntimeError("[!] Invalid component type or num in key_str " + key_str + " : " + key_str[i])
        if i == len(key_str) - 1:
            result[component_type] = compoennt_quantity
    print(result)
    return result

def calculate_rank_from_components(ship_size: str, slot: str, components: dict) -> int:
    result = 0
    score = 0
    for c in components:
        score += component_score_dict[c] * components[c]
    for i in range(10):
        if score <= calculate_score(ship_size, slot, i):
            break
        result += 1
    return min(result, 9)