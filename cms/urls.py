from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [

    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee-management/', views.employee_management, name='employee_management'),
    path('create-employee/', views.create_employee_view, name='create_employee'),
    path('view-employees/', views.view_employees, name='view_employees'),
    path('edit-employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('new-complaint/', views.new_complaint, name='new_complaint'),
    path('my-complaints/', views.my_complaints, name='my_complaints'),
    path('complaint/<int:id>/', views.complaint_timeline, name='complaint_timeline'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('report/pdf/', views.user_report_pdf, name='user_report_pdf'),
    path('report/excel/', views.user_report_excel, name='user_report_excel'),
    # path('assign/<int:cid>/', views.assign_complaint, name='assign_specific'),

    # User actions
    # path('update-complaint/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
    # path('withdraw-complaint/<int:complaint_id>/', views.withdraw_complaint, name='withdraw_complaint'),
    # path('approve-resolution/<int:complaint_id>/', views.approve_resolution, name='approve_resolution'),
    # path('reopen-complaint/<int:complaint_id>/', views.reopen_complaint, name='reopen_complaint'),

    # # Employee actions
    path('update-status/<int:complaint_id>/', views.update_complaint_status, name='update_status'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('assign-grievance/', views.assign_grievance, name='assign_grievance'),
    path('escalate-grievance/', views.escalate_grievance, name='escalate_grievance'),
    path('manage-grievances/', views.manage_grievances, name='manage_grievances'),

    path('view-users/', views.view_users, name='view_users'),
    path('view-all-complaints/', views.view_all_complaints, name='view_all_complaints'),
    path('delete-complaint/<int:pk>/', views.delete_complaint, name='delete_complaint'),

    # # Admin management
    # path('manage-departments/', views.manage_departments, name='manage_departments'),
    # path('manage-categories/', views.manage_categories, name='manage_categories'),
    # path('manage-users/', views.manage_users, name='manage_users'),
    # path('monitor-sla/', views.monitor_sla, name='monitor_sla'),
    path('admin-report-pdf/', views.admin_report_pdf, name='admin_report_pdf'),
    path('admin-report-excel/', views.admin_report_excel, name='admin_report_excel'),
    path('employee-report-pdf/', views.employee_report_pdf, name='employee_report_pdf'),
    path('employee-report-excel/', views.employee_report_excel, name='employee_report_excel'),
    path('escalate/<int:complaint_id>/', views.escalate_complaint, name='escalate_complaint'),
    path('employee-assignment-history/', views.employee_assignment_history, name='employee_assignment_history'),
]
