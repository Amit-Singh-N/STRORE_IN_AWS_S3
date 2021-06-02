
How to run unit test using docker:
==================================

Copy the source code from the github: https://github.com/Amit-Singh-N/STRORE_IN_AWS_S3
or clone the repository using below command:

>git clone https://github.com/Amit-Singh-N/STRORE_IN_AWS_S3.git
>cd STRORE_IN_AWS_S3/source

Now build the docker image named "newimage" using below command, this usually take few min. of time.
>sudo docker build -t "newimage:Dockerfile"

Now run the image by running the below command:
>sudo docker run -e AWS_ACCESS_KEY_ID=AKIAY6P2JYSB27K4EN2Y -e AWS_SECRET_ACCESS_KEY=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 newimage:Dockerfile



prerequisite : 
1. docker is installed on the host and docker is running.
2. user should have sudo permission.


