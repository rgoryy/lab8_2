import tkinter as tk
import random
global probabilities, entry_widgets
def generate_event():

    probabilities = [float(entry.get()) for entry in entry_widgets]
    total = sum(probabilities)

    if total != 1:
        probabilities = [0.1, 0.2, 0.3, 0.4]
        update_probabilities_display()
        result = f"Возвращено к значениям по умолчанию."
        result_label.config(text=result)
        return

    event_index = random.choices(range(len(probabilities)), weights=probabilities, k=1)[0]
    result = f"Событие {event_index + 1} было сгенерировано."
    result_label.config(text=result)

def update_probabilities_display():
    global probabilities, entry_widgets
    for i, entry in enumerate(entry_widgets):
        entry.delete(0, tk.END)
        entry.insert(0, str(probabilities[i])) 

root = tk.Tk()
root.title("Генератор событий")

probabilities = [0.1, 0.2, 0.3, 0.4]
entry_widgets = []

for i in range(len(probabilities)):
    entry = tk.Entry(width=10)
    entry.insert(0, str(probabilities[i]))
    entry.pack()
    entry_widgets.append(entry)

result_label = tk.Label(text="")
result_label.pack()

generate_button = tk.Button(text="Сгенерировать событие", command=generate_event)
generate_button.pack()

root.update()
root.mainloop()