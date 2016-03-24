# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:20:21 2016

@author: nandu
"""

import random
import csv

#items = ['Makita Power Drill', 'Swiss Army Knife', 'Tekton Hex Key Set', 'GearWrench Hook&Pick Set', 'Dewalt Reciprocating Saw', 'Dewalt Table Saw', 'Louisville Baseball Bat', 'Dewalt Drillbit Set', 'Philips LED Bulb', 'Black&Decker Cutting Blade']

items = ['Nikon DSLR Camera', 'Samsung HDMI Cable', 'Philips Torchlight', 'JBL Bluetooth Speaker', 'Primos Tripod', 'Transcend SD Card', 'Dynex Portable Charger', 'Apple iPod', 'Boxware Stylus', 'Android SmartPhone']

items = ['Gillette Shaving Razor', 'Nivea Shaving Cream', 'Gillette Razor Blades', 'Nivea Body Wash', 'Dove Shampoo', 'Oral-B Electric Toothbrush', 'Pepsodent Toothpaste', 'Versace Cologne', 'Listerine Mouthwash', 'Oral-B Dental Floss']

items = ['Canon Inkjet Printer', 'Canon Printer Ink', 'Hammermill Copy Paper', 'PaperMate Ballpoint Pen Set', 'Post-It Notes', 'Mead Composition Notebook', 'Epson Projector', 'IKEA Corner Desk', 'Philips Desk Lamp', 'Sharpie Marker Set']

items = ['Arnold Wheat Bread', 'Kraft Cheese Slice', 'Jif Peanut Butter', 'Eggland Large Eggs', 'White Onion Large', 'Greenhouse Tomatoes', 'Kitchen Knife', 'McCormick Garlic Powder', 'McCormick Black Peppercorn', 'Winco Cutting Board']

items = ['AmazonBasics Backpack', 'AmazonBasics Laptop Sleeve', 'Logitech Wireless Mouse', 'Belkin Mouse Pad', 'Logitech Wireless Keyboard', 'AmazonBasics HDMItoDVI Adapter', 'Acer LED Monitor', 'Corsair CPU Case', 'CoolerMaster CPU Cooler', 'Intel Core i5']

transactions = list()

for i in range(0, 20):
    x = random.randint(4, 8)
    random_items = random.sample(items, x)
    transactions.append(random_items)
    
with open('amazonbasics.csv', 'w') as myfile:
    writer = csv.writer(myfile, lineterminator = '\n')
    for value in transactions:
        writer.writerow(value)
        
