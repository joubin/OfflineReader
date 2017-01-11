from GenPDF import PDFGenerator
from RedditConnector import RedditConnection 

if __name__ == '__main__':
    # p = PDFGenerator()
    # # p.generatePDF("http://joubin.me")
    tag="/u/sastdast"
    client_id = 'K_KAJrOQQxACQw'
    client_secret='C7lVPFLHCgHKZdc2SM0DsiAeQvQ'
    username = "sastdast"
    password = "dastsast"
    redirect_uri = "http://joubin.me/"
    r = RedditConnection(tag, client_id, client_secret, redirect_uri, username, password);
    r.get_posts_from_sub("programming", save_to_pdf=True, limit=10)
    # r.getNPostsFromSub("netsec", 3)
    # p = PDFGenerator()
    # p.generateIterator(r.getNPostsFromSub("netsec"))

