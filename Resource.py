class Resource():
	def __init__(self,url,title,content,size):
		self.__url = url
		self.__title = title
		self.__content = content
		self.__size = "1"

	def getUrl(self):
		return self.__url
	def setUrl(self,url):
		self.__url = url
	def getTitle(self):
		return self.__title
	def setTitle(self,title):
		self.__title = title
	def getContent(self):
		return self.__content
	def setContent(self,content):
		self.__content = content
	def getSize(self):
		return self.__size
	def setSize(self,size):
		self.__size = size
	def toJsonStr(self):
		json = "{"
		imgSrc = "\"imgSrc\":\""+self.__url+"\","
		title = "\"title\":\""+self.__title+"\","
		content = "\"content\":\""+self.__content+"\","
		size = "\"size\":\""+self.__size+"\"}"
		return json+imgSrc+title+content+size





