# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self,x):  
        x = 9 if x == None else int(x)
        y = int(self.get_argument('n',10))
        if 0<y<10:
            x = y
        
        #html部分
        html = '''
        <html>
        <body>
        <table>
        '''
        
        #乘法表
        while(x != 0):
            html += '<TR>'
            for y in range(1,x+1): 
                html += '<TD>'f'{y}*{x}={x*y}\t''</TD>'
                print() 
            x -= 1
            html += '<TR>'

        html += '''
        </html>
        </body>
        </table>
        '''
        self.write(html)



application = tornado.web.Application([
    (r"/(?:/([0-9]+))?", MainHandler),
    ],debug  = True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()





 







 
