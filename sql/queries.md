Here are some of the queries used to push columns and data into the database, as well as pull values when requested for.

//To update columns 
UPDATE Glossary SET class = 'cardiac' WHERE Text = 'arrhythmia’;

//To insert new definition
INSERT INTO `Glossary`(`Text`, `Definition`, `class`) VALUES ('bradycardia', 'slow heart rate, less than 50 bpm', 'cardiac');

/To search for specific words or groups using user input values from form
SELECT * FROM `Glossary` WHERE Text LIKE 'brad%' OR class LIKE '%hema%;
