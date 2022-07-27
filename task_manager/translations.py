from django.utils.translation import gettext_lazy
# Translations
# Common
CHANGE_BUTTON = gettext_lazy('Change')
DELETE_BUTTON = gettext_lazy('Delete')
CREATE_BUTTON = gettext_lazy('Create')

NOT_AUTHORIZED_MESSAGE = gettext_lazy("You are not authorized")

# Users

REGISTER_USER_BUTTON = gettext_lazy('Register')

USER_CREATED_MESSAGE = gettext_lazy('User successfully created!')
USER_CHANGED_MESSAGE = gettext_lazy('User profile successfully changed!')
USER_DELETED_MESSAGE = gettext_lazy('User deleted!')
NO_PERMISSION_MESSAGE = gettext_lazy('You cannot change other users!')
LOGIN_REQUIRED_MESSAGE = gettext_lazy('You are not authorized. Please, log in.')

# VERBOSE_NAME = gettext_lazy('User')
# VERBOSE_NAME_PL = gettext_lazy('Users')

USER_LIST_TITLE = gettext_lazy('Users')
CREATE_USER_TITLE = gettext_lazy('Create user')
CHANGE_USER_TITLE = gettext_lazy('Change user')
DELETE_USER_TITLE = gettext_lazy('Delete user')

# Auth

LOGGED_IN_MESSAGE = gettext_lazy('you successfully logged in!')
LOGGED_OUT_MESSAGE = gettext_lazy('you  successfully logged out!')
LOGIN_BUTTON = gettext_lazy('login')
LOGIN_TITLE = gettext_lazy('Sign in')

# Statuses

STATUS_CREATED_MESSAGE = gettext_lazy('Status successfully created!')
STATUS_CHANGED_MESSAGE = gettext_lazy('Status successfully changed!')
STATUS_DELETED_MESSAGE = gettext_lazy('Status successfully deleted!')

STATUS_NAME = gettext_lazy('Name')
STATUS_CREATED_AT = gettext_lazy('Created at')
VERBOSE_STATUS_NAME = gettext_lazy('Status')
VERBOSE_STATUS_NAME_PL = gettext_lazy('Statuses')

STATUS_LIST_TITLE = gettext_lazy('Statuses')
CREATE_STATUS_TITLE = gettext_lazy('Create status')
CHANGE_STATUS_TITLE = gettext_lazy('Change status')
DELETE_STATUS_TITLE = gettext_lazy('Delete status')

TASK_NAME = gettext_lazy('Name')
TASK_DESCRIPTION = gettext_lazy('Description')
TASK_STATUS = gettext_lazy('Status')
TASK_EXECUTIVE = gettext_lazy('Executor')

TASK_CREATED_MESSAGE = gettext_lazy('Task successfully created!')
TASK_CHANGED_MESSAGE = gettext_lazy('Task successfully changed!')
TASK_DELETED_MESSAGE = gettext_lazy('Task successfully deleted!')
DELETERIGHTS_MESSAGE = gettext_lazy('The task can only be deleted by its creator!')  # noqa: E501

TASK_CREATED_AT = gettext_lazy('Created at')

VERBOSE_TASK_NAME = gettext_lazy('Task')
VERBOSE_TASK_NAME_PL = gettext_lazy('Tasks')

TASK_LIST_TITLE = gettext_lazy('Tasks')
CREATE_TASK_TITLE = gettext_lazy('Create task')
CHANGE_TASK_TITLE = gettext_lazy('Change task')
DELETE_TASK_TITLE = gettext_lazy('Delete task')
