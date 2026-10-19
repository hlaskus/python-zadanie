import argparse

DNI = ['pn', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']
DNI_RANGE = [DNI[i] + '-' + DNI[j] for i in range(len(DNI)) for j in range(i + 1, len(DNI))]
MIESIACE = ['sty', 'lut', 'mar', 'kwi', 'maj', 'cze', 'lip', 'sie', 'wrz', 'paz', 'lis', 'gru']
PORY = ['r', 'w']

def str_to_dni(s: str) -> list[str]:
    if s in DNI:
        return [s]

    d1, d2 = s.split('-')
    return DNI[DNI.index(d1):DNI.index(d2) + 1]


def parse_args():
    parser = argparse.ArgumentParser(
        description='Tworzenie lub odczyt plików CSV/JSON.'
    )
    parser.add_argument("-m", choices=MIESIACE, nargs='+', required=True,
                        help='Miesiące w podanej kolejności (np. sty lut).')
    parser.add_argument("-d", choices=DNI + DNI_RANGE, nargs='+', required=True,
                        help='Jeden dzień lub zakres na każdy miesiąc (np. pn-wt pt).')
    parser.add_argument("-p", choices=PORY, nargs='+',
                        help='Pory kolejnych dni po rozwinięciu zakresów: r = rano, '
                             'w = wieczorem. Brakujące pory: r.')
    parser.add_argument("-t", action="store_true",
                        help='Tworzenie plików; bez tej flagi: odczyt.')
    parser.add_argument("-f", "--format", choices=['csv', 'json'], default='csv',
                        help='Format plików (domyślnie: csv).')

    args = parser.parse_args()

    if len(args.m) != len(args.d):
        parser.error("Liczba zakresów dni musi być równa liczbie miesięcy")

    liczba_dni = sum(len(str_to_dni(d)) for d in args.d)
    args.p = args.p or []
    if len(args.p) > liczba_dni:
        parser.error("Podano więcej pór dnia niż dni wynikających z zakresów")
    args.p += ['r'] * (liczba_dni - len(args.p))

    return args


if __name__ == '__main__':
    args = parse_args()
