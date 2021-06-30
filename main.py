# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bs4 import BeautifulSoup as bs
import urllib.request
import collections

from github_issue import make_github_issue
from config import NEW_SUB_URL, KEYWORD_LIST

def main():
    page = urllib.request.urlopen(NEW_SUB_URL)
    soup = bs(page, features="html.parser")
    content = soup.body.find("div", {'id': 'content'})

    issue_title = content.find("h3").text
    dt_list = content.dl.find_all("dt")
    dd_list = content.dl.find_all("dd")
    arxiv_base = "https://arxiv.org/abs/"

    assert len(dt_list) == len(dd_list)

    assert isinstance(KEYWORD_LIST, dict)
    keyword_dict = KEYWORD_LIST

    pid2keywords = collections.defaultdict(list)
    pid2paper = collections.defaultdict()
    labels = set()

    for i in range(len(dt_list)):
        paper = {}
        paper_number = dt_list[i].text.strip().split(" ")[2].split(":")[-1]
        paper['main_page'] = arxiv_base + paper_number
        paper['pdf'] = arxiv_base.replace('abs', 'pdf') + paper_number

        paper['title'] = dd_list[i].find("div", {"class": "list-title mathjax"}).text.replace("Title: ", "").strip()
        paper['authors'] = dd_list[i].find("div", {"class": "list-authors"}).text.replace("Authors:\n", "").replace(
            "\n", "").strip()
        paper['subjects'] = dd_list[i].find("div", {"class": "list-subjects"}).text.replace("Subjects: ", "").strip()
        paper['abstract'] = dd_list[i].find("p", {"class": "mathjax"}).text.replace("\n", " ").strip()

        for subject, keywords in keyword_dict.items():
            for keyword in keywords:
                if keyword.lower() in paper['abstract'].lower() or keyword.lower() in paper['title'].lower():
                    pid2keywords[paper['title']].append(subject)
                    pid2paper[paper['title']] = paper
                    labels.add(keyword)

    num_papers = 0
    subject2papers = collections.defaultdict(list)
    for pid, paper in pid2paper.items():
        new_key = " + ".join(sorted(list(set(pid2keywords[pid]))))
        subject2papers[new_key].append(paper)
        num_papers += 1

    full_report = ''
    for subject, papers in subject2papers.items():
        if len(subject2papers[subject]) > 0:
            full_report = full_report + '## Keyword: ' + subject + '\n'

            for paper in papers:
                report = '### {}\n - **Authors:** {}\n - **Subjects:** {}\n - **Arxiv link:** {}\n - **Pdf link:** {}\n - **Abstract**\n {}' \
                    .format(paper['title'], paper['authors'], paper['subjects'], paper['main_page'], paper['pdf'],
                            paper['abstract'])
                full_report = full_report + report + '\n'

    issue_title += f" ({num_papers} papers)"
    make_github_issue(title=issue_title, body=full_report, labels=list(labels))

if __name__ == '__main__':
    main()
