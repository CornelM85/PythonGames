import customtkinter as ctk


class Score(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.score = ctk.StringVar(value='0')
        self.attempt = ctk.StringVar(value='0')
        self.remaining_tries = ctk.StringVar(value='5')

        self.score_label = ctk.CTkLabel(self, text='Score: ', font=ctk.CTkFont(size=15),
                                        height=10, text_color='white')
        self.score_label.grid(row=0, column=0, sticky='e')

        self.score_label_1 = ctk.CTkLabel(self, textvariable=self.score, font=ctk.CTkFont(size=15),
                                          height=10, text_color='#3282F6')
        self.score_label_1.grid(row=0, column=1)

        self.attempt_label = ctk.CTkLabel(self, text='Try: ', font=ctk.CTkFont(size=15),
                                          height=10, text_color='white')
        self.attempt_label.grid(row=1, column=0, sticky='e')

        self.attempt_label_1 = ctk.CTkLabel(self, textvariable=self.attempt, font=ctk.CTkFont(size=15),
                                            height=10, text_color='red')
        self.attempt_label_1.grid(row=1, column=1)

        self.rm_tr_label = ctk.CTkLabel(self, text='Remaining tries: ', font=ctk.CTkFont(size=15),
                                        height=10, text_color='white')
        self.rm_tr_label.grid(row=2, column=0, sticky='w')

        self.rm_tr_label_1 = ctk.CTkLabel(self, textvariable=self.remaining_tries, font=ctk.CTkFont(size=15),
                                          height=10, text_color='green')
        self.rm_tr_label_1.grid(row=2, column=1)

    def set_score(self):
        """
        Sets the displayed score in the Application
        """
        if self.get_remaining_tries() != 0:

            result = self.get_score()
            result += 10
            self.score.set(str(result))

    def set_attempt(self):
        """
        Sets the displayed number of tries in the Application
        """
        if self.get_remaining_tries() != 0:

            result = int(self.attempt.get())
            result += 1
            self.attempt.set(str(result))

    def set_remaining_tries(self):
        """
        Sets the displayed remaining tries in the Application
        """
        if self.get_remaining_tries() != 0:

            result = self.get_remaining_tries()
            result -= 1
            self.remaining_tries.set(str(result))

    def get_remaining_tries(self):
        """
        Gets the remaining tries displayed in the Application window
        :return: int
        """
        result = int(self.remaining_tries.get())
        return result

    def get_score(self):
        """
        Gets the score displayed in the Application window
        :return: int
        """
        result = int(self.score.get())
        return result

    def reset_score(self):
        """
        Resets the 3 values displayed in the Application window
        """
        self.score.set(value='0')
        self.attempt.set(value='0')
        self.remaining_tries.set(value='5')
