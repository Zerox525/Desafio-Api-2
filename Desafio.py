#inicio do projeto#
# 1- coleta dos dados da api - ok #
# 2- formatar com o panda - ok #
# 3- criar gráfico - ok #
from pycoingecko import CoinGeckoAPI 
import pandas
import plotly.express as px




print("programa iniciado")

cg = CoinGeckoAPI()

#salvando dados da Api a coleta de dados#
dados= cg.get_price(ids='bitcoin,litecoin,ethereum,solana,cardano', vs_currencies=['usd','eur'])
dados2= cg.get_price(ids='bitcoin,litecoin,ethereum,solana,cardano', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)


#mostrando dados coletadas na api#
print(dados)
print(dados2)



#tratando dados com o panda, usando o dataframe#
criptoMoedas=pandas.DataFrame(dados)
criptoMoedas2=pandas.DataFrame(dados2)



#exibindo dados tratados com o panda#
print(criptoMoedas)
print(criptoMoedas2)



#montando o gráfico#
fig = px.line(criptoMoedas)
fig.write_html('first_figure.html', auto_open=True)
fig = px.line(criptoMoedas2)
fig.write_html('first_figure.html', auto_open=True)
# finalizando o programa
# criar um segundo gráfico para finalizar o projeto#

