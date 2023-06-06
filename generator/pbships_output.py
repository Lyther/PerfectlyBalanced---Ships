#!/usr/bin/python3

def write_section_file(text: str):
    with open("target/pbships_section.txt", "a", encoding="utf-8") as output:
        print(text, file = output)
    # print("[+] Section file write done.")

def write_tech_file(text: str):
    with open("target/pbships_tech.txt", "a", encoding="utf-8") as output:
        print(text, file = output)
    # print("[+] Tech file write done.")

def write_l_simp_chinese_file(text: str):
    with open("target/pbships_l_simp_chinese.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_l_english_file(text: str):
    with open("target/pbships_l_english.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_tech_l_simp_chinese_file(text: str):
    with open("target/pbships_tech_l_simp_chinese.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_tech_l_english_file(text: str):
    with open("target/pbships_tech_l_english.yml", "a", encoding="utf-8") as output:
        print(text, file = output)

def write_random_list_file(text: str):
    with open("target/pbships_random_list.txt", "a", encoding="utf-8") as output:
        print(text, file = output)