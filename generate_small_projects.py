import subprocess

def main():
    directories = [
        '0-mandatory-in-programming-languages',                                                        # Obrigatórios em Linguagens de Programação
        '0-mandatory-in-programming-languages\\00-programming-paradigms',                              # - Paradigmas de Programação
        '0-mandatory-in-programming-languages\\00-programming-paradigms\\imperative-programming',      # - - Programação Imperativa
        '0-mandatory-in-programming-languages\\00-programming-paradigms\\functional-programming',      # - - Programação Funcional
        '0-mandatory-in-programming-languages\\00-programming-paradigms\\object-oriented-programming', # - - Programação Orientada a Objetos
        '0-mandatory-in-programming-languages\\01-string-formatting',                                  # - Formatação de Strings
        '0-mandatory-in-programming-languages\\02-input-output',                                       # - Entrada e Saída de dados
        '0-mandatory-in-programming-languages\\03-exception-handling',                                 # - Manipulação de Exceções
        '0-mandatory-in-programming-languages\\04-file-handling',                                      # - Manipulação de arquivos
        '0-mandatory-in-programming-languages\\05-serialization',                                      # - Serialização
        '0-mandatory-in-programming-languages\\06-graphical-user-interface',                           # - Interface gráfica (GUI)
        '0-mandatory-in-programming-languages\\07-command-line-interface',                             # - Interface em linha de comando (CLI)
        '0-mandatory-in-programming-languages\\08-data-structures',                                    # - Estruturas de Dados
        '0-mandatory-in-programming-languages\\09-algorithms',                                         # - Algoritmos
        '0-mandatory-in-programming-languages\\10-regular-expressions',                                # - Expressão Regulares (RegEx)
        '0-mandatory-in-programming-languages\\11-parallel-and-concurrent-programming',                # - Programação paralela e concorrente
        '0-mandatory-in-programming-languages\\12-computer-networking',                                # - Rede de Computadores
        '0-mandatory-in-programming-languages\\13-databases',                                          # - Banco de dados
        '1-external-libraries',                                                                        # Opcionais da Linguagem
        '2-optional-language-features',                                                                # Bibliotecas externas
        '3-others'                                                                                     # Outros
    ]
    for i in directories:
        subprocess.run(['mkdir', i], shell=True)

if __name__ == '__main__':
    main()

















# Opcionais da Linguagem
# Bibliotecas externas
# Outros



