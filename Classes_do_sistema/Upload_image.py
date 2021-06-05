from flask import Flask, request, send_from_directory, jsonify
import flask
from flask.wrappers import Response
import base64 as request
import datetime
from os.path import isfile, join
from mimetypes import MimeTypes, File
from os import listdir
from wand.image import Image
import wand.image
import hashlib
import json
import time
import hmac
import copy
import sys
import os
import wand.image

# Crie um diretório público na inicialização.
BASE_DIR = os.path.dirname (os.path.abspath (__file__))
publicDirectory = os.path.join (BASE_DIR, "public" )
if not os.path.exists (publicDirectory):
   os.makedirs (publicDirectory)

app = Flask (__name__, static_url_path = "" )

@ app.route ("/") 
def  get_main_html () : 
   return send_from_directory ( "./" , "index.html" )

@ app.route ("/ public / <path: path>") 
def  get_public (path) : 
   return send_from_directory ( "public /" , path)

@ app.route ("/ static / <path: path>") 
def  get_static (path) : 
   return send_from_directory ( "./" , path)

@ app.route ("/ upload_image", methods = ["POST"]) 
def  upload_image () : 
   try:
       response = Image.upload (FlaskAdapter (request), "/ public /" )
   except Exception:
       response = { "erro" : str (sys.exc_info () [ 1 ])}
   return json.dumps (response)

@ app.route ("/ upload_image_validation", methods = ["POST"]) 
def  upload_image_validetion () : 
   def  validetion(filePath, mimetype) : 
       with wand.image.Image (filename = filePath) as img:
            if img.width != img.height:
                return  False 
            return  True

   options = {
       "fieldname" : "myImage" ,
        "validation" : validetion
   }
   
   try:
       response = Image.upload (FlaskAdapter (request), "/ public /" , options)
   except Exception:
       response = { "erro" : str (sys.exc_info () [ 1 ])}
   return json.dumps (response)


class  Image(object):

   defaultUploadOptions = {
       "fieldname" : "arquivo" ,
        "validação" : {
            "allowedExts" : [ "gif" , "jpeg" , "jpg" , "png" , "svg" , "blob" ],
            "allowedMimeTypes" : [ "imagem / gif " , " imagem / jpeg " , " imagem / pjpeg " , " imagem / x-png " , " imagem / png " ,
                                 " imagem / svg + xml " ]
       },
       # string resize param de http://docs.wand-py.org/en/0.4.3/guide/resizecrop.html#transform-images 
       # Exemplos: "100x100", "100x100!". Encontre mais em http://www.imagemagick.org/script/command-line-processing.php#geometry 
       "resize" : None
   }

   @staticmethod 
   def  upload (req, fileRoute, options = None) : 
       """
       Carregamento de imagem para o disco.
       Parâmetros:
           req: adaptador de estrutura para solicitação http. Consulte BaseAdapter.
           fileRoute: string
           options: dict opcional, consulte o atributo defaultUploadOptions
       Retornar:
           dict: {link: "linkPath"}
       """

       if  options == None :
           options = Image.defaultUploadOptions
       else:
           options = Utils.merge_dicts (Image.defaultUploadOptions, options)
           return File.upload (req, fileRoute, options)

   @staticmethod 
   def  delete (src) : 
       """
       Exclua a imagem do disco.
       Parâmetros:
           src: string
       """ 
       return File.delete (src)

   @staticmethod 
   def  list (folderPath, thumbPath = None) : 
       """
       Lista as imagens do disco.
       Parâmetros:
           folderPath: string
           thumbPath: string
       Retornar:
           lista: lista de listas de imagens. exemplo: [{url: "url", polegar: "polegar", nome: "nome"}, ...]
       """

       if thumbPath == None :
           thumbPath = folderPath

       # Matriz de objetos de imagem a serem retornados.
       resposta = []

       absoluteFolderPath = Utils.getServerPath () + folderPath

       # Tipos de imagem. 
       imageTypes = Image.defaultUploadOptions [ "validetion" ] [ "allowedMimeTypes" ]

       # Nomes de arquivos na pasta de uploads. 
       fnames = [f for f in listdir (absoluteFolderPath) if isfile (join (absoluteFolderPath, f))]

       for fname in fnames:
           mime = MimeTypes ()
           mimeType = mime.guess_type (absoluteFolderPath + fname) [ 0 ]

           if mimeType in imageTypes:
               Response.append ({
                   "url" : folderPath + fname,
                    "thumb" : thumbPath + fname,
                    "name" : fname
               })

       return resposta


class  Utils (object) : 
   """
   Classe estática de utilitários.
   """

   @staticmethod 
   def  hmac (key, string, hex = False) : 
       """
       Calcule o hmac.
       Parâmetros:
           chave: string
           string: string
           hex: booleano opcional, retorna em hexadecimal, senão retorna em binário
       Retornar:
           string: hmax em hexadecimal ou binário
       """

       # python 2-3 compatível: 
       try:
          hmac256 = hmac.new (key.encode () if isinstance (key, str) else key, msg = string.encode ( "utf-8" ) if isinstance (string, str) else string, digestmod = hashlib.sha256) # v3 
       except Exception:
           hmac256 = hmac.new (key, msg = string, digestmod = hashlib.sha256) # v2
           return hmac256.hexdigest () if hex else hmac256.digest ()

   @staticmethod 
   def  merge_dicts (a, b, path = None) : 
       """
       Funda profundamente dois dicts sem modificá-los. Fonte: http://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge/7205107#7205107
       Parâmetros:
           a: dict
           b: dict
           caminho: lista
       Retornar:
           dict: dict mesclado profundamente.
       """

       aClone = copy.deepcopy (a);
       # Retorna profundamente b em a sem afetar as fontes. 
       if path ==  None : path = []
       for key in b:
            if key in a:
                if isinstance (a [key], dict) and isinstance (b [key], dict):
                   aClone [key] = Utils.merge_dicts (a [key], b [key], path + [str (key)])
                else:
                   aClone [key] = b [key]
            else:
               aClone [key] = b [key]
            return aClone

   @staticmethod 
   def  getExtension (filename) : 
       """
       Obtenha a extensão do nome do arquivo.
       Parâmetros:
           nome do arquivo: string
       Retornar:
           string: a extensão sem o ponto.
       """ 
       return os.path.splitext (filename) [ 1 ] [ 1 :]

   @staticmethod 
   def  getServerPath () : 
       """
       Obtenha o caminho onde o servidor foi iniciado.
       Retornar:
           string: serverPath
       """ 
       return os.path.abspath (os.path.dirname (sys.argv [ 0 ]))

   @staticmethod 
   def  isFileValid (filename, mimetype, allowedExts, allowedMimeTypes) : 
       """
       Teste se um arquivo é válido com base em sua extensão e tipo MIME.
       Parâmetros:
           string de nome de arquivo
           string mimeType
           lista de permissões permitidas
           lista allowedMimeTypes
       Retornar:
           boleano
       """

       # Ignore se as extensões ou tipos MIME permitidos estiverem ausentes. 
       if not allowedExts or  not allowedMimeTypes:
            return  False

       extension = Utils.getExtension (filename)
       return extension.lower () in allowedExts and mimetype in AllowedMimeTypes

   @staticmethod 
   def  isValid (validetion, filePath, mimetype) : 
       """
       Validação de arquivo genérico.
       Parâmetros:
           validação: dict ou função
           filePath: string
           mimetype: string
       """

       # Sem validação significa que você não deseja validar, portanto, retorne afirmativo. 
       if not validetion:
           return  True

       # A validação é uma função fornecida pelo usuário. 
       if callable(validetion):
            return validetion(filePath, mimetype)

       if isinstance (validetion, dict):
            return Utils.isFileValid (filePath, mimetype, validetion [ "allowedExts" ], validetion [ "allowedMimeTypes" ])

       # Caso contrário: nenhum comportamento de validação específico encontrado. 
       return false


class BaseAdapter(object) : 
   """
   Interface. Herde esta classe para usar a lib em sua estrutura.
   """

   def  __init__ (self, request) : 
       """
       Construtor.
       Parâmetros:
           request: objeto de solicitação http de algum framework.
       """
       self.request = request

   def  riseError (self) : 
       """
       Use-o quando quiser fazer um método abstrato.
       """ 
       raise NotImplementedError ( " Deveria ter implementado este método. " )

   def  getFilename (self, fieldname) : 
       """
       Obtenha o nome do arquivo de upload com base no nome do campo.
       Parâmetros:
           fieldname: string
       Retornar:
           string: nome do arquivo
       """
       self.riseError ()

   def  getMimetype (self, fieldname) : 
       """
       Obtenha o tipo MIME do arquivo de upload com base no nome do campo.
       Parâmetros:
           fieldname: string
       Retornar:
           string: mimetype
       """
       self.riseError ()

   def  saveFile (self, fieldname, fullNamePath) : 
       """
       Salve o arquivo de upload com base no fieldname no local fullNamePath.
       Parâmetros:
           fieldname: string
           fullNamePath: string
       """
       self.riseError ()


class FlaskAdapter (BaseAdapter) : 
   """
   Adaptador de frasco: Verifique BaseAdapter para ver a descrição de quais métodos.
   """

   def  checkFile (self, fieldname) : 
       if fieldname is not in [self.request.files]:
            raise Exception ( "Arquivo não existe." )

   def  getFilename (self, fieldname) :
       self.checkFile (fieldname)
       return self.request.files [fieldname] .filename

   def  getMimetype (self, fieldname) :
       self.checkFile (fieldname)
       return self.request.files [fieldname] .content_type

   def  saveFile (self, fieldname, fullNamePath) :
       self.checkFile (fieldname)
       file = self.request.files [fieldname]
       file.save (fullNamePath)

class Album(jsonify, datetime):
    def cadastro_album(self, id, title):
        flask
        album = Album 
        cadastro = flask.jsonify(id=str(album.id), title= album.title)
        return '{}'.format(cadastro)       

    def upload_momento(self,momento, fullNamePath):
      momento = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
      base = FlaskAdapter(BaseAdapter).saveFile(fullNamePath)
      return '{}:{}'.format(momento, base)

#https://froala.com/wysiwyg-editor/docs/server/flask/image-upload/