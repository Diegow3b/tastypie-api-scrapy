# Basic Api Integration with Web Scrapping using Tastypie and Scrapy

### External Dependency
Virtualenv (This is default instaled with Ubuntu)                      

### Installation
#### 1 - Clone the project to your folder and enter on it
```sh
$ git clone 
```
#### 2 - Create and activate virtualenv to host your packages and external dependencies
```sh
$ virtualenv vm-scrapy-api
$ source vm-scrapy-api/bin/activate
```
#### 3 - Install the requirements (Will install django and other internal dependencies)
Obs.: Enter in project folder
```sh
$ cd scrapy-api 
$ pip install -r requirements.txt
```
#### 4 - Run the server
```sh
$ fab runserver
```
#### 5 - Access the API
Endpoints:
In your brower, curl or postman (nice one to make testes)
GET (**Unimplemented yet**)
Will show you all spiders you sent to crawl
http://localhost:8000/requisicao/api/v1/requisicao/

POST
Send the spider to specific url to count how many words this page have
and returns a json with the name you choose or a default one, that shows
you the count, urls you have accessed, the name of the file and the date
http://localhost:8000/requisicao/api/v1/requisicao/crawler/
```json
{
	"key": "diego",
	"url": "https://github.com/Diegow3b",
	"json": "word_count.json"
}
```
Parameters:
- key: The word you want count
- url: The page url you want to crawl
- json: Optional - The json file you want to write, if you not choose one
this will be created as 'crawler_palavras.json' in the root folder
Obs.: Since this crawl the source code and not the "view page" you must count
the source code instead how many times you seeing the name in reagular page

## Extra
Sedding Spiders in command line
```shell
$ scrapy crawl letras_spider -o nameofjsonfile.json -t json -a url=www.urltocrawl.com -a key=wordyouwantcount -a json=nameofjsonfile.json
```

## Further help
To get more help ask me my github or email.