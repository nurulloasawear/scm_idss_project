from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from reports.models import Report
from .serializers import ReportSerializer
from reports.tasks import generate_report_task 

class ReportViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Report.objects.filter(requested_by_id=self.request.user.id)

    def perform_create(self, serializer):
        report = serializer.save(requested_by_id=self.request.user.id)
        generate_report_task.delay(report.id)

