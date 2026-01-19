def generate_report(data):
    with open("attack_report.txt", "w") as f:
        f.write("Password Security Simulation Report\n\n")
        for k, v in data.items():
            f.write(f"{k}: {v}\n")
