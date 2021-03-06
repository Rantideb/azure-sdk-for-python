# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .execution_activity import ExecutionActivity


class ExecuteSSISPackageActivity(ExecutionActivity):
    """Execute SSIS package activity.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param type: Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param package_location: SSIS package location.
    :type package_location: ~azure.mgmt.datafactory.models.SSISPackageLocation
    :param runtime: Specifies the runtime to execute SSIS package. Possible
     values include: 'x64', 'x86'
    :type runtime: str or ~azure.mgmt.datafactory.models.SSISExecutionRuntime
    :param logging_level: The logging level of SSIS package execution.
    :type logging_level: str
    :param environment_path: The environment path to execution the SSIS
     package.
    :type environment_path: str
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'package_location': {'required': True},
        'connect_via': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'package_location': {'key': 'typeProperties.packageLocation', 'type': 'SSISPackageLocation'},
        'runtime': {'key': 'typeProperties.runtime', 'type': 'str'},
        'logging_level': {'key': 'typeProperties.loggingLevel', 'type': 'str'},
        'environment_path': {'key': 'typeProperties.environmentPath', 'type': 'str'},
        'connect_via': {'key': 'typeProperties.connectVia', 'type': 'IntegrationRuntimeReference'},
    }

    def __init__(self, name, package_location, connect_via, additional_properties=None, description=None, depends_on=None, linked_service_name=None, policy=None, runtime=None, logging_level=None, environment_path=None):
        super(ExecuteSSISPackageActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, linked_service_name=linked_service_name, policy=policy)
        self.package_location = package_location
        self.runtime = runtime
        self.logging_level = logging_level
        self.environment_path = environment_path
        self.connect_via = connect_via
        self.type = 'ExecuteSSISPackage'
