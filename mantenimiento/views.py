from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from mantenimiento.forms import DatabaseBackupForm, MediaBackupForm


class BackupView(TemplateResponseMixin, View):

    template_name = "mantenimiento/backup_view.html"

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        context = {
            "database_backup_form": DatabaseBackupForm(),
            "media_backup_form": MediaBackupForm(),
            "title": "Backup Base de Datos y Media",
        }
        return self.render_to_response(self.update_context(context))

    def post(self, request, *args, **kwargs):
        database_backup_form = DatabaseBackupForm(request.POST)
        media_backup_form = MediaBackupForm(request.POST)

        context = {
            "database_backup_form": database_backup_form,
            "media_backup_form": media_backup_form,
        }

        outputfile, filename = None, None
        if "savebackup" in request.POST and database_backup_form.is_valid():
            outputfile, filename = database_backup_form.do_backup()
        elif "mediabackup" in request.POST and media_backup_form.is_valid():
            outputfile, filename = media_backup_form.do_backup()

        if outputfile and filename:
            response = HttpResponse(
                outputfile.read(), content_type="application/x-gzip"
            )
            response["Content-Disposition"] = "inline; filename=" + filename
            return response

        return self.render_to_response(self.update_context(context))

    def update_context(self, context):
        context.update({"title": "Backup Base de Datos y Media"})
        return context


class RestoreView(TemplateResponseMixin, View):

    template_name = "mantenimiento/restore_view.html"

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        context = {"title": "Recuperacion a partir de Backup"}
        return self.render_to_response(self.update_context(context))

    def update_context(self, context):
        context.update({"title": "Recuperacion"})
        return context


backup = BackupView.as_view()
restore = RestoreView.as_view()
