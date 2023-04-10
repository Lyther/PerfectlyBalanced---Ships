#!/usr/bin/python3

import sys
import random
import math
import string

ship_size_list = ["battleship", "colossus", "frigate", "corvette", "crisis_corvette", "crisis_destroyer", "crisis_cruiser", "star_eater", "cruiser", "destroyer", "eventship_04", "leviathan_01_scavenger_bot", "leviathan_01_elder_tiyanki", "leviathan_01_voidspawn", "juggernaut", "space_dragon_red", "stellarite", "npc_warship_01", "dimensional_horror", "toxic_god", "sphere", "galleon", "wraith_01_blue", "wraith_01_red", "wraith_01_yellow", "space_dragon_blue", "military_station_small", "military_station_medium", "military_station_large", "ion_cannon", "offspring_corvette", "offspring_destroyer", "offspring_cruiser", "offspring_battleship", "titan", "fe_escort", "fe_battlecruiser", "fe_titan", "fe_small_station", "fe_large_station", "fe_goliath"]
fits_on_slot_dict = {"battleship": ["bow", "mid", "stern"], "colossus": ["ship"], "frigate": ["mid"], "corvette": ["mid"], "crisis_corvette": ["mid"], "crisis_destroyer": ["mid"], "crisis_cruiser": ["mid"], "star_eater": ["mid"], "cruiser": ["bow", "mid", "stern"], "destroyer": ["bow", "stern"], "eventship_04": ["mid"], "leviathan_01_scavenger_bot": ["mid"], "leviathan_01_elder_tiyanki": ["mid"], "leviathan_01_voidspawn": ["mid"], "juggernaut": ["core"], "space_dragon_red": ["mid"], "stellarite": ["mid"], "npc_warship_01": ["mid"], "dimensional_horror": ["mid"], "toxic_god": ["mid"], "sphere": ["mid"], "galleon": ["mid"], "wraith_01_blue": ["mid"], "wraith_01_red": ["mid"], "wraith_01_yellow": ["mid"], "space_dragon_blue": ["mid"], "military_station_small": ["north", "west", "east", "south"], "military_station_medium": ["north", "west", "east", "south"], "military_station_large": ["north", "west", "east", "south"], "ion_cannon": ["ship"], "offspring_corvette": ["mid"], "offspring_destroyer": ["bow", "stern"], "offspring_cruiser": ["bow", "mid", "stern"], "offspring_battleship": ["bow", "mid", "stern"], "titan": ["bow", "mid", "stern"], "fe_escort": ["bow", "mid", "stern"], "fe_battlecruiser": ["bow", "mid", "stern"], "fe_titan": ["bow", "mid", "hangar", "stern"], "fe_small_station": ["heavy", "medium"], "fe_large_station": ["xl", "heavy", "medium", "pd"], "fe_goliath": ["bow", "mid", "hangar", "stern"]}
entity_dict = {"battleship": {"bow": ["battleship_bow_L1M1S2_entity", "battleship_bow_L2_entity", "battleship_bow_M1S2SHB_entity", "battleship_bow_XL1_entity"], "mid": ["battleship_mid_L2M2_entity", "battleship_mid_L3_entity", "battleship_mid_M4SHB_entity", "battleship_mid_S4LHB_entity"], "stern": ["battleship_stern_L1_entity", "battleship_stern_M2_entity"]}, "colossus": {"ship": ["colossus_ship_entity"]}, "frigate": {"mid": ["corvette_M1S1_entity", "corvette_S3_entity"]}, "corvette": {"mid": ["corvette_M1S1_entity", "corvette_S3_entity"]}, "crisis_corvette": {"mid": ["crisis_corvette_M1S1_entity", "crisis_corvette_S3_entity"]}, "crisis_destroyer": {"mid": ["crisis_destroyer_1M2S1M_entity", "crisis_destroyer_1L2S_entity"]}, "crisis_cruiser": {"mid": ["crisis_cruiser_hull_entity"]}, "star_eater": {"mid": ["star_eater_ship_entity"]}, "cruiser": {"bow": ["cruiser_bow_L1_entity", "cruiser_bow_M1S2_entity", "cruiser_bow_M2_entity"], "mid": ["cruiser_mid_S2HB_entity", "cruiser_mid_L1M1_entity", "cruiser_mid_M3_entity", "cruiser_mid_M2S2_entity"], "stern": ["cruiser_stern_M1_entity", "cruiser_stern_S2_entity"]}, "destroyer": {"bow": ["destroyer_bow_M1S2_entity", "destroyer_bow_S3_entity", "destroyer_bow_L1_entity"], "stern": ["destroyer_stern_S2_entity", "destroyer_stern_M1_entity"]}, "juggernaut": {"core": ["juggernaut_core_section_entity"]}, "military_station_small": {"north": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "west": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "east": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "south": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"]}, "military_station_medium": {"north": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "west": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "east": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "south": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"]}, "military_station_large": {"north": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "west": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "east": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"], "south": ["military_station_section_light_entity", "military_station_section_medium_entity", "military_station_section_heavy_entity", "military_station_section_hangar_entity"]}, "ion_cannon": {"ship": ["ion_cannon_section_entity"]}, "offspring_corvette": {"mid": ["corvette_M1S1_entity", "corvette_S3_entity"]}, "offspring_destroyer": {"bow": ["destroyer_bow_M1S2_entity", "destroyer_bow_S3_entity", "destroyer_bow_L1_entity"], "stern": ["destroyer_stern_S2_entity", "destroyer_stern_M1_entity"]}, "offspring_cruiser": {"bow": ["cruiser_bow_L1_entity", "cruiser_bow_M1S2_entity", "cruiser_bow_M2_entity"], "mid": ["cruiser_mid_S2HB_entity", "cruiser_mid_L1M1_entity", "cruiser_mid_M3_entity", "cruiser_mid_M2S2_entity"], "stern": ["cruiser_stern_M1_entity", "cruiser_stern_S2_entity"]}, "offspring_battleship": {"bow": ["battleship_bow_L1M1S2_entity", "battleship_bow_L2_entity", "battleship_bow_M1S2SHB_entity", "battleship_bow_XL1_entity"], "mid": ["battleship_mid_L2M2_entity", "battleship_mid_L3_entity", "battleship_mid_M4SHB_entity", "battleship_mid_S4LHB_entity"], "stern": ["battleship_stern_L1_entity", "battleship_stern_M2_entity"]}, "titan": {"bow": ["titan_bow_entity"], "mid": ["titan_mid_entity"], "stern": ["titan_stern_entity"]}, "fe_escort": {"bow": ["fe_escort_bow_entity"], "mid": ["fe_escort_stern_entity"], "stern": ["fe_escort_stern_entity"]}, "fe_battlecruiser": {"bow": ["fe_battlecruiser_bow_entity"], "mid": ["fe_battlecruiser_mid_entity"], "stern": ["fe_battlecruiser_stern_entity"]}, "fe_titan": {"bow": ["fe_titan_bow_entity"], "mid": ["fe_titan_mid_entity"], "hangar": ["fe_titan_hangar_entity"], "stern": ["fe_titan_stern_entity"]}, "fe_small_station": {"heavy": ["fe_small_station_heavy_entity"], "medium": ["fe_small_station_medium_entity"]}, "fe_large_station": {"xl": ["fe_large_station_xl_entity"], "heavy": ["fe_large_station_heavy_entity"], "medium": ["fe_large_station_medium_entity"], "pd": ["fe_large_station_pd_entity"]}, "fe_goliath": {"bow": ["fe_goliath_bow_entity"], "mid": ["fe_goliath_mid_entity"], "hangar": ["fe_goliath_hangar_entity"], "stern": ["fe_goliath_stern_entity"]}}
entity_locator_dict = {"battleship_bow_L1M1S2_entity": {"L": 1, "M": 1, "S": 2}, "battleship_bow_L2_entity": {"L": 2}, "battleship_bow_M1S2SHB_entity": {"HB": 1, "M": 1, "S": 2}, "battleship_bow_XL1_entity": {"X": 1}, "battleship_mid_L2M2_entity": {"L": 2, "M": 2}, "battleship_mid_L3_entity": {"L": 3}, "battleship_mid_M4SHB_entity": {"HB": 1, "M": 4}, "battleship_mid_S4LHB_entity": {"HB": 2, "S": 4}, "battleship_stern_L1_entity": {"L": 1}, "battleship_stern_M2_entity": {"M": 2}, "colossus_ship_entity": {"W": 1}, "corvette_M1S1_entity": {"M": 1, "S": 1}, "corvette_S3_entity": {"S": 3}, "crisis_corvette_M1S1_entity": {"M": 1, "S": 1}, "crisis_corvette_S3_entity": {"S": 3}, "crisis_destroyer_1M2S1M_entity": {"M": 2, "S": 2}, "crisis_destroyer_1L2S_entity": {"L": 1, "S": 2}, "crisis_cruiser_hull_entity": {"L": 1, "M": 2, "S": 2}, "star_eater_ship_entity": {"core": 1, "root": 25}, "cruiser_bow_L1_entity": {"L": 1}, "cruiser_bow_M1S2_entity": {"M": 1, "S": 2}, "cruiser_bow_M2_entity": {"M": 2}, "cruiser_mid_S2HB_entity": {"HB": 1, "S": 2}, "cruiser_mid_L1M1_entity": {"L": 1, "M": 1}, "cruiser_mid_M3_entity": {"M": 3}, "cruiser_mid_M2S2_entity": {"M": 2, "S": 2}, "cruiser_stern_M1_entity": {"M": 1}, "cruiser_stern_S2_entity": {"S": 2}, "destroyer_bow_M1S2_entity": {"M": 1, "S": 2}, "destroyer_bow_S3_entity": {"S": 3}, "destroyer_bow_L1_entity": {"L": 1}, "destroyer_stern_S2_entity": {"S": 2}, "destroyer_stern_M1_entity": {"M": 1}, "juggernaut_core_section_entity": {"X": 2, "HB": 6, "M": 5}, "military_station_section_light_entity": {"S": 4}, "military_station_section_medium_entity": {"M": 2}, "military_station_section_heavy_entity": {"L": 1}, "military_station_section_hangar_entity": {"L": 1}, "ion_cannon_section_entity": {"X": 1}, "titan_bow_entity": {"X": 1}, "titan_mid_entity": {"L": 4}, "titan_stern_entity": {"L": 2}, "fe_escort_bow_entity": {"L": 1}, "fe_escort_stern_entity": {"M": 2}, "fe_battlecruiser_bow_entity": {"L": 2}, "fe_battlecruiser_mid_entity": {"L": 2, "M": 4}, "fe_battlecruiser_stern_entity": {"M": 4}, "fe_titan_bow_entity": {"T": 1, "L": 2}, "fe_titan_mid_entity": {"L": 2}, "fe_titan_hangar_entity": {"M": 2}, "fe_titan_stern_entity": {"M": 2}, "fe_small_station_heavy_entity": {"root": 2, "M": 2}, "fe_small_station_medium_entity": {"M": 4}, "fe_large_station_xl_entity": {"root": 2, "L": 2}, "fe_large_station_heavy_entity": {"L": 2, "M": 4}, "fe_large_station_medium_entity": {"M": 4}, "fe_large_station_pd_entity": {"S": 4}, "fe_goliath_bow_entity": {"X": 1, "L": 2}, "fe_goliath_mid_entity": {"M": 4}, "fe_goliath_hangar_entity": {"M": 2}, "fe_goliath_stern_entity": {"M": 4}}
vanilla_section_score_dict = {"battleship": {"bow": 20, "mid": 24, "stern": 10}, "colossus": {"ship": 24}, "frigate": {"mid": 9}, "corvette": {"mid": 8}, "crisis_corvette": {"mid": 10}, "crisis_destroyer": {"mid": 16}, "crisis_cruiser": {"mid": 26}, "star_eater": {"mid": 141}, "cruiser": {"bow": 12, "mid": 14, "stern": 8}, "destroyer": {"bow": 10, "stern": 6}, "juggernaut": {"core": 142}, "military_station_small": {"north": 12, "west": 12, "east": 12, "south": 12}, "military_station_medium": {"north": 12, "west": 12, "east": 12, "south": 12}, "military_station_large": {"north": 26, "west": 26, "east": 26, "south": 26}, "ion_cannon": {"ship": 46}, "offspring_corvette": {"mid": 8}, "offspring_destroyer": {"bow": 10, "stern": 6}, "offspring_cruiser": {"bow": 12, "mid": 14, "stern": 8}, "offspring_battleship": {"bow": 20, "mid": 24, "stern": 10}, "titan": {"bow": 40, "mid": 40, "stern": 14}, "fe_escort": {"bow": 8, "mid": 10, "stern": 10}, "fe_battlecruiser": {"bow": 32, "mid": 18, "stern": 18}, "fe_titan": {"bow": 38, "mid": 46, "hangar": 38, "stern": 36}, "fe_small_station": {"heavy": 26, "medium": 22}, "fe_large_station": {"xl": 54, "heavy": 38, "mid": 34, "pd": 26}, "fe_goliath": {"bow": 98, "mid": 70, "hangar": 70, "stern": 70}}
section_cost_dict = {"battleship": 80, "frigate": 30, "corvette": 30, "cruiser": 40, "destroyer": 30, "military_station_small": 30, "military_station_medium": 30, "offspring_corvette": 30, "offspring_destroyer": 30, "offspring_cruiser": 40, "offspring_battleship": 80, "titan": 160, "juggernaut": 960, "fe_escort": 30, "fe_battlecruiser": 80, "fe_titan": 160, "fe_small_station": 30, "fe_large_station": 80, "fe_goliath": 360}
component_score_dict = {"PD": 1, "S": 1, "US": 1, "G": 2, "M": 2, "AUX": 2, "UM": 2, "L": 4, "UL": 4, "HB": 4, "X": 8, "T": 16, "W": 0}
component_type_l_simp_chinese = {"PD": "点防", "S": "哨卫", "US": "轻甲", "G": "鱼雷", "M": "炮台", "AUX": "辅助", "UM": "重甲", "L": "重炮", "UL": "铁卫", "HB": "舰载机", "X": "轴基", "T": "泰坦", "W": "歼星"}
component_quantity_l_simp_chinese = {1: "", 2: "点射", 3: "连射", 4: "四重", 5: "齐射", 6: "覆盖", 7: "焚烧", 8: "炼狱", 9: "审判", 10: "天灾"}
ship_size_l_simp_chinese = {"battleship": "战列舰", "colossus": "巨像", "frigate": "雷击艇", "corvette": "护卫舰", "crisis_corvette": "威慑级护卫舰", "crisis_destroyer": "威慑级驱逐舰", "crisis_cruiser": "威慑级巡洋舰", "star_eater": "焚天神兵", "cruiser": "巡洋舰", "destroyer": "驱逐舰", "juggernaut": "主宰", "military_station_small": "小型防御平台", "military_station_medium": "中型防御平台", "military_station_large": "重型防御平台", "ion_cannon": "离子加农炮台", "titan": "泰坦", "fe_escort": "护航舰", "fe_battlecruiser": "战列巡洋舰", "fe_titan": "失落泰坦", "fe_small_station": "防御前哨", "fe_large_station": "防御塔", "fe_goliath": "歌利亚"}
slot_l_simp_chinese = {"bow": "舰艏", "mid": "舰体", "stern": "舰艉", "hangar": "机库", "north": "区段", "west": "区段", "east": "区段", "south": "区段", "ship": "战舰", "core": "核心", "heavy": "重型区段", "medium": "中型区段", "xl": "巨型区段", "pd": "点防区段"}
component_type_l_english = {"PD": "Point Defense ", "S": "Sentinel ", "US": "Spardeck ", "G": "Torpedo ", "M": "Turret ", "AUX": "Assistant ", "UM": "Harmor ", "L": "Artillery ", "UL": "Iron Armor ", "HB": "Aircraft ", "X": "Axial ", "T": "Titan ", "W": "Star Destroyer "}
component_quantity_l_english = {1: "", 2: "Burst ", 3: "Dartle ", 4: "Quad ", 5: "Volley ", 6: "Coverage ", 7: "Incineration ", 8: "Purgatory ", 9: "Judge ", 10: "Crisis "}
ship_size_l_english = {"battleship": "Battleship ", "colossus": "Colossus ", "frigate": "Frigate ", "corvette": "Corvette ", "crisis_corvette": "Crisis Corvette ", "crisis_destroyer": "Crisis Destroyer ", "crisis_cruiser": "Crisis Cruiser ", "star_eater": "Star Eater ", "cruiser": "Cruiser ", "destroyer": "Destroyer ", "juggernaut": "Juggernaut ", "military_station_small": "Small Military Station ", "military_station_medium": "Medium Military Station ", "military_station_large": "Large Military Station ", "ion_cannon": "Ion Cannon ", "titan": "Titan ", "fe_escort": "Escort ", "fe_battlecruiser": "Battlecruiser ", "fe_titan": "Fallen Titan ", "fe_small_station": "Defense Outpost ", "fe_large_station": "Defense Tower ", "fe_goliath": "Goliath "}
slot_l_english = {"bow": "Bow", "mid": "Hull", "stern": "Stern", "hangar": "hangar", "north": "Section", "west": "Section", "east": "Section", "south": "Section", "ship": "Warship", "core": "Core", "heavy": "Heavy Section", "medium": "Medium Section", "xl": "Ultimate Section", "pd": "Point-Defense Section"}

def write_section_file(text: str):
    with open("tmp/pbships_section.txt", "a", encoding="utf-8") as output:
        print(text, file = output)
    # print("[+] Section file write done.")

def write_tech_file(text: str):
    with open("tmp/pbships_tech.txt", "a", encoding="utf-8") as output:
        print(text, file = output)
    # print("[+] Tech file write done.")

def write_l_simp_chinese_file(text: str):
    with open("tmp/pbships_l_simp_chinese.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_l_english_file(text: str):
    with open("tmp/pbships_l_english.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_tech_l_simp_chinese_file(text: str):
    with open("tmp/pbships_tech_l_simp_chinese.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_tech_l_english_file(text: str):
    with open("tmp/pbships_tech_l_english.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_random_list_file(text: str):
    with open("tmp/pbships_random_list.txt", "a", encoding="utf-8") as output:
        print(text, file = output)

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

def draw_random_list_string(tech: str) -> str:
    result = "else_if = {\n"
    result = result + "\tlimit = { NOT = { has_technology = " + tech + " } }\n"
    result = result + "\tgive_technology = { tech = " + tech + " message = yes }\n"
    result = result + "}"
    write_random_list_file(result)
    return result

def draw_localisation_string(key: str, rank: int, ship_size: str, components: dict, slot: str, tech: str) -> list:
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

def draw_tech_template_string(rank: int, tech: str) -> str:
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

def draw_section_template_string(ship_size: str, slot: str, components: dict, entity: str, rank: int) -> str:
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
    result = result + draw_component_slot_string(entity, components) + "\n"
    result = result + draw_cost_string(ship_size, rank) + "\n"
    result = result + "}\n"
    write_section_file(result)
    draw_tech_template_string(rank, tech)
    draw_localisation_string(key, rank, ship_size, components, slot, tech)
    draw_random_list_string(tech)
    return result

def draw_component_slot_string(entity: str, components: dict) -> str:
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
        if entity == "star_eater_ship_entity":
            text = "root"
            result.append(text)
            current_ptr += 1
        else:
            for locatorname in entity_locator_dict[entity]:
                # print("[+] Locatorname:", locatorname)
                # print("[+] Current pointer:", current_ptr)
                if current_ptr == index:
                    break
                text = ""
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

def draw_cost_string(ship_size: str, rank: int) -> str:
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

def generate_section(ship_size: str, slot: str, rank: int, component_queue: list, diversity: float) -> bool:
    # print("[+] Diversity:", diversity)
    # print("[+] Component queue:", component_queue)
    entity = random.choice(entity_dict[ship_size][slot])
    total_score = calculate_score(ship_size, slot, rank)
    components = {}
    if ship_size == "colossus" or ship_size == "star_eater":
        components["W"] = 1
    rest_score = total_score
    for c in component_queue:
        # print("[+] Component:", c)
        if (rest_score == 0):
            break
        num = min(math.ceil(rest_score * diversity / component_score_dict[c]), 20)
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
        section = draw_section_template_string(ship_size, slot, components, entity, rank)
        return True
    except:
        print("[*] Score verify failed, skip this round.")
    # print(section)
    return False

def parse_key_str(key_str: str) -> dict:
    result = {}
    component_type = ""
    compoennt_quantity = 0
    prev_is_digits = False
    for i in range(len(key_str)):
        if key_str[i] in string.ascii_letters and prev_is_digits:
            result[component_type] = compoennt_quantity
            component_type = ""
            compoennt_quantity = 0
            component_type = component_type + key_str[i].upper()
            prev_is_digits = False
        elif key_str[i] in string.ascii_letters and not prev_is_digits:
            component_type = component_type + key_str[i].upper()
        elif key_str[i] in string.digits:
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

def main(args: list):
    ship_size = ""
    fits_on_slot = ""
    rank = 0
    quantity = 0
    component_queue = []
    diversity = 0
    if len(args) == 2:
        key_list = args[1].lower().split("_")
        ship_size = key_list[0]
        fits_on_slot = key_list[1]
        components = parse_key_str(key_list[2])
        rank = calculate_rank_from_components(ship_size, fits_on_slot, components)
        components = dict(sorted(components.items(), key = lambda x: component_score_dict[x[0]], reverse=True))
        print("[+] Generated section:", components)
        section = draw_section_template_string(ship_size, fits_on_slot, components, random.choice(entity_dict[ship_size][fits_on_slot]), rank)
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
                random.shuffle(component_queue)
                diversity = random.random()
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