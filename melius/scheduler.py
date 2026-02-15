from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import logging

class TaskScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        logging.getLogger('apscheduler').setLevel(logging.WARNING)

    def add_task(self, func, run_time, args=None):
        """Schedule a one-time task."""
        job = self.scheduler.add_job(func, 'date', run_date=run_time, args=args)
        return job.id

    def add_recurring_task(self, func, interval_minutes, args=None):
        """Schedule a recurring task."""
        job = self.scheduler.add_job(func, 'interval', minutes=interval_minutes, args=args)
        return job.id

    def list_jobs(self):
        return self.scheduler.get_jobs()

    def remove_job(self, job_id):
        self.scheduler.remove_job(job_id)
