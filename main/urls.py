from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("hos_doc_list/", views.hos_doc_list, name="hos_doc_list"),
    path("Hospital_admin/<str:name>", views.Hospital_admin, name="Hospital_admin"),
    path(
        "Hospital_admin/Hospital_admin_accp/<int:pk>",
        views.Hospital_admin_accp,
        name="Hospital_admin_accp",
    ),
    path("unregis_view/", views.unregis_view, name="unregis_view"),
    path("patient/<int:pk>", views.patient, name="patient"),
    path(
        "edit_info_patient/<int:pk>", views.edit_info_patient, name="edit_info_patient"
    ),
    path("edit_info_patient/update_pat/<int:pk>", views.update_pat, name="update_pat"),
    path("appoint/", views.appoint, name="appoint"),
    path("regi_doc/", views.register_doc, name="regi_doc"),
    path("edit_doc_info/", views.edit_doc, name="edit_doc_info"),
    path("edit_doc_info/deleteDoc/<int:pk>", views.deleteDoc, name="deleteDoc"),
    path("edit_doc_info/update/<int:pk>", views.updateDoc, name="update"),
    path(
        "edit_doc_info/update/updateDoc/<int:pk>",
        views.updaterecord,
        name="updaterecord",
    ),
]
