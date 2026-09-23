### requirements:

clone this CSV file containing the top 4000 most common english words: https://github.com/pkLazer/password_rank/blob/master/4000-most-common-english-words-csv.csv

construct a pandas dataframe from this and export it as a dataset `words-dataset.csv` 

the dataset should contain the following columns:

```jsx
[
	'word',
	'word length',
	'# unique characters',
	'# non-unique characters',
	'contains repeat characters?',
	'# vowels',
	'# consonants'
]
```
