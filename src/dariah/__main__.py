from argparse import ArgumentParser

from dariah.models import dating, diachronic_normalizer, disambiguation, synonyms

parser = ArgumentParser(description="DARIAH CLI tool")


parser.add_argument("mode", type=str, choices=["dating", "diachronic_normalizer", "disambiguation", "synonyms"])
parser.add_argument("text", type=str)
parser.add_argument("--output", "-o", type=str)
ArgumentParser
args = parser.parse_args()

if __name__ == "__main__":
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
