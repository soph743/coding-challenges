### requirements:

using `scikit-learn` and `pandas` , train two different models on the 1990 california housing dataset (https://github.com/ageron/handson-ml/blob/master/datasets/housing/housing.csv). the label is the `median_house_value` column. do not do any pre- or post- processing of the data unless necessary (ex, removing NaN).

when determining the models to use, ask yourself the following:

- what type of value is the label?
- hadare there certain machine learning model types that are not applicable for this label type?
- which machine learning models are applicable without needing to transform the label type?

print at least two scoring statistics that both models share (I.e., are meaningful for both). compute and display the delta between the two scores, along with the better performing model:

```jsx
<model 1>:
	score 1: ..
	score 2: ..
<model 2>:
	score 1: ..
	score 2: ..
<comparison>
	model <X> had the better score (+X) for score 1.
	model <Y> had the better score (+Y) for score 2.
```
