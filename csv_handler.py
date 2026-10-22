import random
from pathlib import Path

def create_csv(directories):
    all_paths = []

    for directory in directories:
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        model = random.choice(["A", "B", "C"])
        wynik = random.randint(0, 1000)
        czas = random.randint(0, 1000)

        file_path = directory / "Dane.csv"
        all_paths.append(file_path)

        plik = open(file_path, "w", newline="", encoding="utf-8")
        plik.write("Model; Wynik; Czas;\n")
        plik.write(f"{model}; {wynik}; {czas}s;\n")
        plik.close()

    return all_paths

def read_csv(directories):
    # Suma czasów dla modeli A
    total_seconds = 0

    for directory in directories:
        file_path = Path(directory) / "Dane.csv"

        if not file_path.exists():
            print(f"Brak pliku: {file_path}")
            continue
        
        plik = open(file_path, "r", encoding="utf-8")
        lines = plik.readlines()
        plik.close()

        parts = lines[1].strip().split(";")

        model = parts[0].strip()
        czas = parts[2].removesuffix("s").strip()

        if model == "A":
            total_seconds += int(czas)
    
    print(f"Suma czasów dla modeli 'A': {total_seconds}s")
    return total_seconds