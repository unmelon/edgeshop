#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys
import string
import MySQLdb
import webbrowser

class mi_event_box(Gtk.EventBox):
    def __init__(self,ident,categoria,url=""):
        super(Gtk.EventBox,self).__init__()
        self.categoria = categoria
        self.ident = ident
        self.url=url

class GUI:

        def __init__(self):
                os.system("scrapy crawl edgeshopspider")
                self.Conexion = MySQLdb.connect(host='localhost', user='melon',passwd='scraper', db='edgedb')
                self.micursor = self.Conexion.cursor(MySQLdb.cursors.DictCursor)

                # Creamos la interface manualmente para poder hacerla dinamica
                
                self.window = Gtk.Window()
                self.window.set_title("Edge Shop")
                self.window.connect('destroy', self.destroy)
                query = "select * from coleccion;"
                self.micursor.execute(query)
                result=self.micursor.fetchall()
                row_count = self.micursor.rowcount
                self.panel = Gtk.VBox(True,1)
                counter = 0
                for res in result:
                    if counter %2 ==0:
                        lpanel = Gtk.HBox(True,1)
                        img = Gtk.Image()                
                        if string.find(os.getcwd(),'itemimgs') != -1:
                            os.chdir('../..')
                        if string.find(os.getcwd(),'categimgs') == -1:
                            os.chdir(os.getcwd()+"/res/categimgs")
                        img.set_from_file(str(res['id'])+'.png')
                        event = mi_event_box(res['id'],res['nombre'])
                        event.add(img)
                        event.connect("button-press-event", self.on_button_clicked)
                        lpanel.pack_start(event, True, True, 1)
                    else:
                        img = Gtk.Image()                
                        if string.find(os.getcwd(),'itemimgs') != -1:
                            os.chdir('../..')
                        if string.find(os.getcwd(),'categimgs') == -1:
                            os.chdir(os.getcwd()+"/res/categimgs")
                        img.set_from_file(str(res['id'])+'.png')
                        event = mi_event_box(res['id'],res['nombre'])
                        event.add(img)
                        event.connect("button-press-event", self.on_button_clicked)
                        lpanel.pack_start(event, True, True, 1)
                        self.panel.pack_start(lpanel, True, True, 1)
                    counter += 1
                    #button = Gtk.Button(label=res['nombre'])
                    #button.connect("clicked", self.on_button_clicked)
                    #self.panel.pack_start(button, True, True, 1)
                self.window.add(self.panel)
                self.window.show_all()
                #self.update_last()

        def destroy(self,window):
            Gtk.main_quit()       
        def close(self,window):
            self.window.show_all()
            window.destroy()
        
        #abrimos la url del elemento seleccionado
        def on_item_clicked(self, widget,position):
            webbrowser.open(widget.url)
        
        
        #"boton" de la categoria, para mostrar los elementos
        #de dicha categoria
        def on_button_clicked(self, widget,position):
            print "Hola Mundo"
            print widget.categoria
            print widget.ident
            self.window.hide()
            window2 = Gtk.Window()
            window2.set_title("Edge Shop")
            window2.connect('destroy', self.close)
            query = "select * from item where coleccion ="+str(widget.ident)+";"
            self.micursor.execute(query)
            result=self.micursor.fetchall()
            row_count = self.micursor.rowcount
            self.panel2 = Gtk.VBox(True,1)
            counter = 0
            print result
            for res in result:
                if counter %6 ==0:
                    lpanel = Gtk.HBox(True,1)
                    img = Gtk.Image()                
                    if string.find(os.getcwd(),'categimgs') != -1:
                        os.chdir('../..')
                    if string.find(os.getcwd(),'itemimgs') == -1:
                        os.chdir(os.getcwd()+"/res/itemimgs")
                    img.set_from_file(str(res['id'])+'.jpg')
                    event = mi_event_box(res['id'],res['nombre'],res['url'])
                    event.add(img)      
                    event.connect("button-press-event", self.on_item_clicked)
                    lpanel.pack_start(event, True, True, 2)
                    if row_count == 1:
                        self.panel2.pack_start(lpanel,True,True,2)
                        break
                else:
                    img = Gtk.Image()                
                    if string.find(os.getcwd(),'categimgs') != -1:
                        os.chdir('../..')
                    if string.find(os.getcwd(),'itemimgs') == -1:
                        os.chdir(os.getcwd()+"/res/itemimgs")
                    img.set_from_file(str(res['id'])+'.jpg')
                    event = mi_event_box(res['id'],res['nombre'],res['url'])
                    event.add(img)
                    event.connect("button-press-event", self.on_item_clicked)
                    lpanel.pack_start(event, True, True, 2)
                    self.panel2.pack_start(lpanel, True, True, 2)
                counter += 1

            window2.add(self.panel2)
            window2.show_all()


def main():
        app = GUI()
        Gtk.main()

if __name__ == "__main__":
    sys.exit(main())

    
