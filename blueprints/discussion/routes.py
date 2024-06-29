from flask import Blueprint, render_template 
from flask_login import login_required

discussions_blueprint = Blueprint('discussion', __name__)

@discussions_blueprint.route('/discussions') 
@login_required
def discussions():
    return render_template('discussions.html')
@discussions_blueprint.route('/create') 
@login_required
def create():
    return render_template('create_post.html')
