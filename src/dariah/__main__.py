from argparse import ArgumentParser

from dariah.models import dating, diachronic_normalizer, disambiguation, synonyms

parser = ArgumentParser(description="DARIAH CLI tool")


parser.add_argument("mode", type=str, choices=["dating", "diachronic_normalizer", "disambiguation", "synonyms"])
parser.add_argument("text", type=str, nargs="?", default=" ")
parser.add_argument("--output", "-o", type=str)
parser.add_argument("--file", "-f", type=str)

ArgumentParser
args = parser.parse_args()

if __name__ == "__main__":
    if args.file:
        with open(args.file, "r") as f:
            text = f.read()
    match args.mode:
        case "dating":
            result = dating(args.text)
            print(result)

        case "diachronic_normalizer":
            result = diachronic_normalizer(args.text)
            print(result)

        case "disambiguation":
            result = disambiguation(args.text)
            print(result)

        case "synonyms":
            result = synonyms(args.text)
            print(result)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
