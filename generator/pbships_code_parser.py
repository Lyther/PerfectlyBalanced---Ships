#!/usr/bin/python3

from pbships_predefines import *
from pbships_output import *
from pbships_utilities import *

def parse_random_list_string(tech: str) -> str:
    result = "else_if = {\n"
    result = result + "\tlimit = { NOT = { has_technology = " + tech + " } }\n"
    result = result + "\tgive_technology = { tech = " + tech + " message = yes }\n"
    result = result + "}"
    write_random_list_file(result)
    return result

def parse_localisation_string(key: str, rank: int, ship_size: str, components: dict, slot: str, tech: str) -> list:
    components = sort_components_by_score(components)
    result_simp_chinese = " " + key + ":0 \""
    if rank < 5:
        for i in range((rank % 5) + 1):
            result_simp_chinese = result_simp_chinese + "☆"
    else:
        for i in range((rank % 5) + 1):
            result_simp_chinese = result_simp_chinese + "★"
    result_simp_chinese = result_simp_chinese + ship_size_l_simp_chinese[ship_size]
    result_simp_chinese = result_simp_chinese + component_quantity_l_simp_chinese[min(list(components.values())[0], 10)]
    result_simp_chinese = result_simp_chinese + component_type_l_simp_chinese[list(components.keys())[0]]
    if len(list(components.keys())) > 1:
        result_simp_chinese = result_simp_chinese + component_quantity_l_simp_chinese[min(list(components.values())[1], 10)]
        result_simp_chinese = result_simp_chinese + component_type_l_simp_chinese[list(components.keys())[1]]
    result_simp_chinese = result_simp_chinese + slot_l_simp_chinese[slot]
    result_simp_chinese = result_simp_chinese + "\""
    write_l_simp_chinese_file(result_simp_chinese)
    result_tech_simp_chinese = result_simp_chinese.replace(key, tech)
    write_tech_l_simp_chinese_file(result_tech_simp_chinese)
    result_english = " " + key + ":0 \""
    if rank < 5:
        for i in range((rank % 5) + 1):
            result_english = result_english + "☆"
    else:
        for i in range((rank % 5) + 1):
            result_english = result_english + "★"
    result_english = result_english + ship_size_l_english[ship_size]
    result_english = result_english + component_quantity_l_english[min(list(components.values())[0], 10)]
    result_english = result_english + component_type_l_english[list(components.keys())[0]]
    if len(list(components.keys())) > 1:
        result_english = result_english + component_quantity_l_english[min(list(components.values())[1], 10)]
        result_english = result_english + component_type_l_english[list(components.keys())[1]]
    result_english = result_english + slot_l_english[slot]
    result_english = result_english + "\""
    write_l_english_file(result_english)
    result_tech_english = result_english.replace(key, tech)
    write_tech_l_english_file(result_tech_english)
    return [result_simp_chinese, result_english, result_tech_simp_chinese, result_tech_english]

def parse_tech_template_string(rank: int, tech: str) -> str:
    result = tech + " = {\n"
    result = result + "\tcost = @tier" + str((rank % 5) + 1) + "cost3\n"
    result = result + "\tarea = engineering\n"
    if 5 <= rank <= 9:
        result = result + "\tis_rare = yes\n"
    result = result + "\ttier = " + str((rank % 5) + 1) + "\n"
    result = result + "\tcategory = { voidcraft }\n"
    result = result + "\tweight = 0\n"
    result = result + "\tai_weight = { factor = 0 }\n"
    result = result + "}\n"
    write_tech_file(result)
    return result

def parse_section_template_string(ship_size: str, slot: str, components: dict, entity: str, rank: int) -> str:
    # print("[+] enter function draw_section_template_string.")
    result = "ship_section_template = {\n"
    key = ship_size.upper() + "_" + slot.upper() + "_"
    result = result + "\tkey = \""
    for c in components:
        key = key + c + str(components[c])
    # print("[+] Generated key:", key)
    result = result + key
    result = result + "\"\n"
    result = result + "\tship_size = " + ship_size + "\n"
    result = result + "\tfits_on_slot = " + slot + "\n"
    result = result + "\tshould_draw_components = yes\n"
    result = result + "\tentity = \"" + entity + "\"\n"
    result = result + "\ticon = \"GFX_ship_part_core_" + slot + "\"\n"
    tech = "tech_" + key.lower()
    result = result + "\tprerequisites = { " + tech + " }\n\n"
    result = result + parse_component_slot_string(entity, components) + "\n"
    result = result + get_cost_string(ship_size, rank) + "\n"
    result = result + "}\n"
    write_section_file(result)
    parse_tech_template_string(rank, tech)
    parse_localisation_string(key, rank, ship_size, components, slot, tech)
    parse_random_list_string(tech)
    return result

def parse_component_slot_string(entity: str, components: dict) -> str:
    # print("[+] enter function draw_component_slot_string.")
    result = ""
    total_components = sum(components.values())
    component_locators = get_turret_locatorname(entity, total_components)
    current_ptr = 0
    local_ptr = 0
    for c in components:
        text = ""
        if c == "AUX":
            text = text + "\taux_utility_slots = " + str(components[c]) + "\n"
        elif c == "G":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"TORPEDO_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"medium_missile_turret\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        elif c == "HB":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"STRIKE_CRAFT_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"large_strike_craft\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        elif c == "L":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"LARGE_GUN_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"large_turret\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        elif c == "M":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"MEDIUM_GUN_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"medium_turret\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        elif c == "PD":
            for i in range(local_ptr + 1, local_ptr + components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"SMALL_GUN_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"point_defence_turret\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
                local_ptr += 1
        elif c == "S":
            for i in range(local_ptr + 1, local_ptr + components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"SMALL_GUN_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"small_turret\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
                local_ptr += 1
        elif c == "T":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"TITANIC_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"invisible_titanic_fixed\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        elif c == "UL":
            text = text + "\tlarge_utility_slots = " + str(components[c]) + "\n"
        elif c == "UM":
            text = text + "\tmedium_utility_slots = " + str(components[c]) + "\n"
        elif c == "US":
            text = text + "\tsmall_utility_slots = " + str(components[c]) + "\n"
        elif c == "X":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"EXTRA_LARGE_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"invisible_extra_large_fixed\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        elif c == "W":
            for i in range(1, components[c] + 1):
                text = text + "\tcomponent_slot = {\n\t\tname = \"PLANET_KILLER_GUN_" + f"{i:0>2d}" + "\"\n"
                text = text + "\t\ttemplate = \"invisible_planet_killer_fixed\"\n\t\tlocatorname = \"" + component_locators[current_ptr] + "\"\n\t}\n"
                current_ptr += 1
        else:
            raise RuntimeError("[!] Unknown turret or utility component: " + c)
        result = result + text
    return result

def get_turret_locatorname(entity: str, index: int) -> list:
    # print("[+] function get_turret_locatorname with index =", index)
    result = []
    current_ptr = 0
    while current_ptr < index:
        for locatorname in entity_locator_dict[entity]:
            # print("[+] Locatorname:", locatorname)
            # print("[+] Current pointer:", current_ptr)
            if current_ptr == index:
                break
            text = ""
            if locatorname == "core" or locatorname == "root":
                text = text + locatorname
                result.append(text)
                current_ptr += 1
                continue
            if locatorname == "W":
                text = "planet_killer_gun_" + f"{(current_ptr % entity_locator_dict[entity][locatorname]) + 1:0>2d}"
            elif locatorname == "PD" or locatorname == "S":
                text = "small_gun_" + f"{(current_ptr % entity_locator_dict[entity][locatorname]) + 1:0>2d}"
            elif locatorname == "G" or locatorname == "M":
                text = "medium_gun_" + f"{(current_ptr % entity_locator_dict[entity][locatorname]) + 1:0>2d}"
            elif locatorname == "L":
                text = "large_gun_" + f"{(current_ptr % entity_locator_dict[entity][locatorname]) + 1:0>2d}"
            elif locatorname == "HB":
                text = "strike_craft_locator_" + f"{(current_ptr % entity_locator_dict[entity][locatorname]) + 1:0>2d}"
            elif locatorname == "X" or locatorname == "T":
                text = "xl_gun_" + f"{(current_ptr % entity_locator_dict[entity][locatorname]) + 1:0>2d}"
            else:
                raise RuntimeError("[!] No such turret type in entity: " + locatorname)
            result.append(text)
            current_ptr += 1
    return result

def get_cost_string(ship_size: str, rank: int) -> str:
    cost = calculate_cost(ship_size, rank)
    result = "\tresources = {\n"
    result = result + "\t\tcategory = ship_sections\n"
    if cost != 0:
        result = result + "\t\tcost = {\n"
        result = result + "\t\t\talloys = " + str(cost) + "\n"
        if ship_size == "fe_goliath":
            result = result + "\t\t\tsr_living_metal = " + str(cost // 10) + "\n"
        result = result + "\t\t}\n"
    result = result + "\t}"
    return result