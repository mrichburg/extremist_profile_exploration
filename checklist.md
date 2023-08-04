### To Do
- Make a hypothesis test
  - communicate: 
    - Null and Alt hypos
    - Which test (Welch's t-test, ANOVA, etc) and the rationale for choosing that test
    - Significance level (alpha, chosen before performing the test)
    - The sample size and power of the test
- Do a regression model 
  - may need to regularize with standardization/normalization
    - standardization changes values from 0-1
    - normalization changes value to individuals std's from the mean
  - model can be linear (inferential or predictive)
  - if inferential:
    - show that you confirmed that you didn't violate any assumptions
    - provide an interpretation of your coefficients as they relate to your business problem.
  - if linear
    - use cross validation
    - Describe the process used to ensure model was properly fit
    - * see directions for logistic classification if you wanna use it

### What makes a good capstone
- Well Written code
  - Make it clean
  - Have clear documentation
    - that means comments everywhere

- Repo
  - Make a csv of a subset of the data that you were working with AFTER EDA and cleaning so others can see what you were working with.
    - 100 rows from a sample function

- Commit often
  - Descriptive commit messages

- Describe how you cleaned your dataset in your readme

### Project Proposal
1. State your Question
  - What are you curious about?
  - What are you looking for?
2. Demonstrate you looked at the date
  - What are your columns?
  - Are they numerical or categorical?
  - Make plots
3. State your MVP
  - What is the minimum you want to accomplish?


### Skills to Feature
- Hypothesis test
- A Regression
- Data Pipline
- Data Visualization
  - Make plots look professional
  - Prioritize clarity over pretty
  - Make them pretty if you have time to

### Evaluation
- They are grading the Github and the Presentation.
- Example capstones:
  - [Traffic Accidents in Denver ](https://github.com/johnherr/Traffic-Accidents-in-Denver)
  - [Purifying Hearthstone Data ](https://github.com/NJacobsohn/Hearthstone-Data-Analysis)
  - [Does Work-Life Balance Matter? ](https://github.com/tsandefer/dsi_capstone_1)
  - [Services provided by Non-State actors](https://github.com/gagejane/Terrorism-NonViolent)


### Scientific Question
- Do USMEs have a different likelihood of commiting a violet crime than civillain extremsists?

### Hypothesis Tests
- Alternative
  - Extremists with a military background have a different likelihood of commiting a violent crime than civillian extremists
- Null
  - Extremists with a military background have the same likelihood of commiting a violent crime as civillian extremists


### Notes
Definitely have to do bootstrapping for the military members

Two separate Logistic regression
- One for civilians
- One for Military

Two questions to answer!
- scientific question/ Hypothesis Tests
- What are the largest factors (coefficients) that contribute to military being violent 
- and what are the largest factors that contribute to civillians being violent

Be as simple as possible in my presentation!!!




### Future research
I'd like to get more general information about military that way I 


### Different regerssions

Here are some possible regression model directions.

Use inferential linear regression to gain insight into how features affect a target.
Use predictive linear regression to create a model that can predict a target when provided with the values of specific features.
Use logistic regression to predict a categorical target that has two possible values.
Be as specific as you can using the data in this dataset. Here are three (somewhat silly) examples using the cars dataset:

Predictive linear regression: "I would like to predict mpg using weight, horsepower, and the number of cylinders"
Inferential linear regression: "I would like to use inferential regression to gain insight as to how the number of cylinders, weight, and horsepower affect the mpg of American cars."
Predicting a Categorical variable with Logistic Regression "I would like to use cylinders, weight, horsepower and mpg to predict whether a car was manufactured in America or not."





### Inclusion Criteria
Inclusion Criteria    
Summary: In order to be eligible for inclusion, each individual must meet one of the following five criteria:
    1. the individual was arrested;  
    2. the individual was indicted of a crime;  
    3. the individual was killed as a result of his or her ideological activities;  
    4. the individual is/was a member of a designated terrorist organization; or  
    5. the individual was associated with an extremist organization whose leader(s) or founder(s) has/have been indicted of an ideologically motivated violent offense.

    In addition, each individual MUST:   
    1. have been radicalized in the United States,  
    2. have espoused or currently espouse ideological motives, and  
    3. show evidence that his or her behaviors are/were linked to the ideological motives he or she espoused/espouses.  


    Criteria for Inclusion   PIRUS includes a sample of individuals espousing Islamist, far right, far left, or single-issue ideologies who have radicalized within the United States to the point of committing ideologically motivated illegal violent or non-violent acts, joining a designated terrorist organization, or associating with an extremist organization whose leader(s) has/have been indicted of an ideologically motivated violent offense.  