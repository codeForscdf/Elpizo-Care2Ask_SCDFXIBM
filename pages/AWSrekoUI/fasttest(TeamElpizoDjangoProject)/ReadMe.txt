WELCOME TO OUR DJANGO project

HERE ARE FUTURE CODES TO BE ADDED BUT DUE TO THE TIME CONSTRAINS,
CERTAIN SERVICES ARE STILL NOT UP YET

READ 	requirements.txt TO VIEW PYTHON PACKAGES AND THEIR RESPECTIVE VERSION INSTALLED

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
