import requests
import web
# '/(.*)', 'hello
	
urls = (
   '/', 'index',
   '/ct.css', 'ct',
   '/forums', 'forums',
   '/forum', 'forum',
)
app = web.application(urls, globals())

	

class index:        
    def GET(self):
        try:
            f = open('test.html', 'r')
            return f.read()
        except:
            return ''
class ct:        
    def GET(self):
        try:
            f = open('ct.css', 'r')
            return f.read()
        except:
            return '' 

class forums:        
	def GET(self):
		r = requests.put("http://0.0.0.0:9090/api/v2/forums")
		return r.text

class forum:        
	def GET(self):
		i = web.input()
		print i
		r = requests.put("http://0.0.0.0:9090/api/v2/forums/"+i['fid'])
		return r.text
		

if __name__ == "__main__":
    app.run()