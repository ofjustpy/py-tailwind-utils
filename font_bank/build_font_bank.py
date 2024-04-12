
"""
create font bank from google webfont link
"""
import cssutils
import requests

parser = cssutils.CSSParser()
def get_font_face_srcs_weights(css_content):
    """
    from the download font css directive
    get font src url and height
    """
    print (css_content)
    font_info = {}
    sheet = parser.parseString(css_content)
    for rule in sheet:
        if rule.type == rule.FONT_FACE_RULE:
            src = rule.style['src'].replace("""format("woff2")""", "").replace("url(", "").replace(")", "").strip()
            weight = rule.style['font-weight'].strip()
            unicode_range = rule.style['unicode-range']
            font_info[f"{src}{weight}"] = [src, weight, unicode_range]


    return font_info

import hashlib

def generate_short_label(src_url, length=14):
    """
    Generate a unique short label from the src URL
    """
    # Hash the src URL using SHA-256
    hash_object = hashlib.sha256(src_url.encode())
    hash_hex = hash_object.hexdigest()
    
    # Truncate the hash to the specified length
    short_label = hash_hex[:length]
    
    return short_label

def download_font_face(src, label):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response_font = requests.get(src, headers=headers)
    if response_font.status_code == 200:

        with open(f"{label}.woff2", 'wb') as f:
            f.write(response_font.content)
            

                    
def create_css_directive(font_family, weight, unicode_range, file_label):
    css_x = f"""@font-face {{
            font-family: '{font_family}';
            src: url('/fonts/{label}.woff2') format('woff2');
            font-weight: {weight};
            font-style: normal;
            unicode-range: {unicode_range}
    }}"""
    
    return css_x
            
def get_content(font_family):
    query_phrase = f"family={font_family.replace(' ', '+')}&display=swap"
    api_url = f"https://fonts.googleapis.com/css2?{query_phrase}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        content = response.text
        return content
    
    assert False

fh = open("css_directive.css", "w")    
    
if __name__ == "__main__":
    font_family_list = ["Georgia",
             ]
    
    for font_family in font_family_list:
        content = get_content(font_family)
        if content:
            for k, v in get_font_face_srcs_weights(content).items():
                src, weight, unicode_range = v
                label = generate_short_label(src)
                download_font_face(src, label)
                fh.write(create_css_directive(font_family, weight, unicode_range, label))
                fh.write("\n")
                 
                


