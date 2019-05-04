import time
from selenium import webdriver
from bs4 import BeautifulSoup
import shutil
import urllib.request


driver = webdriver.Chrome('/home/abc/Documents/python/nonnnnnnnnnnaaaaaaaaaaaaaa/chromedriver')  # Optional argument, if not specified will search path.
user_input=input("Enter your requirement")
formatted_input=user_input.replace(" ","+")
url="https://www.google.com/search?hl=en&biw=1301&bih=672&tbm=isch&sa=1&ei=lz3NXM26EZez9QPkyr_oDw&q="+formatted_input+"&oq="+formatted_input+"&gs_l=img.3...0.0..32979...0.0..0.0.0.......1......gws-wiz-img.NpdwxcBJ7LA"+""
driver.get(url);
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(2)
	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:

		break
	last_height = new_height
html_data=driver.page_source
image_src_list=[]
soup = BeautifulSoup(html_data,'html.parser')
image_list=soup.findAll("img", {"class": "rg_ic"})
for image_src in image_list:
    #print image source
    image_src_list.append(image_src.get('src'))
dirname="/image"
suffix=".jpg"
count=0
for src in image_src_list:
	
	if str(src).startswith('data:image/'):
		print(' yes in starts with')
		continue
	else:
		if src:
			print(' nope  ')
			print(src)
			urllib.request.urlretrieve(src, '/home/abc/Documents/python/nonnnnnnnnnnaaaaaaaaaaaaaa/image/'+str(count)+'.jpg')

	count=count+1
driver.quit()


	# with open(dirname+'/img_'+suffix.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
	# 	shutil.copyfileobj(src, out_file)


        





# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
