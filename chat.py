

# 讀檔
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        chat = [line.strip() for line in f]
    return chat

# 檢查名字：
def check_name(chat, name1, name2):
    new = []
    for d in chat:
        if d == name1:
            person = d
            continue
        elif d == name2:
            person = d
            continue
        if person:
            new.append(person + ':' + d)
    return new
# 寫檔
def write_file(filename, new):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in new:
            f.write(line + '\n')
def main():
    import os
    chat = read_file('input.txt')
    new = check_name(chat, 'Allen', 'Tom')
    write_file('output.txt', new)

main()