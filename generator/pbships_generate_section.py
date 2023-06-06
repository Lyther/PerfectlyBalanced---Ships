#!/usr/bin/python3

import sys
from random import choice, shuffle, random
from math import ceil
from pbships_predefines import *
from pbships_output import *
from pbships_utilities import *
from pbships_code_parser import *

def generate_section(ship_size: str, slot: str, rank: int, component_queue: list, diversity: float) -> bool:
    # print("[+] Diversity:", diversity)
    # print("[+] Component queue:", component_queue)
    entity = choice(entity_dict[ship_size][slot])
    total_score = calculate_score(ship_size, slot, rank)
    components = {}
    if ship_size == "colossus" or ship_size == "star_eater":
        components["W"] = 1
    rest_score = total_score
    for c in component_queue:
        # print("[+] Component:", c)
        if (rest_score == 0):
            break
        num = min(ceil(rest_score * diversity / component_score_dict[c]), 20)
        if num * component_score_dict[c] > rest_score:
            num -= 1
        if num > 0:
            components[c] = num
            rest_score -= component_score_dict[c] * num
            # print("[+] Add", num, c, "component(s) for ship")
    verify_score = 0
    for c in components:
        verify_score += component_score_dict[c] * components[c]
    # print("[+]", verify_score, total_score)
    try:
        assert(verify_score == total_score)
        components = dict(sorted(components.items(), key = lambda x: component_score_dict[x[0]], reverse=True))
        print("[+] Generated section:", components)
        parse_section_template_string(ship_size, slot, components, entity, rank)
        return True
    except:
        print("[*] Score verify failed, skip this round.")
    # print(section)
    return False

def main(args: list):
    ship_size = ""
    fits_on_slot = ""
    rank = 0
    quantity = 0
    component_queue = []
    diversity = 0
    if len(args) == 2:
        key_list = args[1][::-1].replace("_", " ", 2)[::-1].lower().split(" ")
        ship_size = key_list[0]
        fits_on_slot = key_list[1]
        components = parse_key_str(key_list[2])
        rank = calculate_rank_from_components(ship_size, fits_on_slot, components)
        components = dict(sorted(components.items(), key = lambda x: component_score_dict[x[0]], reverse=True))
        print("[+] Generated section:", components)
        parse_section_template_string(ship_size, fits_on_slot, components, choice(entity_dict[ship_size][fits_on_slot]), rank)
    elif len(args) == 5:
        ship_size = args[1]
        fits_on_slot = args[2]
        rank = int(args[3])
        quantity = int(args[4])
        assert(ship_size in ship_size_list)
        assert(fits_on_slot in fits_on_slot_dict[ship_size])
        assert(0 <= rank < 10)
        for _ in range(quantity):
            result = False
            while not result:
                component_queue = list(component_score_dict.copy().keys())
                component_queue.remove("W")
                shuffle(component_queue)
                diversity = random()
                result = generate_section(ship_size, fits_on_slot, rank, component_queue, diversity)
    else:
        print("[!] the length of given args is not correct!")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 5:
        print("Usage: python3 phships_generate_section.py <ship_size> <slot> <rank> <quantity>")
        print("\t<ship_size> allowed:", ship_size_list)
        print("\t<slot>: the generated slot for the given ship_size, some use bow/mid/stern, some just use core")
        print("\t<rank>: a number in [0,10), the higher rank becomes more powerful and more expensive")
        print("\t<quantity>: the number of sections you want to generate")
        print()
        print("Usage: python3 phships_generate_section.py <key_str>")
        print("\t<key_str>: a string to describe the generated section.")
        print("\t\tFor example: CORVETTE_MID_S1M1, means the section is a corvette section, fits on mid slot, and has ")
        print("\t\ta S slot with a M slot.")
    else:
        main(sys.argv)