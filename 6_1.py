with open("pars_logs.txt", "w", encoding="utf-8") as p:
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:
        logs = (f"{line. split()[0]} {line.split()[5]} {line.split()[6]}" for line in f)
        for i in logs:
            print(i, file=p)