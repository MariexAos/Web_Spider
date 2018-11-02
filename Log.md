# Log
* 9/30/2018 
```

#init scrapy anaconda
conda commands:
    conda -n env_name python = version
    conda install package_name
    conda remove package_name
    conda env list
    conda conda env export > environment.yaml 
scrapy commands:
    scrapy startproject project_name
    scrapy crawl spider_name
for more commands use "man conda/scrapy"

```
* 10/05/2018
```
#create scrapy crawlers
#refactor the demo
made the first baidu spider
```
* 10/12/2018

```
class.Spider.Spiders
    #custom_settings 
        [Built-in settings reference](https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref)
        Depth_priority
            LIFO queue
                DFO order
                how to crawl in true BFO order?
                    DEPTH_PRIORITY = 1
                    SCHEDULE_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
                    SCHEDULE_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
    #scrapy shell "url"
        response.css('div').extract()
        response.css('div')
        response.css('div::text').extract()
        
        
    

```
* 10/19/2018
```

```
* 10/26/2018
```

```
* 11/02/2018