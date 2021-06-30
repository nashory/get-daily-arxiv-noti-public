# get-daily-arxiv-noti-public

This is publicly-released version of code for automatic notification of arxiv papers.

This code is migrated from [kobiso's repo](https://github.com/kobiso/get-daily-arxiv-noti)

Arxiv.org announces new submissions every day on fixed time as informed [here](https://arxiv.org/help/submit).

This repository makes it easy to filter papers and follow-up new papers which are in your interests by creating an issue in a github repository.

**What you would get everyday:**

<img src="https://raw.githubusercontent.com/nashory/get-daily-arxiv-noti-public/master/img/sample.png"></img>

## What is changed
+ [ ] Automatic merging between topics.
+ [ ] More convinient keywords configuration in `config.py` file.
+ [ ] Display total number of paers in the title of github issue.
+ [ ] More detailed README for setting up.

## Prerequisites
- Python3.x

Install requirements with below command.

```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## Usage

#### 1. Create a Repo
Create a repository to get notification in your github.

#### 2. Set Config
Revise `config.py` as your perferences.

```python
# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'changeme'
TOKEN = 'changeme'

# The repository to add this issue to
REPO_OWNER = 'changeme'
REPO_NAME = 'changeme'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = {
	"self-supervised": ["self-supervised learning", "constrastive", "SwAV"],
	"multi-modal": ["multi-modal, "cross-modal"]
}
```

#### 3. Set Cronjob
You need to set a cronjob to run the code everyday to get the daily notification.

Refer the [announcement schedule](https://arxiv.org/help/submit) in arxiv.org and set the cronjob as below.

```bash
# cron 설치
sudo apt install -y cron

# cron 시작
sudo service cron start

# cron systemctl 활성화
sudo systemctl enable cron.service

# cron systemctl 등록 확인
sudo systemctl list-unit-files | grep cron && sudo service cron status

# cron 편집
crontab -e
0 9 * * mon-fri python PATH-TO-CODE/get-daily-arxiv-noti-public/main.py
```
