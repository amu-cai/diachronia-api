# project-dariah
## Info 
Library for using models provided in Model Dariah.

## Installation
- Download the .whl package from the releases [section](https://github.com/drfifonz/project-dariah/releases) .
- Install the package using pip: `pip install <package_name>.whl`
## Models
### Dating
Returns the probable year of production of the text
### Diachronic normalizer
Returns the mapping of a historical text to its contemporary spelling. The algorithm includes orthographic rules from the period 1780-2000
### Disambiguation
Returns disambiguation name for given text
### Synonyms
Returns  historical synonyms, i.e. semantic equivalents of words and proper names used in another era.
## Usage examples

In code usage:
```python
>>> from dariah.models import dating, diachronic_normalizer, disambiguation, synonyms
>>> dating("zaprawdę")
1929.0
>>> synonyms( "Na Trusi, cała zabawa polegała. Trusia, Ślązak, ubogi, bezdomny, chudy człek niewesołej twarzy, wiecznie głodny i spragniony, choć błazna piastował urząd, rychlejby do płaczu niż śmiechu pobudził. Prawił głupie żarty jak z musu, sam się nie śmiejąc, może ani myśląc o tem co mówił i co powtarzał po stokroć, gdzie go zawołano.")
[{'chudy': ['biedny']}, {'człek': ['człowiek', 'osoba', 'śmiertelnik']}, {'głupie': ['głupio', 'niemądrze', 'nierozważnie']}, {'myślić': ['myśleć']}, {'prawić': ['domagać', 'mówić', 'opowiadać', 'skarżyć']}, {'śmiech': ['kpina', 'kpiny', 'śmianie', 'żart', 'żarty']}, {'zawołany': ['głośny', 'sławny', 'wspaniały', 'znany']}]
>>>  
```
or us as module by defining mode and giving text as argument:
`python -m dariah <mode> <text>`
Example:
```bash
>> python -m dariah dating bogurodzica
2012.0
``` 
The argument `--output` `-o`, can be used to save the output to a given file.



