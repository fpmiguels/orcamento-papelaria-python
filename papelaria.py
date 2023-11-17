# Definindo as funções
# Função de escolha de serviço 
def escolha_serviço():               
    print ('          Escolha o tipo de serviço')   
    print ('DIG - Digitalização')
    print ('ICO - Impressão colorida')
    print ('IPB - Impressão preto e branco')
    print ('FOT - Fotocópia')
    while True:        
         try:            
            escolha_s = str (input('>>: '))  # str para que sejam só aceitas letras no input
            escolha_s = escolha_s.upper()      
            if escolha_s == 'DIG':
                return 1.1            
            elif escolha_s == 'ICO':
                return 1.0      
            elif escolha_s == 'IPB':
                return 0.4     
            elif escolha_s == 'FOT':
                return 0.2      
            else:
                print ('Serviço não encontrado, tente novamente')
                continue        
         except ValueError:  # caso digite algum número inteiro ou float, será acionado o except ValueError informando que só aceitam str
            print ('Digite apenas letras')
            continue     
# Função de escolha a página
def escolha_página ():             
    while True:         
         try:           
            escolha_p = int(input('Digite o número de páginas >>: ')) # int para que sejam aceitos somentes números inteiros
            if escolha_p < 10:
                return escolha_p            
            elif escolha_p >=10 and escolha_p < 100:         
                return escolha_p * 0.90                      # O 0.90 é o desconto de 10%            
            elif escolha_p >= 100 and escolha_p < 1000:
                return escolha_p * 0.85                      # 0.85 é o valor de 15% de desconto            
            elif escolha_p >= 1000 and escolha_p < 10000:
                return escolha_p * 0.80                      # 0.80 é o valor de 20% de desconto            
            else:
                print('Não fazemos serviços acima ou igual a 10000 páginas, tente novamente.')
                continue        
         except ValueError:
            print('Digite apenas números inteiros')
            continue
# Função de serviço extra
def serviço_extra ():                  
    print('    Deseja algum serviço extra?')
    print('1 - Encadernação simples - R$ 10.00')
    print('2 - Encadernação capa dura - R$ 25.00')
    print('0 - Não desejo mais nada')   
    acumulador = 0
    while True:        
        try:                                
            escolha_ex = int(input('>>: '))
            if escolha_ex == 1:
                return acumulador + 10.00           
            elif escolha_ex == 2:
                return  acumulador + 25.00            
            elif escolha_ex == 0:
                return acumulador
            else:
                print('Digite opções válidas')
                continue        
        except ValueError:                   
            print('Digite apenas números (0/1/2)')
            continue
# Inicio do main
print ('Bem-vindos a Papelaria do Felipe Miguel da Silva') # Mensagem de boas vindas    
serviço = escolha_serviço()  # chamando a função serviço
pagina = escolha_página()    #chamadno a função pagina
extra = serviço_extra()    #chamando a função extra
total = (serviço * pagina) + extra           # operação matemática de multiplicação e soma    
print ('O preço total é R$ {:.2f} (Serviço {:.2f} * Páginas {:.0f} + Extra R$ {:.2f})'.format(total,serviço,pagina,extra))  
# informando o preço total e também os tipos de serviços, numeros de paginas cobradas pois existe o desconto e mais o extra
