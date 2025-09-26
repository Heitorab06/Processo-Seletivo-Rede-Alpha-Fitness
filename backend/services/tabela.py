import pandas as pd


email_regex = r"[a-zA-Z0-9.záàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ]+@.+$"
numero_regex = r"\++[0-9]{13}"
cpf_regex = r"[0-9]{11}"


urlalpha = "https://docs.google.com/spreadsheets/d/1OO7gDKXv4YJiDfpfrIHaXIa_XUgDhl3rG2FQImQ-ixY/export?format=csv"

def carregar_dados():
    dataframe = pd.read_csv(urlalpha, dtype={"cpf": str, "numero": str})
    dataframe = dataframe.dropna()  # remove linhas com valores nulos

    dataframe = dataframe[          #garante que apenas usuários consistentes aparecerão
        dataframe["email"].str.fullmatch(email_regex)
        & dataframe["numero"].str.fullmatch(numero_regex)
        & dataframe["cpf"].str.fullmatch(cpf_regex)
    ]

    dataframe = dataframe.iloc[::-1]    #usuários mais recentes ficam no topo da tabela
    return dataframe
