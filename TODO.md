# TODO: Fix Prioritized Complaints Approval Workflow

## Steps to Complete:
- [x] Add "Resolved - Pending Approval" to STATUS_CHOICES in cms/models.py
- [x] Modify update_complaint_status in cms/views.py to set "Resolved - Pending Approval" for High/Critical priority complaints
- [ ] Update user_dashboard in cms/views.py closed_count to exclude "Resolved - Pending Approval" (only count "Closed")
- [x] Update admin_dashboard in cms/views.py to add pending approvals section and adjust closed_count
- [x] Update manage_grievances in cms/views.py to filter on "Resolved - Pending Approval" instead of "Resolved"
- [x] Update cms/templates/admin/dashboard.html to show pending approvals section
- [ ] Update cms/templates/admin/manage_grievances.html to show "Resolved - Pending Approval" complaints
- [ ] Create and run migrations for the new status
- [ ] Test the workflow
