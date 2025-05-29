# Diachronia API

## TL;DR

Diachronia API makes it possible to access four diachronic text processing tools for the Polish language through a simple Python API.

You can:

- modernize the spelling of texts;
- approximate the year in which a text was written;
- find modern synonyms for potentially archaic words in texts;
- identify and disambiguate anthroponyms (proper names of people) in texts.

The tools were developed specifically for processing texts written in the period **1800-2000**. Their performance might not be satisfactory for textual materials from earlier periods.

## Installation

- Download the `.whl` package from the [releases](https://github.com/amu-cai/diachronia-api/releases).
- Install the package using pip: `pip install <package_name>.whl`.

## Usage

### In-code

You can use the API directly in-code:

```python
>>> from dariah.models import dating, diachronic_normalizer, disambiguation, synonyms
>>> text = "Stara to historya serc ludzkich; daj im najdroższe skarby, pełną sypiąc dłonią, od wrócą się od nich obojętnie; odejm tylko ziarnko drobne i podróż się niem trochę, już ci bez niego żyć nie potrafią. Próżno sobie wmawiał Tomko, że dla niego niczem jest Marysia: złość go na nią brała, a co gorzej, porównywając ją z dziewczętami wiejskimi, widział dowodnie, że od wszystkich była piękniejszą, choć tego przyznać nie chciał."
>>> diachronic_normalizer(text)
"Stara to historia serc ludzkich; daj im najdroższe skarby, pełną sypiąc dłonią, odwrócą się od nich obojętnie; odejm tylko ziarnko drobne i podróż się niem trochę, już ci bez niego żyć nie potrafią. Próżno sobie wmawiał Tomko, że dla niego niczem jest Marysia: złość go na nią brała, a co gorzej, porównywając ją z dziewczętami wiejskimi, widział dowodnie, że od wszystkich była piękniejszą, choć tego przyznać nie chciał."
>>> dating(text)
1906.0
>>> synonyms(text)
[{"imieć": ["mieć", "musieć", "posiadać", "trzymać", "uważać"]}, {"podrożyć": ["sprzyjać", "wyświadczyć przysługę"]}, {"trocha": ["odrobina"]}]
>>> disambiguation(text)
"Stara to historya serc ludzkich ; daj im najdroższe skarby , pełną sypiąc dłonią , odwrócą się od nich obojętnie ; odejm tylko ziarnko drobne i podróż się niem trochę , już ci bez niego żyć nie potrafią . Próżno sobie wmawiał Tomko/tomka , że dla niego niczem jest Marysia/maryś : złość go na nią brała , a co gorzej , porównywając ją z dziewczętami wiejskimi , widział dowodnie , że od wszystkich była piękniejszą , choć tego przyznać nie chciał ."
```

### Command line

You can also use the API in the terminal as a module by defining the mode and giving it some text as an argument:

```bash
python -m dariah dating "Pod oknem stał ten sam czarny stół obity suknem, także niegdyś zielonem, dziś tylko poplamionem."
1908.0
```

#### Optional arguments

- `--file` or `-f` can be used to read text from a file.
- `--output` or `-o` can be used to save the output to a given file.

## Tool overview

### Dating

Returns the probable time of production of a text as a year with a fraction representing a specific day of the year (i.e., a text predicted to have been written in 1850.5 was probably written around the end of July or the beginning of June of that year, etc.).

The solution is based on the [plt5-base](https://huggingface.co/allegro/plt5-base) model fine-tuned with OCR-ed digitized Polish historical documents (mostly periodicals) taken from collections of several Polish digital libraries.

### Diachronic normalizer

Modernizes the input text to align it with contemporary Polish spelling rules.

The solution is based on a set of deterministic rules, initially handcrafted and then adjusted semi-automatically. The rules were created mostly on the basis of expert literature describing changes in the Polish spelling system in the XIX and early XX centuries, as well as consulting a list of similar words with close embeddings acquired by processing a large corpus of historical texts.

For more information on the details of the solution, please refer to the following publications:

- [Two Approaches to Diachronic Normalization of Polish Texts, Dudzic et al. (2024)](https://aclanthology.org/2024.latechclfl-1.19/)
- [Automated Normalization and Analysis of Historical Texts, Skórzewski et al. (2020)](https://link.springer.com/chapter/10.1007/978-3-030-66527-2_6)
- [Mining historical texts for diachronic spelling variants, Graliński and Jassem (2020)](https://www.degruyterbrill.com/document/doi/10.1515/psicl-2020-0021/html)
- [Automatic Diachronic Normalization of Polish Texts, Jassem et al. (2018)](https://pressto.amu.edu.pl/index.php/il/article/view/13397)

### Disambiguation

Detects proper names referring to persons in a text and indicates which references refer to the same individuals.

The solution is based on a custom graph neural network architecture set up for the purpose of character name linking.

For more information on the details of the solution, please refer to the following publication:

- [Geometric Deep Learning Models for Linking Character Names in Novels, Kubis (2020)](https://aclanthology.org/2020.latechclfl-1.15/)

### Synonyms

Returns historical synonyms, i.e. semantic equivalents of words and proper names used in another era.

The solution is based on a semi-automatically created database of Polish archaisms and their modern-language synonyms, along with automatically generated inflected forms.

The synonyms were acquired from the following freely available internet resources:

- [Elektroniczny Słownik Języka Polskiego XVII I XVIII Wieku](https://sxvii.pl/)
- [Słownik Staropolski](http://www.staropolska.pl/slownik/)
- [Synonimy.pl](https://www.synonimy.pl/)

The inflectional generator was a custom, unpublished finite-state transducer-based solution, but a similar tool for the Polish language called `Morfeusz 2` is freely available publicly:

- [Morfeusz 2](http://morfeusz.sgjp.pl/en)

## Credits

All credit goes to Filip Patyk ([@drfifonz](https://github.com/drfifonz)) for implementing the API.

The diachronic processing tools were developed at the [Faculty of Mathematics and Computer Science of Adam Mickiewicz University](https://wmi.amu.edu.pl/en) as part of the [Diachronia](https://csi.amu.edu.pl/en/projects/diachronia) research initiative situated within the [DARIAH-PL](https://dariah.pl/en/) consortium.

Some additional information about the tools, among other places, is also available under the following links:

- [https://lab.dariah.pl/catalogue/resources/92/](https://lab.dariah.pl/catalogue/resources/92/)
- [https://lab.dariah.pl/en/amu-modules/tools-for-text-normalization-and-diachronic-analysis/](https://lab.dariah.pl/en/amu-modules/tools-for-text-normalization-and-diachronic-analysis/)

You can also test the tools online here:

- [https://diachronia.csi.wmi.amu.edu.pl/](https://diachronia.csi.wmi.amu.edu.pl/)
