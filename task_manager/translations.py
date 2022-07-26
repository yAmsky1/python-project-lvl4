from django.utils.translation import gettext_lazy
# Translations
# Common
CHANGE_BUTTON = gettext_lazy('Change')
DELETE_BUTTON = gettext_lazy('Delete')
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

CREATE_STATUS_BUTTON = gettext_lazy('Create')

STATUS_CREATED_MESSAGE = gettext_lazy('Status successfully created!')
STATUS_CHANGED_MESSAGE = gettext_lazy('Status successfully changed!')
STATUS_DELETED_MESSAGE = gettext_lazy('Status successfully deleted!')
NOT_AUTHORIZED_MESSAGE = gettext_lazy("You are not authorized")

STATUS_NAME = gettext_lazy('Name')
STATUS_CREATED_AT = gettext_lazy('Created at')
VERBOSE_STATUS_NAME = gettext_lazy('Status')
VERBOSE_STATUS_NAME_PL = gettext_lazy('Statuses')

STATUS_LIST_TITLE = gettext_lazy('Statuses')
CREATE_STATUS_TITLE = gettext_lazy('Create status')
CHANGE_STATUS_TITLE = gettext_lazy('Change status')
DELETE_STATUS_TITLE = gettext_lazy('Delete status')
