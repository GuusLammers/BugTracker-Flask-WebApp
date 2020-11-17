from flask import Blueprint, render_template, url_for, request, redirect
from .models import User, Project, Ticket
from . import db
from flask_login import login_required, current_user
from datetime import datetime

main = Blueprint('main', __name__)


# index page
@main.route('/')
def index():
    return render_template('index.html')


# profile pages
@main.route('/profile')
@login_required
def profile():
    # query database for all active and complete projects
    projects_active = Project.query.filter_by(owner_id=current_user.id, state='Active').order_by(Project.due_date).all()
    projects_complete = Project.query.filter_by(owner_id=current_user.id, state='Complete').order_by(Project.due_date).all()

    tickets_open = []
    tickets_closed = []
    # search through active projects and sort tickets by state
    for project in projects_active:
        tickets = Ticket.query.filter_by(project_id=project.id).all()
        for ticket in tickets:
            if ticket.state == 'Open':
                tickets_open.append(ticket)
            else:
                tickets_closed.append(ticket)
    # search through complete projects and sort tickets by state
    for project in projects_complete:
        tickets = Ticket.query.filter_by(project_id=project.id).all()
        for ticket in tickets:
            if ticket.state == 'Open':
                tickets_open.append(ticket)
            else:
                tickets_closed.append(ticket)

    # create lists with lengths of projects, active and complete, and tickets, open and closed
    projects = [len(projects_active), len(projects_complete)]
    tickets = [len(tickets_open), len(tickets_closed)]

    return render_template('profile.html', user=current_user, projects=projects, tickets=tickets)


@main.route('/profile/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def profile_edit(id):
    # query database for User
    user = User.query.get_or_404(id)

    # post updated profile to database and refresh profile
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        db.session.commit()
        return redirect('/profile')

    # render profile edit page
    return render_template('profile_edit.html', user=current_user)


# active project page
@main.route('/projects/active')
@login_required
def projects_active():
    # query database for all active and complete projects
    projects_active = Project.query.filter_by(owner_id=current_user.id, state='Active').order_by(Project.due_date).all()
    projects_complete = Project.query.filter_by(owner_id=current_user.id, state='Complete').order_by(
        Project.due_date).all()

    tickets_open = []
    tickets_closed = []
    # search through active projects and sort tickets by state
    for project in projects_active:
        tickets = Ticket.query.filter_by(project_id=project.id).all()
        for ticket in tickets:
            if ticket.state == 'Open':
                tickets_open.append(ticket)
            else:
                tickets_closed.append(ticket)
    # search through complete projects and sort tickets by state
    for project in projects_complete:
        tickets = Ticket.query.filter_by(project_id=project.id).all()
        for ticket in tickets:
            if ticket.state == 'Open':
                tickets_open.append(ticket)
            else:
                tickets_closed.append(ticket)

    # create lists with lengths of projects, active and complete, and tickets, open and closed
    projects = [len(projects_active), len(projects_complete)]
    tickets = [len(tickets_open), len(tickets_closed)]

    return render_template('projects_active.html', active_projects=projects_active, projects=projects, tickets=tickets)


# completed projects page
@main.route('/projects/completed')
@login_required
def projects_completed():
    # query database for all active and complete projects
    projects_active = Project.query.filter_by(owner_id=current_user.id, state='Active').order_by(Project.due_date).all()
    projects_complete = Project.query.filter_by(owner_id=current_user.id, state='Complete').order_by(Project.date_created).all()

    tickets_open = []
    tickets_closed = []
    # search through active projects and sort tickets by state
    for project in projects_active:
        tickets = Ticket.query.filter_by(project_id=project.id).all()
        for ticket in tickets:
            if ticket.state == 'Open':
                tickets_open.append(ticket)
            else:
                tickets_closed.append(ticket)
    # search through complete projects and sort tickets by state
    for project in projects_complete:
        tickets = Ticket.query.filter_by(project_id=project.id).all()
        for ticket in tickets:
            if ticket.state == 'Open':
                tickets_open.append(ticket)
            else:
                tickets_closed.append(ticket)

    # create lists with lengths of projects, active and complete, and tickets, open and closed
    projects = [len(projects_active), len(projects_complete)]
    tickets = [len(tickets_open), len(tickets_closed)]

    return render_template('projects_completed.html', completed_projects=projects_complete, projects=projects, tickets=tickets)


# project edit page
@main.route('/project/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def project_edit(id):
    # query database for Project
    project = Project.query.get_or_404(id)

    # post updated profile to database and refresh profile
    if request.method == 'POST':
        project.name = request.form['name']

        if request.form['due_date']:
            project.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        else:
            project.due_date = datetime.utcnow()

        project.description = request.form['content']

        # commit updates to database
        db.session.commit()
        return redirect(url_for('main.projects_active'))

    # render profile edit page
    return render_template('project_edit.html', project=project)


# project create page
@main.route('/project/create', methods=['GET', 'POST'])
@login_required
def project_create():
    # if posting new projects
    if request.method == 'POST':
        project_name = request.form['name']

        # format due date into python datetime for sqlite database
        if request.form['due_date']:
            project_due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        else:
            project_due_date = datetime.utcnow()

        project_content = request.form['content']

        # create project and commit to database
        new_project = Project(name=project_name, due_date=project_due_date,  description=project_content, owner=current_user)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('main.projects_active'))

    else:
        return render_template('project_create.html')


# project delete from active page, redirect back to active project page
@main.route('/project/active/delete/<int:id>')
@login_required
def project_active_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('main.projects_active'))


# project delete from complete page, redirect back to completed project page
@main.route('/project/complete/delete/<int:id>')
@login_required
def project_completed_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('main.projects_completed'))


# changes the state of the given project to complete
@main.route('/project/complete/<int:id>')
@login_required
def project_complete(id):
    project = Project.query.get_or_404(id)
    project.state = 'Complete'
    db.session.commit()
    return redirect(url_for('main.projects_active'))


# changes the state of the given project back to active
@main.route('/project/reactivate/<int:id>')
@login_required
def project_reactivate(id):
    project = Project.query.get_or_404(id)
    project.state = 'Active'
    db.session.commit()
    return redirect(url_for('main.projects_completed'))


# completed project view page
@main.route('/project/<int:id_project>/closed')
@login_required
def project_closed(id_project):
    project = Project.query.get_or_404(id_project)
    tickets = Ticket.query.filter_by(project_id=project.id).order_by(Ticket.due_date).all()
    return render_template('project_complete.html', project=project, tickets=tickets)


# open tickets
@main.route('/project/<int:id_project>/tickets/open')
@login_required
def tickets_open(id_project):
    project = Project.query.get_or_404(id_project)
    tickets = Ticket.query.filter_by(project_id=project.id, state='Open').order_by(Ticket.priority).all()
    return render_template('tickets_open.html', project=project, tickets=tickets)


# closed tickets
@main.route('/project/<int:id_project>/tickets/closed')
@login_required
def tickets_closed(id_project):
    project = Project.query.get_or_404(id_project)
    tickets = Ticket.query.filter_by(project_id=project.id, state='Closed').all()
    return render_template('tickets_closed.html', tickets=tickets, project=project)


# edit ticket page
@main.route('/project/<int:id_project>/ticket/<int:id_ticket>/edit', methods=['GET', 'POST'])
@login_required
def ticket_edit(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    project = Project.query.get_or_404(id_project)

    # if editing ticket
    if request.method == 'POST':
        ticket.name = request.form['name']
        ticket.priority = request.form['priority']

        # format to python date time for sqlite database
        if request.form['due_date']:
            ticket.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        else:
            ticket.due_date = datetime.utcnow()

        # commit updates to database
        ticket.description = request.form['content']
        db.session.commit()
        return redirect(url_for('main.tickets_open', id_project=id_project))

    else:
        return render_template('ticket_edit.html', ticket=ticket, project=project)


# creating ticket page
@main.route('/project/<int:id_project>/ticket/create', methods=['GET', 'POST'])
@login_required
def ticket_create(id_project):
    project = Project.query.get_or_404(id_project)

    # if creating a new ticket
    if request.method == 'POST':
        ticket_name = request.form['name']

        # format to python date time for sqlite database
        if request.form['due_date']:
            ticket_due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        else:
            ticket_due_date = datetime.utcnow()

        ticket_priority = request.form['priority']
        ticket_description = request.form['content']

        # create new ticket and commit it to database
        new_ticket = Ticket(name=ticket_name, due_date=ticket_due_date, priority=ticket_priority, description=ticket_description, project=project)
        db.session.add(new_ticket)
        db.session.commit()
        return redirect(url_for('main.tickets_open', id_project=project.id))

        pass

    else:
        return render_template('ticket_create.html', project=project)


# delete ticket from open page and redirect back to open page
@main.route('/project/<int:id_project>/ticket/open/<int:id_ticket>/delete')
@login_required
def ticket_open_delete(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('main.tickets_open', id_project=id_project))


# delete ticket from closed page and redirect back to closed page
@main.route('/project/<int:id_project>/ticket/closed/<int:id_ticket>/delete')
@login_required
def ticket_closed_delete(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('main.tickets_closed', id_project=id_project))


# change ticket state to closed
@main.route('/project/<int:id_project>/ticket/<int:id_ticket>/close')
@login_required
def ticket_close(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    ticket.state = 'Closed'
    db.session.commit()
    return redirect(url_for('main.tickets_open', id_project=id_project))


# change ticket state back to open
@main.route('/project/<int:id_project>/ticket/<int:id_ticket>/reopen')
@login_required
def ticket_reopen(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    ticket.state = 'Open'
    db.session.commit()
    return redirect(url_for('main.tickets_closed', id_project=id_project))


# open ticket view page
@main.route('/project/<int:id_project>/ticket/<int:id_ticket>/view')
@login_required
def ticket_view(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    project = Project.query.get_or_404(id_project)
    return render_template('ticket_view.html', ticket=ticket, project=project)


# closed ticket view page
@main.route('/project/<int:id_project>/ticket/<int:id_ticket>/closed/view')
@login_required
def ticket_closed(id_project, id_ticket):
    ticket = Ticket.query.get_or_404(id_ticket)
    project = Project.query.get_or_404(id_project)
    return render_template('ticket_closed.html', ticket=ticket, project=project)
