from guizero import App, Text, TextBox, PushButton, Picture

app = App(title="Nicola's amazing thing that she's made", bg='blue', width=1920, height=1080)
username = 'Nic'
password = '1234'
def check_input():
    if un_box.value == username and pw_box.value == password:
        message = Text(app, text='Correct')
        picture = Picture(app, image="thumbs_up.jpg")
    else:
        message = Text(app, text='Incorrect')
        picture = Picture(app, image="thumbs_down.png")

un_box = TextBox(app)
pw_box = TextBox(app)
submit = PushButton(app, text='SUBMIT', command=check_input)


# text1 = Text(app, text='Hello GUI!', size=50, font='Agency FB', color='yellow', align='left')
# app.yesno(title='Yes or No', text='would you like to close this window?')
# app.warn(title='oh no!', text='something bad has happened!')

app.display()
