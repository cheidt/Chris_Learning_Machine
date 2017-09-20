# 09-19-2017

## From the face book log

1.  Visualize the distributions of each numeric variable
2.  Visualize each variable with respect to wine type, and quality score
3.  Determine which numeric variables are correlated
4.  Plot all numerics with respect to one-another
5.  Propose a model, write out the steps to do predictions / inference in words
6.  Based on your findings, give a qualitative explanation for which features
    might provide the best way to differentiate a white wine from a red wine,
    assuming that you couldn't look at the wine type ahead of time

## Tasks 1 - 3 are mostly finished

I could not get Plot\_Against\_Color working.  Something to do with the
dimensions of the axis

I am literally in and out of conciseness while working on this, so my idea of
what a model is and isn't might need some work Before getting to the writing it
in plain text task though, my first thought is to take the correlation for
quality to give guidelines to making a better wine.  Second is to take the
histograms and fit distributions to those, try to find any parameter that
clearly separates between white and red so that some sort of WID (Wine ID) can
be preformed.  Ideally there would be a third thing, which is looking for
distributions in multiple dimensions.  But I don't know how to do that and I
can think about it right now... because I am asleep.

# 09-20-2017

## Mike Feedback

The analysis API doesn't make sense for scaling up. Its not clear who the API
is built for - why do I need to continuously pass in data to make plots? Are we
expecing to use a different data set for different endpoints to the Wine class?

I would avoid trying to compartmentalize/optimize the code too early so that
you don't get yourself stuck using something you have to rebuild later (you'll
have to rebuild it later anyway!).

Nice work with the compact visualization stuff.

Next: tell me what the correlation matrix means. Put your shit into a jupyter
notebook and add some words around your analysis that describes your thought
process. Lets see some progress on 4,5,6

## Homework

Put your analysis and code into a jupyter notebook with explainations of
what/why you're doing what you're doing. You can import your code as a python
module if you really want.

Generate a model that predicts whether or not a wine is red or white. Provide
model accuracy visualization. Your model should use the sklearn library.

Hints:
- Random Forest Classfier
- Naive Bayes Classifier

Due: Friday

## Hint: take this course, its only 10 bucks.
https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp

I'm mostly familiar with everything here, so can answer your questions.

