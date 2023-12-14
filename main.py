import modules.SayHello as App
from diaries.DiarySample import DiarySample

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

# def run():
#     app = App.SayHello("Git")
#     app.say()
# if __name__ == '__main__':
#     run()
