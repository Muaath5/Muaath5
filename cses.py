import requests
from bs4 import BeautifulSoup

class CSES_Task:
    ID = 0
    Name = ""
    SolvesCount = 0
    SubmissionsCount = 0
    #SectionName = ""  [TODO Later]

    def __init__(self, id: int, name: str, subscnt: int, solvescnt: int) -> None:
        self.ID = id
        self.Name = name
        self.SolvesCount = solvescnt
        self.SubmissionsCount = subscnt
        pass


class CSES:
    BASE_URL = "https://cses.fi"
    LOGIN_URL = BASE_URL + "/login"
    LOGOUT_URL = BASE_URL + "/logout"
    PROBLEMSET_URL = BASE_URL + "/problemset/list"
    STATS_URL = BASE_URL + "/problemset/stats/"
    session = requests.session()

    def __init__(self) -> None:
        pass

    def open_page(self, url: str) -> BeautifulSoup:
        response = self.session.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def login(self, username: str, password: str) -> bool:
        csrf_token = self.open_page(self.LOGIN_URL).find('input', {'name': 'csrf_token'})['value']

        # Set the login data
        login_data = {
            'csrf_token': csrf_token,
            'nick': username,
            'pass': password,
            'submit': 'Login'
        }

        # Post the login data to the login page
        response = self.session.post(self.LOGIN_URL, data=login_data)

        # Check if the login was successful
        if response.url == self.LOGIN_URL:
            return False
        else:
            return True
    
    def logout(self):
        self.session.get(self.LOGOUT_URL)
    
    def get_problemset_tasks(self) -> list:
        tasks = []
        soap = self.open_page(self.PROBLEMSET_URL)
        tsks = soap.find_all('li', {'class': 'task'})
        for tsk in tsks:
            tasks.append(CSES_Task(
                int(tsk.a['href'].split('/')[-1]),
                tsk.a.text,
                int(tsk.span.text.split('/')[0]),
                int(tsk.span.text.split('/')[1])
            ))
        return tasks

    # TODO: Implement submission, with file or without
    def submit_code(self, code, language):
        pass

    # Requires login
    def get_statistics(self, problem_id):
        soap = self.open_page(self.STATS_URL + str(problem_id))
        tables = soap.find_all('table', {'class': 'narrow'})
        shortest = []
        time = []
        for row in tables[1].find_all('tr'):
            cells = row.find_all('td')
            shortest.append(cells[1].a.text)
        for row in tables[0].find_all('tr'):
            cells = row.find_all('td')
            time.append(cells[1].a.text)
        return {
            'shortest': shortest,
            'time': time
        }
        

    def submit_file(self, filepath, language):
        pass


CSES_USERNAME = "WhatEver"
CSES_PASSWORD = "rELl!y_$EcREt_@A$sWoRD"

def test():
    cses = CSES()
    print("Login: ", cses.login(CSES_USERNAME, CSES_PASSWORD))
    tasks = cses.get_problemset_tasks()
    for t in tasks:
        print(f"Task[{t.ID}]: {t.Name} ({t.SubmissionsCount}/{t.SolvesCount})")
    cses.logout()

def standings(users: dict):
    cses = CSES()
    print("Login: ", cses.login(CSES_USERNAME, CSES_PASSWORD))
    tasks = cses.get_problemset_tasks()
    stands = {}
    for u in users:
        stands[u] = 0
    cnt=1
    for t in tasks:
        stats = cses.get_statistics(t.ID)
        print(cnt)
        for i in range(5):
            if (stats['time'][i] in users):
                stands[stats['time'][i]] += 5-i
            if (stats['shortest'][i] in users):
                stands[stats['shortest'][i]] += 5-i
        cnt+=1
    for i in stands:
        print(i, stands[i])
        
