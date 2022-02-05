from collections import Counter
with open("pars_logs.txt", "r", encoding="utf-8") as p:
    my_dict = Counter()
    for i in p:
        my_dict[i.split()[0]] += 1

    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
    print(f"Spammer {ip} - {count} times")