def files_1():
    with open("files_1.txt", mode = 'a', encoding="utf-8") as f:
        f.writelines([f"{c + 1}\n" for c in range(100)])
def change(count):
    count = count%100
    if count > 19:
        count = count%10
    if count == 1:
        return "кот"
    if count in range(2, 5):
        return "кота"
    if count in range(5, 21):
        return "котов"
    return "котов"
def files_2():
    with open("files_2.txt", mode = 'a', encoding="utf-8") as f:
        f.writelines([f"{c+1} {change(c + 1)}\n" for c in range(999)])
def numbers(count):
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    tens = ["", "", " двадцать", " тридцать", " сорок", " пятьдесят", " шестьдясят", " семьдесят", " восемьдесят", " девяносто"]
    ones = ["", " один", " два", " три", " четыре", " пять", " шесть", " семь", " восемь", " девять",
            " десять", " одинадцать", " двенадцать", " тринадцать", " четырнадцать", " пятнадцать",
                " шестнадцать", " семнадцать", " восемнадцать", " девятнадцать"]
    comp = count % 100
    if comp > 19:
        comp = comp % 10
    return f"{hundreds[count//100]}{tens[count%100//10]}{ones[comp]}"
def files_3():
    with open("files_3.txt", mode = 'a', encoding="utf-8") as f:
        f.writelines([f"{numbers(c + 1)} {change(c + 1)}\n" for c in range(999)])
# считает, сколько кириллицы в files_2.txt
def files_4():
    ret = -1
    with open("files_2.txt", mode = 'r', encoding = "utf-8") as f:
        all = f.read()
        ret = 0
        for letr in range(1040, 1104):
            ret += all.count(chr(letr))
        ret += all.count("ё")
        ret += all.count("Ё")
    return ret

print(files_4())
