# -*- coding: utf-8 -*-
import os
from datetime import datetime
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlsplit

def clean_html(selector):
    # NOTE removing '\t\n' here will break <pre> content
    return ' '.join(
        s.strip()
        for s in selector.xpath('node()').getall()
        if s.strip()
    ) #.translate({ord(c): None for c in '\t\n'})

def drop_tree_css(selector, css):
    for sel in selector.css(css):
        sel.root.drop_tree()

def save_files(data, out_dir, date_time, type, name):
    if data:
        if not os.path.exists(f'{out_dir}/{date_time}_{name}'):
            os.makedirs(f'{out_dir}/{date_time}_{name}')
        if type == 'json':
            file_name = data['postid']+'.json'
            json_object = json.dumps(data, indent = 4)
            path = f'{out_dir}/{date_time}_{name}'
            if data['date']:
                sub_dir = data['date'].split('T')[0]
                if not os.path.exists(f'{path}/{sub_dir}'):
                    os.makedirs(f'{path}/{sub_dir}')
                    path = f'{path}/{sub_dir}'
                else:
                    path = f'{path}/{sub_dir}'
            with open(f'{path}/{file_name}', 'w') as f:
                f.write(json_object)
        else:
            file_name = f'{date_time}_{name}.jsonl'
            json_object = json.dumps(data)
            with open(f'{out_dir}/{date_time}_{name}/{file_name}', 'a') as f:
                f.write(json_object+'\n')


def remove_html_tags(html_string):
    # parse html content
    soup = BeautifulSoup(html_string, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    return ' '.join(soup.stripped_strings).strip()


def remove_tags(html_desc, hostname):
    # parse html content
    soup = BeautifulSoup(html_desc, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # Change URLs for images to absolute urls with respect to url of the page
    imgages = soup.find_all('img')
    for img in imgages:
        if not img.has_attr('src'):
            continue
        imgSrc = img['src']
        if imgSrc.startswith('../'):
            img['src'] = urljoin(hostname, imgSrc)
        elif imgSrc.startswith('/'):
            img['src'] = urljoin(hostname, imgSrc)
        else:
            print('unhandled url cleanup = ' + imgSrc)

    links = soup.find_all('a')
    for link in links:
        if link.has_attr('href') and not link['href'].strip() == '':
            if not link['href'].startswith('http'):
                link['href'] = "#"
            # elif link['href'].startswith('http://tpcg.io/'):
            #     link['href'] = "#"

    demo_view = soup.find("div", {"class": "demo-view"})
    if demo_view:
        demo_view.decompose()

    tutorial_menu = soup.find("div", {"class": "center-aligned tutorial-menu"})
    if tutorial_menu:
        tutorial_menu.decompose()

    bottom_navigation = soup.find("div", {"id": "bottom_navigation"})
    if bottom_navigation:
        bottom_navigation.decompose()

    top_navigation = soup.find("div", {"class": "mui-container-fluid button-borders"})
    if top_navigation:
        top_navigation.decompose()

    google_bottom_ads = soup.find("div", {"id": "google-bottom-ads"})
    if google_bottom_ads:
        google_bottom_ads.decompose()

    google_top_ads = soup.find("div", {"id": "google-top-ads"})
    if google_top_ads:
        google_top_ads.decompose()

    return soup.decode_contents(indent_level=2)

