# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .database import *
from .grant import *
from .provider import *
from .role import *
from .user import *
from .user_password import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_mysql.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_mysql.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "mysql",
  "mod": "index/database",
  "fqn": "pulumi_mysql",
  "classes": {
   "mysql:index/database:Database": "Database"
  }
 },
 {
  "pkg": "mysql",
  "mod": "index/grant",
  "fqn": "pulumi_mysql",
  "classes": {
   "mysql:index/grant:Grant": "Grant"
  }
 },
 {
  "pkg": "mysql",
  "mod": "index/role",
  "fqn": "pulumi_mysql",
  "classes": {
   "mysql:index/role:Role": "Role"
  }
 },
 {
  "pkg": "mysql",
  "mod": "index/user",
  "fqn": "pulumi_mysql",
  "classes": {
   "mysql:index/user:User": "User"
  }
 },
 {
  "pkg": "mysql",
  "mod": "index/userPassword",
  "fqn": "pulumi_mysql",
  "classes": {
   "mysql:index/userPassword:UserPassword": "UserPassword"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "mysql",
  "token": "pulumi:providers:mysql",
  "fqn": "pulumi_mysql",
  "class": "Provider"
 }
]
"""
)
