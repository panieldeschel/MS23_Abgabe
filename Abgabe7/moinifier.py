def moinify(text):
    replace_these = [
        "Hallo",
        "Guten Tag",
        "Guten Morgen",
        "Guten Abend",
        "Servus",
        "Hi",
        "Hey",
        "Grüß Gott",
        "Schönen guten Tag",
        "Herzlich willkommen",
        "Willkommen",
        "Frohen Tag",
        "Moin Moin",
        "Salut",
        "Tach",
        "Tagchen",
        "Griaß di",
        "Mahlzeit",
        "Ahoi",
        "Holla",
        "Hallo zusammen"
    ]
    for word in replace_these:
        text = text.replace(word, "Moin")    
    return text

