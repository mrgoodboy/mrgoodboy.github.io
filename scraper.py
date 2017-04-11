from selenium import webdriver
from bs4 import BeautifulSoup
import csv, time
from selenium.webdriver.support.ui import Select

def search(brand):
    browser.find_element_by_id('frm-sizeChartSearchForm-keyword').send_keys(brand)
    browser.find_element_by_css_selector("input.btn-primary").click()

def check():
    html_source = browser.page_source
    soup = BeautifulSoup(html_source)
    if len(soup.find_all('td', class_="no-items")) != 0:
        return False

def input_gender(gender):
    select = Select(browser.find_element_by_id('frm-sizeChartsGrid-form-filters-gender'))
    if gender == 1: #women
        select.select_by_value('1')
    else:
        select.select_by_value('2')
    browser.find_element_by_css_selector('input.btn-do-filter').click()

def add_brands():
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    num_tables = len(soup.find_all('td', class_='row-actions'))
    num_tables = min(10, num_tables)
    for x in range(num_tables):
        time.sleep(2)
        add = browser.find_element_by_class_name("sb-c-green")
        add.click()
    return num_tables

def go_to_dashboard():
    # browser.find_element_by_xpath("(//div[@class='sb-menu-text'])[position()=2]").click()
    browser.find_element_by_xpath("(//a[@class='sb-sub-item'])").click()

def go_to_info():
    browser.find_element_by_class_name("sb-if-eye").click()

def clothing_info():
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    info_table = soup.find('table', class_='sb-general-info')
    table_body = info_table.find('tbody')
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    print(data)

def size_info():
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    info_table = soup.find('table', class_='sb-sizes')
    table_header = info_table.find('thead')
    header = []
    rows = table_header.find_all('th')
    for row in rows:
        header.append(row.text.strip())

    table_body = info_table.find('tbody')
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip().replace('\n', "") for ele in cols]
        data.append([ele for ele in cols if ele])
    data = [header] + data
    print(data)

def remove():
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    num_tables = len(soup.find_all('td', class_='row-actions'))
    if num_tables > 0:
        # time.sleep(2)
        remove = browser.find_element_by_class_name("sb-c-red")
        remove.click()

def go_to_search():
    browser.find_element_by_xpath("(//a[@class='sb-sub-item'])").click()

def scrape_brand(brand, gender):
    go_to_search()
    search(brand)
    input_gender(gender)
    num_tables = add_brands()
    go_to_dashboard()
    for x in range(num_tables):
        go_to_info()
        clothing_info()
        size_info()
        time.sleep(2)
        browser.find_element_by_xpath("(//a[@class='sb-sub-item'])").click()
        browser.find_element_by_xpath("(//a[@class='sb-sub-item'])").click()
        remove()
        time.sleep(2)

brands = ['Dakine', 'Columbia', 'Reebok', 'Lee Cooper', 'Forever 21', 'Napapijri', 'etnies', 'Diesel', 'Merell', 'GAP', 'New Balance', 'G-star', 'Saucony', 'Lacoste', 'Salomon', 'Asos', 'Peak Performance', 'Burton', 'Aldo', 'Puma', 'Helly Hansen', 'Roxy', 'Jack Wolfskin', 'Timeout', 'Ripzone', 'Hunter', 'Represent Clothing', 'Meatfly', 'Tatuum', 'Supra', 'Bench', 'Fred Perry', 'Pepe Jeans', 'PULL&BEAR', 'Botas', 'Under Armour', 'Carhartt', 'Calvin Klein', 'Bushman', 'ESPRIT', 'Replay', 'Timezone', 'Lee', 'Timberland', 'Marks & Spencer','Converse', 'Vans', 'VERO MODA', 'Onitsuka Tiger', 'Orsay','Lindex', 'Oakley', 'Sorel', 'Guess', 'Mango', 'Stradivarius', 'Gant', 'Fox']
# brands2 = ['Quiksilver', 'Thomas Pink', 'Addicted', 'Marmot', 'Tally Weijl', 'Camaieu', 'Superdry', 'Zara', 'Alpha industries', 'Electric', 'Dockers', 'Camaïeu', 'Tommy Hilfiger', 'Hurley', "S'Oliver", 'Mizuno', 'Lakai', 'Geox', 'American Eagle','Toms', 'Forever 21 - Plus', 'H&M','Alpine Pro', 'Patagonia', 'Nike', 'Volcom', 'Wrangler', "Church's",  'Abercrombie & Fitch', 'Circa', 'Forever 21 - Contemporary', 'Element', 'Levis', 'Next', "Clark's", "Victoria's Secret", "Arc'teryx", 'Canada Goose', 'Crocs', 'Salming', 'Ecco',  'Nautica', 'Asics', 'Horsefeathers', 'Fila', 'Red Wing Shoes', 'F&F', "O'Neill", 'Billabong', 'Ripcurl', 'Adidas', 'Bershka',  'Hollister', 'Keds', 'Air Jordan', 'The North Face','Mustang', 'Fjällräven']

# path_to_chromedriver = '/Users/christopherwan/Downloads/chromedriver' # change path as needed
# browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser = webdriver.PhantomJS()
browser.set_window_size(1680, 1050)

url = 'https://sizeid.com/en/business.business/'
browser.get(url)
browser.find_element_by_class_name('login').click()
browser.find_element_by_id('frm-signInForm-username').send_keys('blake1')
browser.find_element_by_id('frm-signInForm-password').send_keys('helloworld')
browser.find_element_by_css_selector("input.btn-primary").click()
browser.find_element_by_xpath("(//div[@class='sb-menu-text'])[position()=2]").click()
time.sleep(2)
browser.find_element_by_xpath("(//a[@class='sb-sub-item'])").click()
for b in brands:
    print("NOW SEARCHING {}".format(b))
    scrape_brand(b, 1)
    scrape_brand(b, 2)