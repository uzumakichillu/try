#hello is folder (package) name inside which forms.py is present

from flask import render_template, url_for, flash, redirect, render_template_string
from project.forms import Edit,Delete
from project import app
from .makehtml import *
from .update_db import *
import pandas as pd
import numpy as np
import random,os



@app.route("/")
@app.route("/home")
def home():
    data=readData()
    print("data fetched")
    table=makeTable(data)    
    mapped_table,releases,ver_map=mapTable(table)
    ver_map=assignColorNumber(ver_map)
    colors=colorMap(ver_map)
    black_list=getBlackList(readBlackListDB())
    css=makeCSS(colors)
    html=makeHTMLtable(mapped_table,ver_map,black_list,css)
    print("webpage sent")    
    return render_template_string(html)



@app.route("/edit", methods=['GET', 'POST'])
def edit():
    print("edit attempt")
    form = Edit()        
    if form.validate_on_submit():
        data=readFlaskDB()
        block=form.information_block.data
        value=form.attribute.data   
        des=form.description.data     
        if form.access.data != '1234':
            flash('Wrong Access Code !!  Please retry', 'danger')
        elif check(block,value,data)== True:
            data=updateDescription(block,value,des,data)
            updateFlaskDB(data)
            flash(' Description Updated ! Please refresh the page.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Description not updated ( Invalid Information Block / Attribute ), Please retry ', 'danger')
    return render_template('edit.html', title='Edit', form=form)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    print("delete attempt")
    form = Delete()    
    if form.validate_on_submit():
        data=readFlaskDB()
        block=form.information_block.data
        value=form.attribute.data
        if form.access.data != '1234':
            flash('Wrong Access Code !!  Please retry', 'danger')
        elif check(block,value,data) == True:
            new_block,new_value=getBlockValue(block,value,data)
            blacklist_db = readBlackListDB()
            updateBlackListDB(blacklist_db,new_value)
            flash(' Attribute Removed ! Please refresh the page.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Attribute Not Deleted ( Invalid Information Block / Attribute ), Please retry ', 'danger')
    return render_template('delete.html', title='Delete', form=form)




