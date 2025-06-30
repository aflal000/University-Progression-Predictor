from graphics import *

Progress = 0
Trailer = 0
Retriever = 0
Exclude = 0
progression_data = []

print("  ┌──────┐    ┌───────┐     ┌──────┐                         ┌───────────────────────────────┐")
print("  │ Pass │    │ Defer │     │ Fail │                         │          yes-y / quit-q       │")
print("  └──────┘    └───────┘     └──────┘                         └───────────────────────────────┘\n")

def credits():
    global Progress, Trailer, Retriever, Exclude
    true = True
    while true:
        while True:
            try:
                passes = int(input('   '))
                if passes not in range(0, 121, 20):
                    print('Out of range\n')
                    continue
            except ValueError:
                print('Integer required\n')
                continue
            break
        while True:
            try:
                defer = int(input('\t       '))
                if defer not in range(0, 121, 20):
                    print('\t        Out of range\n')
                    continue
            except ValueError:
                print('\t        Integer required\n')
                continue
            break
        while True:
            try:
                fail = int(input('\t\t             '))
                if fail not in range(0, 121, 20):
                    print('\t\t             Out of range\n')
                    continue
            except ValueError:
                print('\t\t              Integer required\n')
                continue
            break
        total = passes + defer + fail
        while True:
            if total != 120:
                print('\t\t\t\t             Total incorrect')
                credits()
            break

        if passes == 120:
            print('\t\t\t\t      ★ Progress')
            Progress += 1
        elif passes == 100 and (defer == 20 or fail == 20):
            print('\t\t\t\t      ★ Progress (Module trailer)')
            Trailer += 1
        elif fail >= 80:
            print('\t\t\t\t      ★ Exclude')
            Exclude += 1
        else:
            print('\t\t\t\t      ★ Do not progress - Module retriever')
            Retriever += 1

        progression_data.append([passes, defer, fail])

        while True:
            response = str(input("\t\t\t\t\t\t\t\t\t      "))
            if response == 'y':
                print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
                break
            elif response == 'q':
                display_bar_graph()
                break
            else:
                print('\t\t\t\t\t\t\t\t\t Invalid command')
                continue
        if response == 'q':
            break

def display_bar_graph():
    win = GraphWin("Histogram Results", 600, 600)
    win.setBackground("white")

    bar_width = 100
    space_between_bars = 20
    total_bar_width = (4 * bar_width) + (3 * space_between_bars)
    starting_x_position = (600 - total_bar_width) / 2
    x_position = starting_x_position
    counts = [Progress, Trailer, Retriever, Exclude]

    bar_colors = ["green", "blue", "orange", "red"]

    for i, count in enumerate(counts):
        bar_height = count * 400
        bar = Rectangle(Point(x_position, 500 - bar_height), Point(x_position + bar_width, 500))
        bar.setFill(bar_colors[i])
        bar.draw(win)

        count_text = Text(Point(x_position + bar_width / 2, 500 - bar_height - 30), str(count))
        count_text.setSize(18)
        count_text.draw(win)

        x_position += bar_width + space_between_bars

    x_position = starting_x_position
    labels = ["Progress", "Trailer", "Retriever", "Excluded"]
    for label in labels:
        label_text = Text(Point(x_position + bar_width / 2, 530), label)
        label_text.setSize(16)
        label_text.draw(win)
        x_position += bar_width + space_between_bars

    total_outcomes = sum(counts)
    total_text = Text(Point(150, 570), f"{total_outcomes} outcomes in total.")
    total_text.setSize(18)
    total_text.draw(win)

    win.getMouse()
    win.close()

credits()