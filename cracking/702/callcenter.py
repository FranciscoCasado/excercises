from employee import Director, Manager, Respondent
from call import Call

class CallCenter:
    def __init__(self, personel):

        self._director_queue = [Director() for e in range(personel['director'])]
        self._manager_queue = [Manager() for e in range(personel['manager'])]
        self._respondent_queue = [Respondent() for e in range(personel['respondent'])]
        self._busy_people = []

    def handle_call(self, call):
        pass

        

