#!/usr/bin/env python
# Módulos
# Versão feita por - Kiny
# Pix - (21) 97918-0533
from os import system, name,path;
from sys import executable;
from time import sleep;
#from json import loads;
try: from requests import get;
except:
	system('%s -m pip install requests'%executable);
	from requests import get;

# Cores

Azul='\033[1;34m';Branco='\033[1;37m';Verde='\033[1;32m';Vermelho='\033[1;31m';

# Logo
logo="""%s
 .--------.____________
 || ° ° ° °     .2021.|| ®
 ||                    | ©                          
 ||\     ______________________
 || \   // ° ° ° ° ° ° ° ° ° °/
 ||\ \ //                    /
 || \ //                    /
 ||\ //                    /
 || //                    /
 ||//                    /
 ||/                    /
 |/____________________/
 
 %sRecodado por -%s Kiny
 %sPix do Painel%s - (21) 97918-0533
 
 %s<%s Arquivo Clownters %s>%s
"""%(Verde,Azul,Branco,Azul,Branco,Vermelho,Branco,Vermelho,Branco)

clean={'posix':'clear','nt':'cls'}[str(name)];

def clear(): system(clean);
def update(): system('git pull');
def sair():
	global Sair
	Sair=True

# Variável para mandar o loop do menu
Sair=False;

# Função para requisição
def requests(api,verify=True): return get(api,verify=verify).json()

# Funções de Consulta
def ddd():
	clear();
	try:
		result=requests('https://brasilapi.com.br/api/ddd/v1/'+input('%s %s> Digite o DDD que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)));
		try:
			msg=''
			for i in result['cities']:
				msg+=' %s,'%i
			msg='''
%sEstado%s - %s
%sCidade%s - %s
'''%(Azul,Branco,result['state'],Azul,Branco,msg[:-1])
		except Exception as e:
			msg='%s<%s DDD não encontrado. %s>%s'%(Vermelho,Branco,Vermelho,Branco);msg=e
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg;

def cep():
	clear();
	try:
		result=requests('https://viacep.com.br/ws/'+input('%s %s> Digite o CEP que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde))+'/json');
		try:
			msg='''
%sCEP%s - %s
%sLogradouro%s - %s
%sComplemento%s - %s
%sBairro%s - %s
%sLocalidade%s - %s
%sEstado%s - %s
%sIBGE%s - %s
%sGIA%s - %s
%sDDD%s - %s
%sSIAFI%s - %s
'''%(Azul,Branco,result['cep'],Azul,Branco,result['logradouro'],Azul,Branco,result['complemento'],Azul,Branco,result['bairro'],Azul,Branco,result['localidade'],Azul,Branco,result['uf'],Azul,Branco,result['ibge'],Azul,Branco,result['gia'],Azul,Branco,result['ddd'],Azul,Branco,result['siafi']);
		except Exception:
			msg='%<% CEP não encontrado. %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except Exception as e:
		msg='%s<%s CEP INVÁLIDO OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg;

def ip():
	clear();
	try:
		result=requests('https://ipwhois.app/json/'+input('%s %s> Digite o IP que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)));
		msg='';
		try:
			msg='''
%sIP%s - %s
%sTipo%s - %s
%sContinente%s - %s
%sPaís%s - %s
%sCapital%s - %s
%sRegião%s - %s
%sCidade%s - %s
%sDDI%s - %s
%sLatitude%s - %s
%sLongitude%s - %s
'''%(Azul,Branco,result['ip'],Azul,Branco,result['type'],Azul,Branco,result['continent'],Azul,Branco,result['country'],Azul,Branco,result['country_capital'],Azul,Branco,result['region'],Azul,Branco,result['city'],Azul,Branco,result['country_phone'],Azul,Branco,result['latitude'],Azul,Branco,result['longitude']);
		except:
			msg='%s<%s Endereço de IP não encontrado %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except:
		msg='%<% API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg;

def nome():
	clear();
	try:
		result=requests('http://ghostcenter.xyz/api/nome/'+input('%s %s> Digite o nome que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)));
		msg='';
		try:
			for i in range(int(len(result['dados']))):
				msg+='''\n%sNOME%s - %s\n%sCPF%s - %s\n%sANIVERSARIO%s - %s\n%sSEXO%s - %s\n'''%(Azul,Branco,result['dados'][i]['nome'],Azul,Branco,result['dados'][i]['cpf'],Azul,Branco,result['dados'][i]['nascimento'],Azul,Branco,result['dados'][i]['sexo']);
		except Exception:
			msg='\n%s<%s Nome inválido ou Curto; demais %s>%s\n'%(Vermelho,Branco,Vermelho,Branco);
	
	except Exception as e:
		msg= '%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg;

def covid():
	clear();
	try:
		result=requests('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/'+input('%s %s> Digite o UF do estado que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)));
		try:
			msg='''
%sEstado%s - %s
%sCasos%s - %s
%sMortes%s - %s
%sSuspeitas%s - %s
%sCasos Recusados%s - %s
'''%(Azul,Branco,result['state'],Azul,Branco,result['cases'],Azul,Branco,result['deaths'],Azul,Branco,result['suspects'],Azul,Branco,result['refuses'])
		except Exception:
			msg= '%s<%s UF INVÁLIDO %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except Exception:
		msg= '%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg;
	
def cpf():
	clear();
	cpf=input('%s %s> Digite o CPF que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde));
	try:
		if len(cpf) != 11:
			msg='%s<%s QUANTIDADE DE DÍGITOS INVÁLIDA %s>%s'%(Vermelho,Branco,Vermelho,Branco);
		else:
			result=requests('http://191.235.72.119/api/v1/esus/?q='+cpf);
			try:
				msg='';
				for c in range(int(len(result['dados']))):
					for i in result['dados'][c]:
						msg+='%s%s%s - %s\n'%(Azul,str(i),Branco,str(result['dados'][c][i]));
				msg='\n%s'%msg;
			except Exception as e:
				msg='%s<%s CPF NÃO ENCONTRADO %s>%s\n%s'%(Vermelho,Branco,Vermelho,Branco,e);
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg

def cns():
	clear();
	cns=input('%s %s> Digite o CNS que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde));
	try:
		if len(cns) != 15:
			msg='%s<%s QUANTIDADE DE DÍGITOS INVÁLIDA %s>%s'%(Vermelho,Branco,Vermelho,Branco);
		else:
			result=requests('http://191.235.72.119/api/v1/esus/?q='+cns);
			try:
				msg='';
				for c in range(int(len(result['dados']))):
					for i in result['dados'][c]:
						msg+='%s%s%s - %s\n'%(Azul,str(i),Branco,str(result['dados'][c][i]));
				msg='\n%s'%msg;
			except Exception as e:
				msg='%s<%s CNS NÃO ENCONTRADO %s>%s\n%s'%(Vermelho,Branco,Vermelho,Branco,e);
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg

def bank():
	clear();
	try:
		result=requests('https://brasilapi.com.br/api/banks/v1/'+input('%s %s> Digite o Código Bancário que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)))
		try:
			msg='''
%sISPB%s - %s
%sNome - %s
%sCódigo - %s
%sNome Completo - %s
'''%(Azul,Branco,result['ispb'],Azul,Branco,result['name'],Azul,Branco,result['code'],Azul,Branco,result['fullName'])
		except Exception:
			msg='%s<%s CÓDIGO BANCÁRIO INVÁLIDO OU NÃO ENCONTRADO %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg

def placa():
	clear();
	try:
		result=requests('https://apicarros.com/v1/consulta/%s'%input('%s %s> Digite a Placa que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)),verify=False);
		try:
			msg=''
			for i in result:
				msg+='%s%s%s - %s\n'%(Azul,str(i.upper()),Branco,result[i]);
			msg='\n%s'%msg;
		except Exception:
			msg='%s<%s PLACA INVÁLIDA %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	return msg

def bin():
	clear();
	try:
		result=requests('https://lookup.binlist.net/%s'%input('%s %s> Digite a BIN que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)));
		try:
			msg='''
%sTipo%s - %s
%sMarca%s - %s
%sPré-Pago%s - %s
%sPaís%s - %s
%sNome do Banco%s - %s
%sTelefone%s - %s
%sCidade%s - %s
'''%(Azul,Branco,result['type'],Azul,Branco,result['brand'],Azul,Branco,result['prepaid'],Azul,Branco,result['country']['name'],Azul,Branco,result['bank']['name'],Azul,Branco,result['bank']['phone'],Azul,Branco,result['bank']['city']);
		except Exception:
			msg='%s<%s BIN INVÁLIDA %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);

def cnpj():
	clear();
	try:
		result=requests('https://www.receitaws.com.br/v1/cnpj/%s'%input('%s %s> Digite o CPNJ que deseja buscar %s===>%s '%(logo,Branco,Azul,Verde)));
		try:
			msg=''
			for i in result:
				msg+='%s%s%s - %s'%(Azul,str(i.upper()),Branco,result[i])
			msg='\n%s'%msg
		except Exception:
			msg='%s<%s CNPJ NÃO ENCONTRADO %s>%s'%(Vermelho,Branco,Vermelho,Branco);
	except Exception:
		msg='%s<%s API OFFLINE OU SERVIDOR FORA DO AR %s>%s'%(Vermelho,Branco,Vermelho,Branco);

# Dict para guardar os valores de cada função
fun={1:bank,2:bin,3:cep,4:cnpj,5:covid,6:ddd,7:ip,8:cns,9:cpf,10:nome,11:placa}
sub_fun={99:update,00:sair}

# Menu
def main(user):
	while(Sair==False):
		clear();
		try:
			option=int(input(f'''%s%s<%s Seja Bem-Vindo, %s %s>%s
%s=============================%s
[%s1%s] Consulta Bancária    > ()
[%s2%s] Consulta de BIN      > ()
[%s3%s] Consulta de CEP      > ()
[%s4%s] Consulta de CNPJ     > ()
[%s5%s] Consulta de Covid-19 > ()
[%s6%s] Consulta de DDD      > ()
[%s7%s] Consulta de IP       > ()
[%s8%s] Consulta de CNS      > ()
[%s9%s] Consulta de CPF      > ()
[%s10%s] Consulta de Nome    > ()
[%s11%s] Consulta de Placa   > ()
%s=============================%s
[%s99%s] Atualizar           > ()
[%s00%s] Sair                > ()

%s>>>%s '''%(logo,Azul,Branco,user,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Verde,Branco,Vermelho,Branco,Azul,Verde)));
			try:
				retorno=str(fun[option]());
				clear();
				input(logo+retorno+'\n%s<%s APERTE ENTER PARA RETORNAR AO MENU %s>%s'%(Verde,Branco,Verde,Branco));
			except Exception:
				#print(e)
				try:
					sub_fun[option]();
				except:
					print('%s[%s X %s] Opção inválida.'%(Branco,Vermelho,Branco));sleep(3);
		except: print('%s[%s X %s] Caractére(s) não reconhecido(s).'%(Branco,Vermelho,Branco));sleep(3);
	clear();print(logo+'\n %s!%s Até breve. %s!%s'%(Verde,Branco,Verde,Branco))

if __name__=='__main__':
	if path.exists('login') == False:
		clear();
		senha=None;
		user=str(input(f'%s > %sDigite seu nome %s===>%s '%(logo,Branco,Azul,Verde)));
		while(senha not in ['KoRn']):
			clear();
			senha=str(input('%s > %sDigite seu nome %s===>%s %s\n%s > Digite a senha%s  ===>%s '%(logo,Branco,Azul,Verde,user,Branco,Azul,Verde)));
		with open('login','w+') as f:
			f.write(user);
	else:
		with open('login','r') as c:
			user=c.read();
	main(user);
