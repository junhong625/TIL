from datetime import datetime
from pytz import timezone
import requests, pprint

from jira import JIRA


class Jira:
    def __init__(self):
        self.options = {'server': 'https://ssafy.atlassian.net/'}  # 사용중인 JIRA URL
        self.jira = JIRA(self.options, basic_auth=('junhong625@naver.com', 'ATATT3xFfGF0k2hYB3fGvhUJH4o5IRwqEa9g8cDkNzahE-MrVHa4ht_ioDCLuSijoJs5yjpZNvPNbz9ywHjBPj6CzSuTEvsGhXTHWPsE9JpO2WCQFSTjdsaU227rRxZSITg-rq8PIbYgKEJLM2kxiYX_HoyECQkApXbrkEj3jiEUFCYRESUtPtE=79015900'))
        self.proj = 'S08P12A602'  # 프로젝트 키
        self.reporter = 'notification'  # reporter username
        self.member = {
            'notification': 'junhong625',
            'tomas': '5a24ed556af22e14116095f6',
            'james': '63ad4a27741248746bf6af33'
        }
    def create_issue_comment(self, error):
        jira_issue = self._search_issue()
        text = f"발생 시간-{datetime.now(timezone('Asia/Seoul'))} [~accountid:{self.member['tomas']}] \n*{error}*"
        
        if not jira_issue:
            jira_issue_form = {
                'project': {'key': f"{self.proj}"},
                'summary': '[긴급] 비정상 동작 감지 모니터링 필요 - AsyncError',
                'description': text,
                'issuetype': {'id': '10014'},  # 이슈 유형 - 에픽:10000, 스토리:10001, 작업:10002, 하위 작업:10003, 버그:10004 
            }
            self.jira.create_issue(fields=jira_issue_form)
        else:
            for issue in jira_issue:
                self.jira.add_comment(issue, text)
                self.jira.create_issue
        
    def _search_issue(self, name):
        search_issue_jql = f"project={self.proj} and assignee={name} and status not in (closed, done)"
        # search_issue_jql = f"reporter = '{name}' and status not in (closed, done)"
        jira_issue = self.jira.search_issues(search_issue_jql, json_result=True)
        # jira_issue = self.jira.search_assignable_users_for_issues("junhong625")
        print(self.jira.issue_types())
        return jira_issue
        
        
if __name__ == '__main__':
    jira = Jira()
    JIRA.search_issues
    # jira.create_issue_comment(error)
    issues = jira._search_issue("안준홍")['issues']
    print(len(issues))
    for issue in issues:
        print(issue['fields']['summary'])
    # print(len(issues))
    # pprint.pprint(issues['issues'])
