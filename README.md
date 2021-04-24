# Pands Project 2021
This is for Emma Farrell's submission of the project for the Programming and Scripting module.

## Project Purpose
The purpose of this project is to use Python to interpret the Iris Data Set through a Data Analytics lens. 

## Table of Contents
* [The Iris Data Set](#the-iris-data-set)

## The Iris Data Set
### Background
Fisher’s Iris Data Set is a set of data that describes the dimensions of three species of the iris flower. The dataset was gathered by botanist Edgar Anderson and used by statistician Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” to demonstrate a method used in statistics called linear discriminant analysis. This method can be used in statistics to characterise two or more classes of data, which is useful for analysing and categorising data. The dataset is used often today as a test set in machine learning to demonstrate pattern recognition.

### Data Within the Dataset
The data itself is comprised of 150 sets of measurements of two parts of the flowers, the petal and the sepal.
<picture showing petal and sepal>
 There are five columns of data: four measurements and the species of iris the flower belongs to. The measurements are sepal length, sepal width, petal length and petal width. There are three species of iris in the dataset: setosa, versicolor and virginica. There are 50 measurements of each species of iris.
<show head of data>

The purpose of this project is to use Python to analyse the data in this dataset and demonstrate the relationship between the different inputs and how they may differ according to species.


## Reading from the File
The file downloaded from the site is a simple text file. The values are all separated using commas, so I have saved it as a .csv file (comma separated values). The Pandas library is able to read in csv files and process them in a way that makes it easy to perform analysis on the data and output it to plots. 