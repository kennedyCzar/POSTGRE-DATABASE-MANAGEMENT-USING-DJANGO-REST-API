from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


#views of application subdirectories
class index(TemplateView):
    """docstring for index."""
    template_name = 'index.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class profile(TemplateView):
    """docstring for profile."""
    template_name = 'profile.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class contacts(TemplateView):
    """docstring for contacts."""
    template_name = 'contacts.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class mailbox(TemplateView):
    """docstring for mailbox."""
    template_name = 'mailbox.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class login_module(TemplateView):
    """docstring for login_module."""
    template_name = 'login.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class dashboard_2(TemplateView):
    """docstring for dashboard_2."""
    template_name = 'dashboard_2.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)
        

class dashboard_3(TemplateView):
    """docstring for dashboard_3."""
    template_name = 'dashboard_3.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class dashboard_4_1(TemplateView):
    """docstring for dashboard_4_1."""
    template_name = 'dashboard_4_1.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class dashboard_5(TemplateView):
    """docstring for dashboard_5."""
    template_name = 'dashboard_5.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class layouts(TemplateView):
    """docstring for layouts."""
    template_name = 'layouts.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_flot(TemplateView):
    """docstring for graph_flot."""
    template_name = 'graph_flot.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_morris(TemplateView):
    """docstring for graph_morris."""
    template_name = 'graph_morris.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_rickshaw(TemplateView):
    """docstring for graph_rickshaw."""
    template_name = 'graph_rickshaw.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_chartjs(TemplateView):
    """docstring for graph_chartjs."""
    template_name = 'graph_chartjs.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_chartist(TemplateView):
    """docstring for graph_chartist."""
    template_name = 'graph_chartist.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class c3(TemplateView):
    """docstring for c3."""
    template_name = 'c3.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_peity(TemplateView):
    """docstring for graph_peity."""
    template_name = 'graph_peity.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class graph_sparkline(TemplateView):
    """docstring for graph_sparkline."""
    template_name = 'graph_sparkline.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class mail_detail(TemplateView):
    """docstring for mail_detail."""
    template_name = 'mail_detail.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class mail_compose(TemplateView):
    """docstring for mail_compose."""
    template_name = 'mail_compose.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class email_template(TemplateView):
    """docstring for email_template."""
    template_name = 'email_template.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class widgets(TemplateView):
    """docstring for widgets."""
    template_name = 'widgets.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class metrics(TemplateView):
    """docstring for metrics."""
    template_name = 'metrics.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class form_basic(TemplateView):
    """docstring for form_basic."""
    template_name = 'form_basic.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class form_advanced(TemplateView):
    """docstring for form_advanced."""
    template_name = 'form_advanced.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class form_wizard(TemplateView):
    """docstring for form_wizard."""
    template_name = 'form_wizard.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class form_file_upload(TemplateView):
    """docstring for form_file_upload."""
    template_name = 'form_file_upload.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class form_editors(TemplateView):
    """docstring for form_editors."""
    template_name = 'form_editors.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)
    
class form_autocomplete(TemplateView):
    """docstring for form_autocomplete."""
    template_name = 'form_autocomplete.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class form_markdown(TemplateView):
    """docstring for form_markdown."""
    template_name = 'form_markdown.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class profile_2(TemplateView):
    """docstring for profile_2."""
    template_name = 'profile_2.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class contacts_2(TemplateView):
    """docstring for contacts_2."""
    template_name = 'contacts_2.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class projects(TemplateView):
    """docstring for projects."""
    template_name = 'projects.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class project_detail(TemplateView):
    """docstring for project_detail."""
    template_name = 'project_detail.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class activity_stream(TemplateView):
    """docstring for activity_stream."""
    template_name = 'activity_stream.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class teams_board(TemplateView):
    """docstring for teams_board."""
    template_name = 'teams_board.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class social_feed(TemplateView):
    """docstring for social_feed."""
    template_name = 'social_feed.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class clients(TemplateView):
    """docstring for clients."""
    template_name = 'clients.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class full_height(TemplateView):
    """docstring for full_height."""
    template_name = 'full_height.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class vote_list(TemplateView):
    """docstring for vote_list."""
    template_name = 'vote_list.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class file_manager(TemplateView):
    """docstring for file_manager."""
    template_name = 'file_manager.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class calendar(TemplateView):
    """docstring for calendar."""
    template_name = 'calendar.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class issue_tracker(TemplateView):
    """docstring for issue_tracker."""
    template_name = 'issue_tracker.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class blog(TemplateView):
    """docstring for blog."""
    template_name = 'blog.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class article(TemplateView):
    """docstring for article."""
    template_name = 'article.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class faq(TemplateView):
    """docstring for faq."""
    template_name = 'faq.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class timeline(TemplateView):
    """docstring for timeline."""
    template_name = 'timeline.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class pin_board(TemplateView):
    """docstring for pin_board."""
    template_name = 'pin_board.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class search_results(TemplateView):
    """docstring for search_results."""
    template_name = 'search_results.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class lockscreen(TemplateView):
    """docstring for lockscreen."""
    template_name = 'lockscreen.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class invoice(TemplateView):
    """docstring for invoice."""
    template_name = 'invoice.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class login_two_columns(TemplateView):
    """docstring for login_two_columns."""
    template_name = 'login_two_columns.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class forgot_password(TemplateView):
    """docstring for forgot_password."""
    template_name = 'forgot_password.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class register(TemplateView):
    """docstring for register."""
    template_name = 'register.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class view_404(TemplateView):
    """docstring for 404."""
    template_name = '404.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)
    
class view_505(TemplateView):
    """docstring for 500."""
    template_name = '500.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class empty_page(TemplateView):
    """docstring for empty_page."""
    template_name = 'empty_page.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class toastr_notifications(TemplateView):
    """docstring for toastr_notifications."""
    template_name = 'toastr_notifications.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)
        
class nestable_list(TemplateView):
    """docstring for nestable_list."""
    template_name = 'nestable_list.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class agile_board(TemplateView):
    """docstring for agile_board."""
    template_name = 'agile_board.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class timeline_2(TemplateView):
    """docstring for timeline_2."""
    template_name = 'timeline_2.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class diff(TemplateView):
    """docstring for diff."""
    template_name = 'diff.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class pdf_viewer(TemplateView):
    """docstring for pdf_viewer."""
    template_name = 'pdf_viewer.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class i18support(TemplateView):
    """docstring for i18support."""
    template_name = 'i18support.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class sweetalert(TemplateView):
    """docstring for sweetalert."""
    template_name = 'sweetalert.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class idle_timer(TemplateView):
    """docstring for idle_timer."""
    template_name = 'idle_timer.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class truncate(TemplateView):
    """docstring for truncate."""
    template_name = 'truncate.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class password_meter(TemplateView):
    """docstring for password_meter."""
    template_name = 'password_meter.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class spinners(TemplateView):
    """docstring for spinners."""
    template_name = 'spinners.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class spinners_usage(TemplateView):
    """docstring for spinners_usage."""
    template_name = 'spinners_usage.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class tinycon(TemplateView):
    """docstring for tinycon."""
    template_name = 'tinycon.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class google_maps(TemplateView):
    """docstring for google_maps."""
    template_name = 'google_maps.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class datamaps(TemplateView):
    """docstring for datamaps."""
    template_name = 'datamaps.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class social_buttons(TemplateView):
    """docstring for social_buttons."""
    template_name = 'social_buttons.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)
    
class code_editor(TemplateView):
    """docstring for code_editor."""
    template_name = 'code_editor.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class modal_window(TemplateView):
    """docstring for modal_window."""
    template_name = 'modal_window.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class clipboard(TemplateView):
    """docstring for clipboard."""
    template_name = 'clipboard.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class text_spinners(TemplateView):
    """docstring for text_spinners."""
    template_name = 'text_spinners.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class forum_main(TemplateView):
    """docstring for forum_main."""
    template_name = 'forum_main.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class validation(TemplateView):
    """docstring for validation."""
    template_name = 'validation.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class tree_view(TemplateView):
    """docstring for tree_view."""
    template_name = 'tree_view.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class loading_buttons(TemplateView):
    """docstring for loading_buttons."""
    template_name = 'loading_buttons.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class chat_view(TemplateView):
    """docstring for chat_view."""
    template_name = 'chat_view.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class masonry(TemplateView):
    """docstring for masonry."""
    template_name = 'masonry.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class tour(TemplateView):
    """docstring for tour."""
    template_name = 'tour.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class typography(TemplateView):
    """docstring for typography."""
    template_name = 'typography.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class icons(TemplateView):
    """docstring for icons."""
    template_name = 'icons.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class draggable_panels(TemplateView):
    """docstring for draggable_panels."""
    template_name = 'draggable_panels.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class buttons(TemplateView):
    """docstring for buttons."""
    template_name = 'buttons.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class video(TemplateView):
    """docstring for video."""
    template_name = 'video.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class tabs_panels(TemplateView):
    """docstring for tabs_panels."""
    template_name = 'tabs_panels.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class tabs(TemplateView):
    """docstring for tabs."""
    template_name = 'tabs.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class notifications(TemplateView):
    """docstring for notifications."""
    template_name = 'notifications.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class helper_classes(TemplateView):
    """docstring for helper_classes."""
    template_name = 'helper_classes.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class badges_labels(TemplateView):
    """docstring for badges_labels."""
    template_name = 'badges_labels.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class grid_options(TemplateView):
    """docstring for grid_options."""
    template_name = 'grid_options.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class table_basic(TemplateView):
    """docstring for table_basic."""
    template_name = 'table_basic.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

'''
Model for database interaction
--------------------------------------------------------
Contains output for database objects
in the following format
CSV
JSON
EXCEL
'''
from .models import cactea
import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from .tables import CacteaTable, CacResource
from .filters import TableFilter
from django.template import RequestContext

class table_data_tables(TemplateView):
    """docstring for table_data_tables."""
    template_name = 'table_data_tables.html'
    def get(self, request, **kwargs):
        cac = cactea.objects.all()
        table = CacteaTable(cac, order_by_field = 'sort')
        if request.method == 'GET':
            return render(request, self.template_name, {'table': cac})

#export csv
class export_csv(TemplateView):
    def get(self, request, **kwargs):
        export = CacResource()
        dataset = export.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cactea.csv"'
        return response

#export json
class export_json(TemplateView):
    def get(self, request, **kwargs):
        export = CacResource()
        dataset = export.export()
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="cactea.json"'
        return response

#export excel
class export_excel(TemplateView):
    def get(self, request, **kwargs):
        export = CacResource()
        dataset = export.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="cactea.xls"'
        return response



#Serialization junction
from .serializers import CacteaSerializer
from rest_framework import viewsets

class CacteaViewSet(viewsets.ModelViewSet):
    queryset = cactea.objects.all()
    serializer_class = CacteaSerializer  


def populate_database():
    import csv
    from .models import cactea
    from os import chdir
    # path = chdir('D:\\FREELANCER\\DjangoProjectGamma\\DIRECTORY\\CACTEA\\data')
    with open('D:\\FREELANCER\\DjangoProjectGamma\\DIRECTORY\\CACTEA\\data\\new_storage.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = cactea(id_IT = row['id'], SERIAL_NUMBER = row['SERIAL_NUMBER'], MANUFACTURER = row['MANUFACTURER'], 
            NAME = row['NAME'], MODEL = row['MODEL'], LOCATION = row['LOCATION'], ROOM = row['ROOM'], 
            ENERGY_CONSUMPTION = row['ENERGY_CONSUMPTION'], BTU = row['BTU'], MICROCODE = row['MICROCODE'], 
            PATCH_LEVEL = row['PATCH_LEVEL'], CUSTOMER_ID = row['CUSTOMER_ID'], HOSTS_APPLICATION = row['HOSTS_APPLICATION'],
            TCPADDR1 = row['TCPADDR1'], TCPADDR2 = row['TCPADDR2'], TCPADDR3 = row['TCPADDR3'], 
            SW_GUI = row['SW_GUI'], INVESTMENT_DATE = row['INVESTMENT_DATE'], 
            MAINTENANCE_EXPIRATION_DATE = row['MAINTENANCE_EXPIRATION_DATE'], MAINTENANCE_PROVIDER = row['MAINTENANCE_PROVIDER'],
            MAINTENANCE_CONTRACT = row['MAINTENANCE_CONTRACT'], IS_EXTENSION_REQUIRED = row['IS_EXTENSION_REQUIRED'], 
            IS_MIGRATION_REQUIRED = row['IS_MIGRATION_REQUIRED'], RAID_CONFIG = row['RAID_CONFIG'], 
            USABLE_CAPACITY_GB = row['USABLE_CAPACITY_GB'], CAPACITY_IN_USE_GB = row['CAPACITY_IN_USE_GB'], 
            FREE_CAPACITY_GB = row['FREE_CAPACITY_GB'], EXTENSION = row['EXTENSION'], COMMENT_1 = row['COMMENT_1'], 
            STORAGE_TYPE = row['STORAGE_TYPE'], READADMIN = row['READADMIN'], RACK = row['RACK'], 
            COST_CENTER = row['COST_CENTER'], CO2_KG = row['CO2_KG'], SECOND_INVESTMENT_DATE = row['SECOND_INVESTMENT_DATE'])
            p.save()
        

populate_database()


class table_foo_table(TemplateView):
    """docstring for table_foo_table."""
    template_name = 'table_data_tables.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class jq_grid(TemplateView):
    """docstring for jq_grid."""
    template_name = 'jq_grid.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class ecommerce_products_grid(TemplateView):
    """docstring for ecommerce_products_grid."""
    template_name = 'ecommerce_products_grid.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class ecommerce_product_list(TemplateView):
    """docstring for ecommerce_product_list."""
    template_name = 'ecommerce_product_list.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class ecommerce_product(TemplateView):
    """docstring for ecommerce_product."""
    template_name = 'ecommerce_product.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class ecommerce_product_detail(TemplateView):
    """docstring for ecommerce_product_detail."""
    template_name = 'ecommerce_product_detail.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class ecommerce_cart(TemplateView):
    """docstring for ecommerce-cart."""
    template_name = 'ecommerce-cart.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class ecommerce_orders(TemplateView):
    """docstring for ecommerce-orders."""
    template_name = 'ecommerce-orders.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class ecommerce_payments(TemplateView):
    """docstring for ecommerce_payments."""
    template_name = 'ecommerce_payments.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class basic_gallery(TemplateView):
    """docstring for basic_gallery."""
    template_name = 'basic_gallery.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

class slick_carousel(TemplateView):
    """docstring for slick_carousel."""
    template_name = 'slick_carousel.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)
            
class carousel(TemplateView):
    """docstring for carousel."""
    template_name = 'carousel.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class css_animation(TemplateView):
    """docstring for css_animation."""
    template_name = 'css_animation.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class landing(TemplateView):
    """docstring for landing."""
    template_name = 'landing.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)


class package(TemplateView):
    """docstring for package."""
    template_name = 'package.html'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)

    
# from .table import CacteaTable
# #Views for application table
# def cac_view(request):
#     table = CacteaTable(cactea.objects.all())
#     return render(request, 'table_data_tables.html', {'table': table})