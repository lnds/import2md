import argparse
import urllib.request
import urllib.parse
import html2text
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("md_name")
parser.add_argument("output_dir")
args = parser.parse_args()


with urllib.request.urlopen(args.url) as response:
    content = response.read()
    charset = response.headers.get_content_charset()
    html = content.decode(charset)

    converter = html2text.HTML2Text()
    text = converter.handle(html)

    url_parts = urllib.parse.urlparse(args.url)
    name = args.md_name + '.md'
    os.makedirs(args.output_dir, exist_ok=True)

    md_output = os.path.join(args.output_dir, name)
    with open(md_output, 'w', encoding=charset) as md:
        md.write(text)

