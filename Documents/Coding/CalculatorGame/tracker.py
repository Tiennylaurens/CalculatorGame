class Status:
    def __init__(self):
        self.started_game = False
        self.finished_first_tran = False
        self.finished_game = False
        self.end_score_displayed = False
        self.run = True

    def set_started(self):
        self.started_game = True

    def set_finished_first_tran(self):
        self.finished_first_tran = True

    def set_finished(self):
        self.finished_game = True
        
    def set_end_score(self):
        self.end_score_displayed = True

    def set_number(self,num):
        self.number = num
    
    def set_operator(self,num):
        self.operator = num