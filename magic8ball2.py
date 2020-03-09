import random
messages = ['It is certain',
            'It is decidently',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Consetrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
