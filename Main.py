from GenPDF import PDFGenerator
from RedditConnector import RedditConnection 
from test import MyClass

if __name__ == '__main__':
    # p = PDFGenerator()
    # # p.generatePDF("http://joubin.me")
    tag="/u/username"
    client_id = 'client_id'
    client_secret='client_secret'
    username = "username"
    password = "password"
    redirect_uri = "http://joubin.me/"
    r = RedditConnection(tag, client_id, client_secret, redirect_uri, username, password);
    
    p = PDFGenerator()
    p.generateIterator(r.getNPostsFromSub("programming"))

