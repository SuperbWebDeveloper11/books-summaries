
# Books Summaries

books summaries is a django prject that allow users to create summaries for books, and they could also read each summary or download a pdf copy 


## Installed apps :
```python
INSTALLED_APPS = [
    'accounts.apps.AccountsConfig', # authentication app
    ...
    'crispy_forms',
    'taggit',
    'summary.apps.SummaryConfig',
]
```

## root url configuration :
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('summary/', include('summary.urls', namespace='summary')),
]
```

