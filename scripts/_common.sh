#!/bin/bash

#=================================================
# RETRIEVE ARGUMENTS FROM THE MANIFEST
#=================================================

domain=$YNH_APP_ARG_DOMAIN
path=""

admin=$YNH_APP_ARG_ADMIN
is_public=$YNH_APP_ARG_IS_PUBLIC
app=$YNH_APP_INSTANCE_NAME

# Transfer the main SSO domain to the App:
ynh_current_host=$(cat /etc/yunohost/current_host)
__YNH_CURRENT_HOST__=${ynh_current_host}

#=================================================
# ARGUMENTS FROM CONFIG PANEL
#=================================================

# 'debug_enabled' -> '__DEBUG_ENABLED__' -> settings.DEBUG
debug_enabled="0"

# 'log_level' -> '__LOG_LEVEL__' -> settings.LOG_LEVEL
log_level="WARNING"

# 'admin_email' -> '__ADMIN_EMAIL__' add in settings.ADMINS
admin_email="${admin}@${domain}"

# 'default_from_email' -> '__DEFAULT_FROM_EMAIL__' -> settings.DEFAULT_FROM_EMAIL
default_from_email="${app}@${domain}"

#=================================================
# SET CONSTANTS
#=================================================

public_path=/var/www/$app
final_path=/opt/yunohost/$app
log_path=/var/log/$app
log_file="${log_path}/${app}.log"

#=================================================
# COMMON VARIABLES
#=================================================

# dependencies used by the app
pkg_dependencies="build-essential autoconf python3 python3-dev python3-pip python3-venv git libpq-dev postgresql postgresql-server-dev-all postgresql-contrib postgis libxml2-dev libxslt1-dev zlib1g-dev"
