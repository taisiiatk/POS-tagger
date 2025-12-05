import gradio as gr

from pos_tagger import replace_words_with_pos, load_spacy_model

try:
    nlp = load_spacy_model()
except:
    nlp = None
    print(f"Помилка завантаження моделі. Перевірте встановлення spaCy та uk_core_news_sm.")

def process_text(text):
    if not text.strip():
        return "Будь ласка, введіть текст для аналізу."
    try:
        result = replace_words_with_pos(text, nlp)
        return result
    except Exception as e:
        return f"Помилка: {str(e)}"

with gr.Blocks(title="Аналіз частин мови") as demo:
    gr.Markdown("# Аналізатор частин мови")
    gr.Markdown("Введіть текст для аналізу частиномовних належностей")

    input_text = gr.Textbox(label="Текст", placeholder="Наприклад: День буде хорошим.", lines=4)
    output_text = gr.Textbox(label="Результат", interactive=False, lines=4)

    btn = gr.Button("Аналізувати")
    btn.click(fn=process_text, inputs=input_text, outputs=output_text)

    gr.Markdown("### Приклади:")
    gr.Examples(
        examples=[
            "Сьогодні сонце світить яскраво. Я вирішив піти на прогулянку. У парку було багато людей. Всі насолоджувалися теплим літнім повітрям.",
            "Книга, яку я читаю, дуже цікава. Вона розповідає про подорожі дитини у казковому світі. Головний герой — хоробрий хлопчик на ім'я Олег. Він подорожує зі своїм вірним другом — ведмедем.",
            "Мій кіт дуже ласкавий. Він любить лежати на сонці. Іноді він грається з іграшковим м'ячем. Ввечері він сидить біля мене й муркоче.",
        ],
        inputs=input_text
    )
    

demo.launch(theme = gr.themes.Soft())