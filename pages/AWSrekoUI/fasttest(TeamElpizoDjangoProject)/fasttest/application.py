# DO from application import cpface @@@@@@@@ and use it as cpface("name1", "type1", "name2", "type2")
import boto3

def compare_faces(sourceFile, targetFile):

    client=boto3.client('rekognition')

    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    response=client.compare_faces(SimilarityThreshold=90,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])
# PLEASE PLEASE PLEASE DONT FORGET TO PUT THE "" ON THE IMG AND TYPE NAMES
def cpface(img1, type1, img2, type2):

    a= str(img1)
    b= str(img2)
    c="."
    d=str(type1)
    e=str(type2)
    source_file= a+c+d
    target_file= b+c+e
    face_matches=compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))
