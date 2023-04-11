<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Twitter Airflow Etl" />

  &#xa0;

  <!-- <a href="https://twitterairflowetl.netlify.app">Demo</a> -->
</div>

<h1 align="center">ETL Project - Automating Twitter Data Extraction With Airflow</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/ryzncodes/twitter-airflow-etl?color=56BEB8"> 

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/ryzncodes/twitter-airflow-etl?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/ryzncodes/twitter-airflow-etl?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/ryzncodes/twitter-airflow-etl?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/twitter-airflow-etl?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/twitter-airflow-etl?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/twitter-airflow-etl?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Twitter Airflow Etl 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/ryzncodes" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This project is an ETL (Extract, Transform, Load) pipeline designed to extract data from Twitter API, transform it, and then load it into an S3 bucket using Airflow. The goal of this project is to collect and store Twitter data for further analysis and insights.

## :sparkles: Features ##

:heavy_check_mark: Feature 1 - Twitter API integration\
:heavy_check_mark: Feature 2 - Airflow integration\
:heavy_check_mark: Feature 3 - S3 data storage\
:heavy_check_mark: Feature 4 - EC2 instance for Airflow

## :rocket: Technologies ##

The following tools were used in this project:

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api/)
- [Airflow](https://airflow.apache.org/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Python](https://www.python.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have an [AWS Account](https://aws.amazon.com), [Python](https://www.python.org/) installed & sign up for the [Twitter API](https://developer.twitter.com/en/docs/twitter-api).

# :checkered_flag: Starting #

## Part 1: Twitter API ##

1. Go to the "Projects & Apps" tab in the developer dashboard and create a new project by clicking the "Create Project" button.
2. Choose the appropriate project type based on your intended use case and follow the prompts to create the project.
3. From the project dashboard, click on the "Keys and Tokens" tab to access your API keys and tokens.
4. Generate your access token and secret by clicking the "Generate" button under the "Access token & secret" section.
5. Copy and save your API keys and tokens in a secure location. These keys will be required to access the Twitter API and should be kept confidential.
6. Create a file called <b>creds.py</b>, which is where you store your twitter api credentials.
7. Note that you can directly save your access keys inside your ETL script but it's good practice to keep anything confidential a secret.

```bash
# Replace these keys with your own
# creds.py

API_KEY = "API_KEY"
API_SECRET_KEY = "API_SECRET_KEY"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

```

The files above and later in this project are to be saved in a folder. Create a folder called twitter_etl_project and store creds.py inside the folder.

## Part 2: Creating a Python script ##

Before creating a py script, make sure you install these packages from your command:

```bash

pip3 install pandas # Python package used for data manipulation and analysis.
pip3 install tweepy # Python package used to interact with the Twitter API.
pip3 install s3fs # Python package used to interact with Amazon S3 using the file system interface.

```

Create a file called <b>twitter_etl.py</b> inside your twitter_etl_project folder. Make sure it's in the same directory.

1. The documentation for Tweepy can be accessed [here](https://docs.tweepy.org/en/stable/).
2. Make sure that your sensitive credentials are stored somewhere else if you are planning to make this code public.
3. For this project <b>.user_timeline</b> is used from the Tweepy package. This will return in a JSON format with alot of key-value pairs. Choose with key you want to do analysis with.
4. Change the JSON into a list:

```bash
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {'user': tweet.user.screen_name,
                        'text' : text,
                        'favorite_count': tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        tweet_list.append(refined_tweet)
```
5. The tweet_list will be converted into a dataframe & stored into .csv using the pandas package.
6. For now, store your .csv file in your local machine first:

```bash
  df = pd.DataFrame(tweet_list)
  df.to_csv("your_twitter_data.csv")
```
7. Add run_twitter_etl() at the end of your code. <b>(To test the script ONLY. Remove it once the script shows no error)</b>

8. Run this script in your terminal:

```bash
python3 twitter_etl.py
```

9. You should now have three files in your folder: <b>creds.py, twitter_etl.py & your_twitter_data.csv!</b>

## Part 3: Making a DAG script ##

1. Create a python script, twitter_dag.py
2. Make sure you import the function run_twitter_etl from twitter_etl.py into twitter_dag.py:

```bash
from datetime import timedelta
from airflow import DAG # to define a directed acyclic graph (DAG) in Airflow.
from airflow.operators.python_operator import PythonOperator #execute arbitrary Python code as a task in a DAG.
from airflow.utils.dates import days_ago 
from datetime import datetime
from twitter_etl import run_twitter_etl # importing run_twitter_etl function
```

3. A dictionary called default_args is defined to provide default configuration options for the DAG, such as the owner, email addresses, and retry settings.
4. A new instance of the DAG class is created with the ID twitter_dag and the default configuration options from default_args.
5. A new instance of the PythonOperator class is created with the ID complete_twitter_etl, the Python function run_twitter_etl as the callable to execute, and the DAG object as the parent.
6. run_etl is an instance of the PythonOperator class, which is a task that executes a Python callable (function) called run_twitter_etl when the DAG is run.

## Part 3: Setting up an S3 bucket ##

1. Once you have an AWS account, go to S3 to create a bucket.
2. Click the "Create bucket" button to create a new bucket.
3. Give your bucket a unique name, choose the region where you want to store your data, and click "Next".
4. Review your settings and click "Create bucket" to create the bucket.
5. Once the bucket is created, copy the file path e.g. s3://enter_your_bucket_name_here/
6. Open your twitter_etl.py file and replace the output .csv file into your s3 path:

```bash

df.to_csv("s3://enter_your_bucket_name_here/twitter_data.csv")

```

## Part 4: Creating an instance from EC2

1. Go to the EC2 service and click on "Launch an instance"
2. Give it a name, choose the Ubuntu OS & t3.medium instance type.
3. Please be noted that t3.medium is not free, but the free tier, t2.micro is very slow when running Airflow. Just remember to stop your instance once you are done with this project!
4. Create a key pair and you'll be given a .pem file containing the key pair. This is important as this will allow you to connect with the instance.
5. Allow SSH,HTTPS & HTTP traffic from the internet. Launch your instance!

## Part 4.1: IAM Role & Security Groups - EC2 ##

To enable our EC2 instance to connect from our IP/local machine & instance have permission to access the S3 bucket, we have to give it permissions.

1. Click on the Instance ID of the instance you've created, go to the Security tab and click on the IAM Role. This will redirect you to the IAM page.
2. Create a role, choose AWS service and EC2 as our use case.
3. Search for "AmazonEC2FullAccess" & "AmazonS3FullAccess"
4. This role will enable full access to EC2 & S3 service for this instance.
5. Now, going back to the security tab, click the security group link.
6. Edit inbound rules and add rule.
7. This is not recommended and not the best practice, but for the sake of this project, select <b>Type: All traffic, Source: My IP</b> and save the rules.

## Part 4.2: Connecting to the instance ##

1. In the EC2 homepage, select the EC2 instance that you've created and click on connect. It will redirect you to a set of instructions on how to connect to your instance via SSH
2. Open your terminal and make sure you are in the .pem file directory.
3. Run this command:
```bash

chmod 400 YOUR_PEM_KEY.pem
ssh -i "YOUR_PEM_KEY.pem" ubuntu@....INSTANCE_PUBLIC_DNS..compute.amazonaws.com

```

4. If successful, you should see something like this in the terminal:

```bash
ubuntu@ip-145-31-3-39:~$
```

5. Congrats! You have successfully connected to your instance.

6. Run these commands to install python packages needed for this project:

```bash

sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy

```

Think of your instance as an "empty slate" and is not connected to your local machine. This is why we need to install these packages for our product to work.

## Part 5: Initializing Airflow ##

Now it's time to open up airflow via our instance!

1. Run this command to initialize airflow:

```bash
airflow standalone
```

2. After a few minutes you should be able to open up airflow. There should be a username & password as your credentials to the airflow webserver.

3. To open the webserver, use your instance Public IPv4 DNS with the port 8080 & enter this in your browser, e.g. <b>ec2-3-109-207-157.ap-south-1.compute.amazonaws.com:8080 on Chrome/Firefox/IE/Safari</b>

You can get this Public IPv4 at the instance page @ EC2.

4. If you have done everything correctly, you should be in the Airflow login page. Enter your credentials there.

5. Now, click the DAGs tab to see the list of DAG templates provided by Airflow. Our own DAG, twitter_dag.py is not in this list yet because we haven't inserted it inside our instance!

## Part 6: Inserting the DAG into the instance ##

1. If you still have the airflow webserver running in the terminal, press Ctrl+C to terminate it. Now the directory should be your instance IP. If you closed your connection to your instance, just follow Part 4.2.3 to connect back.

2. Type "ls" to see the instance home directory and see what files are inside. There should be one, called airflow.

3. Go into the folder by typing "cd airflow" & type "ls" again.

4. There are multiple files inside this folder but what we want to focus on is the <b>airflow.cfg</b> file.

5. Write "sudo nano airflow.cfg". This will enable us to modify the contents inside airflow.cfg.

6. For now, the only thing that you should change in this file is the "dags_folder" path. Change it to:

```bash
dags_folder = /home/ubuntu/airflow/twitter_dag
```

This variable is used by Airflow to locate your DAG files when it starts up. By default, Airflow looks for DAG files in the dags_folder directory.

7. Press Ctrl+X and Enter to save the modification.

8. Now we want to create the twitter_dag folder and store all of our python scripts inside that folder. Type "mkdir twitter_dag" and ls to check if it's created. If it exists, cd into twitter_dag.

9. There are three python scripts that we want to insert here. But we can't actually drag those files into the instance, so we use sudo nano instead.

10. "sudo nano creds.py" into your terminal, copy the contents of creds.py and paste it into the terminal. Press Ctrl+X and Enter to save the modification.

By default, the creds.py created using sudo nano is empty, and we are essentially pasting the code we did in our local machine to the file inside the instance.

11. Do the previous step with twitter_dag.py & twitter_etl.py.

12. Check the three files if they are created correctly or not. Congrats!

## Part 7: Running the DAG ##

1. Now, make sure your terminal is on the root directory of the instance and open up airflow again by the <b>airflow standalone</b> command.

2. When you open up your DAGs tab in the airflow, there should be a DAG called twitter_dag now! Click on the DAG to see the graph, code, grid & etc.

3. To run the dag, go to the graph tab, click on the task, complete-twitter-etl and click on the Play button around the top-right corner.

4. Your DAG is now queued and will run the code you provided inside. Yay!

## Part Final : Checking if the output goes to S3 ##

1. The hard part is done, hopefully. Go to your S3 bucket that you pointed earlier inside your code.

2. When you refresh your bucket, there should be the .csv file inside the bucket now.

3. You did it! You've successfully ran the code from Airflow. This is particularly useful because Airflow is designed to run on a schedule and say if you want to get new data daily, you can run this once everyday.


## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/ryzncodes" target="_blank">Faiz Kasman</a>

&#xa0;

<a href="#top">Back to top</a>
