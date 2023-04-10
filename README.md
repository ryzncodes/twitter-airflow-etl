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
#Replace these keys with your own

API_KEY = "API_KEY"
API_SECRET_KEY = "API_SECRET_KEY"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/ryzncodes" target="_blank">Faiz Kasman</a>

&#xa0;

<a href="#top">Back to top</a>
