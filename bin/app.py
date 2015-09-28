#!/usr/bin/python2.7
### Port to Django
### Iteration: 0.1

import web,site

site.addsitedir("/home/tk/pprojects/save/manuscript/")
import manuscript_analyze


urls = (
"/manuscripter", "MANU"
)

render = web.template.render(
	"/home/tk/pprojects/save/manuscript/bin/templates"
	) ### Directory to HTML templates.  Change based on frame.

class MANU(object):
	
	def GET(self):
		
		M = manuscript_analyze.ManuscriptAnalyzer()
		
		content = """
		<h1 style = "font-size: 60px;">
		Manuscript Analyzer
		</h1>
		
		
		Connected to Frame.
		
		
		"""
		return render.index(content = content)
		
	def POST(self):
		pass  

application = web.application(urls, globals())

if __name__ == "__main__":
	application.run()
