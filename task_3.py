from faker import Faker


def generate_paragraph(language):
    fake = Faker(language)
    return fake.paragraph()


languages = ['en', 'it', 'de', 'es', 'fr']

with open("paragraphs.txt", "w", encoding="utf-8") as file:
    for language in languages:
        Faker(language)
        paragraph = generate_paragraph(language)
        file.write(f"{language.upper()}: {paragraph}\n\n")
