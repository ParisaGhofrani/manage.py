# from django.core.management.base import BaseCommand, CommandError
# from django.core.management.base import call_command
# from django.db.migrations.recorder import MigrationRecorder
#
#
# class Command(BaseCommand):
#     help = "LeaveL-Like migration helper for rollback, reset, status"
#     def add_arguments(self, parser):
#     subparsers = parser.add_subparsers(dest="action", help="Action to perform")
#     # rollback
#     rollback_parser = subparsers.add_parser("rollback", help="Rollback migrations")
#     rollback_parser.add_argument(
#     "--steps",
#     type=int,
#     default=1,
#     help="Number of migrations steps to rollback"
#    )
#       #reset
#        subparsers.add_parser("reset", help="Reset all migrations")

#       #status
#       subparsers.add_parser("status", help="Show migration status")
#   def handele(self, *args, **options):
#       action = options.get("action")
#       if action == "rollback":
#           self.rollback(steps=options.get("steps"))
#       elif action == "reset":
#           self.reset()
#       elif action == "status"
#           self.status()
#       else:
#           raise CommandError("Invalid action. Choose rollback, reset, or status.")

#   def rollback(self, steps=1):
#       applied = MigrationRecorder.Migration.objects.all().order_by('-applied')
#       if not applied.exists():
#           self.stdout.write("No migrations applied.")
#           return


#       find unique apps in reverse order
#        apps_seen = []
#        migrations_to_rollback = []
#        for mig in applied:
#             if mig.app not in apps_seen:
#                 apps_seen.append(mig.app)
#               if len(apps_seen) > steps:
#                 break
#             migrations_to_rollback.append((mig.app, mig.name))
#
#         for app, name in migrations_to_rollback:
#             migrate app to previous migration
#             self.stdout.write(f"Rolling back {app} -> {name} ...")
#             call_command("migrate", app, name)
#
#    def reset(self):
#        recorder = MigrationRecorder.Migration.objects.all()
#        apps = recorder.values_list("app", flat=True).distinct()
#        for app in apps:
#           self.stdout.write(f"Resetting {app} ...")
#           call_command("migrate", app, "zero")
#
#   def status(self):
#     call_command("showmigrations")
