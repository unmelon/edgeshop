# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb
import urllib2
import os
import string

class EdgeshopPipeline(object):
    def process_item(self, item, spider):
        conector = MySQLdb.connect(host='localhost', user='melon',passwd='scraper', db='edgedb')
        cursor =  conector.cursor(MySQLdb.cursors.DictCursor)
        if (item.type == 'categoria'):
            query="select * from coleccion where id = "+item['ident']+";"
            cursor.execute(query)
            #El elemento no se encuentra en la base de datos
            if cursor.rowcount == 0:
                #guardamos la imagen del elemento
                query = "insert into coleccion (id, nombre,imagen) values ("+item['ident']+",\'"+item['nombre']+"\',\'"+item['imagen']+"\');"
                cursor.execute(query)
                conector.commit()
                #print "esta categoria no esta en la db"
            fname=str(item['ident'])+'.png'
            if not os.path.isfile(fname):
                if string.find(os.getcwd(),'itemimgs') != -1:
                    os.chdir('../..')
                if string.find(os.getcwd(),'categimgs') == -1:
                    os.chdir(os.getcwd()+"/res/categimgs")
                f = open(fname,'wb')
                contenido = urllib2.urlopen(item['imagen']).read()
                f.write(contenido)
                f.close()
        else:
            query="select * from item where nombre like \'"+item['nombre']+"\';"
            cursor.execute(query)
            #El elemento no se encuentra en la base de datos
            if cursor.rowcount == 0: 
                query = "insert into item (nombre,imagen,url,coleccion) values (\'"+item['nombre']+"\',\'"+item['imagen']+"\',\'"+item['url']+"\',"+str(item['coleccion'])+");"
                #query = "insert into item (id, nombre,imagen,coleccion) values ("+str(max_id)+",\'"+item['nombre']+"\',\'"+item['imagen']+"\',"+str(item['coleccion'])+");"
                cursor.execute(query)
                conector.commit()
            
            cursor.execute("select id from item where nombre like \'"+item['nombre']+"\';")
            res = cursor.fetchone()
            if string.find(os.getcwd(),'categimgs') != -1:
                os.chdir('../..')
            if string.find(os.getcwd(),'itemimgs') == -1:
                os.chdir(os.getcwd()+"/res/itemimgs")
            fname = str(res['id'])+'.jpg'
            if not os.path.isfile(fname):
                f = open(fname,'wb')
                contenido = urllib2.urlopen(item['imagen']).read()
                f.write(contenido)
                f.close()  
        cursor.close()
        conector.close()
        return item
