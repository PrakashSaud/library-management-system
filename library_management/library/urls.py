from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name="logout"),


    path('books/', views.AllBooksListView.as_view(), name="all_book_list"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book_detail"),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(), name="book_update"),
    path('book/create', views.BookAddView.as_view(), name="book_add"),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(), name="book_delete"),

    path('books/issued', views.issued_book_list, name="issued_book_list"),
    path('book/issue', views.book_issue, name="issue_book"),

    path('students/', views.AllStudentListView.as_view(), name="all_student_list"),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name="student_detail"),
    path('student/add', views.add_new_student, name="student_add"),
    path('student/<int:pk>/register', views.register_student, name="register_student"),



]