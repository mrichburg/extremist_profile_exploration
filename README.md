# US Military Extremist Profile Data Analysis  
![US Patch on UCPs](../extremist_profile_exploration/img/intro_flag_patch.png)  

# Table of Contents
1. [Overview](#overview)
2. [Questions](#questions)
4. [Cleaning](#cleaning)
5. [Visualization](#visualization)
6. [Conclusion](#conclusion)
7. [Photo and Data Credits](#photo-and-data-credits)

# Overview
The Oxford Advanced American Dictionary defines the word [extremist](https://www.oxfordlearnersdictionaries.com/us/definition/american_english/extremist) as 'a person whose opinions, especially about religion or politics, are extreme, and who may do things that are violent, illegal, etc. for what they believe'.  

 As our country becomes more divided, it is important that the military as an institution remains apolitical so that the public may continue to leave their trust and confidence in the men and women dedicated to serving in their nation's interests. All members are discplined to incorporate this standard into their very being; however, there are still the few who are susceptible to stray from the norm, and of that group there are a minority that have turned to extremism.

 The following analysis undertakes the challenge of identifying the commonalities between all recorded extremists with US military backgrounds from the years 2000 to 2021. It will identify common extremist ideologies and subcategories, common means of radicalization, family influence, and more. 
 
 The purpose of this analysis is to provide early warning to DoD decision makers so that they may begin the planning phases to counter radicalization of military members.

### DataFrame shape
(3203, 130)

### Description of Fields
Categorical - 13; Represents locations and affiliations  
Quantitative - 117; Represents time, counts of occurrences, degrees of severities, or categories

### Missing Data
There is missing data under certain columns like loc_plot_state2 and plot_target2 but it seems like that is intended, not by accident.

### Summarized?
The data has not been summarized.

### Potential Avenues of Inquiry  

What are the top ideologies for extremist?  
What are the top ideological subcategories for extremist?  
Through which means were they radicalized?  
Family history?
How many were violent/nonviolent?
What was their desired result?*
What were the races of these individuals.
Were they working alone?  
Were they attached to foreign extremist groups/foreign powers?  

### Value Proposition
1. Department of Homeland Security can use this information to conduct more tailored investigations.
2. More investigations into the cause of extremism given discovered insights on certain patterns


## Military

This is the only one that reflects on us

we want to look at this because we want to intervene

Do they pick up extremis values before military/

Early Warning

Because we 


# Photo and Data Credits

- This data was collected from National Consortium for the Study of Terrorism and Response to Terrorism's [Profiles of Individual Radicalization in the United States (PIRUS) Dataset](https://www.start.umd.edu/data-tools/profiles-individual-radicalization-united-states-pirus) 
- I did not create nor do I own any data from the PIRUS Dataset
- In depth information about the dataset, certain terms, and criteria codes can be found [here](https://www.start.umd.edu/sites/default/files/files/research/PIRUSCodebook.pdf).
