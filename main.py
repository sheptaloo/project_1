authors = {
    'Косач': 'Видатна українська поетеса, драматургиня, перекладачка та громадська діячка. Її творчість насичена патріотизмом та глибоким громадським звучанням',
    'Коцюбинський': 'Український письменник, прозаїк, драматург, есеїст, громадський діяч. Його творчість сповнена патріотизму та любові до України',
    'Шевченко': 'Великий український поет, художник, мислитель і громадський діяч. Національний герой та символ України, Шевченко став одним з найзначніших діячів української культури',
}


name = input()
if name in authors:
    print("Біографія:", authors[name])
else:
    n = input('Автор не знайдений. Додати?')

    if n == "так":
        b = input("Біографія")
        authors[name] = b
        print(authors)
    else:
        print("Відповідь отримано")
