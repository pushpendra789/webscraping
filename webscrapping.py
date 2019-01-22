import urllib2
product = "https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=lapto&ignorear=0&N=-1&isNodeId=1"
page = urllib2.urlopen(product)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page,"html.parser")
containers = soup.findAll("div",{"class":"item-container"})
len=(containers)
containers[0].a
#store containers html in container
container = containers[0]
filename = "products.csv"

headers = "brand , product_name\n"
f.write(headers)
for container in containers:
	
	
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text
	
	images = container.findAll("a",{"class":"item-brand"})
	brand = images[0].img["title"]

	print("product_name:" + product_name)
	print("brand:" + brand)
	
	f.write(brand +"," +product_name.replace(",")+ "\n")

f.close()
