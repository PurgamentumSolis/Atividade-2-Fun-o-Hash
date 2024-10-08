import hashlib

frases_e_hashes = [
    {
        "frase": "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
        "SHA256_fornecido": "d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9",
        "MD5_fornecido": "c850e1a34a6ed572e0758ccd9c615bda"
    },
    {
        "frase": "A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus",
        "SHA256_fornecido": "6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337",
        "MD5_fornecido": "b710771da8d7521524f45233ea9dd9e1"
    },
    {
        "frase": "Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
        "SHA256_fornecido": "6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6",
        "MD5_fornecido": "55748c2cb669a9d9508677cb914cb025"
    },
    {
        "frase": "A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.",
        "SHA256_fornecido": "254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e",
        "MD5_fornecido": "f4a8a299fd4da2a5d70b374be2e48147"
    },
    {
        "frase": "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982",
        "SHA256_fornecido": "d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0",
        "MD5_fornecido": "1c4ecc238571333ae507f82ff6a5e9e4"
    },
    {
        "frase": "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.",
        "SHA256_fornecido": "faefb927a21dd282ee00effe42bc0688f649450677a61edce15863a15461b721",
        "MD5_fornecido": "98420532cbf1be32a98be579f592cd72"
    },
    {
        "frase": "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
        "SHA256_fornecido": "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        "MD5_fornecido": "2e20bfbece6fdc62de4c4bb80a77ba1f"
    },
    {
        "frase": "Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.",
        "SHA256_fornecido": "56f4ba0ea34d91fe386f09dc687f1c35c757009b0230a828fa43e48ac08f8d0c",
        "MD5_fornecido": "5cbf7c58bf9acd451c3bf1b48392a9e6"
    },
    {
        "frase": "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.",
        "SHA256_fornecido": "2707325bd4929bbbadb422851a2248615bf7998bf3607b6ad934168be6a45859",
        "MD5_fornecido": "a0a80cbc42bcd7b4b6ab317d0d2efa33"
    },
    {
        "frase": "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.",
        "SHA256_fornecido": "b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8",
        "MD5_fornecido": "0288b32001adf2f237ba8410f8415e50"
    }
]

for item in frases_e_hashes:
    frase = item["frase"]
    SHA256_calculado = hashlib.sha256(frase.encode('utf-8')).hexdigest()
    MD5_calculado = hashlib.md5(frase.encode('utf-8')).hexdigest()

    print(f"Frase: \"{frase}\"")
    print()
    print(f"SHA256 fornecido: {item['SHA256_fornecido']}")
    print(f"SHA256 calculado: {SHA256_calculado}")
    print("SHA256 correto?" , SHA256_calculado == item["SHA256_fornecido"])
    print()
    print(f"MD5 fornecido: {item['MD5_fornecido']}")
    print(f"MD5 calculado: {MD5_calculado}")
    print("MD5 correto?" , MD5_calculado == item["MD5_fornecido"])
    print("-" * 50)
