python_sources(
    name="src",
    restartable=True,
    dependencies=[
        "django_project/project_root:src"
    ]
)

docker_image(
    name="django_project_image",
    dependencies=[
        "django_project:manage_local",
    ],
)

pex_binary(
    name="manage_local",
    entry_point="manage.py:main",
    dependencies=[
        ":src",
        "django_project/hello_app"
    ],
    layout='loose', # layout loose is essential for the django server to restart when library modules are updated.
)

# production pex packages should used the default layout of 'zipped'
pex_binary(
    name="manage_prod",
    entry_point="manage.py:main",
    dependencies=[
        ":src",
        "django_project/hello_app"
    ]
)
