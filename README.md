Short description of your team members, and team name.<br/>
<ul>
<li>a) A short description of the problem you are tackling, how technology can help, as well as the idea your team is proposing*</li>
<li>b) Pitch Video*</li>
 <li>c) The architecture of your proposed solution*</li>
 <li>d) A hyperlink to your detailed solution* (Long description of your solution)</li>
 <li>e) Project Roadmap/ Proposed timeline</li>
 <li>f) Getting started* (Step-by-step instructions to install the required software and how to run a demo of your solution)</li>
 <li>g) Running the tests (Explanation and breakdown on how to run tests for the proposed solution)</li>
 <li>h) Live demo (Link to an actual working demo/website)</li>
 <li>i) What your team used to build your solution* (e.g. IBM Cloudant, IBM Cloud Functions, etc…)</li>
 </ul>

--------------------------------------------------------------------

Short description of your team members, and team name.
Team name: Elpizo
Team Members: Jia Hui, Ansel, Fei Fan, Marcus, Sam
Description about the team name and members can be found <a href="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/aboutus.html" title="Who We Are"> on our About Us page</a>. <br/>

a) A short description of the problem you are tackling, how technology can help, as well as the idea your team is proposing*
With an ageing population in Singapore, there is increasing need for quick emergency response. Community First Responders (CFRs) are activated to provide timely relief and response to emergency situations. However, they need expert knowledge for effective responses. Therefore, our chatbot and will effectively guide them through early intervention response. Additionally, with rising numbers of people living with dementia and cases of wandering, we employ facial recognition software for the community to better help find our lost patients.

b) Pitch Video*<br/>
https://youtu.be/dCOi3h2vThY

c) The architecture of your proposed solution*<br/>
The three applications of our solution come together into an integrated platform to provide SAAS. The chatbot we created is a weblet made using Watson assistant. Our facial recognition runs through Amazon Web Service’s Rekognition software, and an API request is sent to their software using Django platform where they will pull the 2 images to compare out from a s3 bucket storage directory . The images to upload for comparison can be done through our form on https://www.alg3bras.com/Care2Ask . The results of the images will then be used and if a facial match is found, the contact details of the patient’s next of kin will be displayed, or a push notification using IBM Push Notification, can be sent to the mobile device belonging to the family of the patient,  We have a database of glossary for members to look up conditions and terms they are unsure of added-on to add more functionality to our application. This is to better equip the Community First Responders with tools that engage them.

d) A hyperlink to your detailed solution* (Long description of your solution)<br/>
https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/solution.html


f) Getting started* (Step-by-step instructions to install the required software and how to run a demo of your solution) <br/>
Disclaimer <all codes and changes are on our github, these general instructions will provide the basic idea and understanding for projects>
The application of our solution can be found on https://www.alg3bras.com/Care2Ask . A demo version is accessible after login with the <b>username: pride</b> and <b>password: &Care!</b>  (case  sensitive). As the codes used to build the app includes username and passwords to access a secure database, portion of the redacted code can be found on our GitHub repository for the challenge.

AWS Rekognition<br/>
1.The whole tutorial is found here.https://docs.aws.amazon.com/rekognition/latest/dg/setting-up.html
2. We use our S3 bucket to do our image processing. Uploading tutorial found here. https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadObjSingleOpPHP.html
3. Upon uploading, our site brings you to a link containing the names of the images you have uploaded, which links to our Django website, where it receives the url request and runs the image rekognition, and displaying the results on the webpage. Read more about Django application/Website below.
4. Custom labels is used for detecting hazards, Link to tutorial here : https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html
We have created a site to process custom labels, however due to money and time constraints, we are unable to fully create a fully taught and reliable image recognizer on AWS rekognition. With more time and funding, we will be able to create a model to detect hazards and other labels for our solution. <br/>
Live Demo	 for facial comparison<br/>
https://alg3bras.com/Care2Ask/	<br/>
User Name: pride<br/>
Password: &Care!

Django application/Website<br/>
1.First download python from https://www.python.org/downloads/
2. Download pip from https://pypi.org/project/pip/
3. Download the django from more information form the site.
 https://docs.djangoproject.com/en/3.0/topics/install/
4. Using <django-admin startproject NAME_OF_project> command start your django project
5. Urls.py on your django project defines your url, using the respective path function under url patterns.
6. Create a views.py and add the function which returns a render function, holding the html page, python codes in this function may be used to input processed data into the website.
Here is where you add AWS rekognition lines.
7. Add a Templates folder containing the html files under your main django project folder.
8. Using terminals, run the
 <python manage.py runserver (port number)(optional for local demo)> 
command to start the server.
9.The Whole django project we worked on may be found on the link below. We use input variable via html, passed to our python code and display the results in our results show.html. We use our main site, with php and html files to upload images to use for our applications. Read AWS Rekognition for more details
Here is the download link to our django project, https://github.com/codeForscdf/Elpizo-Care2Ask_SCDFXIBM/tree/master/pages/AWSrekoUI &nbsp; ((((Live Demo	 for facial comparison)))
(https://alg3bras.com/Care2Ask/ <br/>
User Name: pride <br/>
Password: &Care!<br/>

h)Live Demo<br/>
https://alg3bras.com/Care2Ask/ <br/>
User Name: pride
Password: &Care!

i) What your team used to build your solution* (e.g. IBM Cloudant, IBM Cloud Functions, etc…)<br/>
IBM Cloud
IBM Watson Assistant
IBM Speech to Text
IBM Cloud Foundry
IBM Push Notification
IBM Db2
Github
Atom.io
Eclipse IDE
Composer
MAMP
phpmyadmin
Amazon Web Services
Amazon Rekognition
Django
html, css, js, php, python, jsp, md, sql
<br/>
<p><h3> This is the main folder containing all the codes we used to create our dynamic web application.</h3></p>

--------------------------------------------------------------------------------------------------------------------

<u><h2>pages folder </h2><u>
Contains all the site structure and division ids.

<br/>
<u><h2> css folder </h2><u>
Contains the font design, division styling, colours, sizes, icons. Uses bootstrap to preset the h1-h6, tag values and hex values for colour names. Also holds all the images we used to develope our application inside.

<br/>

<u><h2> js folder </h2><u>
Contain the jquery library we used to animate elements such as scrollbars and iframes, on our site, as well as define parameters for screen size based on desktop monitor screen size.

<br/>

<u><h2> sql folder </h2><u>
Contains othe Glossary table for our application. We also used a login table and a contact/image table for the application, but due to the private information that the tables contain, we have excluded them from this public GitHub repositary.

<br/>
<u><h2>README.md </h2><u>
This folder which you are reading now... Contains the information about different folders on this repositary, as well as the information about our solution.
  
  
<h3>Thank you for checking us out. Do drop us an email at scdfinnovationchallenge@gmail.com if you have any recommendations for us.</h3>
