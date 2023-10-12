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

    def submit_file(self, filepath, language):
        pass


CSES_USERNAME = "WhatEver"
CSES_PASSWORD = "rELl!y_$EcREt_@A$sWoRD"

def main():
    cses = CSES()
    print("Login: ", cses.login(CSES_USERNAME, CSES_PASSWORD))
    tasks = cses.get_problemset_tasks()
    for t in tasks:
        print(f"Task[{t.ID}]: {t.Name} ({t.SubmissionsCount}/{t.SolvesCount})")
    cses.logout()

main()
