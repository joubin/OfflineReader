import html2text
import os

from markdown2 import markdown
from praw.models import Submission
from requests import HTTPError
import pdfkit


def slugify(value: str):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    return " ".join(x for x in value if x.isalnum())


class PDFGenerator:
    class __PDFGenerator:

        def __init__(self):
            import os
            self.path = "pdf"
            self.options = {
                'page-size': 'Letter',
                'minimum-font-size': '18',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'no-outline': None,
                'quiet': ''
            }
            if not os.path.exists(self.path):
                os.makedirs(self.path)

        def generate_pdf(self, submission: Submission) -> None:
            from urllib import request

            if "//reddit.com" in submission.url:
                return

            with request.urlopen(submission.url) as response:
                try:
                    html = response.read()
                except HTTPError:
                    return

            base_path = slugify(submission.title)
            # text = html2text.html2text(html)
            # md = os.path.join(self.path, base_path + ".md")
            pdf = os.path.join(self.path, base_path + '.pdf')
            pdfkit.from_url(submission.url, pdf)

        def generate_from_text(self, url: str, file: str):
            from urllib import request
            h = html2text.HTML2Text()
            h.ignore_links = True

            with request.urlopen(url) as response:
                try:

                    content = response.read()
                    charset = response.headers.get_content_charset()
                    if charset is None:
                        charset = "utf-8"
                    html = content.decode(charset)
                    # html = response.read()
                except HTTPError:
                    return

            text = h.handle(html)
            print(text)
            md = markdown(text)
            with open(file, "w+") as file:
                file.write(md)

            # pdfkit.from_string(md, file)


    instance = None

    def __init__(self):
        if not PDFGenerator.instance:
            PDFGenerator.instance = PDFGenerator.__PDFGenerator()
        else:
            pass

if __name__ == '__main__':
    PDFGenerator()
    site = "http://www.darknet.org.uk/2017/01/exitmap-tor-exit-relay-scanner/"
    PDFGenerator.instance.generate_from_text(site, "test.html")

