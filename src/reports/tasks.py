import time
from celery import shared_task
from .models import Report

@shared_task
def generate_report_task(report_id):
    """
    Hisobotni fonda (asinxron) generatsiya qiladigan Celery vazifasi.
    """
    try:
        report = Report.objects.get(id=report_id)
        report.status = Report.ReportStatus.GENERATING
        report.save()

        # Bu yerda haqiqiy hisobot yaratish mantig'i bo'ladi.
        # Masalan, PDF yoki Excel fayl yaratish.
        # Hozircha bu jarayonni 15 soniyalik kutish bilan simulyatsiya qilamiz.
        print(f"Generating report {report_id}...")
        time.sleep(15)
        print("Report generation simulation finished.")

        # Hisobot faylini saqlash (namuna)
        file_name = f"reports/report_{report_id}.txt"
        with open(file_name, "w") as f:
            f.write(f"This is a sample report for {report.get_report_type_display()}.\n")
            f.write(f"Parameters: {report.parameters}")

        # Modelni yangilash
        report.file_path = file_name
        report.status = Report.ReportStatus.COMPLETED
        report.save()
        print(f"Report {report_id} completed successfully.")

    except Report.DoesNotExist:
        print(f"Error: Report with id {report_id} not found.")
    except Exception as e:
        # Xatolik yuzaga kelsa, statusni 'FAILED'ga o'zgartirish
        if 'report' in locals():
            report.status = Report.ReportStatus.FAILED
            report.error_message = str(e)
            report.save()
        print(f"Error generating report {report_id}: {e}")
