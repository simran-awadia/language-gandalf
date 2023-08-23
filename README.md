## Language Gandalf 
Inspired by [Gandalf](https://gandalf.lakera.ai/), this is a leveled french assessment game. 
For each level you will be given 2-3 sentences to read and a question to answer to determine your French proficiency. 
There are currently 3 levels: Novice, Intermediate and Champion.

### Requirements
1. Python >= 3.9
2. Poetry >= 1.6.0 

### How to Run 
1. Git clone repo 
2. In the directory, run: 
```
poetry shell
poetry install
python3 main.py
```

### Prompt Engineering 
The content and question generation is done using one-shot prompting, which means for each level the model has an example to reference to understand what kind of content to generate. 

### Caveats 
The model used comes from one of the providers available through [gpt4free](https://github.com/xtekky/gpt4free). If that provider becomes unavailable or reaches its daily API limit, the service will stop working as expected. 
Ideally I'd like to add a status check for the provider and a fallback list but that's not currently implemented. I've tried out most of them and found `g4f.Provider.You` to be fairly stable so far.
