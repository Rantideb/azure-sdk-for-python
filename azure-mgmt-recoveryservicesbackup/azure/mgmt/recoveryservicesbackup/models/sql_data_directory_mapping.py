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

from msrest.serialization import Model


class SQLDataDirectoryMapping(Model):
    """Encapsulates information regarding data directory.

    :param mapping_type: Type of data directory mapping. Possible values
     include: 'Invalid', 'Data', 'Log'
    :type mapping_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.SQLDataDirectoryType
    :param source_logical_name: Restore source logical name path
    :type source_logical_name: str
    :param source_path: Restore source path
    :type source_path: str
    :param target_path: Target path
    :type target_path: str
    """

    _attribute_map = {
        'mapping_type': {'key': 'mappingType', 'type': 'str'},
        'source_logical_name': {'key': 'sourceLogicalName', 'type': 'str'},
        'source_path': {'key': 'sourcePath', 'type': 'str'},
        'target_path': {'key': 'targetPath', 'type': 'str'},
    }

    def __init__(self, mapping_type=None, source_logical_name=None, source_path=None, target_path=None):
        super(SQLDataDirectoryMapping, self).__init__()
        self.mapping_type = mapping_type
        self.source_logical_name = source_logical_name
        self.source_path = source_path
        self.target_path = target_path
