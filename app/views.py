"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from app import db
from app import forms
from app.models import Property
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kayla Blake 620096888")

@app.route('/uploads/<filename>') 
def get_Image(filename):
    rootdir = os.getcwd()
    return send_from_directory(rootdir+"/"+app.config['UPLOAD_FOLDER'],filename)

@app.route('/images/<filename>')
def get_Icon(filename):
    rootdir = os.getcwd()
    return send_from_directory(rootdir+"/"+app.config['ICON_FOLDER'],filename)

@app.route('/property', methods=['POST','GET'])
def new_property():
    form = forms.PropertyForm()
    if request.method == 'POST':
        # Validate form on submit
        if form.validate_on_submit():
            photoData = form.photo.data
            photo = secure_filename(photoData.filename)

            prop = Property(title = form.title.data, description = form.description.data, rooms = form.rooms.data, bath = form.bath.data, price = form.price.data, propType = form.propType.data, location = form.location.data, photo = photo)
            db.session.add(prop)
            db.session.commit()
            #save property photo to folder
            photoData.save(os.path.join(app.config['UPLOAD_FOLDER'],photo))
            
            flash('File Saved', 'success')
            return redirect(url_for('properties'))

    return render_template('new_property.html',form = form)

@app.route('/properties')
def properties():
    prop = Property.query.all()
    return render_template('properties.html',prop = prop)

@app.route('/property/<propertyid>', methods=['POST','GET'])
def view_property(propertyid):
    if request.method == 'POST':
       #form = view_form.ViewForm()
       prop = Property.query.get(propertyid)
       return render_template('view_property.html',prop = prop)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
