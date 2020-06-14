from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from . import application
from django.core.files.storage import FileSystemStorage
import boto3
import subprocess
import time
def home(request):
    return render(request, 'home/home.html')
def manning365(request):
    return render(request, 'home/Manning365.html')
def solutions(request):
    return render(request, 'home/solutions.html')
def aboutus(request):
    return render(request, 'home/aboutus.html')

def upload(request):
    if request.method == 'post':
        upload_file=request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'home/upload.html')


def search(request):
    cpface= "#got to save that image.........."
    return render(request, 'search.html', {'app' : cpface})
def SResult(request):
    result = "#request form server"
    return render(request, 'SResult.html', {'result' : result})

def website(request,nm1,nm2):
    def compare_faces(img1, bucket1, img2, bucket2):

        client=boto3.client('rekognition')
        response=client.compare_faces(SimilarityThreshold=10,
                                      SourceImage={'S3Object': {'Bucket': bucket1, 'Name': img1}},
                                      TargetImage={'S3Object': {'Bucket': bucket2, 'Name': img2}},
                                      )
        global Thatlist, a
        Thatlist=[" "," "," "," "]
        a=0
        try:
            for faceMatch in response['FaceMatches']:
                    position = faceMatch['Face']['BoundingBox']
                    similarity = str(faceMatch['Similarity'])
                    simar = float(similarity)
                    simar = int(simar)
                    simar = str(simar)
                    global positleft, posittop
                    if float(position['Left'])<0.3:
                        positleft='left'
                    elif float(position['Left'])<0.6:
                        positleft='middle'
                    else:
                        positleft = 'right'

                    if float(position['Top'])<0.3:
                        posittop = '-top'
                    elif float(position['Top'])<0.6:
                        posittop = ''
                    else:
                        posittop = '-bottom'
                    Thatlist[a]= ['The face towards the ' + positleft + posittop +' matches with ' + simar + '% confidence.']
                    if a<3:
                        a+=1
        except:
            Thatlist[a]=['opps!']
        if Thatlist[0]==Thatlist[3]:
                Thatlist[0]=["No face matches, please try another image."]
        try:
            Thatlist.remove(" ")
        except:
            return len(response['FaceMatches'])
        try:
            Thatlist.remove(" ")
        except:
            return len(response['FaceMatches'])
        try:
            Thatlist.remove(" ")
        except:
            return len(response['FaceMatches'])
    # PLEASE PLEASE PLEASE DONT FORGET TO PUT THE "" ON THE IMG AND TYPE NAMES
    def cpface(img1, img2,):
        bucket1="testingaps"
        bucket2="testingaps"
        face_matches=compare_faces(img1, bucket1, img2, bucket2)
        print(Thatlist)
        print("Face matches: " + str(face_matches))

    cpface(nm1,nm2)
    results = Thatlist
    return render(request, 'home/show.html', {'results':results})
##############################THIS IS THE SITE FOR CUSTOM LABEL AND AI LEARNING FOR IDENTIFYING HAZARDS#################################################

''' CUSTOM LABEL SETUP COMMAND
aws rekognition start-project-version \
  --project-version-arn "ARN_CODE_IS_PERSONAL(THIS IS A FAKE)" \
  --min-inference-units 1\
  --region us-west-2

CUSTOM LABEL CALL (EDIT THIS INTO def customlabel below)
aws rekognition detect-custom-labels \
  --project-version-arn "ARN_CODE_IS_PERSONAL(THIS IS A FAKE)" \
  --image "{"S3Object": {"Bucket": "testingaps","Name": "PATH_TO_MY_IMAGE"}}" \
   --region us-west-2

CUSTOM LABEL SHUT DOWN (SAVE MONEY )
aws rekognition stop-project-version \
  --project-version-arn "ARN_CODE_IS_PERSONAL(THIS IS A FAKE)" \
  --region us-west-2



OUR DJANGO SITES ARE FOR RESULTS PAGE AFTER USING AWS REKOGNITION SERVICES
AND ITS CONNECTED TO OUR MAIN SITE

'''
###OPENS THE CUSTOM LABEL RESULTS SITE AND
###SHOWS HAZARDS SIGNS AI TRAINING MODEL ARE TO BE DELT WITH ON
###https://us-west-2.console.aws.amazon.com/rekognition/custom-labels#/
def customlabel(request, pc):
    global photo
    photo=     '{\"S3Object\":{\"Bucket\":\"testingaps\",\"Name\":\"'    +  pc  +  '\"}}'
    with open('temp.txt', 'w') as f:
        process = subprocess.Popen(['aws', 'rekognition', 'detect-labels', '--image', photo, '--region', 'ap-southeast-1'], shell=True, stdout=f)
        time.sleep(3)
        f.close()
    temp_process=open("temp.txt", "r")
    temp_read=temp_process.read()
    label = temp_read
    return render(request, 'home/customlabel.html', {'label':label})
