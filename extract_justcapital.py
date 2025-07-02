from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd



# utilizando google chrome para extração
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



def extrair_valores(url):
    '''Extrai os indicadores de desempenho de uma empresa a partir de sua página no site Just Capital.

    A função acessa a página da empresa informada por meio da URL, utilizando Selenium, e coleta os valores das três métricas:
    - industry_average
    - industry_best
    - overall_best
    
    Essas métricas são extraídas para cinco categorias de avaliação:
    - Workers
    - Customers
    - Shareholders & Governance
    - Communities
    - Environment

    Retorna um DataFrame contendo o nome da empresa e os respectivos indicadores coletados.

    Parâmetros:
    ----------
    url : str
        URL da página da empresa no site Just Capital.

    Retorna:
    -------
    pandas.DataFrame
        Um DataFrame com uma linha contendo o nome da empresa e os valores das métricas para cada categoria.
        '''

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    import pandas as pd
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get(url)

    nome_empresa_url = driver.find_element(By.CLASS_NAME, 'company-header__info')
    nome_empresa = nome_empresa_url.find_element(By.TAG_NAME,'h1').text

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "industry-average.chart-marker.visible")))
    
    categoria_workers = driver.find_element(By.CSS_SELECTOR, 'li[data-name="Workers"]')
    workers_industry_average = categoria_workers.find_element(By.CLASS_NAME, 'industry-average.chart-marker.visible').get_attribute('innerText')
    workers_industry_best = categoria_workers.find_element(By.CLASS_NAME,'industry-max.chart-marker.visible').get_attribute('innerText')
    workers_overall_best = categoria_workers.find_element(By.CLASS_NAME,'overall-max.chart-marker.visible').get_attribute('innerText')
    
    categoria_customers = driver.find_element(By.CSS_SELECTOR, 'li[data-name="Customers"]')
    customers_industry_average = categoria_customers.find_element(By.CLASS_NAME, 'industry-average.chart-marker.visible').get_attribute('innerText')
    customers_industry_best = categoria_customers.find_element(By.CLASS_NAME,'industry-max.chart-marker.visible').get_attribute('innerText')
    customers_overall_best = categoria_customers.find_element(By.CLASS_NAME,'overall-max.chart-marker.visible').get_attribute('innerText')

    categoria_ShareholderseGovernance = driver.find_element(By.CSS_SELECTOR, 'li[data-name="Shareholders & Governance"]')
    ShareholderseGovernance_industry_average = categoria_ShareholderseGovernance.find_element(By.CLASS_NAME, 'industry-average.chart-marker.visible').get_attribute('innerText')
    ShareholderseGovernance_industry_best = categoria_ShareholderseGovernance.find_element(By.CLASS_NAME,'industry-max.chart-marker.visible').get_attribute('innerText')
    ShareholderseGovernance_overall_best = categoria_ShareholderseGovernance.find_element(By.CLASS_NAME,'overall-max.chart-marker.visible').get_attribute('innerText')
    
    categoria_communities = driver.find_element(By.CSS_SELECTOR, 'li[data-name="Communities"]')
    communities_industry_average = categoria_communities.find_element(By.CLASS_NAME, 'industry-average.chart-marker.visible').get_attribute('innerText')
    communities_industry_best = categoria_communities.find_element(By.CLASS_NAME,'industry-max.chart-marker.visible').get_attribute('innerText')
    communities_overall_best = categoria_communities.find_element(By.CLASS_NAME,'overall-max.chart-marker.visible').get_attribute('innerText')

    categoria_environment = driver.find_element(By.CSS_SELECTOR, 'li[data-name="Environment"]')
    environment_industry_average = categoria_environment.find_element(By.CLASS_NAME, 'industry-average.chart-marker.visible').get_attribute('innerText')
    environment_industry_best = categoria_environment.find_element(By.CLASS_NAME,'industry-max.chart-marker.visible').get_attribute('innerText')
    environment_overall_best = categoria_environment.find_element(By.CLASS_NAME,'overall-max.chart-marker.visible').get_attribute('innerText')
 

    df = pd.DataFrame([{'nome_empresa':nome_empresa, 
                       'workers_industry_average': workers_industry_average, 'workers_industry_best': workers_industry_best, 
                       'workers_overall_best': workers_overall_best, 'customers_industry_average': customers_industry_average, 
                       'customers_industry_best': customers_industry_best, 'customers_overall_best': customers_overall_best, 
                       'ShareholderseGovernance_industry_average': ShareholderseGovernance_industry_average, 
                       'ShareholderseGovernance_industry_best': ShareholderseGovernance_industry_best,
                       'ShareholderseGovernance_overall_best': ShareholderseGovernance_overall_best,
                       'communities_industry_average': communities_industry_average, 'communities_industry_best': communities_industry_best,
                       'communities_overall_best': communities_overall_best, 'environment_industry_average': environment_industry_average,
                       'environment_industry_best': environment_industry_best, 'environment_overall_best': environment_overall_best                    
    }])

    driver.close()

    return df



def extrair_empresas():
    '''
    Extrai os links das páginas individuais das empresas presentes no ranking da Just Capital.

    A função utiliza Selenium para abrir a página de ranking das 100 maiores empresas no site 
    https://justcapital.com/rankings/. Ela aguarda o carregamento completo da lista de empresas,
    localiza os elementos de cada empresa e extrai os links (href) correspondentes. 
    Esses links são armazenados em uma lista que é retornada ao final da execução.

    Returns:
        list: Uma lista de strings contendo as URLs das páginas individuais das empresas.

    Observações:
        - É necessário que o Google Chrome esteja instalado na máquina.
        - O ChromeDriver é gerenciado automaticamente via webdriver_manager.
        - A função abre e fecha automaticamente o navegador durante sua execução.
    '''

    
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager

    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://justcapital.com/rankings/')

    
    # Aguarda até que o elemento com ID 'rankings' esteja presente (tempo máximo de 10 segundos)
    wait = WebDriverWait(driver, 10)
    ranking = wait.until(EC.presence_of_element_located((By.ID, 'rankings')))

    # Aguarda os <li> dentro do ranking estarem presentes
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'li')))
    lista_ranking = ranking.find_elements(By.TAG_NAME, 'li')

    lista_empresas = []

    for url in lista_ranking:
        try:
            link = url.find_element(By.TAG_NAME, 'a').get_attribute('href')
            lista_empresas.append(link)
        except:
            continue  # Pula se não encontrar link

    driver.quit()
    return lista_empresas  
    
    
    
def main():
    
    
    # chamando a função para capturar a lista das 100 empresas
    lista_empresas = extrair_empresas()
    
   
    # aplicando um loop for na lista de urls, utilizando a função extrair_valores 

    df = pd.DataFrame()  # foi utilizado pandas para salvar o DataFrame de resultado

    for empresa in lista_empresas:
        try:
            dados = extrair_valores(empresa)
            df = pd.concat([dados, df])
        
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")
         
         
    # ordenando o df corretamente, pois a extração considerou a ordem decrescente (100º para 1º)

    df_ordenado = df.iloc[::-1].reset_index(drop=True)
    
    
    
    # salvando o df final em formato csv
    
    try:
        df_ordenado.to_csv('ranking_justcapital.csv', index=False)
        
    except Exception as e:
        print(f"Erro ao processar: {e}")
        



if __name__ == '__main__':

    main()