<u>Here are some of the queries used to push columns and data into the database, as well as pull values when requested for.</U>

<p style="text-align:left;"> To update columns </p>
UPDATE Glossary SET class = 'cardiac' WHERE Text = 'arrhythmia’;

<p style="text-align:centre;">To insert new definition </p>
INSERT INTO `Glossary`(`Text`, `Definition`, `class`) VALUES ('bradycardia', 'slow heart rate, less than 50 bpm', 'cardiac');

<p style="text-align:right;">To search for specific words or groups using user input values from form </p>
SELECT * FROM `Glossary` WHERE Text LIKE 'brad%' OR class LIKE '%hema%;
