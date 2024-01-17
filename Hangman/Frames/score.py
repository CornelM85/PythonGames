import customtkinter as ctk


class Score(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.score = ctk.StringVar(value='Score: 0')
        self.attempt = ctk.StringVar(value='Try: 0')
        self.remaining_tries = ctk.StringVar(value='Remaining tries: 5')

        self.score_label = ctk.CTkLabel(self, textvariable=self.score, font=ctk.CTkFont(size=15),
                                        height=10, text_color='white')
        self.score_label.grid(row=0, column=0, sticky='w')

        self.attempt_label = ctk.CTkLabel(self, textvariable=self.attempt, font=ctk.CTkFont(size=15),
                                          height=10, text_color='white')
        self.attempt_label.grid(row=1, column=0, sticky='w')

        self.rm_tr_label = ctk.CTkLabel(self, textvariable=self.remaining_tries, font=ctk.CTkFont(size=15),
                                        height=10, text_color='white')
        self.rm_tr_label.grid(row=2, column=0, sticky='w')

    def set_score(self):
        if self.get_remaining_tries() != 0:

            result = int(self.score.get().removeprefix('Score: '))
            result += 10
            self.score.set('Score: ' + str(result))

    def set_attempt(self):
        if self.get_remaining_tries() != 0:

            result = int(self.attempt.get().removeprefix('Try: '))
            result += 1
            self.attempt.set('Try: ' + str(result))

    def set_remaining_tries(self):
        if self.get_remaining_tries() != 0:

            result = int(self.remaining_tries.get().removeprefix('Remaining tries: '))
            result -= 1
            self.remaining_tries.set('Remaining tries: ' + str(result))

    def get_remaining_tries(self):
        result = int(self.remaining_tries.get().removeprefix('Remaining tries: '))
        return result

    def get_score(self):
        result = int(int(self.score.get().removeprefix('Score: ')))
        return result

    def reset_score(self):
        self.score.set(value='Score: 0')
        self.attempt.set(value='Try: 0')
        self.remaining_tries.set(value='Remaining tries: 5')
