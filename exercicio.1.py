# def criar_arquivo(nome_arquivo:str,conteudo:str):
#     """cria um arquivo com o nome e conteudo fornecidos"""
#     with open(nome_arquivo, 'w') as arquivo:
#         arquivo.write(conteudo)
#         print("arquivo criado")

# nome = input('digite o nome do arquivo:')
# criar_arquivo(f'arquivos/{nome}.txt',"0\n7\n5")

#ler o arquivo

#def ler_arquivo(nome_arquivo: str ):
    #retorna o contéudo  de um arquivo 
 #   with open(nome_arquivo, 'r') as arquivo:
  #      return arquivo.read()
       

#nome = input('digite o nome do arquivo:')
#print(ler_arquivo(f"arquivos/{nome}.txt"))
#ler_arquivo(f'arquivos/{nome}.txt')
#adicionar conteudo


#def adicionar_arquivo(nome_arquivo:str,conteudo:str):
    #adicionar um arquivo com o nome e conteudo fornecidos
 #   with open(nome_arquivo, 'a') as arquivo:
   #     arquivo.write('\n' + conteudo)
  #  print("arquivo criado")

#nome = input('informe  o nome do arquivo:')
#conteudo = input('digite o texto a ser adicionado')
#adicionar_arquivo(f'arquivos/{nome}.txt',"um exemplo de arquivo criado em python")

#remover

#import os 
#def remover_arquivo(nome_arquivo:str):
 # """exclui um arquivo se ele existe"""
        
  #  if os.path.exists(nome_arquivo):  
   #     os.remove(nome_arquivo)
    #    print('aruqivo removido com sucesso')
    #else:
     #   print('arquivo não encontrado')
    #nome = input('informe o nome do arquivo que deseja remover:')

    #remover_arquivo(f'arquivos/{nome}.txt')


#contar quantas linhas


#def contar_linhas(nome_arquivo: str) -> str:
 #   """ retorna o contéudo de um arquivo."""
  #  with open(nome_arquivo, 'r')as arquivo:
   #     return len(arquivo.readlines())
#nome = input('digite o nome do arquivo:')
#print(contar_linhas(f'arquivos/{nome}.txt'))

#verificar se uma palavra existe no contéudo

#def verifica_palavra(nome_arquivo: str , palavra:str ) -> bool:
 #   """ retorna a verifiação  de uma palavra  dentro de um arquivo:"""
  #  with open(nome_arquivo, 'r') as arquivo:
   #     return palavra in arquivo.read()

    
#nome  = input('informe o nome do arquivo')
#print(verifica_palavra(f'arquivos/{nome}.txt'))


#criar um arquivo com 3 linhas contendo um número em cada linha 
#criar uma função que soma os números desse arquivo

def soma_numeros(nome_arquivo: str) -> bool:
    """ retorna a dos numeros de um arquivo"""
    with open(nome_arquivo, 'r') as arquivo:
        return sum(int(linha.strip())for  linha in arquivo)
nome = input ('informe o nome do arquivo')
print(soma_numeros(f'arquivos/{nome}.txt'))

#atualiza uma linha especifica do arquivo

def atualizar_linha(nome_arquivo:str ,novo_conteudo: str, linha_alvo: int ):
    """atualiza uma linha especifica de um arquivo"""
    with open(nome_arquivo,'r') as arquivo: 
        linhas = arquivo.readlines()
        if 0 < linhas < len(linhas):
            linhas[linha_alvo] =  novo_conteudo + '\n'
    with open(nome_arquivo, 'w') as arq:
        arq.write(linhas)
        print(linhas)

nome = input('informe o nome do arquivo:')
conteudo = input('informe o conteudo do arquivo:')
nome = int(input('informe o numero de linha  do arquivo:'))
print(atualizar_linha(f'arquivos/{nome}.txt'))