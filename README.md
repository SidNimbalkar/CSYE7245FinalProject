# Real Time Twitter Sentiment Analysis for Trend tracking or Brand Improvement<br />
<p align="center">
  <img src="https://github.com/SidNimbalkar/CSYE7245FinalProject/blob/master/Images/logo.png">
</p>

### Collabarators 
Gurjot Kaur<br/>
Harshitha Sanikommu<br/>
Sid Nimbalkar

### Professor
Sri Krishnamurthy

[Codelab](https://codelabs-preview.appspot.com/?file_id=1YoUtFfHCL5bHXWiUgjyCTtFCO-uAxqrq3rBP0-dcWqw#7)

## Overview
- Scrape Historic Tweets
- Create labelled dataset using Amazon Comprehend
- Train a BERT model using the labelled Dataset
- Create a microservice using the trained model
- Scrape live data on a user specified topic
- Ingest data into kafka
- Set up kafka producer to produce event stream
- Set up kafka consumers to process the events, extract essential information and perform sentiment analysis on the tweet
- Stream this live data in a topic
- Read the live stream into Druid
- Flatten the data and store it as rows and column in a database
- Visualize and Analyze data using Turnilo
- Dockerize various components 
- Use K8 to manage containers 
- Deploy to EC2

## System Architecture

![alt text](https://github.com/SidNimbalkar/CSYE7245FinalProject/blob/master/Images/arch.png)

## Install instructions

### Create an Amazon Web Services (AWS) account


If you already have an account, skip this step.

Go to this [link](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fportal.aws.amazon.com%2Fbilling%2Fsignup%2Fresume&client_id=signup) and follow the instructions.
You will need a valid debit or credit card. You will not be charged, it is only to validate your ID.


### Install AWS Command Line Interface (AWSCLI)

Install the AWS CLI Version 1 for your operating system. Please follow the appropriate link below based on your operating system.

* [macOS](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)

* [Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#install-msi-on-windows)

** Please make sure you add the AWS CLI version 1 executable to your command line Path.
Verify that AWS CLI is installed correctly by running `aws --version`.

* You should see something similar to `aws-cli/1.17.0 Python/3.7.4 Darwin/18.7.0 botocore/1.14.0`.

#### Configuring the AWS CLI

You need to retrieve AWS credentials that allow your AWS CLI to access AWS resources.

1. Sign into the AWS console. This simply requires that you sign in with the email and password you used to create your account.
If you already have an AWS account, be sure to log in as the root user.
2. Choose your account name in the navigation bar at the top right, and then choose My Security Credentials.
3. Expand the Access keys (access key ID and secret access key) section.
4. Press Create New Access Key.
5. Press Download Key File to download a CSV file that contains your new AccessKeyId and SecretKey. Keep this file somewhere where you can find it easily.

Now, you can configure your AWS CLI with the credentials you just created and downloaded.

1. In your Terminal, run `aws configure`.

   i. Enter your AWS Access Key ID from the file you downloaded.\
   ii. Enter the AWS Secret Access Key from the file.\
   iii. For Default region name, enter `us-east-1`.\
   iv. For Default output format, enter `json`.

2. Run `aws s3 ls` in your Terminal. If your AWS CLI is configured correctly, you should see nothing (because you do not have any existing AWS S3 buckets) or if you have created AWS S3 buckets before, they will be listed in your Terminal window.

** If you get an error, then please try to configure your AWS CLI again.

### Get Twitter API Keys
1. Create a free Twitter user account, This will allow you to access the Twitter developer portal.

2. Navigate to [Twitter Dev Site](https://apps.twitter.com), sign in, and create a new application.
After that, fill out all the app details. 
Once you do this, you should have your access keys.


### Install Postman

Follow the instructions of your operating system:

[macOS](https://learning.postman.com/docs/postman/launching-postman/installation-and-updates/#installing-postman-on-mac)

[Windows](https://learning.postman.com/docs/postman/launching-postman/installation-and-updates/#installing-postman-on-windows)

### Install Docker

Install Docker Desktop. Use one of the links below to download the proper Docker application depending on your operating system. Create a DockerHub account if asked.

* For macOS, follow this [link](https://docs.docker.com/docker-for-mac/install/).

* For Windows 10 64-bit Home, follow this [link](https://docs.docker.com/docker-for-windows/install/)

 i.  Excecute the files "first.bat" and "second.bat" in order, as administrator.

 ii. Restart your computer.

 iii.Excecute the following commands in terminal, as administrator.
 
     ```
     REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /f /v EditionID /t REG_SZ /d "Professional"
     REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /f /v ProductName /t REG_SZ /d "Windows 10 Pro"
     ```
     
 iv. Follow this [link](https://docs.docker.com/docker-for-windows/install/) to install Docker.
 
 v.  Restart your computer, do not log out.

 vi. Excecute the following commands in terminal, as administrator.
 
     ```
     REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v EditionID /t REG_SZ /d "Core"\
     REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName /t REG_SZ /d "Windows 10 Home"
     ```

Open a Terminal window and type `docker run hello-world` to make sure Docker is installed properly . It should appear the following message:

`` Hello from Docker!``  
``This message shows that your installation appears to be working correctly.``

Finally, in the Terminal window excecute `docker pull tensorflow/tensorflow:2.1.0-py3-jupyter`.

### Install Anaconda

Follow the instructions for your operating system.

* For macOS, follow this [link](https://docs.anaconda.com/anaconda/install/mac-os/)
* For Windows, follow this [link](https://docs.anaconda.com/anaconda/install/windows/)


### Install Sublime

Follow the [instructions](https://www.sublimetext.com/3) for your operating system.\
If you already have a prefered text editor, skip this step.

### Install Kafka 

Follow the following [instructions](https://kafka.apache.org/quickstart) to install zookeeper and kafka on your system. <br />
Once done you can use the following commands to run the kafka server.

Start Zookeeper <br />
`
 bin/zookeeper-server-start.sh config/zookeeper.properties
`

Start Kafka <br />
`
bin/kafka-server-start.sh config/server.properties
`

### Install Druid (Windows not supported)

Follow the following [instructions](https://druid.apache.org/docs/latest/tutorials/index.html) to install Druid on your system. <br />

#### Pre-requisites <br />
- Java 8 (8u92+) or later
- Linux, Mac OS X, or other Unix-like OS (Windows is not supported)

### Install Turnilo (Windows not supported)

#### Pre-requisites <br />
- Node.js - 10.x or 8.x version.
- npm - 6.5.0 version.

Once you have the pre-requisite packages:

Install Turnilo distribution using npm. <br />
`
npm install -g turnilo
`

To connect to the existing Druid broker using --druid command line option. Turnilo will automatically introspect your Druid broker and figure out available datasets. <br />
`
turnilo --druid http[s]://druid-broker-hostname[:port]
`

### Install Superset (Windows not supported)

#### Pre-requisites <br />
- Docker Client

Use the commands to install Superset Incubator  <br />
`git clone https://github.com/apache/incubator-superset/ ` <br />
`cd incubator-superset` <br />
`docker-compose up` <br />

Use the port: `http://localhost:8088` to access superset portal 

## Run Sequence

1. Run requirements.txt
```
pip install -U -r requirements.txt
```
This command will instal all the required packages and update any older packages.

2. Now that we have our enviornment set up, we will create an S3 bucket.

Follow this [link](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) and create a S3 bucket. 

3. Scraping Tweets: To run the scraping pipeline follow the detailed [instructions](https://github.com/SidNimbalkar/CSYE7245FinalProject/tree/master/ScrapingPipeline) in the Scraping Pipeline folder. <br />
This pipeline will scrape historic tweets using tweepy library and label the dataset and save it on s3 bucket. <br />
Run the scraping pipeline using to following command: <br />
`
python annotation_pipeline.py --environment=conda run
`

4. Training Pipeline: To run the scraping pipeline follow the detailed [instructions](https://github.com/SidNimbalkar/CSYE7245FinalProject/tree/master/TrainingPipeline) in the Training Pipeline folder. <br />
This pipeline will read the labelled dataset from the s3 and train a ML sentiment analysis model (BERT), which we will use to service a flask api.
Run the scraping pipeline using to following command: <br />
`
python training.py run
`

5. Run the Flask App: You can use a docker hub image to run this app or run it locally, you will find detailed instructions on how to run the api [here](https://github.com/SidNimbalkar/CSYE7245FinalProject/tree/master/api) <br />
This is a sentiment analysis api, which will take in a text input (tweet, in our case) and provide us with a sentiment and it's score.
Run the api using to following command: <br />
`
python app.py
`

6. Analysis Pipeline: This is a kafka pipeline which will injest real-time tweets and perform sentiment analysis on them and process each tweet as a event, we then store this events in druid and flatten the data, and then use turnilo for visualization. <br />
Detailed instruction on how to run this pipeline can be found [here](https://github.com/SidNimbalkar/CSYE7245FinalProject/tree/master/StreamingPipeline)

7. Now that we have our kafka stream running, we will start Druid and configure it to ingest the kafka stream. <br />
To start Druid use the following command: <br />
`
./bin/start-micro-quickstart
`<br />
Configure Druid to take in the kafka stream using the following [steps](https://druid.apache.org/docs/latest/tutorials/tutorial-kafka.html) <br />
Once configured, Druid will ingest real time data from kafka and store it in a database 

8. Now that we have our data in the Druid database, we use turnilo for Data Visualization and Analysis <br />
To start Turnilo use the following command: <br />
`
turnilo --druid DRUITPORT 
` <br />
DRUIDPORT is the port where Druid is running, which is `http://localhost:8888` by default.

9. Load the Superset Dashboard <br />
One you open Superset, load the druid dataset into it using the following [link](https://superset.incubator.apache.org/druid.html) <br />
Then select import, and import the `analysis.json` file, which will start up the dashboard.


## Future Implementations

- Create a react web app as the front end of the system
- Currently we have our kafka cluster and micro-service running on EC2, we'd like to house our database on cloud too, so it's remotely accessible 


