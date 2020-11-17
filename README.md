
# Books Summaries

books summaries is a django prject that allow users to create summaries for books, then they could search in those summaries and read them or download a pdf copy of the summary.


# Installed apps :
INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    ...
    'crispy_forms',
    'taggit',
    'summary.apps.SummaryConfig',
]

# root url configuration :
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('summary/', include('summary.urls', namespace='summary')),
]

